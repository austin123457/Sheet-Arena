"""Might Guy, Caleb's sheet (command-line name guy-caleb): Monk (Warrior of the Eight Gates) 20.
263 HP, AC 19, seven gates open on turn one, Morning Peacock and Flurry with Stunning Strike;
the Eighth Gate below 70 HP for Evening Elephant, then Night Guy on the next turn, then he dies."""
from ..engine import Combatant, attack, d, d20, roll


class GuyCaleb(Combatant):
    name = "Guy2"; danger = 7; melee = True
    averts_eyes = True; monk_evasion = True
    # NOTE: the sheet's Night Guy is 20d12+15; the canon merge's 60d12+15 replaced it for this sheet too
    night_dice = 60
    g8_adv = False      # advantage on Evening Elephant

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 263; self.ac = 19
        self.saves = dict(Str=9, Dex=13, Con=10, Int=6, Wis=8, Cha=5)
        self.focus = 20; self.gate = 0; self.sup_def = False; self.g8 = None; self.night_used = False

    def init(self): return d(20) + 13
    def ac_now(self): return self.ac + (2 if self.gate >= 4 else 0)

    def save(self, ab, dc, spell=False):
        ok = super().save(ab, dc, spell)
        if not ok and self.focus > 0:
            self.focus -= 1; ok = d20(adv=(ab == "Str" and self.gate >= 1)) + self.saves[ab] >= dc
        return ok

    def incoming_attack(self, attacker, bonus, adv, dis):
        if self.gate >= 7: dis = True
        return adv, dis

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        if (self.sup_def and dtype != "force" or self.gate >= 8) and not ignore_res: dmg //= 2
        if from_attack and self.reaction:
            self.reaction = False; dmg = max(0, dmg - (d(10) + 27))
        return dmg

    def dmg_bonus(self): return 7 + (8 if self.gate >= 8 else self.gate)

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        if self.g8 == "spent": self.out = True; return          # the Gate of Death closed: 0 HP, dying
        if 1 <= self.gate <= 7:
            self.hp -= (14 if self.gate >= 6 else self.gate)
            if self.hp <= 0: self.out = True; return
        bonus = None
        if self.gate == 0:
            self.gate = 7; bonus = "gates"
        elif self.gate == 7 and self.hp < 70 and (tgt.hp + tgt.thp) > 0.15 * tgt.maxhp:
            self.gate = 8; self.g8 = fight.round; self.stun_immune = True; bonus = "gates"
        if not self.sup_def and self.focus >= 3: self.sup_def = True; self.focus -= 3
        if self.gate >= 8:
            if self.g8 == fight.round:
                for k in range(1, 6):      # Evening Elephant
                    if tgt.out: tgt = fight.pick_target(self)
                    if not tgt: return
                    attack(fight, self, tgt, 13, (lambda crit, kk=k: roll(kk * (2 if crit else 1), 12) + 15), "force", True, adv=self.g8_adv, crit_range=19, ignore_res=True)
                    if fight.over(): return
                return
            # Night Guy: automatic, unreducible, ignores immunity; then the Gate of Death closes
            self.night_used = True
            tgt.take(roll(self.night_dice, 12) + 15, "force", "Night Guy", ignore_res=True, ignore_imm=True)
            self.g8 = "spent"
            if fight.over(): return
            self.hp = 0; self.out = True
            return
        # seven gates: Morning Peacock (5 fire strikes, 2 Focus) + free Flurry (3) + Stunning Strike on the first hit
        peacock = self.focus >= 2
        if peacock: self.focus -= 2
        strikes = (5 if peacock else 3) + (3 if bonus is None else 0)
        first = False
        for i in range(strikes):
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: return
            is_pk = peacock and i < 5
            def dmg(crit, pk=is_pk, de=(fight.round == 1 and not first)):
                v = roll(2 if crit else 1, 12) + self.dmg_bonus()
                if de: v += d(8)
                return v
            def extra(crit, dealt, t=tgt, pk=is_pk, i=i):
                if dealt and not first and self.focus > 0 and not t.never_stunned and not t.shrugs_stunning_strike and not t.stun_immune and not t.paralyzed:
                    self.focus -= 1
                    if not t.save("Con", 16): t.paralyzed = True; t.stun_until = fight.round
                if dealt and not pk and not t.prone and not t.susanoo:
                    if not t.save("Dex", 16): t.prone = True
            hit, crit, dealt = attack(fight, self, tgt, 13, dmg, "fire" if is_pk else "bludgeoning", True, crit_range=19)
            if hit: first = True
            if fight.over(): return
