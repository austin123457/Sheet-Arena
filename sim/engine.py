"""The arena engine: dice, the Combatant base class, one attack roll, and the fight loop.

Fighters live in sim/fighters/, one file each. Anything a fighter does to someone
else's attack, save or turn goes through one of the hooks on Combatant; nothing
patches this file from outside.

Hooks a fighter can override (all default to doing nothing):
  incoming_attack   adjust adv/dis on an attack aimed at you (Spike's Lucky, the Gates' disadvantage)
  attack_advantage  advantage on your own attack against this target (Smasher's Studied Attacks)
  natural_bonus     extra damage for a given natural roll (Smasher's nat-20 kicker)
  defend_ac         reaction on an incoming attack: AC bonus, or None to negate it
  reduce_hit        flat reduction on a hit after it lands
  immune            take nothing at all (Nayru's Love), unless the source ignores immunity
  shrug_off_save    turn a failed save into a success (Smasher's Mage Slayer)
  on_targeted_by_spell  react when a caster targets you (Smasher's ICE)
  before_first_round    act before initiative (Jin's Standoff)
  answer_standoff   what you do when you win Jin's Standoff
  retaliate         swing back after a melee hit (set retaliates = True)
  on_missed         react when an attack misses you (Talion's Riposte; queue it with fight.after_turn)
  counter_spell     react when an enemy casts a spell: return True to stop it (Itachi's Counterspell)
  on_enemy_speeds_up  react when an enemy switches on a Sandevistan or Haste (Smasher's Counter-Sandevistan)
  legendary_action  a raid boss's move at the end of someone else's turn (legendary_actions per round)
  negates_spells    True when spells and quickhacks simply don't take (Madara's Truth-Seeking Balls)
  seal              what a sealing technique does to you (Itachi's Totsuka): by default you're out
  on_massive        a hit that leaves at least your maximum HP past 0 (5e's massive damage): by default you're dead,
                    with no Relentless Rage or death saves; only a way back from death answers it (Link's fairies)

Exponents. Every creature has an exponent (tier): E1 the ladder (city, mountain), E2 the moon, E3 a planet, E4 a
star, E5 a galaxy, E6 a universe. Its physical stats, HP and damage are written in its own units, so two creatures of
the same exponent play ordinary 5e. Across exponents, damage converts: x100 per exponent up, /100 per exponent down
(a 30-point E1 hit on an E2 body is 0.3, which is nothing). A technique can carry its own exponent (Night Guy is an
E2 attack from an E1 body). The d20 doesn't scale, it gets an edge: one exponent apart, the higher creature has
advantage on attacks and saves against the lower one and the lower has disadvantage; two or more apart, the higher
one always hits and always saves, and the lower one can't touch it.

Raid bosses (raid_boss = True) are built to fight a party: Legendary Resistance (turn a failed save into a
success, legendary_resist a day), Legendary Actions, and usually a second phase. They stay off the ladder.

Conditions the engine handles for everyone: paralyzed/stunned (stun_until), asleep, charmed (Dominate
Person breaks on a save when hurt, Hypnotic Pattern on any damage; a dominated creature turns on its own
allies if it has any and otherwise stands still), dread (disadvantage on attacks), sliver (-1d4 on the
next save), effects (callables run at the end of the creature's turn; return False to end), frightened (fear_dc: a Wis save at the end of each turn ends it), invisible, sapped (disadvantage
on your next attack), and a worthy opponent's mark (disadvantage on attacks against anyone else).
Summons (summon = True, owner = the caster) act on their owner's turn, vanish with him, and never
count for winning.
"""
import secrets

ROUND_CAP = 40
MENTAL = ("Int", "Wis", "Cha")


def d(n): return secrets.randbelow(n) + 1


def roll(n, s, gwf=False, minv=None):
    r = [d(s) for _ in range(n)]
    if gwf: r = [3 if x <= 2 else x for x in r]
    if minv: r = [max(x, minv) for x in r]
    return sum(r)


def d20(adv=False, dis=False):
    a, b = d(20), d(20)
    if adv and dis: adv = dis = False
    return max(a, b) if adv else (min(a, b) if dis else a)


class Combatant:
    name = "?"                      # internal id; roster.py maps command-line names onto it
    danger = 0                      # who the others fear most: Jin's Standoff, Itachi, Link and the Beast pick by it
    melee = False

    # traits other fighters' abilities check
    caster = False                  # everyone goes for the caster first
    evil = False                    # the Master Sword's extra damage
    poison_immune = False
    charm_immune = False
    fright_immune = False
    never_stunned = False           # Guts (and the Beast): no stun or paralysis that checks this lands
    shrugs_stunning_strike = False  # Smasher: a monk's Stunning Strike doesn't land
    evasion = False                 # Dex-save-for-half: nothing on a success, half on a failure (see dex_damage)
    averts_eyes = False             # Itachi doesn't bother with Tsukuyomi
    retaliates = False              # Fight.run calls retaliate() after an enemy's turn that hit you in melee
    susanoo = False                 # Itachi's ribcage is up: no prone, no topple
    humanoid = True                 # Hold Person and Dominate Person need it
    summon = False                  # a clone or a conjured creature: see Fight.over()
    raid_boss = False
    tier = 1                        # the exponent: 1 the ladder, 2 the moon (the raid tier), 3 a planet...
    legendary_actions = 0           # per round, refreshed at the start of its turn

    def __init__(self):
        self.out = False; self.team = None; self.acted = False
        self.thp = 0; self.prone = False; self.paralyzed = False; self.poisoned = False; self.frightened = False
        self.asleep = False; self.burning = False; self.stun_immune = False; self.stun_until = None
        self.reckless = False; self.reaction = True; self.disadv_attacks = False; self.sa_used = False
        self.struck_on = {}; self.indomitable = 0; self.indom_bonus = 0
        self.last_hit_by_melee = None; self.adjacent = set(); self.trip_done = False
        self.surge_used = False; self.down = False; self.death_fail = 0
        self.charmed = None; self.fear_dc = 0; self.invisible = False; self.sapped = False; self.marked_by = None
        self.owner = None; self.fight = None; self.dread = False; self.sliver = False; self.effects = []
        self.ambushed = False      # disadvantage on the next save (a hack out of hiding)
        self.legendary_resist = 0; self.la_left = 0

    def alive(self): return not self.out and (self.owner is None or self.owner.alive())
    def incapacitated(self): return self.paralyzed or self.asleep or self.charmed is not None
    def can_act(self): return self.alive() and not self.incapacitated()
    def init(self): return d(20)
    def ac_now(self): return self.ac

    # ---------- saves ----------
    def save(self, ab, dc, spell=False, kind=None, adv=False):
        """kind names what the save is against when it matters: "charm", "fear", "illusion", "enchantment"."""
        adv = adv or self.save_adv(ab, spell)
        if (self.paralyzed or self.asleep) and ab in ("Str", "Dex"): return False
        pen = 0
        if self.sliver: self.sliver = False; pen = d(4)        # Mind Sliver
        dis = self.ambushed; self.ambushed = False
        gap = self.tier_gap()
        if gap >= 2: return True
        if gap <= -2: return False
        if gap == 1: adv = True
        if gap == -1: dis = True
        ok = d20(adv=adv, dis=dis) + self.saves[ab] - pen >= dc
        if not ok and self.shrug_off_save(ab, spell): return True
        if not ok and self.indomitable > 0:
            self.indomitable -= 1
            ok = d20(adv=adv) + self.saves[ab] + self.indom_bonus >= dc
        if not ok and self.legendary_resist > 0 and self.spend_legendary_resistance(ab, dc, spell, kind):
            self.legendary_resist -= 1; ok = True
        return ok
    def spend_legendary_resistance(self, ab, dc, spell, kind): return True
    def save_adv(self, ab, spell): return False
    def shrug_off_save(self, ab, spell): return False
    def tier_gap(self):
        """My exponent minus that of whoever's acting (the effect I'm saving against is theirs)."""
        a = self.fight.actor if self.fight else None
        return 0 if a is None or a is self else self.tier - a.tier

    # ---------- damage ----------
    def take(self, dmg, dtype, src, from_attack=False, melee=False, crit=False, ignore_res=False, ignore_imm=False, exp=None):
        if self.out: return 0
        if self.immune(dtype) and not ignore_imm: return 0
        e = exp if exp is not None else (self.fight.tier_of(src) if self.fight else 1)
        if e != self.tier: dmg = int(dmg * 100 ** (e - self.tier))      # convert to my units
        if dmg <= 0: return 0
        dmg = self.modify_incoming(dmg, dtype, src, from_attack, melee, ignore_res)
        if dmg <= 0: return 0
        a = min(self.thp, dmg); self.thp -= a
        self.hp -= dmg - a
        if self.asleep: self.asleep = False          # being hurt wakes you
        self.after_damage(dmg, dtype, src, melee)
        if self.charmed is not None and self.charmed["mode"] != "genjutsu":
            # Hypnotic Pattern breaks on any damage; Dominate Person gets a new save; a genjutsu doesn't care
            c = self.charmed
            if c["mode"] == "pattern" or self.save("Wis", c["dc"], spell=True, kind="charm"): self.charmed = None
        if self.hp <= 0:
            overflow = -self.hp; self.hp = 0
            # massive damage (5e): what's left after 0 is at least your maximum, and you're killed outright:
            # no Relentless Rage, no death saves, no 'if you aren't killed outright'
            if overflow >= self.maxhp and not self.raid_boss: self.on_massive(src)
            else: self.on_zero(src, crit)
        return dmg
    def on_massive(self, src): self.out = True
    def immune(self, dtype): return False
    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res): return dmg
    def after_damage(self, dmg, dtype, src, melee): pass
    def on_zero(self, src, crit): self.out = True

    def dex_damage(self, saved, dmg):
        """Damage from a Dex-save-for-half effect, after the save. Evasion: nothing on a success and half on a
        failure, unless he's incapacitated."""
        if self.evasion and not self.incapacitated(): return 0 if saved else dmg // 2
        return dmg // 2 if saved else dmg

    def turns_struck_by(self, attacker):
        """How many separate rounds this attacker has hit you in."""
        return len(self.struck_on.get(attacker, ()))

    # ---------- attacks against you ----------
    def incoming_attack(self, attacker, bonus, adv, dis): return adv, dis
    def defend_ac(self, attacker, total, melee, crit): return 0
    def reduce_hit(self, dmg, melee): return dmg
    def on_targeted_by_spell(self, fight, caster): pass
    def on_missed(self, fight, attacker, melee): pass
    def counter_spell(self, fight, caster, level): return False
    def on_enemy_speeds_up(self, fight, who): pass
    def legendary_action(self, fight): pass
    def negates_spells(self): return False
    def seal(self, fight): self.out = True
    def sealable(self): return False             # only a seal ends it (an Edo Tensei body)
    def needs_moon(self): return False           # a win condition that dies with the moon

    # ---------- your own attacks ----------
    def attack_advantage(self, target): return False
    def natural_bonus(self, nat): return 0
    def on_miss(self, fight, tgt, total, ac, melee): pass
    def on_hit(self, fight, tgt, crit, dealt, melee): pass

    # ---------- the turn ----------
    def before_first_round(self, fight): pass
    def answer_standoff(self, fight, jin): pass
    def retaliate(self, fight, attacker): pass
    def start_turn(self):
        self.reaction = True; self.disadv_attacks = False; self.sa_used = False; self.la_left = self.legendary_actions
        if self.prone: self.prone = False
        if self.burning: amaterasu(self, roll(4, 10))
    def turn(self, fight): pass
    def end_turn(self, fight):
        if self.effects: self.effects = [fn for fn in self.effects if fn(self)]
        if self.charmed is not None and self.charmed["mode"] == "genjutsu":
            self.charmed = None             # a gaze in a fight costs a turn; holding someone for good takes setup
        if self.frightened and self.fear_dc and self.save("Wis", self.fear_dc, kind="fear"):
            self.frightened = False; self.fear_dc = 0
        # a stun lasts until the end of the stunned creature's next turn; anything else paralyzing gets a save
        if self.stun_until is not None and self.paralyzed:
            self.paralyzed = False; self.stun_until = None; return
        if self.paralyzed and self.save("Wis", 19, spell=True): self.paralyzed = False


def amaterasu(tgt, dmg):
    """The black flames ignore resistance to fire and treat immunity as resistance."""
    if tgt.immune("fire"): dmg //= 2
    return tgt.take(dmg, "fire", "Amaterasu", ignore_res=True, ignore_imm=True)


def attack(fight, att, tgt, bonus, dmg_fn, dtype, melee=True, adv=False, dis=False, crit_range=20,
           sneak=0, extra=None, ignore_res=False, ignore_imm=False):
    """One attack roll. Returns (hit, crit, damage dealt)."""
    adv, dis = tgt.incoming_attack(att, bonus, adv, dis)
    if tgt.out: return (False, False, 0)
    gap = att.tier - tgt.tier
    if gap <= -2: return (False, False, 0)        # two exponents up: it can't be touched
    if gap == 1: adv = True
    if gap == -1: dis = True
    if tgt.reckless or tgt.prone or tgt.paralyzed or tgt.asleep: adv = True
    if att.poisoned or att.disadv_attacks or att.prone or att.frightened: dis = True
    if att.attack_advantage(tgt): adv = True
    if tgt.invisible: dis = True
    if att.invisible: adv = True
    if att.sapped: dis = True; att.sapped = False
    if att.dread: dis = True
    if att.marked_by is not None and att.marked_by.alive() and tgt is not att.marked_by: dis = True
    nat = d20(adv=adv, dis=dis)
    total = nat + bonus
    crit = nat >= crit_range
    acb = tgt.defend_ac(att, total, melee, crit)
    if acb is None: return (False, False, 0)  # negated
    ac = tgt.ac_now() + acb
    hit = crit or (nat != 1 and total >= ac) or gap >= 2
    if not hit:
        att.on_miss(fight, tgt, total, ac, melee)
        tgt.on_missed(fight, att, melee)
        return (False, False, 0)
    tgt.struck_on.setdefault(att, set()).add(fight.round)
    dmg = dmg_fn(crit)
    if sneak and not att.sa_used and ((adv and not dis) or any(a.alive() and a is not att and a.melee for a in fight.allies(att))):
        dmg += roll(sneak * (2 if crit else 1), 6); att.sa_used = True
    dmg += att.natural_bonus(nat)
    dmg = tgt.reduce_hit(dmg, melee)
    dealt = tgt.take(dmg, dtype, att.name, from_attack=True, melee=melee, crit=crit, ignore_res=ignore_res, ignore_imm=ignore_imm)
    if melee or att.name in tgt.adjacent: tgt.last_hit_by_melee = att
    if melee: att.adjacent = att.adjacent | {tgt.name}; tgt.adjacent = tgt.adjacent | {att.name}
    if extra: extra(crit, dealt)
    att.on_hit(fight, tgt, crit, dealt, melee)
    return (True, crit, dealt)


class Fight:
    """Open sand, daylight, everyone fresh. teams is a list of lists of Combatants;
    run() returns (winning team index or None, rounds)."""
    def __init__(self, teams, verbose=False):
        self.teams = teams; self.all = [c for t in teams for c in t]
        for i, t in enumerate(teams):
            for c in t: c.team = i; c.acted = False; c.fight = self
        self.round = 0; self.notes = []; self.verbose = verbose; self.pending = []
        self.moon = True            # the Infinite Tsukuyomi needs it; Piccolo has blown one up before
        self.actor = None           # whose turn (or legendary action) it is: saves are against them
    def tier_of(self, src):
        """The tier of whoever a damage source belongs to; a technique's name (Night Guy, BFG) counts as the ladder."""
        for c in self.all:
            if c.name == src: return c.tier
        return 1
    def add(self, c, team):
        """Bring a summon into the fight on a team; it acts on its owner's turn, not in initiative."""
        c.team = team; c.fight = self; c.acted = True; self.all.append(c)
    def after_turn(self, fn):
        """Run fn once the current creature's turn is over (reactions that would interrupt a turn)."""
        self.pending.append(fn)
    def speeds_up(self, c):
        """c switches on a Sandevistan, Haste or anything else that buys it extra actions."""
        for e in self.enemies(c): e.on_enemy_speeds_up(self, c)
    def cast(self, caster, level):
        """caster casts a spell of this level; an enemy may stop it. Returns False if countered."""
        return not any(e.counter_spell(self, caster, level) for e in self.enemies(caster))
    def note(self, m):
        if self.verbose: self.notes.append(f"R{self.round}: {m}")
    def enemies(self, c): return [e for e in self.all if e.alive() and e.team != c.team]
    def allies(self, c): return [a for a in self.all if a.alive() and a.team == c.team and a is not c]
    def pick_target(self, c):
        """The caster first, then whoever is lowest as a fraction of their maximum."""
        es = self.enemies(c)
        if not es: return None
        casters = [e for e in es if e.caster]
        if casters and not c.caster:
            return casters[0] if len(casters) == 1 else casters[d(len(casters)) - 1]   # which Itachi is real?
        return min(es, key=lambda e: (e.hp + e.thp) / (e.maxhp + 1))
    def over(self):
        return len({c.team for c in self.all if c.alive() and not c.summon}) <= 1
    def run(self):
        order = sorted(self.all, key=lambda c: c.init(), reverse=True)
        for c in self.all: self.actor = c; c.before_first_round(self)
        if all(c.tier >= 2 for c in self.all):
            for c in self.all: c.legendary_resist = 0      # raid against raid: Legendary Resistance is a party-fight device, not a canon ability
        while not self.over() and self.round < ROUND_CAP:
            self.round += 1
            for c in order:
                if self.over(): break
                if not c.alive(): continue
                self.actor = c
                c.start_turn()
                c.acted = True
                for e in self.all: e.trip_done = False
                if c.incapacitated():
                    ch = c.charmed
                    if ch and ch["mode"] == "dominate" and not (c.paralyzed or c.asleep) and self.allies(c):
                        home = c.team; c.team = ch["by"].team      # commanded against its own side
                        c.turn(self); c.team = home
                    c.end_turn(self)
                else:
                    c.turn(self)
                    c.end_turn(self)
                    for fn in self.pending: fn()
                    self.pending = []
                for b in self.all:          # legendary actions come at the end of someone else's turn
                    if b is not c and b.la_left > 0 and b.alive() and not b.incapacitated() and not self.over():
                        self.actor = b; b.legendary_action(self); self.actor = c
                for g in self.all:
                    if g.retaliates and g.alive() and g.last_hit_by_melee is c and c.alive() and g is not c:
                        self.actor = g; g.retaliate(self, c); g.last_hit_by_melee = None; self.actor = c
        alive_teams = {c.team for c in self.all if c.alive() and not c.summon}
        return (next(iter(alive_teams)) if alive_teams else None), self.round
