"""Talion, the Gravewalker: Ranger (Wraith-Bound) 17 / Fighter (Battle Master) 3, Shadow of War Act 3.
Sheet: Talion_5e_Build.pdf (Caleb's). 224 HP, AC 17, initiative +11 (Alert).

Urfael +13 for 1d8+9 (Sap), Azkar's Elf-shot +15 for 1d8+7 radiant with Focus (8 a short rest), and
Shadow Strike: after an Elf-shot hit, a bonus-action teleport and one Urfael strike. Hunter's Mark is free
six times a day, gives advantage against the marked foe (Precise Hunter) and damage can't break it.
The Might bar: +1 a weapon hit (3 a turn at most), -2 whenever an attack hits him; Execution (3: the hit
is a critical, and a foe left at 30 HP or fewer makes a DC 16 Con save or dies; everyone in this arena is
a named captain), Wraith Flash (2: Con save, 3d8 radiant and stunned), Combat Drain (2), Brutalize (2),
Elven Rage (all 6: resistance, advantage, every melee hit a free Execution).
Battle Master: Riposte and Menacing Attack from four d8s. Action Surge, Second Wind twice, Nature's Veil
twice, Last Chance at 0 HP (DC 10, +5 a use), Two Minds against charm and fear, Steel Wind Strike and
Conjure Barrage for crowds.

Not here: Brand and the army (orcs and beasts only, and the sheet says they don't matter against one foe),
the New Ring's bodyguard, mounts, and Banished from Death (it brings him back after the fight, not during)."""
from ..engine import Combatant, attack, d, d20, roll

WRAITH_DC = 16; MANEUVER_DC = 19


class Talion(Combatant):
    name = "Talion"; danger = 4; melee = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 224; self.ac = 17
        self.saves = dict(Str=7, Dex=11, Con=3, Int=0, Wis=2, Cha=-1)
        self.might = 0; self.might_round = -1; self.might_gained = 0
        self.elf_shot = 8; self.marks = 6; self.mark = None; self.slots = {1: 4, 2: 3, 3: 3, 4: 3, 5: 1}
        self.sup = 4; self.sw = 2; self.surge = 1; self.veil = 2; self.veil_until = None
        self.last_chance_dc = 10; self.two_minds = True; self.rage_until = None; self.menaced = []

    def init(self): return d(20) + 11
    def raging(self): return self.rage_until is not None

    # ---------- the Might bar ----------
    def gain(self, fight, n=1):
        if self.might_round != fight.round: self.might_round = fight.round; self.might_gained = 0
        n = min(n, 3 - self.might_gained)
        if n > 0: self.might = min(6, self.might + n); self.might_gained += n

    def take(self, dmg, dtype, src, **kw):
        if kw.get("from_attack") and not self.out: self.might = max(0, self.might - 2)     # the streak breaks
        return super().take(dmg, dtype, src, **kw)

    # ---------- defence ----------
    def save(self, ab, dc, spell=False, kind=None, adv=False):
        ok = super().save(ab, dc, spell, kind, adv)
        if not ok and kind in ("charm", "fear") and self.two_minds:
            self.two_minds = False; ok = super().save(ab, dc, spell, kind, adv)     # Celebrimbor's will
        return ok

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        return dmg // 2 if self.raging() and not ignore_res else dmg

    def on_zero(self, src, crit):
        # Last Chance
        if d20() + self.saves["Con"] >= self.last_chance_dc: self.last_chance_dc += 5; self.hp = 1; return
        self.out = True

    def on_missed(self, fight, att, melee):
        # Riposte: a melee miss buys a counter-strike, +1d8
        if melee and self.reaction and self.sup > 0 and self.alive() and not self.incapacitated():
            self.reaction = False; self.sup -= 1
            fight.after_turn(lambda: att.alive() and self.alive() and self.strike(fight, att, die=True))

    # ---------- attacks ----------
    def mark_bonus(self, t, crit): return roll(2 if crit else 1, 6) if t is self.mark else 0

    def strike(self, fight, tgt, die=False, execution=False, brutalize=False, menace=False):
        """One Urfael attack."""
        adv = tgt is self.mark or self.raging()
        def dmg(crit):
            c = crit or execution          # an Execution's hit is a critical hit
            v = roll(2 if c else 1, 8) + 9 + self.mark_bonus(tgt, c)
            if die or menace: v += roll(2 if c else 1, 8)
            if brutalize: v += roll(6 if c else 3, 8)
            return v
        def extra(crit, dealt, t=tgt):
            if dealt and not t.out: t.sapped = True
            if dealt and execution and not t.out and (t.hp + t.thp) <= 30 and not t.save("Con", WRAITH_DC):
                t.out = True; fight.note(f"Talion executes {t.name}")
            if dealt and menace and not t.out and not t.fright_immune and not t.save("Wis", MANEUVER_DC, kind="fear"):
                t.frightened = True; self.menaced.append((t, fight.round))
            if brutalize and t.out:
                for e in fight.enemies(self):
                    if not e.fright_immune and not e.save("Wis", WRAITH_DC, kind="fear"): e.frightened = True; e.fear_dc = WRAITH_DC
        hit, crit, dealt = attack(fight, self, tgt, 13, dmg, "slashing", True, adv=adv, extra=extra)
        if hit: self.gain(fight)
        return hit

    def elf_shot_at(self, fight, tgt):
        self.elf_shot -= 1
        def dmg(crit): return roll(2 if crit else 1, 8) + 7 + self.mark_bonus(tgt, crit)
        hit, crit, dealt = attack(fight, self, tgt, 15, dmg, "radiant", melee=False, adv=True)   # Focus
        if hit: self.gain(fight)
        return hit

    def wraith_flash(self, fight):
        self.might -= 2
        for e in [e for e in fight.enemies(self) if e.melee]:
            saved = e.save("Con", WRAITH_DC)
            e.take(roll(3, 8) // (2 if saved else 1), "radiant", "Wraith Flash")
            if not saved and e.alive() and not e.never_stunned and not e.stun_immune:
                e.paralyzed = True; e.stun_until = fight.round

    def melee_attack(self, fight, tgt, first):
        """One melee attack of the Attack action, with whatever Might technique fits."""
        if self.raging(): return self.strike(fight, tgt, execution=True)
        if self.might >= 3 and (tgt.hp + tgt.thp) <= 55:
            self.might -= 3; return self.strike(fight, tgt, execution=True)
        if self.might == 2 and (tgt.hp + tgt.thp) <= 35:
            self.might -= 2; return self.strike(fight, tgt, brutalize=True)
        menace = first and self.sup > 1 and not tgt.fright_immune and not tgt.frightened
        if menace: self.sup -= 1
        return self.strike(fight, tgt, menace=menace)

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        # bonus action first when it can't wait
        bonus = None
        if self.might >= 6 and not self.raging():
            self.might = 0; self.rage_until = fight.round + 1; bonus = "rage"            # Elven Rage
        elif (self.mark is None or not self.mark.alive()) and self.marks > 0:
            self.marks -= 1
            if fight.cast(self, 1): self.mark = tgt
            bonus = "mark"
        elif self.hp <= 0.35 * self.maxhp and self.sw > 0:
            self.sw -= 1; self.hp = min(self.maxhp, self.hp + d(10) + 3); bonus = "sw"
        elif self.hp <= 0.5 * self.maxhp and self.veil > 0 and not self.invisible:
            self.veil -= 1; self.invisible = True; self.veil_until = fight.round + 1; bonus = "veil"
        if self.mark is not None and self.mark.alive(): tgt = self.mark
        actions = 1 + (1 if self.surge else 0); self.surge = 0
        shot_hit = False
        for a in range(actions):
            enemies = fight.enemies(self)
            if not enemies: return
            if len(enemies) >= 3 and self.slots[5]:
                self.slots[5] -= 1
                if fight.cast(self, 5):            # Steel Wind Strike through up to five of them
                    for e in enemies[:5]:
                        attack(fight, self, e, 8, lambda c: roll(12 if c else 6, 10), "force", True)
                continue
            if len(enemies) >= 3 and self.slots[3]:
                self.slots[3] -= 1
                if fight.cast(self, 3):            # Conjure Barrage, a fan of Elf-shot
                    for e in enemies:
                        dmg = e.dex_damage(e.save("Dex", WRAITH_DC, spell=True), roll(5, 8))
                        if dmg: e.take(dmg, "force", "Conjure Barrage")
                continue
            if self.might >= 2 and sum(1 for e in enemies if e.melee) >= 2 and not self.raging():
                self.wraith_flash(fight); n = 1     # Wraith Flash replaces one of the two attacks
            else:
                n = 2
            bow = bonus is None and self.elf_shot >= n and not self.raging() and not shot_hit
            for i in range(n):
                if tgt.out: tgt = fight.pick_target(self)
                if not tgt: return
                if bow: shot_hit = self.elf_shot_at(fight, tgt) or shot_hit
                else: self.melee_attack(fight, tgt, first=(a == 0 and i == 0))
                if fight.over(): return
        # bonus action afterwards: Shadow Strike off an Elf-shot hit (no arrow needed in Elven Rage), or Combat Drain
        if bonus is None:
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: return
            if shot_hit or self.raging():
                self.melee_attack(fight, tgt, first=False)
            elif self.might >= 2 and (tgt.paralyzed or tgt.prone) and self.hp < self.maxhp - 20:
                self.might -= 2
                tgt.take(roll(2, 8), "necrotic", "Combat Drain")
                self.hp = min(self.maxhp, self.hp + roll(2, 8) + 2); self.elf_shot = min(8, self.elf_shot + 3)

    def end_turn(self, fight):
        super().end_turn(fight)
        if self.rage_until is not None and fight.round >= self.rage_until: self.rage_until = None
        if self.veil_until is not None and fight.round >= self.veil_until: self.invisible = False; self.veil_until = None
        keep = []
        for t, r in self.menaced:       # Menacing Attack lasts until the end of his next turn
            if fight.round > r:
                if t.fear_dc == 0: t.frightened = False
            else: keep.append((t, r))
        self.menaced = keep
