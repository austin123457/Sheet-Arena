"""Kyle Crane, Caleb's sheet (v3): Barbarian (Path of the Beast) 14 / Rogue (Thief) 5 / Fighter 1.
Sheet: Kyle_Crane_5e_Build.pdf. 233 HP, AC 16, initiative +3 with advantage.

The Beast Meter (six boxes) starts empty after a rest. Outside Beast Mode it fills: one per hit (two for
the first each turn), one every time he takes damage, one per Perfect Block, one the first time each round
an attack misses him. Unleashed on a full meter (he lets it out the moment it fills) he heals to full and
roars (Con 19 or stunned); with three or more boxes he can go early, with no heal and no roar. As the Beast:
resistance to physical damage, three claws and a Savage Bite at +11 for 2d10+8 that ignore resistance, each
hit heals 7, each kill refills a box; one box drains at the start of each of his turns and Beast Mode ends at
the end of the turn the last one goes. Dropping to 0 empties the meter (Relentless Rage still puts him up at 28).
Always: Perfect Block (Reaction: +6 AC against melee until his next turn, which can turn the hit into a miss)
or, when a block won't stop it, Uncanny Dodge (halve the hit); Danger Sense.
The finisher (a claw hit that leaves an ordinary creature at 15 HP or fewer kills it) never applies here:
nobody in this arena is ordinary."""
from ..engine import Combatant, attack, d, d20, roll


class Crane(Combatant):
    name = "Crane"; danger = 4; melee = True
    one_handed = property(lambda self: not self.beast)      # the machete, not the claws

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 233; self.ac = 16
        self.saves = dict(Str=11, Dex=3, Con=9, Int=-1, Wis=0, Cha=-1)
        self.meter = 0; self.beast = False; self.ending = False; self.rel_dc = 10
        self.sw = 2; self.bandages = 4; self.rare = 2; self.morphine = 1
        self.regen = 0; self.dmg_boost = False; self.booster_used = False
        self.miss_this_round = False; self.block_up = False; self.unleashed_round = None

    def init(self): return d20(adv=True) + 3
    def save_adv(self, ab, spell): return ab == "Dex" or (ab == "Str" and self.beast)

    def fill(self, n):
        if not self.beast: self.meter = min(6, self.meter + n)

    def defend_ac(self, att, total, melee, crit):
        if not crit and total < self.ac and not self.miss_this_round: self.miss_this_round = True; self.fill(1)
        if melee and self.block_up: return 6
        # Perfect Block: catch a melee hit at the last instant if +6 turns it into a miss
        if melee and self.reaction and not crit and self.ac <= total < self.ac + 6 and not self.incapacitated():
            self.reaction = False; self.block_up = True; self.fill(1); return 6
        return 0

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        if self.beast and dtype in ("slashing", "piercing", "bludgeoning") and not ignore_res: dmg //= 2
        if from_attack and self.reaction and not self.incapacitated(): self.reaction = False; dmg //= 2     # Uncanny Dodge
        return dmg

    def after_damage(self, dmg, dtype, src, melee): self.fill(1)

    def on_zero(self, src, crit):
        self.meter = 0
        if self.beast and d(20) + 9 >= self.rel_dc: self.rel_dc += 5; self.hp = 28; return
        self.out = True

    def start_turn(self):
        super().start_turn(); self.miss_this_round = False; self.block_up = False

    def unleash(self, fight, full):
        self.beast = True; self.reckless = True; self.ending = False; self.unleashed_round = fight.round
        if full:
            self.hp = self.maxhp
            for e in fight.enemies(self):
                if e.melee and not e.out and not e.stun_immune and not e.never_stunned:
                    if not e.save("Con", 19): e.paralyzed = True; e.stun_until = fight.round

    def claw(self, fight, tgt, savage, brutal, adv):
        def dmg(crit):
            w = roll(4 if crit else 2, 10)
            if savage: w = max(w, roll(4 if crit else 2, 10))
            return w + 8 + (2 if self.dmg_boost else 0) + (roll(2 if crit else 1, 10) if brutal else 0)
        def extra(crit, dealt, t=tgt):
            if dealt: self.hp = min(self.maxhp, self.hp + 7)
            if t.out: self.meter = min(6, self.meter + 1)          # every kill refills a box
        hit, crit, dealt = attack(fight, self, tgt, 11, dmg, "slashing", True, adv=adv, extra=extra, ignore_res=True)
        return hit

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        if self.regen > 0: self.regen -= 1; self.hp = min(self.maxhp, self.hp + 5)
        bonus = False
        if self.beast:
            self.meter -= 1
            if self.meter <= 0: self.meter = 0; self.ending = True     # the Beast goes at the end of this turn
        elif self.meter >= 6: self.unleash(fight, True); bonus = True
        elif self.meter >= 3 and self.hp < 80: self.unleash(fight, False); bonus = True
        if self.beast:
            first = False
            for i in range(3):
                if tgt.out: tgt = fight.pick_target(self)
                if not tgt: return
                brutal = (i == 2) and not self.disadv_attacks and not self.poisoned
                if self.claw(fight, tgt, savage=not first, brutal=brutal, adv=not brutal): first = True
                if fight.over(): return
            if not bonus:       # Savage Bite, from the turn after he changes
                if tgt.out: tgt = fight.pick_target(self)
                if tgt: self.claw(fight, tgt, savage=False, brutal=False, adv=True)
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

    def end_turn(self, fight):
        super().end_turn(fight)
        if self.ending: self.beast = False; self.ending = False
