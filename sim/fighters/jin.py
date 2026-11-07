"""Jin Sakai, the Ghost. 215 HP, AC 19 (Deflect +6), a katana at +13 with Sneak Attack 5d6,
Heavenly Strike on Resolve, Last Stand once, Iron Will to keep getting up, and the Standoff."""
from ..engine import Combatant, attack, d, d20, roll


class Jin(Combatant):
    name = "Jin"; danger = 4; melee = True
    evasion = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 215; self.ac = 19
        self.saves = dict(Str=7, Dex=5, Con=9, Int=0, Wis=8, Cha=-1); self.indomitable = 1
        self.resolve = 8; self.fs = 3; self.sw = 4; self.last_stand = True; self.iron_n = 0; self.recover = 10
        self.doses = 6; self.blade = True; self.dd_up = False; self.surge = True; self.darts = 3

    def init(self): return d20(adv=True) + 11
    def ac_now(self): return self.ac + (6 if self.dd_up else 0)

    def defend_ac(self, att, total, melee, crit):
        if melee and self.reaction and not crit and total < self.ac + 6 and total >= self.ac:
            self.reaction = False; self.dd_up = True; self.resolve += 1; return 0
        return 0

    def reduce_hit(self, dmg, melee):
        if self.reaction:
            if melee: self.reaction = False; return dmg // 2
            red = d(10) + 16
            self.reaction = False
            return max(0, dmg - red) if red >= dmg // 2 else dmg // 2
        return dmg

    def start_turn(self):
        super().start_turn(); self.dd_up = False

    def on_zero(self, src, crit):
        if self.last_stand: self.last_stand = False; self.hp = 108; return
        if self.resolve >= 2:
            if self.iron_n == 0 or d(20) + 8 >= 10 + 5 * self.iron_n:
                self.resolve -= 2; self.iron_n += 1; self.hp = 22; return
        self.out = True

    @staticmethod
    def big_target(t): return t.name == "Smasher" or t.susanoo

    def before_first_round(self, fight):
        # the Standoff: one cut at the most dangerous enemy before initiative; lose it and he answers
        es = fight.enemies(self)
        if not es: return
        foe = max(es, key=lambda e: e.danger)
        if d20(adv=True) + 11 >= foe.init():
            def dmg(crit): return roll(2 if crit else 1, 10, gwf=True) + 7 + 9 + (roll(1, 10) if foe.name == "Smasher" else 0)
            attack(fight, self, foe, 13, dmg, "slashing", True, adv=True, crit_range=1, sneak=5)
            if foe.out: self.resolve += 3
        else:
            foe.answer_standoff(fight, self)

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        adv_turn = False
        if self.hp <= 100 and self.sw > 0: self.sw -= 1; self.hp = min(self.maxhp, self.hp + d(10) + 11)
        elif self.hp <= 100 and self.resolve > 3: self.resolve -= 1; self.hp = min(self.maxhp, self.hp + roll(2, 8) + 2)
        elif self.hp <= 100 and self.recover > 0: k = min(3, self.recover); self.recover -= k; self.hp = min(self.maxhp, self.hp + roll(k, 10))
        elif self.fs > 0 and (fight.round <= 2 or tgt.danger >= 4): self.fs -= 1; self.thp = max(self.thp, 10); adv_turn = True
        elif not self.blade and self.doses > 0 and not tgt.poison_immune: self.doses -= 1; self.blade = True
        else: adv_turn = "steady"
        n = 3 + (3 if self.surge else 0); self.surge = False
        first = False
        for i in range(n):
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: break
            # a sleep dart on the soft target, once
            if i == 0 and self.darts > 0 and tgt.name == "Itachi" and not tgt.poison_immune and not tgt.susanoo:
                self.darts -= 1
                if not tgt.save("Con", 19): tgt.asleep = True
                continue
            adv = adv_turn is True or (adv_turn == "steady" and i == 0) or (fight.round == 1 and not tgt.acted)
            heavenly = (not first) and self.resolve >= 3
            def dmg(crit, hv=heavenly, t=tgt):
                v = roll(2 if crit else 1, 10, gwf=True) + 7
                if hv: v += roll(6 if crit else 3, 10)
                if self.big_target(t): v += roll(2 if crit else 1, 10)
                if fight.round == 1 and not t.acted: v += 9
                return v
            def extra(crit, dealt, t=tgt, hv=heavenly):
                if dealt and hv: self.resolve -= 1
                if dealt and self.blade and not t.poison_immune:
                    self.blade = False
                    if not t.save("Con", 19): t.take(roll(2, 8), "poison", "Jin"); t.poisoned = True
                if dealt and t.asleep: t.asleep = False
            hit, crit, dealt = attack(fight, self, tgt, 13, dmg, "slashing", True, adv=adv, sneak=5, extra=extra)
            if hit: first = True
            if tgt.out: self.resolve += 1
            if fight.over(): return
