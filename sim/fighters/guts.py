"""Guts: the Black Swordsman. Sheet: Guts_5e_Build.pdf.
236 HP, AC 18, the Dragonslayer at +13 for 4d6 (crits on 19), raging and reckless from turn one,
Relentless Rage, and a reaction swing at anyone who hits him in melee."""
from ..engine import Combatant, attack, d, d20, roll


class Guts(Combatant):
    name = "Guts"; danger = 5; melee = True
    never_stunned = True; retaliates = True
    charm_immune = True; fright_immune = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 236; self.ac = 18
        self.saves = dict(Str=11, Dex=2, Con=9, Int=-1, Wis=7, Cha=-1)
        self.raging = False; self.sw = 3; self.rel_dc = 10; self.hew = False

    def init(self): return d20(adv=True) + 2
    def save_adv(self, ab, spell): return (ab == "Str" and self.raging) or ab == "Dex"

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        if self.raging and dtype != "psychic" and not ignore_res: return dmg // 2
        return dmg

    def on_zero(self, src, crit):
        if self.down:
            self.death_fail += 2 if crit else 1
            if self.death_fail >= 3: self.out = True
            return
        if self.raging:
            if d(20) + 9 >= self.rel_dc: self.rel_dc += 5; self.hp = 24; return
            self.rel_dc += 5; self.down = True; self.hp = 0; return
        self.out = True

    def retaliate(self, fight, att):
        if self.reaction and att.alive() and self.raging:
            self.reaction = False; self.swing(fight, att, adv=True, frenzy=False, savage=True, can_hew=False)

    def answer_standoff(self, fight, jin):
        self.raging = True; self.reckless = True; self.swing(fight, jin, True, True, True)

    def swing(self, fight, tgt, adv, frenzy, savage, brutal=False, can_hew=True):
        def dmg(crit):
            n = 8 if crit else 4
            w = roll(n, 6, gwf=True)
            if savage: w = max(w, roll(n, 6, gwf=True))
            v = w + (16 if self.raging else 13)
            if frenzy: v += roll(6 if crit else 3, 6)
            if brutal: v += roll(2 if crit else 1, 10)
            return v
        hit, crit, dealt = attack(fight, self, tgt, 13, dmg, "slashing", True, adv=adv, crit_range=19)
        if crit:
            tgt.disadv_attacks = True
            if can_hew: self.hew = True
        if hit:     # the sword is big enough to clip the next melee enemy too
            others = [e for e in fight.enemies(self) if e is not tgt and e.melee]
            if others: others[0].take(roll(4, 6, gwf=True), "slashing", "Guts cleave", from_attack=True, melee=True)
        return hit

    def turn(self, fight):
        if self.down:       # death saves, with advantage
            r = d20(adv=True)
            if r == 20: self.hp = 1; self.down = False; self.death_fail = 0
            elif r < 10:
                self.death_fail += 1
                if self.death_fail >= 3: self.out = True; return
        tgt = fight.pick_target(self)
        if not tgt: return
        bonus = False
        if not self.raging: self.raging = True; self.reckless = True; bonus = True
        n = 2 + (2 if not self.surge_used else 0); self.surge_used = True
        first = False
        for i in range(n):
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: break
            brutal = (i == 1) and not self.poisoned and not self.disadv_attacks
            hit = self.swing(fight, tgt, adv=not brutal, frenzy=not first, savage=not first, brutal=brutal)
            if hit: first = True
            if fight.over(): return
        if not bonus and self.hew and tgt and not tgt.out: self.hew = False; self.swing(fight, tgt, True, False, False, can_hew=False)
        elif not bonus and self.hp <= 118 and self.sw > 0 and not self.down: self.sw -= 1; self.hp = min(self.maxhp, self.hp + d(10) + 8)
        self.hew = False
