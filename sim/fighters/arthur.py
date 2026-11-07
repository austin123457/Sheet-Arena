"""Arthur Morgan, Caleb's sheet: Fighter (Dead Eye) 19 / Rogue 1, on open sand (no cover).
223 HP, AC 16, Schofield shots at +13; Dead Eye gives advantage and crits on 18-20, Painting empties
the bar into one target, Fatal Areas kills on a crit under 50, Peerless Aim turns one miss a turn into a hit."""
from ..engine import Combatant, attack, d, roll


class Arthur(Combatant):
    name = "Arthur"; danger = 3

    def __init__(self, cover=0):
        super().__init__()
        self.hp = self.maxhp = 223; self.ac = 16 + cover
        self.saves = dict(Str=9, Dex=5, Con=9, Int=0, Wis=1, Cha=0); self.indomitable = 3; self.indom_bonus = 19
        self.boxes = 6; self.deadeye = False; self.surges = 2; self.sw = 4; self.snake = 2; self.cures = 3; self.potent = 1; self.miracle = 1
        self.refund_turn = -1; self.prowess = True

    def init(self): return d(20) + 11

    def shot(self, fight, tgt, sa_ok):
        def dmg(crit):
            v = roll(4 if crit else 2, 6) + 5
            if sa_ok and not self.sa_used: v += roll(2 if crit else 1, 6); self.sa_used = True
            return v
        def extra(crit, dealt, t=tgt):
            if dealt and self.deadeye and crit and 0 < (t.hp + t.thp) <= 50 and not t.out:
                t.hp = 0; t.on_zero("Arthur", True)                # Fatal Areas
            if dealt and (crit or t.out) and self.refund_turn != fight.round:
                self.refund_turn = fight.round; self.boxes = min(6, self.boxes + 1)
        cr = 18 if self.deadeye else 20
        hit, crit, dealt = attack(fight, self, tgt, 13, dmg, "piercing", melee=False, adv=self.deadeye, crit_range=cr, extra=extra)
        if not hit and self.prowess:
            self.prowess = False
            tgt.take(dmg(False), "piercing", "Arthur", from_attack=True, melee=False)   # Peerless Aim
            return True
        return hit

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        self.prowess = True; self.sa_used = False
        if self.deadeye:
            if self.boxes > 0: self.boxes -= 1
            else: self.deadeye = False
        # bonus action
        if self.hp <= 100 and self.sw > 0: self.sw -= 1; self.hp = min(self.maxhp, self.hp + d(10) + 19)
        elif self.boxes == 0 and not self.deadeye and self.snake > 0: self.snake -= 1; self.boxes = 3
        elif not self.deadeye and self.boxes >= 1:
            self.boxes -= 1; self.deadeye = True; self.shot(fight, tgt, True)          # the free shot
            if fight.over(): return
        elif self.hp <= 150 and self.miracle: self.miracle = 0; self.hp = min(self.maxhp, self.hp + roll(4, 4) + 4); self.boxes = min(6, self.boxes + 2)
        elif self.hp <= 150 and self.potent: self.potent = 0; self.hp = min(self.maxhp, self.hp + roll(4, 4) + 4)
        elif self.hp <= 150 and self.cures: self.cures -= 1; self.hp = min(self.maxhp, self.hp + roll(2, 4) + 2)
        # action: Painting when he can afford a big turn, else four shots
        if self.deadeye and self.boxes >= 3 and self.surges > 0:
            n = self.boxes; self.boxes = 0
        else:
            n = 4
        for i in range(n):
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: return
            self.shot(fight, tgt, True)
            if fight.over(): return
        if self.surges > 0:
            self.surges -= 1
            for i in range(4):
                if tgt.out: tgt = fight.pick_target(self)
                if not tgt: return
                self.shot(fight, tgt, True)
                if fight.over(): return
