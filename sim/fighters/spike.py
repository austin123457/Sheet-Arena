"""Spike Spiegel: Human, Criminal, Monk (Open Hand) 14 / Rogue (Assassin) 6. Sheet: Spike_Spiegel_5e_Build.pdf.
183 HP, AC 17, two Jericho rounds with Sneak Attack, then a Flurry with Stunning Strike and Topple;
Deflect on every attack, Lucky (six points, shared between attacks and saves) and Nine Lives once."""
from ..engine import Combatant, attack, d, d20, roll


class Spike(Combatant):
    name = "Spike"; danger = 3; melee = True
    evasion = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 183; self.ac = 17
        self.saves = dict(Str=6, Dex=11, Con=8, Int=6, Wis=8, Cha=6)
        self.focus = 14; self.luck = 6; self.nine = True; self.wob = 4

    def init(self): return d20(adv=True) + 11

    def save(self, ab, dc, spell=False, kind=None, adv=False):
        ok = super().save(ab, dc, spell, kind, adv)
        if not ok and self.focus > 0: self.focus -= 1; ok = d20() + self.saves[ab] >= dc
        if not ok and self.luck > 0: self.luck -= 1; ok = d20(adv=True) + self.saves[ab] >= dc
        return ok

    def incoming_attack(self, attacker, bonus, adv, dis, melee=True):
        # Lucky: if a straight roll would hit, spend a point to give the attack disadvantage
        if self.luck > 0 and not dis:
            nat = d20(adv=adv)
            if nat + bonus >= self.ac_now() and nat != 1:
                self.luck -= 1; dis = True; adv = False
        return adv, dis

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        if from_attack and self.reaction: self.reaction = False; dmg = max(0, dmg - (d(10) + 19))
        return dmg

    def on_zero(self, src, crit):
        if self.nine: self.nine = False; self.hp = 1; return
        self.out = True

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        if self.hp <= 90 and self.wob > 0: self.wob -= 1; self.hp = min(self.maxhp, self.hp + roll(2, 10) + 2)
        first_round = fight.round == 1 and not tgt.acted
        adv = first_round or tgt.reckless or tgt.prone or tgt.paralyzed
        sa = True
        for i in range(2):      # the Jericho
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: return
            def dmg(crit): return roll(2 if crit else 1, 10) + 5
            def extra(crit, dealt, t=tgt, fr=first_round):
                nonlocal sa
                if dealt and sa and adv: t.take(roll(6 if crit else 3, 6) + (6 if fr else 0), "piercing", "Spike"); sa = False
            attack(fight, self, tgt, 11, dmg, "piercing", melee=False, adv=adv, extra=extra)
            if fight.over(): return
        if self.focus > 0:          # Flurry of three, Stunning Strike on the first hit, Topple on the rest
            self.focus -= 1; stunned = False
            for i in range(3):
                if tgt.out: tgt = fight.pick_target(self)
                if not tgt: return
                def dmg(crit): return roll(2 if crit else 1, 10) + 5
                def extra(crit, dealt, t=tgt):
                    nonlocal stunned
                    if dealt and not stunned and self.focus > 0 and not t.never_stunned and not t.shrugs_stunning_strike and not t.stun_immune and not t.paralyzed:
                        self.focus -= 1; stunned = True
                        if not t.save("Con", 16): t.paralyzed = True; t.stun_until = fight.round
                    elif dealt and not t.prone and not t.susanoo and not t.save("Dex", 16): t.prone = True
                attack(fight, self, tgt, 11, dmg, "bludgeoning", True, adv=(tgt.reckless or tgt.prone or tgt.paralyzed), extra=extra)
                if fight.over(): return
