"""Battle Beast: Barbarian (Path of the Berserker) 20, Of Dornn. Sheet: Battle_Beast_5e_Build.pdf.
265 HP, AC 19, Draskula at +16 for 4d6+20 (Savage Attacker, Frenzy +4d6 on the first hit, Brutal Strike
+2d10 on the second), Irresistible Offense (ignores resistance, +27 on a natural 20), Graze on a miss.
Raging: resistance to physical damage, immune to Charmed and Frightened, Str saves never below 27.
Names the strongest enemy Worthy: crits on 19 against it, and it has disadvantage on anyone else.
Hew after a crit or a kill, Retaliation when hit in reach, Intimidating Presence (DC 22), Relentless Rage
back at 40, and one last swing at his worthy opponent if it drops him for good (Glorious Death)."""
from ..engine import Combatant, attack, d, d20, roll


class BattleBeast(Combatant):
    name = "Beast"; danger = 6; melee = True
    retaliates = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 265; self.ac = 19
        self.saves = dict(Str=14, Dex=0, Con=12, Int=0, Wis=1, Cha=-1)
        self.raging = False; self.rel_dc = 10; self.hew = False; self.worthy = None
        self.rages = 6          # Persistent Rage refills them as initiative is rolled
        self.presence = 1       # free once a long rest; after that a Rage use buys another

    # Mindless Rage
    @property
    def charm_immune(self): return self.raging
    @property
    def fright_immune(self): return self.raging

    def init(self): return d20(adv=True) + 0
    def save_adv(self, ab, spell): return ab == "Dex" or (ab == "Str" and self.raging)

    def save(self, ab, dc, spell=False, kind=None, adv=False):
        if ab == "Str": return True if 27 >= dc else super().save(ab, dc, spell, kind, adv)
        return super().save(ab, dc, spell, kind, adv)

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        if self.raging and dtype in ("slashing", "piercing", "bludgeoning") and not ignore_res: return dmg // 2
        if dtype == "cold": return dmg // 2
        return dmg

    def on_zero(self, src, crit):
        if self.raging and d(20) + 12 >= self.rel_dc: self.rel_dc += 5; self.hp = 40; return
        self.rel_dc += 5; self.out = True
        w = self.worthy
        if w is not None and src == w.name and self.reaction and self.fight:
            # Glorious Death: one last swing at the one who finally dropped him, and thanks for the fight
            self.reaction = False
            self.fight.after_turn(lambda: self.swing(self.fight, w, adv=True, frenzy=False, savage=True, can_hew=False))

    def natural_bonus(self, nat): return 27 if nat == 20 else 0

    def start_rage(self, fight):
        self.raging = True; self.reckless = True; self.rages -= 1
        self.frightened = False; self.charmed = None
        es = fight.enemies(self)
        if es:
            self.worthy = max(es, key=lambda e: e.danger); self.worthy.marked_by = self

    def retaliate(self, fight, att):
        if self.reaction and att.alive() and self.raging:
            self.reaction = False; self.swing(fight, att, adv=True, frenzy=False, savage=True, can_hew=False)

    def answer_standoff(self, fight, jin):
        self.start_rage(fight); self.swing(fight, jin, True, True, True)

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
        if can_hew and (crit or (hit and tgt.out)): self.hew = True
        return hit

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        bonus = False
        if not self.raging:
            self.start_rage(fight); bonus = True
        else:
            # Intimidating Presence on whoever within 30 ft isn't already afraid of him
            scared = [e for e in fight.enemies(self) if not e.fright_immune and not e.frightened]
            if scared and (self.presence > 0 or self.rages > 0):
                if self.presence > 0: self.presence -= 1
                else: self.rages -= 1
                bonus = True
                for e in scared:
                    if not e.save("Wis", 22, kind="fear"): e.frightened = True; e.fear_dc = 22
        if self.worthy is not None and self.worthy.alive(): tgt = self.worthy
        first = False
        for i in range(2):
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: break
            brutal = (i == 1) and not self.poisoned and not self.disadv_attacks
            hit = self.swing(fight, tgt, adv=not brutal, frenzy=not first, savage=not first, brutal=brutal)
            if hit: first = True
            if fight.over(): return
        if not bonus and self.hew:
            tgt = tgt if tgt and not tgt.out else fight.pick_target(self)
            if tgt: self.swing(fight, tgt, True, False, False, can_hew=False)
        self.hew = False
