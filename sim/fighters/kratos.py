"""Kratos at the end of Valhalla: Demigod (son of Zeus), Fighter (Battle Master) 11 / Barbarian (Path of the World
Tree) 9. Sheet: Kratos_5e_Build.pdf. 293 HP (Tough), AC 20 (Brok and Sindri's armor and the Guardian Shield),
Strength 26 and Constitution 22 by blood, initiative with advantage.

Three attacks a turn at +17: the Leviathan Axe (2d8+16 slashing and 1d6 cold) or the Blades of Chaos (2d6+16
slashing and 1d8 fire, and a Burn of 1d10 fire at the end of the target's next turn), plus Shield Master's bash
(Str 22 or prone), and Savage Attacker on the first hit each turn. Runic attacks, each on a 5-6 recharge: the light one replaces an attack (+3d10 cold or fire on a
hit: Winter's Bite, Nemean Crush), the heavy one is a Bonus Action (Con 22, 6d10 cold or fire and Frozen or
Burning, half on a save: Fog of Fimbulwinter, Rampage of the Furies). He opens with Spartan Rage in its Valhalla form, Legacy: the Blade of Olympus in his hand for
the Rage (+1d10 radiant on every weapon hit), resistance to physical damage and Vitality Surge's 9 temporary HP.
Valor spends another Rage use to heal 4d12+6. Battle Master Parry on the shield (1d10+8 off a hit) from five d10s,
Second Wind, Action Surge, Indomitable. A demigod: resistance to lightning, can't be Frightened, and once a day the
first blow that would kill him leaves him at 1 HP (he's climbed out of Hades three times).
He takes the Blades against anything that regenerates, and against a downed Anderson he does what Anderson's own
sheet allows: grapple him and tear his heart out (a Strength contest)."""
from ..engine import Combatant, attack, d, d20, roll


class Kratos(Combatant):
    name = "Kratos"; danger = 7; melee = True
    fright_immune = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 293; self.ac = 20
        self.saves = dict(Str=14, Dex=2, Con=12, Int=0, Wis=2, Cha=-1); self.indomitable = 1; self.indom_bonus = 11
        self.raging = False; self.rages = 4; self.dice = 5; self.sw = 4; self.surge = 1; self.hades = True
        self.blades = False; self.grappling = None; self.light = True; self.heavy = True

    def init(self): return d20(adv=True) + 2
    def save_adv(self, ab, spell): return ab == "Str" and self.raging

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        if not ignore_res and ((self.raging and dtype in ("slashing", "piercing", "bludgeoning")) or dtype == "lightning"):
            dmg //= 2
        return dmg

    def reduce_hit(self, dmg, melee):
        # Parry on the Guardian Shield
        if self.reaction and self.dice > 0 and dmg >= 20 and not self.incapacitated():
            self.reaction = False; self.dice -= 1; return max(0, dmg - (d(10) + 8))
        return dmg

    def on_zero(self, src, crit):
        if self.hades: self.hades = False; self.hp = 1; return      # back out of the Underworld
        self.out = True

    def before_first_round(self, fight):
        self.blades = any(hasattr(e, "radiant_taken") for e in fight.enemies(self))   # something that grows back

    def element(self): return "fire" if self.blades else "cold"

    def heavy_runic(self, fight, tgt):
        self.heavy = False
        saved = tgt.save("Con", 22)
        tgt.take(roll(6, 10) // (2 if saved else 1), self.element(), self.name)
        if not saved and not tgt.out:
            if self.blades:
                def burn(c): c.take(roll(2, 10), "fire", "Burn"); return False
                tgt.effects.append(burn)
            else:
                tgt.dread = True                                 # Frozen: everything it swings is slow
                def thaw(c): c.dread = False; return False
                tgt.effects.append(thaw)

    def weapon(self, fight, tgt, first, runic=False):
        def dmg(crit):
            n, s = (4 if crit else 2), (6 if self.blades else 8)
            w = roll(n, s)
            if first: w = max(w, roll(n, s))                     # Savage Attacker
            return w + 16
        def extra(crit, dealt, t=tgt):
            m = 2 if crit else 1
            # the fire or the frost, and Legacy's Blade of Olympus, each its own damage type
            if not t.out: t.take(roll(m, 8) if self.blades else roll(m, 6), self.element(), self.name)
            if runic and not t.out: t.take(roll(3 * m, 10), self.element(), self.name)
            if self.raging and not t.out: t.take(roll(m, 10), "radiant", self.name)
            if self.blades and not t.out:
                def burn(c): c.take(d(10), "fire", "Burn"); return False
                t.effects.append(burn)
            if first and not t.out and not t.prone and not t.susanoo and not t.save("Str", 22):
                t.prone = True                                   # Shield Master
        hit, crit, dealt = attack(fight, self, tgt, 17, dmg, "slashing", True, extra=extra)
        return hit

    def tear_heart(self, fight, tgt):
        """Anderson's own sheet: grappled at 0, a Strength contest, and his heart comes out."""
        if self.grappling is not tgt:
            self.grappling = tgt; return                         # the grapple, against a body that can't resist
        if d20(adv=self.raging) + 14 >= d20() + 9:
            tgt.out = True; fight.note("Kratos tears out Anderson's heart")

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        if not self.light and d(6) >= 5: self.light = True
        if not self.heavy and d(6) >= 5: self.heavy = True
        if self.grappling is not None and (not self.grappling.alive() or not getattr(self.grappling, "down", False)):
            self.grappling = None
        bonus = False
        if not self.raging and self.rages > 0:
            self.raging = True; self.rages -= 1; self.thp = max(self.thp, 9); bonus = True     # Spartan Rage: Legacy
        if not bonus and self.hp <= 0.4 * self.maxhp:
            if self.raging and self.rages > 0: self.rages -= 1; self.hp = min(self.maxhp, self.hp + roll(4, 12) + 6); bonus = True   # Valor
            elif self.sw > 0: self.sw -= 1; self.hp = min(self.maxhp, self.hp + d(10) + 11); bonus = True
        actions = 1 + (1 if self.surge else 0); self.surge = 0
        for a in range(actions):
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: return
            if getattr(tgt, "down", False) and not getattr(tgt, "nail", False) and hasattr(tgt, "radiant_taken"):
                self.tear_heart(fight, tgt)
                if fight.over(): return
                continue
            for i in range(3):
                if tgt.out: tgt = fight.pick_target(self)
                if not tgt: return
                runic = self.light and i == 0
                if runic: self.light = False
                self.weapon(fight, tgt, first=(i == 0), runic=runic)
                if fight.over(): return
        if not bonus and self.heavy:
            if tgt.out: tgt = fight.pick_target(self)
            if tgt and not getattr(tgt, "down", False): self.heavy_runic(fight, tgt)
