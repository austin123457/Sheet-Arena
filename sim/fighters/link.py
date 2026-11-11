"""Link, the Hero of Time. Sheet: Hero_of_Time_5e_Build.pdf.
224 HP, AC 20, the Master Sword at +14 (extra against evil), Nayru's Love (immune to everything
that doesn't ignore immunity), two fairies, Deku Nuts, the Triforce of Courage on a failed save.
The Fierce Deity's Mask only works in a boss's lair, so he never has it here."""
from ..engine import Combatant, attack, d, roll


class Link(Combatant):
    name = "Link"; danger = 5; melee = True
    fright_immune = True; one_handed = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 224; self.ac = 20
        self.saves = dict(Str=8, Dex=5, Con=9, Int=0, Wis=3, Cha=-1); self.indomitable = 3
        self.magic = 12; self.nayru = 0; self.fairies = 2; self.red = 1; self.blue = 1; self.surges = 2; self.sw = 4
        self.dice = 6; self.nuts = 10; self.triforce = True

    def init(self): return d(20) + 11

    def save(self, ab, dc, spell=False, kind=None, adv=False):
        ok = super().save(ab, dc, spell, kind, adv)
        if not ok and self.triforce: self.triforce = False; ok = True
        return ok

    def immune(self, dtype): return self.nayru > 0

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        if from_attack and not melee and self.reaction: self.reaction = False; dmg = max(0, dmg - (d(10) + 11))
        elif from_attack and melee and self.reaction and self.dice > 0: self.reaction = False; self.dice -= 1; dmg = max(0, dmg - (d(12) + 5))
        return dmg

    def on_zero(self, src, crit):
        if self.fairies > 0: self.fairies -= 1; self.hp = 90; return
        self.out = True

    def on_massive(self, src): self.on_zero(src, False)      # a fairy in a bottle brings you back from dead, too

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        if self.nayru > 0: self.nayru -= 1
        # bonus action: potions
        if self.hp <= 80 and self.red: self.red = 0; self.hp = self.maxhp
        elif self.hp <= 80 and self.blue: self.blue = 0; self.hp = self.maxhp; self.magic = 12
        elif self.hp <= 120 and self.sw > 0: self.sw -= 1; self.hp = min(self.maxhp, self.hp + d(10) + 20)
        actions = 1 + (1 if self.surges > 0 else 0)
        if self.surges > 0: self.surges -= 1
        for a in range(actions):
            if self.nayru == 0 and self.magic >= 3 and tgt.danger >= 4:
                self.magic -= 3; self.nayru = 10; continue      # Nayru's Love takes the action
            first = False
            for i in range(4):
                if tgt.out: tgt = fight.pick_target(self)
                if not tgt: return
                # a Deku Nut on the first attack of the action when the target is upright and stunnable
                if i == 0 and self.nuts > 0 and not tgt.paralyzed and not tgt.never_stunned and not tgt.stun_immune:
                    self.nuts -= 1
                    if not tgt.save("Con", 18): tgt.paralyzed = True; tgt.stun_until = fight.round
                    continue
                prone = tgt.prone
                use_die = self.dice > 0 and not first
                def dmg(crit, d_=use_die, t=tgt):
                    v = roll(2 if crit else 1, 8) + 10
                    if d_: v += roll(2 if crit else 1, 12)
                    if t.evil: v += roll(4 if crit else 2, 8)
                    return v
                def extra(crit, dealt, t=tgt, d_=use_die):
                    if dealt and d_:
                        self.dice -= 1
                        if not t.prone and not t.susanoo and not t.save("Str", 19): t.prone = True
                adv = tgt.paralyzed or tgt.prone or tgt.reckless
                hit, crit, dealt = attack(fight, self, tgt, 14, dmg, "slashing", True, adv=adv, crit_range=1 if prone else 20, extra=extra)
                if hit: first = True
                if fight.over(): return
