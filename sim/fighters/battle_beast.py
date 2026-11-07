"""Battle Beast. 265 HP, AC 19, raging and reckless, +16 for 4d6+20 that ignores resistance (not
immunity), Graze on a miss, crits on 19 against the one he names Worthy, Str saves he can't fail,
Frightful Presence, Relentless Rage, and Guts's reaction swing."""
from ..engine import Combatant, attack, d, d20, roll


class BattleBeast(Combatant):
    name = "Beast"; melee = True
    # NOTE: the old engine renamed him "Guts" for the whole fight to borrow the reaction swing, so he
    # also picked up Guts's danger (5, not the intended 6), stun-proofing and answer to Jin's Standoff.
    # All three are kept here as they were.
    danger = 5
    never_stunned = True; retaliates = True
    charm_immune = True; fright_immune = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 265; self.ac = 19
        self.saves = dict(Str=14, Dex=0, Con=12, Int=0, Wis=1, Cha=-1)
        self.raging = False; self.rel_dc = 10; self.hew = False; self.worthy = None; self.presence = True

    def init(self): return d20(adv=True) + 0
    def save_adv(self, ab, spell): return ab == "Dex" or (ab == "Str" and self.raging)

    def save(self, ab, dc, spell=False):
        if ab == "Str": return True if 27 >= dc else super().save(ab, dc, spell)
        return super().save(ab, dc, spell)

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        if self.raging and dtype in ("slashing", "piercing", "bludgeoning") and not ignore_res: return dmg // 2
        if dtype == "cold": return dmg // 2
        return dmg

    def on_zero(self, src, crit):
        if self.raging and d(20) + 12 >= self.rel_dc: self.rel_dc += 5; self.hp = 40; return
        self.rel_dc += 5; self.out = True

    def retaliate(self, fight, att):
        if self.reaction and att.alive() and self.raging:
            self.reaction = False; self.swing(fight, att, adv=True, frenzy=False, savage=True, can_hew=False)

    def answer_standoff(self, fight, jin):
        self.raging = True; self.reckless = True; self.swing(fight, jin, True, True, True)

    def swing(self, fight, tgt, adv, frenzy, savage, brutal=False, can_hew=True):
        def dmg(crit):
            n = 8 if crit else 4
            w = roll(n, 6)
            if savage: w = max(w, roll(n, 6))
            v = w + (20 if self.raging else 16)
            if frenzy: v += roll(8 if crit else 4, 6)
            if brutal: v += roll(4 if crit else 2, 10)
            return v
        cr = 19 if (tgt is self.worthy) else 20
        hit, crit, dealt = attack(fight, self, tgt, 16, dmg, "slashing", True, adv=adv, crit_range=cr, ignore_res=True)
        if not hit and not tgt.out: tgt.take(8, "slashing", "Graze", ignore_res=True)
        if crit and can_hew: self.hew = True
        return hit

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        bonus = False
        if not self.raging:
            self.raging = True; self.reckless = True; bonus = True
            self.worthy = max(fight.enemies(self), key=lambda e: e.danger)
        elif self.presence and not tgt.fright_immune and tgt.name not in ("Guts", "Smasher", "Link", "Slayer", "GuyC"):
            self.presence = False; bonus = True
            if not tgt.save("Wis", 22): tgt.frightened = True
        if self.worthy is not None and not self.worthy.out: tgt = self.worthy
        first = False
        for i in range(2):
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: break
            brutal = (i == 1) and not self.poisoned and not self.disadv_attacks
            hit = self.swing(fight, tgt, adv=not brutal, frenzy=not first, savage=not first, brutal=brutal)
            if hit: first = True
            if fight.over(): return
        if not bonus and self.hew and tgt and not tgt.out: self.hew = False; self.swing(fight, tgt, True, False, False, can_hew=False)
        self.hew = False
