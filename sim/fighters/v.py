"""V (Vincent), Nomad of the Bakker clan, the merc who did everything: Rogue (Arcane Trickster) 9 /
Fighter (Battle Master) 11. Sheet: V_5e_Build.pdf. 194 HP (Tough), AC 18 (Chitin subdermal plating),
initiative +11 (Alert), saves Dex +11, Int +11, Indomitable at +11.

Chrome he always has: Mantis Blades (Tier 5++, +3: +14 for 1d10+8, three a turn and a fourth from Nick, Sneak Attack
5d6), the Scalpel (a +3 electrical katana, three a turn, that he takes against anything that shorts out), Second Heart (back to full HP the first time he drops to 0),
Uncanny Dodge, Evasion, Battle Master dice (five d10s: Precision Attack, Riposte), Second Wind, Action Surge, and the
Relic's Jailbreak: a crit or a kill charges a Mantis Blade leap that crits on a hit. Vulnerability Analytics (Relic): the
first blade hit each turn finds a weak point and is a critical hit. Reflex Tuner: the first time he drops below 50 HP,
time slows for him until the end of his next turn (attacks against him at disadvantage).

One Operating System slot, picked before each fight:
  Sandevistan (Militech Apogee): a bonus action, three rounds back to back after it recharges. An extra Attack action
    each turn, +2 AC, attacks against him at disadvantage (85% slow), advantage on Dex saves, crits on 18-20, a kill
    adds a round; switching it on fires Ticking Time
    Bomb (Con 19 or stunned, everyone within reach). Back three rounds after it ends.
  Cyberdeck (Militech Canto Mk.6): 20 RAM, 4 back at the start of each turn. He opens from Optical Camo (invisible
    until he swings a blade; hacks from hiding give the target disadvantage on the save: Magical Ambush). An action
    uploads a queue of two quickhacks (Queue Mastery: the last costs half), a bonus action one more of 2 RAM. Short Circuit, Overheat,
    Synapse Burnout, Contagion, Reboot Optics, Weapon Glitch and Blackwall Gateway; save DC 19. Suicide, System
    Collapse, Cyberpsychosis and Memory Wipe don't work on bosses, and everyone here is one.
"""
from ..engine import Combatant, attack, d, d20, roll

DC = 19

# which OS V installs against the most dangerous enemy he'll face, from arena testing (300 fights a loadout,
# Nov 2026); everything else, crowds included, gets the Sandevistan
PREFERS = {"Beast": "deck", "Jin": "deck", "Itachi": "deck"}


class V(Combatant):
    name = "V"; danger = 6; melee = True
    evasion = True
    one_handed = property(lambda self: not self.scalpel)    # a Mantis Blade, not the katana in both hands
    forced = None           # "sandy" or "deck" to skip his own choice

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 194; self.ac = 18
        self.saves = dict(Str=-1, Dex=11, Con=2, Int=11, Wis=0, Cha=-1); self.indomitable = 1; self.indom_bonus = 11
        self.os = self.forced; self.sandy = 0; self.sandy_ready = 0; self.ram = 20
        self.dice = 5; self.sw = 4; self.surge = 1; self.second_heart = True; self.leap = False; self.scalpel = False
        self.camo = 1; self.weak_point = False; self.tuner = True; self.tuned = False

    def init(self): return d(20) + 11

    # ---------- picking the chrome ----------
    def before_first_round(self, fight):
        es = fight.enemies(self)
        if self.os is None:
            self.os = PREFERS.get(max(es, key=lambda e: e.danger).name, "sandy") if es else "sandy"
        self.scalpel = any(e.name == "Smasher" or e.mirrors for e in es)    # electricity shorts him out; a mirror can't copy two hands

    def ac_now(self): return self.ac + (2 if self.sandy > 0 else 0)
    def save_adv(self, ab, spell): return ab == "Dex" and self.sandy > 0

    def incoming_attack(self, attacker, bonus, adv, dis, melee=True):
        if self.sandy > 0 or self.tuned: dis = True           # the world at 15% speed
        return adv, dis

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        if from_attack and self.reaction and dmg >= 20 and not self.incapacitated():
            self.reaction = False; dmg //= 2           # Uncanny Dodge
        return dmg

    def after_damage(self, dmg, dtype, src, melee):
        if self.tuner and 0 < self.hp < 50: self.tuner = False; self.tuned = True       # Reflex Tuner

    def on_zero(self, src, crit):
        if self.second_heart: self.second_heart = False; self.hp = self.maxhp; return
        self.out = True

    def on_missed(self, fight, att, melee):
        if melee and self.reaction and self.dice > 1 and self.alive() and not self.incapacitated():
            self.reaction = False; self.dice -= 1           # Riposte
            fight.after_turn(lambda: att.alive() and self.alive() and self.blade(fight, att, die=True))

    def on_miss(self, fight, tgt, total, ac, melee):
        # Precision Attack: a d10 when it would turn the miss into a hit
        if self.dice > 1 and total + 10 >= ac:
            self.dice -= 1
            if total + d(10) >= ac:
                tgt.take(tgt.reduce_hit(roll(1, 10) + 5, melee), self.weapon_type(), self.name, from_attack=True, melee=melee)

    # ---------- attacks ----------
    def weapon_type(self): return "lightning" if self.scalpel else "slashing"

    def blade(self, fight, tgt, die=False, leap=False):
        cr = 18 if self.sandy > 0 else 20
        def dmg(crit):
            c = crit or leap or self.weak_point
            v = roll(2 if c else 1, 10) + 8
            if die: v += roll(2 if c else 1, 10)
            return v
        def extra(crit, dealt, t=tgt):
            if crit or t.out: self.leap = True                  # Jailbreak charge
            if t.out and self.sandy > 0: self.sandy += 1        # kills stretch the Sandevistan
        hit, crit, dealt = attack(fight, self, tgt, 14, dmg, self.weapon_type(), True, crit_range=cr, sneak=5, extra=extra)
        if hit: self.invisible = False; self.weak_point = False       # a blade gives away where he is
        return hit

    def attack_action(self, fight, tgt):
        for i in range(3 if self.scalpel else 4):      # two Mantis Blades: Nick adds a fourth
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: return None
            self.blade(fight, tgt)
            if fight.over(): return None
        return tgt

    # ---------- quickhacks ----------
    def upload(self, fight, tgt, which, cost):
        if self.ram < cost or not tgt.alive(): return False
        self.ram -= cost
        tgt.on_targeted_by_spell(fight, self)        # Smasher's ICE hacks back
        if not self.alive() or not tgt.alive() or tgt.negates_spells(): return True
        if self.invisible: tgt.ambushed = True       # Magical Ambush
        if which == "short":
            dmg = roll(6, 10) + (roll(2, 10) if tgt.name == "Smasher" else 0)       # extra against a full-body borg
            tgt.take(dmg // (2 if tgt.save("Con", DC, spell=True) else 1), "lightning", "Short Circuit")
        elif which == "overheat":
            if tgt.save("Con", DC, spell=True): tgt.take(roll(3, 10) // 2, "fire", "Overheat")
            else:
                tgt.take(roll(3, 10), "fire", "Overheat")
                def burn(t, n=[2]):
                    t.take(roll(2, 10), "fire", "Overheat"); n[0] -= 1
                    return n[0] > 0
                tgt.effects.append(burn)
        elif which == "burnout":
            dmg = roll(8, 10) + (roll(2, 10) if tgt.hp < tgt.maxhp // 2 else 0)
            tgt.take(dmg // (2 if tgt.save("Int", DC, spell=True) else 1), "psychic", "Synapse Burnout")
        elif which == "contagion":
            for e in [tgt] + [x for x in fight.enemies(self) if x is not tgt][:1]:
                if not e.poison_immune:
                    saved = e.save("Con", DC, spell=True)
                    e.take(roll(3, 8) // (2 if saved else 1), "poison", "Contagion")
                    if not saved: e.poisoned = True
        elif which == "optics":
            if not tgt.save("Con", DC, spell=True):
                tgt.dread = True
                def clear(t): t.dread = False; return False
                tgt.effects.append(clear)
        elif which == "glitch":
            tgt.sapped = True
        elif which == "blackwall":
            for e in [tgt] + [x for x in fight.enemies(self) if x is not tgt][:2]:
                saved = e.save("Con", DC, spell=True)
                e.take(roll(8, 10) // (2 if saved else 1), "necrotic", "Blackwall Gateway")
        return True

    def deck_turn(self, fight, tgt):
        self.ram = min(20, self.ram + 4)
        enemies = fight.enemies(self)
        # the queue: Blackwall for a crowd, Synapse Burnout and Short Circuit for one
        if len(enemies) >= 2 and self.ram >= 8:
            self.upload(fight, tgt, "blackwall", 8)
        elif self.ram >= 6:
            self.upload(fight, tgt, "burnout", 5); self.upload(fight, tgt, "short", 1)
        elif self.ram >= 3 and not tgt.burning:
            self.upload(fight, tgt, "overheat", 3)
        else:
            tgt = self.attack_action(fight, tgt)
        return tgt

    # ---------- the turn ----------
    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        self.weak_point = True          # Vulnerability Analytics: one weak point a turn
        bonus = False
        if self.os == "deck" and self.camo and not self.invisible:
            self.camo -= 1; self.invisible = True; bonus = True           # Optical Camo, and Emergency Cloaking keeps it
        if self.os == "sandy":
            if self.sandy > 0: self.sandy -= 1
            if self.sandy == 0 and self.sandy_ready > 0: self.sandy_ready -= 1
            if self.sandy == 0 and self.sandy_ready == 0:
                self.sandy = 3; self.sandy_ready = 4; bonus = True
                fight.speeds_up(self)
                for e in [e for e in fight.enemies(self) if e.melee]:      # Ticking Time Bomb
                    if not e.never_stunned and not e.stun_immune and not e.save("Con", DC):
                        e.paralyzed = True; e.stun_until = fight.round
        if not bonus and self.hp <= 90 and self.sw > 0:
            self.sw -= 1; self.hp = min(self.maxhp, self.hp + d(10) + 11); bonus = True
        actions = 1 + (1 if self.surge else 0) + (1 if self.sandy > 0 else 0); self.surge = 0
        for a in range(actions):
            if tgt is None or tgt.out: tgt = fight.pick_target(self)
            if not tgt: return
            if self.os == "deck" and a == 0: tgt = self.deck_turn(fight, tgt)
            else: tgt = self.attack_action(fight, tgt)
            if fight.over() or tgt is None: return
        if not bonus:
            if tgt is None or tgt.out: tgt = fight.pick_target(self)
            if not tgt: return
            if self.leap:
                self.leap = False; self.blade(fight, tgt, leap=True)          # Jailbreak leap: a hit is a critical
            elif self.os == "deck" and self.ram >= 2:
                self.upload(fight, tgt, "glitch" if tgt.danger >= 5 else "short", 2)

    def end_turn(self, fight):
        super().end_turn(fight)
        self.tuned = False              # Reflex Tuner's slow lasts until the end of his next turn
