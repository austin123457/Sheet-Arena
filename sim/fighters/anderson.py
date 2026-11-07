"""Alexander Anderson, the Paladin. Sheet: Alexander_Anderson_5e_Build.pdf.
284 HP, AC 17, regenerates 30 a turn (60 with the Nail) and gets back up from 0 unless 20 radiant
or fire stopped it; Haste, Hold Monster, Divine Smite and Radiant Strikes on bayonets.
The Nail of Helena is a desperation move once he's been dropped three times."""
from ..engine import Combatant, attack, d, roll


class Anderson(Combatant):
    name = "Anderson"; danger = 6; melee = True
    fright_immune = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 284; self.ac = 17
        self.saves = dict(Str=9, Dex=9, Con=10, Int=3, Wis=12, Cha=14)
        self.radiant_taken = 0; self.haste = False; self.vow = None; self.slots = {5: 2, 4: 3, 3: 3, 2: 3, 1: 4}
        self.hold_used = False; self.nail = False; self.nail_broken = False; self.down_dmg = 0; self.times_down = 0

    def init(self): return d(20) + 11
    def ac_now(self): return self.ac + (2 if self.haste else 0)
    def save_adv(self, ab, spell): return ab == "Dex" and self.haste

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        if self.nail and dtype in ("slashing", "piercing", "bludgeoning") and not ignore_res: dmg //= 2
        if dtype in ("radiant", "fire"): self.radiant_taken += dmg
        if self.down: self.down_dmg += dmg
        return dmg

    def on_zero(self, src, crit):
        self.times_down += 1
        self.hp = 0; self.down = True

    def take(self, dmg, dtype, src, **kw):
        # Only three things kill him: a single blow for his full hit points, his heart torn out (nobody here
        # grapples), or the Nail. While the Nail is in him, only breaking it does.
        if self.down and not self.nail:     # a body that's already down only notices a blow that big
            self.down_dmg += dmg
            if dtype in ("radiant", "fire"): self.radiant_taken += dmg      # still keeps him from regrowing
            if dmg >= self.maxhp: self.out = True
            return dmg
        r = super().take(dmg, dtype, src, **kw)
        if not self.nail and r >= self.maxhp: self.out = True
        if self.down and self.nail and self.down_dmg >= 40: self.out = True; self.nail_broken = True
        return r

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        # regeneration
        if self.down:
            if self.radiant_taken >= 20:
                self.radiant_taken = 0; return             # nothing regrows this turn
            self.down = False; self.hp = 60 if self.nail else 30; self.down_dmg = 0; self.radiant_taken = 0
            self.prone = False
        else:
            self.hp = min(self.maxhp, self.hp + (60 if self.nail else 30)); self.radiant_taken = 0
        if self.vow is None: self.vow = tgt
        # the Nail: desperation
        if not self.nail and self.times_down >= 3 and (tgt.hp + tgt.thp) > 0.5 * tgt.maxhp:
            self.nail = True; self.hp = min(284, self.hp + 60); return
        if not self.haste and self.slots[3] > 0 and not (tgt.saves.get("Wis", 0) <= 3 and not self.hold_used and self.slots[5] > 0):
            self.slots[3] -= 1; self.haste = True; return
        # Hold Monster on a weak-willed target (not Smasher, whose Mage Slayer and advantage eat it)
        if not self.hold_used and tgt.saves.get("Wis", 0) <= 3 and self.slots[5] > 0 and not tgt.paralyzed and tgt.name != "Smasher":
            self.hold_used = True; self.slots[5] -= 1
            if not tgt.save("Wis", 18, spell=True): tgt.paralyzed = True
            return
        if self.nail:
            for e in fight.enemies(self):
                if e.melee and not e.out: e.take(roll(2, 8), "radiant", "Holy Thorns")
        n = 3 + (1 if self.haste else 0)
        smited = False
        for i in range(n):
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: return
            adv = (tgt is self.vow) or tgt.paralyzed
            def dmg(crit, sm=not smited, nail=self.nail):
                v = (roll(4 if crit else 2, 8) + 5) if nail else (roll(2 if crit else 1, 6) + 5)
                v += roll(2 if crit else 1, 8)           # Radiant Strikes
                if sm:
                    lvl = next((L for L in (5, 4, 3, 2, 1) if self.slots[L] > 0), None)
                    if lvl: self.slots[lvl] -= 1; v += roll((2 + lvl - 1) * (2 if crit else 1), 8)
                return v
            hit, crit, dealt = attack(fight, self, tgt, 11, dmg, "radiant", True, adv=adv, crit_range=1 if tgt.paralyzed else 20)
            if hit: smited = True
            if fight.over(): return
