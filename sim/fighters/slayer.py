"""The Doom Slayer. Sheet: Doom_Slayer_5e_Build.pdf.
298 HP plus 60 temporary, AC 20, the Super Shotgun, the BFG, the Crucible (ignores immunity),
the Blood Punch, the Hammer, Ice Bomb and Flame Belch, Relentless Rage."""
from ..engine import Combatant, attack, d, d20, roll


class Slayer(Combatant):
    name = "Slayer"; danger = 8; melee = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 298; self.thp = 60; self.ac = 20
        self.saves = dict(Str=13, Dex=4, Con=12, Int=-1, Wis=1, Cha=-1)
        self.raging = False; self.rages = 5; self.bfg = 3; self.crucible = 3; self.blood = 2; self.hammer = 1; self.surge = 1; self.sw = 3
        self.rel_dc = 10; self.ff = True; self.ice_cd = 0; self.flame_cd = 0; self.rbd = False

    def init(self): return d20(adv=True) + 4
    def save_adv(self, ab, spell): return ab == "Dex"

    def save(self, ab, dc, spell=False):
        ok = super().save(ab, dc, spell)
        if not ok and self.ff and self.raging:
            self.ff = False; ok = d20(adv=self.save_adv(ab, spell)) + self.saves[ab] + 3 >= dc
        return ok

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        if not ignore_res and ((self.raging and dtype in ("slashing", "piercing", "bludgeoning")) or dtype in ("fire", "radiant")): dmg //= 2
        if from_attack and self.reaction:
            self.reaction = False; dmg = max(0, dmg - (d(10) + 13))
        return dmg

    def on_zero(self, src, crit):
        if self.rbd:        # already down: death saves
            self.death_fail += 2 if crit else 1
            if self.death_fail >= 3: self.out = True
            return
        if self.raging and d(20) + 12 >= self.rel_dc: self.rel_dc += 5; self.hp = 28; return
        if self.raging: self.rel_dc += 5; self.rbd = True; self.hp = 0; return
        self.out = True

    def shoot(self, fight, tgt, fury):
        def dmg(crit, f=fury):
            w = roll(8 if crit else 4, 8); w = max(w, roll(8 if crit else 4, 8))
            return w + (roll(2 if crit else 1, 6) + 7 if f else 0)
        return attack(fight, self, tgt, 12, dmg, "piercing", melee=False, crit_range=19)

    def turn(self, fight):
        if self.rbd:
            r = d20()
            if r == 20: self.hp = 1; self.rbd = False; self.death_fail = 0
            elif r < 10:
                self.death_fail += 1
                if self.death_fail >= 3: self.out = True; return
        enemies = fight.enemies(self)
        if not enemies: return
        tgt = fight.pick_target(self)
        if self.ice_cd: self.ice_cd -= 1
        if self.flame_cd: self.flame_cd -= 1
        bonus_used = False
        if not self.raging: self.raging = True; self.rages -= 1; self.reckless = True; bonus_used = True
        actions = 1 + (1 if self.surge else 0); self.surge = 0
        fury = True
        for a in range(actions):
            if tgt is None or tgt.out: tgt = fight.pick_target(self)
            if not tgt: return
            cur = tgt.hp + tgt.thp
            if self.hammer and len([e for e in enemies if e.melee and not e.out]) >= 2:
                self.hammer = 0
                for e in enemies:
                    if e.out or not e.melee: continue
                    e.take(roll(6, 10), "force", "Hammer")
                    if not e.save("Con", 19) and not e.never_stunned and not e.stun_immune: e.paralyzed = True; e.stun_until = fight.round
            elif self.bfg > 0 and (len(enemies) >= 2 or cur > 150):
                self.bfg -= 1
                for e in list(enemies):
                    if e.out: continue
                    dmg = e.dex_damage(e.save("Dex", 18), roll(20, 10))
                    if dmg: e.take(dmg, "force", "BFG")
            elif self.crucible > 0 and cur <= 240:
                self.crucible -= 1
                frozen = tgt.paralyzed
                def dmg(crit): return roll(24 if crit else 12, 12) + 7 + 3
                def extra(crit, dealt, t=tgt):
                    if dealt and not t.out and (t.hp + t.thp) <= 150: t.out = True; fight.note("Crucible")
                attack(fight, self, tgt, 13, dmg, "slashing", True, adv=True, crit_range=1 if frozen else 19, extra=extra,
                       ignore_res=True, ignore_imm=True)
                fury = False
            else:
                for i in range(2):
                    if tgt.out: tgt = fight.pick_target(self)
                    if not tgt: return
                    if self.blood > 0 and i == 0 and tgt.paralyzed:
                        self.blood -= 1
                        attack(fight, self, tgt, 13, (lambda crit: roll(16 if crit else 8, 10) + 10), "bludgeoning", True, adv=True, crit_range=1)
                    else:
                        hit, crit, dealt = self.shoot(fight, tgt, fury)
                        if hit: fury = False
                    if fight.over(): return
            if fight.over(): return
        # bonus action
        if not bonus_used:
            if self.hp <= 150 and self.sw > 0: self.sw -= 1; self.hp = min(self.maxhp, self.hp + d(10) + 6)
            elif self.ice_cd == 0 and tgt and not tgt.out and not tgt.paralyzed and not tgt.never_stunned:
                self.ice_cd = 4
                if not tgt.save("Dex", 18) and not tgt.stun_immune: tgt.paralyzed = True; tgt.stun_until = fight.round
            elif self.flame_cd == 0 and tgt and not tgt.out:
                self.flame_cd = 3; tgt.take(roll(2, 6), "fire", "Flame Belch"); self.thp = min(60, self.thp + 10)
