"""Kyle Crane, Caleb's retune (command-line name crane): Barbarian (Path of the Beast, homebrew) 14 /
Rogue (Thief) 5 / Fighter 1. Sheet addendum: Kyle_Crane_Beast_Mode_Addendum.pdf.
The Beast Meter starts empty after a rest and fills on hits, on being hit and on being missed;
at six it unleashes at full HP and stuns the melee crowd."""
from ..engine import Combatant, attack, d, d20, roll


class CraneBeast(Combatant):
    name = "Crane2"; danger = 2; melee = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 233; self.ac = 16
        self.saves = dict(Str=11, Dex=3, Con=9, Int=-1, Wis=0, Cha=-1)
        self.meter = 0; self.beast = False; self.rel_dc = 10; self.sw = 2; self.bandages = 4; self.rare = 2; self.morphine = 1
        self.regen = 0; self.dmg_boost = False; self.booster_used = False
        self.dmg_this_round = False; self.miss_this_round = False

    def init(self): return d20(adv=True) + 3
    def save_adv(self, ab, spell): return ab == "Dex" or (ab == "Str" and self.beast)

    def fill(self, n):
        if not self.beast: self.meter = min(6, self.meter + n)

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        if self.beast and dtype in ("slashing", "piercing", "bludgeoning") and not ignore_res: dmg //= 2
        if from_attack and self.reaction: self.reaction = False; dmg //= 2
        return dmg

    def after_damage(self, dmg, dtype, src, melee):
        if not self.dmg_this_round: self.dmg_this_round = True; self.fill(1)

    def defend_ac(self, att, total, melee, crit):
        if not crit and total < self.ac and not self.miss_this_round: self.miss_this_round = True; self.fill(1)
        return 0

    def on_zero(self, src, crit):
        if self.beast and d(20) + 9 >= self.rel_dc: self.rel_dc += 5; self.hp = 28; return
        self.out = True

    def start_turn(self):
        super().start_turn(); self.dmg_this_round = False; self.miss_this_round = False

    def unleash(self, fight, full):
        self.beast = True; self.reckless = True
        if full:
            self.hp = self.maxhp
            for e in fight.enemies(self):
                if e.melee and not e.out and not e.stun_immune and not e.never_stunned:
                    if not e.save("Con", 19): e.paralyzed = True; e.stun_until = fight.round

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        if self.regen > 0: self.regen -= 1; self.hp = min(self.maxhp, self.hp + 5)
        bonus = False
        if self.beast:
            self.meter -= 1
            if self.meter <= 0: self.beast = False; self.meter = 0
        if not self.beast and self.meter >= 6: self.unleash(fight, True); bonus = True
        elif not self.beast and self.meter >= 3 and self.hp < 80: self.unleash(fight, False); bonus = True
        if self.beast:
            first = False
            for i in range(3):
                if tgt.out: tgt = fight.pick_target(self)
                if not tgt: return
                brutal = (i == 2) and not self.disadv_attacks and not self.poisoned
                def dmg(crit, sav=not first, br=brutal):
                    w = roll(2 if crit else 1, 10)
                    if sav: w = max(w, roll(2 if crit else 1, 10))
                    return w + 8 + (2 if self.dmg_boost else 0) + (roll(2 if crit else 1, 10) if br else 0)
                def extra(crit, dealt, t=tgt):
                    if dealt:
                        self.hp = min(self.maxhp, self.hp + 7)
                        if 0 < t.hp + t.thp <= 15: t.hp = 0; t.on_zero("Crane2", False)
                hit, crit, dealt = attack(fight, self, tgt, 11, dmg, "slashing", True, adv=not brutal, extra=extra)
                if hit: first = True
                if fight.over(): return
            return
        # human form: the bonus action goes to the booster, then the medicine
        if not bonus:
            if self.regen == 0 and not self.booster_used: self.booster_used = True; self.regen = 10; self.dmg_boost = True; bonus = True
            elif self.hp <= 150 and self.rare > 0: self.rare -= 1; self.hp = min(self.maxhp, self.hp + roll(4, 8) + 8); bonus = True
            elif self.hp <= 150 and self.bandages > 0: self.bandages -= 1; self.hp = min(self.maxhp, self.hp + roll(2, 8) + 4); bonus = True
            elif self.hp <= 100 and self.morphine > 0: self.morphine -= 1; self.hp = min(self.maxhp, self.hp + roll(6, 8) + 12); bonus = True
            elif self.hp <= 150 and self.sw > 0: self.sw -= 1; self.hp = min(self.maxhp, self.hp + d(10) + 1); bonus = True
        self.reckless = True
        first = False
        for i in range(2):
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: break
            def dmg(crit, sav=not first):
                w = roll(2 if crit else 1, 6)
                if sav: w = max(w, roll(2 if crit else 1, 6))
                return w + 7 + (2 if self.dmg_boost else 0) + roll(2 if crit else 1, 6)
            def extra(crit, dealt, t=tgt, f=not first):
                if dealt: self.fill(2 if f else 1)
            hit, crit, dealt = attack(fight, self, tgt, 11, dmg, "slashing", True, adv=True, sneak=3, extra=extra)
            if hit: first = True
            if fight.over(): return
        if not bonus and self.meter >= 6: self.unleash(fight, True)
