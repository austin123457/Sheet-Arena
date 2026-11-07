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
"""
import secrets
from collections import Counter

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
    evasion = False                 # nothing on a made Dex save
    monk_evasion = False            # the Guys' Evasion; only the BFG honours it so far
    averts_eyes = False             # Itachi doesn't bother with Tsukuyomi
    retaliates = False              # Fight.run calls retaliate() after an enemy's turn that hit you in melee
    susanoo = False                 # Itachi's ribcage is up: no prone, no topple

    def __init__(self):
        self.out = False; self.team = None; self.acted = False
        self.thp = 0; self.prone = False; self.paralyzed = False; self.poisoned = False; self.frightened = False
        self.asleep = False; self.burning = False; self.stun_immune = False; self.stun_until = None
        self.reckless = False; self.reaction = True; self.disadv_attacks = False; self.sa_used = False
        self.hits_on = Counter(); self.indomitable = 0; self.indom_bonus = 0
        self.last_hit_by_melee = None; self.adjacent = set(); self.trip_done = False
        self.surge_used = False; self.down = False; self.death_fail = 0

    def alive(self): return not self.out
    def can_act(self): return self.alive() and not self.paralyzed
    def init(self): return d(20)
    def ac_now(self): return self.ac

    # ---------- saves ----------
    def save(self, ab, dc, spell=False):
        adv = self.save_adv(ab, spell)
        if self.paralyzed and ab in ("Str", "Dex"): return False
        ok = d20(adv=adv) + self.saves[ab] >= dc
        if not ok and self.shrug_off_save(ab, spell): return True
        if not ok and self.indomitable > 0:
            self.indomitable -= 1
            ok = d20(adv=adv) + self.saves[ab] + self.indom_bonus >= dc
        return ok
    def save_adv(self, ab, spell): return False
    def shrug_off_save(self, ab, spell): return False

    # ---------- damage ----------
    def take(self, dmg, dtype, src, from_attack=False, melee=False, crit=False, ignore_res=False, ignore_imm=False):
        if self.out: return 0
        if self.immune(dtype) and not ignore_imm: return 0
        dmg = self.modify_incoming(dmg, dtype, src, from_attack, melee, ignore_res)
        if dmg <= 0: return 0
        a = min(self.thp, dmg); self.thp -= a
        self.hp -= dmg - a
        self.after_damage(dmg, dtype, src, melee)
        if self.hp <= 0: self.hp = 0; self.on_zero(src, crit)
        return dmg
    def immune(self, dtype): return False
    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res): return dmg
    def after_damage(self, dmg, dtype, src, melee): pass
    def on_zero(self, src, crit): self.out = True

    # ---------- attacks against you ----------
    def incoming_attack(self, attacker, bonus, adv, dis): return adv, dis
    def defend_ac(self, attacker, total, melee, crit): return 0
    def reduce_hit(self, dmg, melee): return dmg
    def on_targeted_by_spell(self, fight, caster): pass

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
        self.reaction = True; self.disadv_attacks = False; self.sa_used = False
        if self.prone: self.prone = False
        if self.burning: self.take(roll(4, 10), "fire", "Amaterasu", ignore_res=True)
    def turn(self, fight): pass
    def end_turn(self, fight):
        # a stun lasts until the end of the stunned creature's next turn; anything else paralyzing gets a save
        if self.stun_until is not None and self.paralyzed:
            self.paralyzed = False; self.stun_until = None; return
        if self.paralyzed and self.save("Wis", 19, spell=True): self.paralyzed = False


def attack(fight, att, tgt, bonus, dmg_fn, dtype, melee=True, adv=False, dis=False, crit_range=20,
           sneak=0, extra=None, ignore_res=False, ignore_imm=False):
    """One attack roll. Returns (hit, crit, damage dealt)."""
    adv, dis = tgt.incoming_attack(att, bonus, adv, dis)
    if tgt.out: return (False, False, 0)
    if tgt.reckless or tgt.prone or tgt.paralyzed or tgt.asleep: adv = True
    if att.poisoned or att.disadv_attacks or att.prone or att.frightened: dis = True
    if att.attack_advantage(tgt): adv = True
    nat = d20(adv=adv, dis=dis)
    total = nat + bonus
    crit = nat >= crit_range
    acb = tgt.defend_ac(att, total, melee, crit)
    if acb is None: return (False, False, 0)  # negated
    ac = tgt.ac_now() + acb
    hit = crit or (nat != 1 and total >= ac)
    if not hit:
        att.on_miss(fight, tgt, total, ac, melee)
        return (False, False, 0)
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
            for c in t: c.team = i; c.acted = False
        self.round = 0; self.notes = []; self.verbose = verbose
    def note(self, m):
        if self.verbose: self.notes.append(f"R{self.round}: {m}")
    def enemies(self, c): return [e for e in self.all if e.alive() and e.team != c.team]
    def allies(self, c): return [a for a in self.all if a.alive() and a.team == c.team and a is not c]
    def pick_target(self, c):
        """The caster first, then whoever is lowest as a fraction of their maximum."""
        es = self.enemies(c)
        if not es: return None
        casters = [e for e in es if e.caster]
        if casters and not c.caster: return casters[0]
        return min(es, key=lambda e: (e.hp + e.thp) / (e.maxhp + 1))
    def over(self):
        return len({c.team for c in self.all if c.alive()}) <= 1
    def run(self):
        order = sorted(self.all, key=lambda c: c.init(), reverse=True)
        for c in self.all: c.before_first_round(self)
        while not self.over() and self.round < ROUND_CAP:
            self.round += 1
            for c in order:
                if self.over(): break
                if not c.alive(): continue
                c.start_turn()
                c.acted = True
                for e in self.all: e.trip_done = False
                if c.paralyzed or c.asleep:
                    c.end_turn(self); continue
                c.turn(self)
                c.end_turn(self)
                for g in self.all:
                    if g.retaliates and g.alive() and g.last_hit_by_melee is c and c.alive() and g is not c:
                        g.retaliate(self, c); g.last_hit_by_melee = None
        alive_teams = {c.team for c in self.all if c.alive()}
        return (next(iter(alive_teams)) if alive_teams else None), self.round
