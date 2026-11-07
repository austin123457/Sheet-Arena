"""Might Guy, Austin's sheet (command-line name guy-mine). Sheet: Might_Guy_5e_Build.pdf.
203 HP, AC 21, opens the gates as the fight demands; the Eighth keeps him at 1 HP for ten rounds
and then kills him, and Night Guy ends it either way."""
from ..engine import Combatant, attack, d, d20, roll


class Guy(Combatant):
    name = "Guy"; danger = 7; melee = True
    averts_eyes = True; monk_evasion = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 203; self.ac = 21
        self.saves = dict(Str=7, Dex=13, Con=9, Int=5, Wis=10, Cha=5)
        self.focus = 20; self.gate = 0; self.gate8_turn = None; self.night_used = False; self.sup_def = False
        self.dead_after = False; self.tiger_used = False

    def init(self): return d(20) + 7
    def ac_now(self): return self.ac + (2 if self.gate >= 5 else 0)

    def save(self, ab, dc, spell=False):
        ok = super().save(ab, dc, spell)
        if not ok and self.focus > 0:
            self.focus -= 1; ok = d20() + self.saves[ab] >= dc
        return ok

    def incoming_attack(self, attacker, bonus, adv, dis):
        if self.gate >= 7: dis = True          # the Seventh Gate: attacks against him have disadvantage
        return adv, dis

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        if self.sup_def and dtype != "force" and not ignore_res: dmg //= 2
        if from_attack and self.reaction:
            self.reaction = False; dmg = max(0, dmg - (d(10) + 27))
        return dmg

    def take(self, dmg, dtype, src, **kw):
        if self.gate >= 8 and src != "gate":
            r = super().take(dmg, dtype, src, **kw)
            if self.hp <= 0: self.hp = 1; self.out = False
            return r
        return super().take(dmg, dtype, src, **kw)

    def on_zero(self, src, crit):
        if self.gate >= 8: self.hp = 1; return
        self.out = True

    def gate_dice(self):
        return 6 if self.gate >= 8 else 3 if self.gate >= 7 else 2 if self.gate >= 6 else 1 if self.gate >= 3 else 0

    def to_hit(self):
        return 13 + (5 if self.gate >= 8 else 4 if self.gate >= 7 else 2 if self.gate >= 5 else 0)

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        # the gates' bill
        if self.gate >= 8:
            if fight.round - self.gate8_turn >= 10 or self.dead_after: self.out = True; return
        elif self.gate >= 7: self.hp -= roll(3, 10)
        elif self.gate >= 6: self.hp -= roll(2, 10)
        elif self.gate >= 4: self.hp -= d(10)
        if self.hp <= 0: self.out = True; return
        # open gates: 6 on turn 1 (7 against the worst), 7 if the target is still healthy, 8 if losing
        if self.gate < 6: self.gate = 7 if tgt.danger >= 5 else 6; self.hp = min(self.maxhp, self.hp + 20)
        elif self.gate < 7 and (tgt.hp + tgt.thp) > 0.4 * tgt.maxhp: self.gate = 7
        elif self.gate < 8 and self.hp < 70 and (tgt.hp + tgt.thp) > 0.15 * tgt.maxhp:
            self.gate = 8; self.gate8_turn = fight.round; self.stun_immune = True
        if not self.sup_def and self.focus >= 3: self.sup_def = True; self.focus -= 3
        hit_bonus = self.to_hit()
        gd = self.gate_dice()
        if self.gate >= 8:
            if not self.night_used and (tgt.hp + tgt.thp) <= 250:
                self.night_used = True; self.dead_after = True
                dmg = roll(30, 12)
                if tgt.save("Con", 25): dmg //= 2
                tgt.take(dmg, "force", "Night Guy", ignore_res=True, ignore_imm=True)
                return
            # Evening Elephant
            for k in range(1, 6):
                if tgt.out: tgt = fight.pick_target(self)
                if not tgt: return
                attack(fight, self, tgt, 18, (lambda crit, kk=k: roll(4 * kk * (2 if crit else 1), 12)), "force", True, adv=True)
                if fight.over(): return
            return
        if self.gate >= 7 and not self.tiger_used and (tgt.hp + tgt.thp) > 120:
            self.tiger_used = True; self.hp -= roll(4, 10)
            if self.hp <= 0: self.out = True; return
            dmg = roll(20, 10)
            if tgt.save("Con", 18): dmg //= 2
            else: tgt.prone = True
            tgt.take(dmg, "force", "Daytime Tiger")
            if fight.over(): return
            strikes = 3
        elif self.gate >= 6:
            strikes = 6 + 3  # Morning Peacock + Flurry
            tgt.reaction = False
        else:
            strikes = 3 + 3
        self.focus = max(0, self.focus - 1)
        first = False
        for i in range(strikes):
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: return
            peacock = (self.gate >= 6 and i < 6)
            def dmg(crit, sav=not first, pk=peacock, g=gd):
                w = roll(2 if crit else 1, 12)
                if sav: w = max(w, roll(2 if crit else 1, 12))
                v = w + 7
                if g: v += roll(g * (2 if crit else 1), 12)
                if pk: v += roll(4 if crit else 2, 6)
                return v
            def extra(crit, dealt, t=tgt, i=i):
                # Stunning Strike on the first hit (stunned until the end of its next turn), Topple after
                if dealt and not first and self.focus > 0 and not t.stun_immune and not t.never_stunned and not t.shrugs_stunning_strike and not t.paralyzed:
                    self.focus -= 1
                    if not t.save("Con", 18): t.paralyzed = True
                    t.stun_until = fight.round
                if dealt and i >= 1 and not t.prone and not t.susanoo:
                    if not t.save("Dex", 18): t.prone = True
            hit, crit, dealt = attack(fight, self, tgt, hit_bonus, dmg, "bludgeoning", True, extra=extra)
            if hit: first = True
            if fight.over(): return
