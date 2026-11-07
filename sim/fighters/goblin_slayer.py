"""Goblin Slayer: Human, Farmer, Fighter (Battle Master) 16 / Rogue (Scout) 4.
Sheet: Goblin_Slayer_5e_Build.pdf. 220 HP, AC 17, three shortsword attacks at +10."""
from ..engine import Combatant, attack, d, roll


class GoblinSlayer(Combatant):
    name = "GS"; danger = 1; melee = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 220; self.ac = 17
        self.saves = dict(Str=10, Dex=2, Con=9, Int=0, Wis=8, Cha=-1); self.indomitable = 2
        self.sw = 4; self.dice = 5; self.doses = 5; self.blade = True; self.hitdice = 10

    def init(self): return d(20) + 8 + d(10)

    def reduce_hit(self, dmg, melee):
        # Parry: a superiority die off a melee hit
        if melee and self.reaction and self.dice > 0:
            self.reaction = False; self.dice -= 1; return max(0, dmg - (d(10) + 4))
        return dmg

    def answer_standoff(self, fight, jin):
        attack(fight, self, jin, 10, lambda c: roll(2 if c else 1, 6) + 6, "piercing", True)

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        # bonus action: Second Wind when hurt, re-poison the blade, or a Durable Hit Die when it's bad
        bonus = None
        if self.hp <= 160 and self.sw > 0: self.sw -= 1; self.hp = min(self.maxhp, self.hp + d(10) + 16); bonus = "sw"
        elif not self.blade and self.doses > 0 and not tgt.poison_immune: self.doses -= 1; self.blade = True; bonus = "poison"
        elif self.hp <= 120 and self.hitdice > 0: self.hitdice -= 1; self.hp = min(self.maxhp, self.hp + d(10) + 3); bonus = "hd"
        steady = (bonus is None and fight.round > 1)     # Steady Aim when the bonus action is free
        n = 3 + (3 if (fight.round == 1 and not self.surge_used) else 0); self.surge_used = True
        first_hit = False
        for i in range(n):
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: break
            adv = steady and i == 0
            def dmg(crit): return roll(2 if crit else 1, 6) + 6
            def extra(crit, dealt, t=tgt):
                nonlocal first_hit
                if dealt and self.blade and not t.poison_immune:
                    self.blade = False
                    if not t.save("Con", 14): t.take(roll(2, 8), "poison", "GS"); t.poisoned = True
                if dealt and not first_hit and not t.susanoo:      # Shield Master rim
                    first_hit = True
                    if not t.save("Str", 18): t.prone = True
            attack(fight, self, tgt, 10, dmg, "piercing", True, adv=adv, sneak=2, extra=extra)
            if fight.over(): return
