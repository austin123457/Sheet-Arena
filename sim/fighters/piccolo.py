"""Piccolo (Piccolo Jr.) in the Raditz saga, raid boss. Sheet: Piccolo_Raditz_Saga_Raid.pdf. A moon-level monster:
months after Raditz, at the same strength, he blows up the moon to stop Gohan's Great Ape (chapter 208).

Exponent 2 (moon). In moon units: Str 30, Dex 16, Con 30 (the moon on the page, and Raditz's blows taken; his
mind isn't tiered: Int 16, Wis 20, Cha 12); proficiency +9. 270 HP, AC 11 in the weighted cape and turban, 14 once
they come off (his first bonus action), flies. Legendary Resistance (3), three Legendary Actions. A barrage of five
ki blasts a turn (+19, 2d10+3 force); the mouth blast (recharge 5-6: 6d10 force through up to three, Dex 27 half);
the Special Beam Cannon: one turn charging (he can't attack, and a hit makes him hold his concentration), the
next turn it fires (+19, 12d10 piercing, crits on 19-20, through resistance, immunity and thresholds alike: it
went through Raditz, who outclassed him). He opens a
release turn with a ki blast as a bonus action, to draw whatever's guarding against it. Namekian regeneration
(10 HP at the start of each of his turns, and Regrowth: a bonus action, three times, 40 HP back and the limb with it). And the moon: if an enemy needs it, he spends an
action to blow it up, the way he did for Gohan. Legendary Actions: an eye laser (+19, 1d10+1 fire).
"""
from ..engine import Combatant, attack, d, d20, roll


class Piccolo(Combatant):
    name = "Piccolo"; danger = 10; melee = True
    raid_boss = True; legendary_actions = 3; tier = 2

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 270; self.ac = 11
        self.saves = dict(Str=19, Dex=12, Con=19, Int=3, Wis=14, Cha=1); self.legendary_resist = 3
        self.weights = True; self.regen = 3; self.charged = False; self.wave = True; self.energy = False
        self.broken = False         # a charge has been knocked out of him: no more charging into open fire

    def init(self): return d(20) + 4

    def after_damage(self, dmg, dtype, src, melee):
        # holding a charged Special Beam Cannon through a hit (2024: the DC tops out at 30)
        if self.charged and d20() + self.saves["Con"] < min(30, max(10, dmg // 2)):
            self.charged = False; self.broken = True

    def blast(self, fight, tgt):
        self.energy = True
        attack(fight, self, tgt, 19, lambda c: roll(4 if c else 2, 10) + 3, "force", melee=False)
        self.energy = False

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        self.hp = min(self.maxhp, self.hp + 10)                                    # Namekian regeneration
        bonus = False
        if self.weights: self.weights = False; self.ac = 14; bonus = True          # the cape and turban come off
        elif self.hp <= self.maxhp // 2 and self.regen > 0:
            self.regen -= 1; self.hp = min(self.maxhp, self.hp + 40); bonus = True   # Regrowth
        if not self.wave and d(6) >= 5: self.wave = True
        # the moon goes first if anyone out there needs it
        if fight.moon and any(e.needs_moon() for e in fight.enemies(self)):
            fight.moon = False; fight.note("Piccolo blows up the moon"); return
        if self.charged:
            if not bonus: self.blast(fight, tgt)                                   # draw the guard off
            if tgt.out: return
            self.charged = False; self.energy = True
            attack(fight, self, tgt, 19, lambda c: roll(24 if c else 12, 10), "piercing", melee=False,
                   crit_range=19, ignore_res=True, ignore_imm=True)
            self.energy = False; fight.note("Special Beam Cannon"); return
        held = tgt.paralyzed or tgt.charmed is not None or tgt.asleep
        # the Makankosappo is for what his blasts can't handle: immunity, or something a tier above him (Raditz)
        if (tgt.immune("force") or tgt.tier > self.tier) and len(fight.enemies(self)) == 1 and (not self.broken or held):
            self.charged = True; return
        if self.wave:
            self.wave = False
            for e in fight.enemies(self)[:3]:
                saved = e.save("Dex", 27)
                dmg = e.dex_damage(saved, roll(6, 10))
                if dmg: e.take(dmg, "force", self.name)
            return
        for i in range(5):                                                     # a barrage
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: return
            self.blast(fight, tgt)
            if fight.over(): return

    def legendary_action(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        self.la_left -= 1
        self.energy = True
        attack(fight, self, tgt, 19, lambda c: roll(2 if c else 1, 10) + 1, "fire", melee=False)  # eye laser
        self.energy = False
