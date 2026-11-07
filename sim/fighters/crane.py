"""Kyle Crane, the first sheet (command-line name crane-old). The retuned Beast Mode
version in crane_beast.py is the one on the roster."""
from ..engine import Combatant, attack, d, d20, roll


class Crane(Combatant):
    name = "Crane"; danger = 2; melee = True
    evasion = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 227; self.ac = 16
        self.saves = dict(Str=11, Dex=3, Con=9, Int=-1, Wis=0, Cha=-1)
        self.raging = False; self.fury = 6; self.rel_dc = 10; self.greater = 2; self.potions = 4; self.sw = 2; self.surge = True

    def init(self): return d20(adv=True) + 3
    def save_adv(self, ab, spell): return ab == "Dex" or (ab == "Str" and self.raging)

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        if self.raging and dtype in ("slashing", "piercing", "bludgeoning") and not ignore_res: dmg //= 2
        if from_attack and self.reaction and not self.paralyzed:
            self.reaction = False; dmg //= 2
        return dmg

    def after_damage(self, dmg, dtype, src, melee):
        if self.raging and self.surge and 0 < self.hp < 113: self.surge = False; self.hp = min(self.maxhp, self.hp + 44)

    def on_zero(self, src, crit):
        if self.raging and d(20) + 9 >= self.rel_dc: self.rel_dc += 5; self.hp = 22; return
        self.out = True

    def answer_standoff(self, fight, jin):
        attack(fight, self, jin, 11, lambda c: roll(2 if c else 1, 6) + 8, "slashing", True)

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        bonus = False
        if not self.raging: self.raging = True; self.reckless = True; bonus = True
        if not bonus:
            if self.hp <= 150 and self.greater: self.greater -= 1; self.hp = min(self.maxhp, self.hp + roll(4, 4) + 4)
            elif self.hp <= 150 and self.potions: self.potions -= 1; self.hp = min(self.maxhp, self.hp + roll(2, 4) + 2)
            elif self.hp <= 150 and self.sw: self.sw -= 1; self.hp = min(self.maxhp, self.hp + d(10) + 1)
        first = False
        for i in range(3):
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: break
            brutal = (i == 2) and not self.disadv_attacks and not self.poisoned
            def dmg(crit, sav=not first, br=brutal):
                w = roll(2 if crit else 1, 6)
                if sav: w = max(w, roll(2 if crit else 1, 6))
                return w + 8 + (roll(2 if crit else 1, 10) if br else 0)
            def extra(crit, dealt, t=tgt):
                if dealt:
                    self.hp = min(self.maxhp, self.hp + 6)
                    if self.fury > 0 and not t.out:
                        self.fury -= 1
                        if not t.save("Wis", 17, spell=True): t.take(roll(4 if crit else 2, 12), "psychic", "Fury")
            hit, crit, dealt = attack(fight, self, tgt, 11, dmg, "slashing", True, adv=not brutal, extra=extra)
            if hit: first = True
            if fight.over(): return
