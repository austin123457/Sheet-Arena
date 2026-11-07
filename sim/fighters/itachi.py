"""Itachi Uchiha, living and healthy (the Edo body can't lose without a seal): Wizard (Illusionist) 17 /
Rogue (Assassin) 3. Sheet: Itachi_Uchiha_5e_Build.pdf. 85 HP, AC 19 against what he can see (Sharingan),
spell save DC 19, spell attack +11, slots 4/3/3/3/2/1/1/1/1.

What he uses here, by slot:
  cantrips  Fire Bolt (4d10, 1s count as 2, ignores fire resistance), Mind Sliver (the clone's opener)
  1st       Shield
  2nd       Mirror Image, Hold Person, Phantasmal Force, Illusory Self past its free use
  3rd       Fireball, Hypnotic Pattern, Counterspell
  4th       Shadow Clone, Phantasmal Killer
  5th       Dominate Person, Mislead
  6th-9th   Amaterasu, Tsukuyomi, Izanami, Susanoo (Yata Mirror, Totsuka, Yasaka Magatama)
Every Mangekyo casting costs a level of exhaustion (-2 on his d20 tests per level; six kills him), and
Susanoo ending costs two more. Concentration checks have advantage (War Caster). The Sharingan gives
advantage on saves against charm, illusion and enchantment.

Left out because they do nothing on open sand or are strictly worse than something above: Misty Step,
Disguise Self, Silent Image, Minor Illusion, Dispel Magic, the rituals, Scorching Ray and the Sneak Attack
kunai (both below Fire Bolt), Tidal Wave (below Fireball), Summon Beast and Summon Fey (concentration he
always has a better use for)."""
from ..engine import Combatant, amaterasu, attack, d, d20, roll

DC = 19


def p_fail(t, ab, adv=False):
    """Rough chance a target fails a DC 19 spell save, counting what he can see coming: advantage,
    Mage Slayer, Indomitable and the Triforce."""
    if getattr(t, "mage_slayer", False) and ab in ("Int", "Wis", "Cha"): return 0.0
    if getattr(t, "triforce", False): return 0.0
    p = min(1.0, max(0.0, (21 - (DC - t.saves[ab])) / 20))
    if adv or t.save_adv(ab, True): p = 1 - (1 - p) ** 2
    f = 1 - p
    return f * f if t.indomitable > 0 else f


class ShadowClone(Combatant):
    """4th level, bonus action, 1 minute, no concentration: a duplicate with his AC, saves and attack, 10 HP,
    acting on his turn with cantrips. Nobody can tell which Itachi is real."""
    name = "Itachi"; danger = 3; caster = True; summon = True

    def __init__(self, owner):
        super().__init__()
        self.owner = owner; self.hp = self.maxhp = 10; self.ac = 19; self.saves = dict(owner.base_saves)

    def act(self, fight, tgt, sliver):
        if tgt is None or not tgt.alive(): return
        if sliver:      # Mind Sliver: Int save or 4d6 psychic and -1d4 on its next save
            tgt.on_targeted_by_spell(fight, self)
            if self.alive() and not tgt.save("Int", DC, spell=True):
                tgt.take(roll(4, 6), "psychic", "Mind Sliver"); tgt.sliver = True
        else:
            attack(fight, self, tgt, 11, lambda c: roll(8 if c else 4, 10, minv=2), "fire", melee=False, ignore_res=True)


class Itachi(Combatant):
    name = "Itachi"; danger = 3
    caster = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 85; self.ac = 19
        self.base_saves = dict(Str=-1, Dex=4, Con=0, Int=11, Wis=7, Cha=0); self.saves = dict(self.base_saves)
        self.slots = {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
        self.exh = 0; self.conc = None; self.conc_round = 0
        self.shield_up = False; self.illusory = True; self.mirror = 0; self.yata = 0; self.sus_turns = 0
        self.clone = None; self.fooled = set()

    def init(self): return d20(adv=True) + 10
    def atk(self): return 11 - 2 * self.exh

    def ac_now(self):
        ac = self.ac
        if self.susanoo: ac = max(ac, 21)
        if self.shield_up: ac += 5
        return ac

    # ---------- costs ----------
    def exhaust(self, n):
        self.exh += n
        self.saves = {k: v - 2 * self.exh for k, v in self.base_saves.items()}
        if self.exh >= 6: self.out = True; self.hp = 0

    def spend(self, fight, level):
        self.slots[level] -= 1
        if level >= 6: self.exhaust(1)
        return fight.cast(self, level) and self.alive()

    def start_conc(self, spell, tgt=None, rnd=0):
        if self.conc: self.drop_conc()
        self.conc = (spell, tgt); self.conc_round = rnd

    def drop_conc(self):
        if not self.conc: return
        spell, t = self.conc; self.conc = None
        if spell == "susanoo":
            self.susanoo = False; self.thp = 0; self.yata = 0; self.exhaust(2)
        elif spell == "hold":
            if getattr(t, "held_by", None) is self: t.paralyzed = False; t.held_by = None
        elif spell in ("dominate", "pattern"):
            for x in (t if isinstance(t, list) else [t]):
                if x.charmed and x.charmed["by"] is self: x.charmed = None
        elif spell == "killer":
            t.dread = False
        elif spell == "mislead":
            self.invisible = False

    # ---------- defence ----------
    def save(self, ab, dc, spell=False, kind=None, adv=False):
        ok = super().save(ab, dc, spell, kind, adv or kind in ("charm", "illusion", "enchantment"))
        if not ok and self.susanoo and self.yata > 0 and self.reaction:
            self.yata -= 1; self.reaction = False; ok = True       # the Yata Mirror: the effect fails
        return ok

    def defend_ac(self, att, total, melee, crit):
        if self.invisible and att not in self.fooled:
            self.fooled.add(att); return None                   # Mislead: it swung at the double
        if self.mirror > 0:
            need = {3: 6, 2: 8, 1: 11}[self.mirror]
            if d(20) >= need: self.mirror -= 1; return None
        would_hit = crit or total >= self.ac_now()
        if would_hit and self.reaction:
            if self.susanoo and self.yata > 0: self.yata -= 1; self.reaction = False; return None
            if self.slots[1] > 0 and not self.shield_up: self.slots[1] -= 1; self.reaction = False; self.shield_up = True; return 0
            if self.illusory or self.slots[2] > 0:
                if self.illusory: self.illusory = False
                else: self.slots[2] -= 1
                self.reaction = False; return None                 # Illusory Self: an Itachi scatters into crows
        return 0

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        return dmg // 2 if self.susanoo else dmg

    def after_damage(self, dmg, dtype, src, melee):
        if self.conc and d20(adv=True) + self.saves["Con"] < min(30, max(10, dmg // 2)): self.drop_conc()

    def counter_spell(self, fight, caster, level):
        if level >= 3 and self.reaction and self.slots[3] > 0 and self.alive() and not self.incapacitated():
            self.reaction = False; self.slots[3] -= 1
            return not caster.save("Con", DC, spell=True)
        return False

    def start_turn(self):
        super().start_turn(); self.shield_up = False

    def cast_on(self, fight, tgt):
        tgt.on_targeted_by_spell(fight, self)
        return self.alive() and not tgt.negates_spells()

    # ---------- the turn ----------
    def keep_books(self, fight):
        if not self.conc: return
        spell, t = self.conc
        if spell == "hold" and (not t.alive() or not t.paralyzed): self.drop_conc()
        elif spell == "dominate" and (not t.alive() or not t.charmed or fight.round - self.conc_round >= 10): self.drop_conc()
        elif spell == "pattern" and not any(x.alive() and x.charmed and x.charmed["by"] is self for x in t): self.drop_conc()
        elif spell == "killer" and (not t.alive() or not t.dread): self.drop_conc()
        elif spell == "force":
            if t.alive(): t.take(roll(2, 8), "psychic", "Phantasmal Force")
            else: self.drop_conc()
        elif spell == "mislead" and not self.invisible: self.drop_conc()

    def mangekyo_ok(self):
        # never spend the level that would kill him, counting the two Susanoo leaves behind
        return self.exh + 1 + (2 if self.susanoo else 0) <= 5

    def choose(self, fight, enemies):
        cands = [e for e in enemies if not (e.name == "Smasher" and (e.mage_slayer or e.indomitable > 0))] or enemies
        main = max(cands, key=lambda e: e.danger)
        free = self.conc is None
        ready = [e for e in enemies if self.turns_struck_by(e) >= 2]
        if ready and self.slots[8] and self.mangekyo_ok():
            return "izanami", max(ready, key=lambda e: e.danger)
        melee_n = sum(1 for e in enemies if e.melee)
        if len(enemies) >= 3 and self.slots[3] and free and not self.susanoo:
            return "pattern", None
        if len(enemies) >= 2 and self.slots[3] and melee_n >= 2:
            return "fireball", None
        # genjutsu first: Tsukuyomi on the one who must be stopped, when it will probably land
        eyes = [e for e in cands if not e.averts_eyes]
        if eyes and self.slots[7] and self.mangekyo_ok():
            t = max(eyes, key=lambda e: (p_fail(e, "Wis") >= 0.5, e.danger))
            if p_fail(t, "Wis") >= 0.5: return "tsukuyomi", t
        # Susanoo when what is coming would kill him
        if self.slots[9] and self.exh <= 2 and (max(e.danger for e in enemies) >= 3 or self.hp <= 50):
            return "susanoo", None
        if self.hp <= 35 and self.slots[5] and free and not self.invisible and not self.susanoo:
            return "mislead", None
        if self.susanoo:
            # Amaterasu for the one who cannot be reached; otherwise the Sword of Totsuka or the Magatama
            big = [e for e in cands if not e.burning and e.maxhp >= 250]
            if big and self.slots[6] and self.mangekyo_ok(): return "amaterasu", max(big, key=lambda e: e.danger)
            seal = [e for e in enemies if e.sealable()]        # the Totsuka is what ends an Edo body
            if seal: return "totsuka", seal[0]
            return ("totsuka" if p_fail(main, "Wis") >= 0.25 else "magatama"), main
        if free:
            if self.slots[5] and main.humanoid and not main.charm_immune and p_fail(main, "Wis", adv=True) >= 0.35:
                return "dominate", main
            if self.slots[2] > 1 and main.humanoid and not main.paralyzed and p_fail(main, "Wis") >= 0.35:
                return "hold", main
            if self.slots[4] and p_fail(main, "Wis") >= 0.3:
                return "killer", main
        eyes = [e for e in eyes if p_fail(e, "Wis") > 0.1]
        if eyes and self.slots[7] and self.mangekyo_ok():
            return "tsukuyomi", max(eyes, key=lambda e: e.danger)
        if self.slots[6] and not main.burning and self.mangekyo_ok():
            return "amaterasu", main
        if not self.mirror and self.slots[2]:
            return "mirror", None
        if free and self.slots[2] and p_fail(main, "Int") >= 0.4:
            return "force", main
        return "firebolt", main

    def turn(self, fight):
        if self.susanoo:
            self.sus_turns += 1
            if self.sus_turns > 1:
                self.hp -= 5           # nothing prevents it
                if self.hp <= 0: self.hp = 0; self.out = True; return
        self.keep_books(fight)
        if not self.alive(): return
        enemies = fight.enemies(self)
        if not enemies: return
        # bonus action: a Shadow Clone, keeping a 4th-level slot for Phantasmal Killer
        if (self.clone is None or not self.clone.alive()) and self.slots[4] > 1:
            if self.spend(fight, 4):
                self.clone = ShadowClone(self); fight.add(self.clone, self.team)
            if not self.alive(): return
        act, tgt = self.choose(fight, enemies)
        # the clone acts first: Mind Sliver to soften the save he is about to force, otherwise a Fire Bolt
        if self.clone is not None and self.clone.alive():
            save_spell = act in ("tsukuyomi", "dominate", "hold", "killer", "totsuka", "force")
            self.clone.act(fight, tgt or fight.pick_target(self.clone), sliver=save_spell and tgt is not None and not tgt.sliver)
            if not self.alive() or fight.over(): return
            if tgt is not None and not tgt.alive():
                enemies = fight.enemies(self)
                if not enemies: return
                act, tgt = self.choose(fight, enemies)
        self.do(fight, act, tgt, enemies)
        if act != "mislead": self.invisible = False       # attacking or casting ends Mislead's invisibility

    def do(self, fight, act, tgt, enemies):
        if act == "izanami":
            if not self.spend(fight, 8) or not self.cast_on(fight, tgt): return
            tgt.out = True; fight.note(f"Izanami on {tgt.name}")
        elif act == "pattern":
            if not self.spend(fight, 3): return
            caught = []
            for e in enemies:
                if not self.cast_on(fight, e): return
                if e.alive() and not e.charm_immune and not e.save("Wis", DC, spell=True, kind="charm"):
                    e.charmed = {"mode": "pattern", "by": self, "dc": DC}; caught.append(e)
            if caught: self.start_conc("pattern", caught, fight.round)
        elif act == "fireball":
            if not self.spend(fight, 3): return
            for e in list(enemies):
                if e.melee or len(enemies) == 1:
                    if not self.cast_on(fight, e): return
                    dmg = e.dex_damage(e.save("Dex", DC, spell=True), roll(8, 6, minv=2))
                    if dmg: e.take(dmg, "fire", "Fireball", ignore_res=True)
        elif act == "susanoo":
            if not self.spend(fight, 9): return
            self.start_conc("susanoo", None, fight.round)
            self.susanoo = True; self.thp = 150; self.yata = 3; self.sus_turns = 1
        elif act == "tsukuyomi":
            if not self.spend(fight, 7) or not self.cast_on(fight, tgt): return
            if tgt.save("Wis", DC, spell=True, kind="illusion"): tgt.take(roll(5, 10), "psychic", "Tsukuyomi")
            else: tgt.take(roll(10, 10), "psychic", "Tsukuyomi"); tgt.out = True; fight.note(f"Tsukuyomi drops {tgt.name}")
        elif act == "totsuka":
            def dmg(crit): return roll(12 if crit else 6, 8)
            def extra(crit, dealt, t=tgt):
                if dealt and not t.out and not t.save("Wis", DC, spell=True): t.seal(fight); fight.note(f"Totsuka seals {t.name}")
            attack(fight, self, tgt, self.atk(), dmg, "force", melee=False, extra=extra)
        elif act == "magatama":
            attack(fight, self, tgt, self.atk(), lambda c: roll(16 if c else 8, 8), "force", melee=False)
        elif act == "amaterasu":
            if not self.spend(fight, 6) or not self.cast_on(fight, tgt): return
            if not tgt.save("Dex", DC, spell=True): amaterasu(tgt, roll(6, 10)); tgt.burning = True
        elif act == "dominate":
            if not self.spend(fight, 5) or not self.cast_on(fight, tgt): return
            if not tgt.save("Wis", DC, spell=True, kind="charm", adv=True):
                tgt.charmed = {"mode": "dominate", "by": self, "dc": DC}; self.start_conc("dominate", tgt, fight.round)
        elif act == "hold":
            if not self.spend(fight, 2) or not self.cast_on(fight, tgt): return
            if not tgt.save("Wis", DC, spell=True, kind="enchantment"):
                tgt.paralyzed = True; tgt.held_by = self; self.start_conc("hold", tgt, fight.round)
        elif act == "killer":
            if not self.spend(fight, 4) or not self.cast_on(fight, tgt): return
            if tgt.save("Wis", DC, spell=True, kind="illusion"):
                tgt.take(roll(4, 10) // 2, "psychic", "Phantasmal Killer")
            else:
                tgt.take(roll(4, 10), "psychic", "Phantasmal Killer"); tgt.dread = True
                self.start_conc("killer", tgt, fight.round)
                def nightmare(t, me=self):
                    if me.conc != ("killer", t) or not t.dread: t.dread = False; return False
                    if t.save("Wis", DC, spell=True, kind="illusion"): t.dread = False; me.drop_conc(); return False
                    t.take(roll(4, 10), "psychic", "Phantasmal Killer"); return True
                tgt.effects.append(nightmare)
        elif act == "force":
            if not self.spend(fight, 2) or not self.cast_on(fight, tgt): return
            if not tgt.save("Int", DC, spell=True, kind="illusion"): self.start_conc("force", tgt, fight.round)
        elif act == "mislead":
            if not self.spend(fight, 5): return
            self.start_conc("mislead", None, fight.round); self.invisible = True; self.fooled = set()
        elif act == "mirror":
            if self.spend(fight, 2): self.mirror = 3
        else:
            attack(fight, self, tgt, self.atk(), lambda c: roll(8 if c else 4, 10, minv=2), "fire", melee=False, ignore_res=True)
