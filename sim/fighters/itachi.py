"""Itachi Uchiha, living and healthy (the Edo body can't lose without a seal). Sheet: Itachi_Uchiha_5e_Build.pdf.
85 HP, AC 19, a wizard: Susanoo, Tsukuyomi, Amaterasu, Izanami, Hold, Fireball, Mirror Image."""
from ..engine import Combatant, attack, d, d20, roll


class Itachi(Combatant):
    name = "Itachi"; danger = 3
    caster = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 85; self.ac = 19
        self.saves = dict(Str=-1, Dex=4, Con=0, Int=11, Wis=7, Cha=0)
        self.shield = 4; self.shield_up = False; self.illusory = True; self.susanoo_cast = False; self.yata = 0
        self.tsukuyomi = True; self.amaterasu = True; self.izanami = True; self.hold = 2; self.fireball = 3
        self.mirror = 0; self.mirror_cast = False; self.sus_turns = 0

    def init(self): return d20(adv=True) + 10

    def ac_now(self):
        ac = self.ac
        if self.susanoo: ac = max(ac, 21)
        if self.shield_up: ac += 5
        return ac

    def defend_ac(self, att, total, melee, crit):
        if self.mirror > 0:
            need = {3: 6, 2: 8, 1: 11}[self.mirror]
            if d(20) >= need: self.mirror -= 1; return None
        would_hit = crit or total >= self.ac_now()
        if would_hit and self.reaction:
            if self.susanoo and self.yata > 0: self.yata -= 1; self.reaction = False; return None
            if self.shield > 0 and not self.shield_up: self.shield -= 1; self.reaction = False; self.shield_up = True; return 0
            if self.illusory: self.illusory = False; self.reaction = False; return None
        return 0

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        return dmg // 2 if self.susanoo else dmg

    def after_damage(self, dmg, dtype, src, melee):
        if self.susanoo:
            dc = max(10, dmg // 2)
            if d20(adv=True) < dc: self.susanoo = False; self.thp = 0; self.yata = 0

    def start_turn(self):
        super().start_turn(); self.shield_up = False

    def cast_on(self, fight, tgt):
        tgt.on_targeted_by_spell(fight, self)

    def turn(self, fight):
        enemies = fight.enemies(self)
        if self.tsukuyomi and any(e.averts_eyes for e in enemies):
            self.tsukuyomi = False          # Guy fights watching your feet; he never bothers
        if self.susanoo:
            self.sus_turns += 1
            if self.sus_turns > 1:
                self.hp -= 5
                if self.hp <= 0: self.hp = 0; self.out = True; return
        if not enemies: return
        # Izanami: a loop of sensation, so it needs someone who has struck him on two separate turns
        ready = [e for e in enemies if self.turns_struck_by(e) >= 2]
        tgt = None; act = None
        if ready and self.izanami:
            tgt = max(ready, key=lambda e: e.danger); act = "izanami"
        elif len(enemies) >= 2 and self.fireball > 0 and sum(1 for e in enemies if e.melee) >= 2:
            act = "fireball"
        elif not self.susanoo_cast:
            act = "susanoo"
        else:
            # Smasher's Mage Slayer and Indomitable eat a spell
            cands = [e for e in enemies if not (e.name == "Smasher" and (e.mage_slayer or e.indomitable > 0))]
            tgt = max(cands, key=lambda e: e.danger) if cands else max(enemies, key=lambda e: e.danger)
            if self.tsukuyomi: act = "tsukuyomi"
            elif self.susanoo: act = "totsuka"
            elif self.hold > 0 and not tgt.susanoo: act = "hold"
            elif self.amaterasu and not tgt.burning: act = "amaterasu"
            elif not self.mirror_cast: act = "mirror"
            else: act = "firebolt"
        if act == "izanami":
            self.izanami = False; self.cast_on(fight, tgt)
            if self.out: return
            tgt.out = True; fight.note(f"Izanami on {tgt.name}")
        elif act == "fireball":
            self.fireball -= 1
            for e in list(enemies):
                if e.melee or len(enemies) == 1:
                    self.cast_on(fight, e)
                    if self.out: return
                    dmg = e.dex_damage(e.save("Dex", 19, spell=True), roll(8, 6, minv=2))
                    if dmg: e.take(dmg, "fire", "Fireball")
        elif act == "susanoo":
            self.susanoo = True; self.susanoo_cast = True; self.thp = 150; self.yata = 3; self.sus_turns = 1
        elif act == "tsukuyomi":
            self.tsukuyomi = False; self.cast_on(fight, tgt)
            if self.out: return
            if tgt.save("Wis", 19, spell=True): tgt.take(roll(5, 10), "psychic", "Tsukuyomi")
            else: tgt.take(roll(10, 10), "psychic", "Tsukuyomi"); tgt.out = True; fight.note(f"Tsukuyomi drops {tgt.name}")
        elif act == "totsuka":
            tgt = max(enemies, key=lambda e: e.danger)
            def dmg(crit): return roll(12 if crit else 6, 8)
            def extra(crit, dealt, t=tgt):
                if dealt and not t.out and not t.save("Wis", 19, spell=True): t.out = True; fight.note(f"Totsuka seals {t.name}")
            attack(fight, self, tgt, 11, dmg, "force", melee=False, extra=extra)
        elif act == "hold":
            self.hold -= 1; self.cast_on(fight, tgt)
            if self.out: return
            if not tgt.save("Wis", 19, spell=True): tgt.paralyzed = True
        elif act == "amaterasu":
            self.amaterasu = False; self.cast_on(fight, tgt)
            if self.out: return
            if not tgt.save("Dex", 19, spell=True): tgt.take(roll(6, 10), "fire", "Amaterasu", ignore_res=True); tgt.burning = True
        elif act == "mirror":
            self.mirror = 3; self.mirror_cast = True
        else:
            tgt = tgt or max(enemies, key=lambda e: e.danger)
            def dmg(crit): return roll(8 if crit else 4, 10, minv=2)
            attack(fight, self, tgt, 11, dmg, "fire", melee=False, adv=tgt.paralyzed)
