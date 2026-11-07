"""Madara Uchiha, raid boss. Sheet: Madara_Uchiha_Raid.pdf. Built as a monster in two phases, off the ladder.

Phase 1, the Edo Tensei Madara who beat the Five Kage (ch 560-591): 700 HP, AC 22, Legendary Resistance (3),
three Legendary Actions a round. The reanimated body regrows 50 HP at the start of each of his turns and can't
be killed: at 0 HP, or put down by a genjutsu, the Edo body is pinned and Phase 2 begins. Only a seal ends him
here (Itachi's Totsuka). Gunbai and kama (+16, 3d10+9, three a turn), Tengai Shinsei once (two meteors on two
turns: 18d10 to everyone, Dex 24 half), Great Fire Annihilation (recharge 5-6: 14d10 fire to everyone, Dex 24
half), the pollen of the Advent of a World of Flowering Trees once (Con 24 or asleep until hurt), and Perfect
Susanoo below half HP (AC 25; its sword cuts a line through up to four enemies for 12d10, Dex 24 half).
Legendary Actions: a gunbai strike (1); the Wood Dragon (2): Str 24 or held, 4d10 drained into him.

Phase 2, revived as the Ten-Tails jinchuriki (ch 663-677): 900 HP, AC 24, regrows 30 HP a turn, flies. Six Paths
Senjutsu: spells and quickhacks don't take, spell saves always succeed, nothing kills him outright (the
Crucible, an Execution), and any single hit under 100 damage does nothing (the Seventh Gate punch did nothing and
Daytime Tiger only pushed him back; Night Guy took half his body). Truth-Seeking Balls (+18,
4d10+9 force, three a turn, cancelling resistance and Nayru's Love alike), Chibaku Tensei (recharge 5-6: 18d10
to everyone, Dex 25 half, and held), Limbo's shadows as his Legendary Actions (+18, 3d10+9, unseen). At the start
of his fourth Phase 2 turn the moon rises: the Infinite Tsukuyomi takes everyone who isn't under a Rinnegan
or Susanoo's cover. Itachi's Susanoo shelters him and two others, the way Sasuke's sheltered Team 7.
"""
from ..engine import Combatant, attack, d, d20, roll


class Madara(Combatant):
    name = "Madara"; danger = 10; caster = True
    raid_boss = True; legendary_actions = 3

    def __init__(self):
        super().__init__()
        self.phase = 1; self.sealed = False; self._out = False
        self.hp = self.maxhp = 700; self.ac = 22
        self.saves = dict(Str=5, Dex=14, Con=15, Int=14, Wis=14, Cha=6)
        self.legendary_resist = 3
        self.meteors = 2; self.meteor_cast = False; self.flame = True; self.pollen = True; self.perfect = False
        self.chibaku = True; self.p2_turns = 0

    # the Edo body can't be put down for good; Phase 2 starts instead
    @property
    def out(self): return self._out
    @out.setter
    def out(self, v):
        if v and getattr(self, "phase", 2) == 1 and not getattr(self, "sealed", False):
            self.phase_two(); return
        if v and getattr(self, "phase", 1) == 2 and self.hp > 0: return      # no instant kills on the jinchuriki
        self._out = v

    def seal(self, fight):
        if self.phase == 1: self.sealed = True; fight.note("the Totsuka seals Madara"); self.out = True

    def phase_two(self):
        self.phase = 2; self.hp = self.maxhp = 900; self.ac = 24; self.thp = 0
        self.paralyzed = False; self.asleep = False; self.charmed = None; self.burning = False; self.dread = False
        self.effects = []; self.p2_turns = 0; self.perfect = False

    def init(self): return d20(adv=True) + 7
    def ac_now(self): return 25 if (self.phase == 1 and self.perfect) else self.ac
    def save_adv(self, ab, spell): return False

    def save(self, ab, dc, spell=False, kind=None, adv=False):
        if self.phase == 2 and spell: return True                       # Six Paths: ninjutsu doesn't take
        return super().save(ab, dc, spell, kind, adv or kind in ("illusion", "charm"))   # the Sharingan

    def spend_legendary_resistance(self, ab, dc, spell, kind):
        return spell or kind is not None or dc >= 20                    # he saves them for what matters

    def negates_spells(self): return self.phase == 2
    def sealable(self): return self.phase == 1

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        if self.phase == 2 and dmg < 100: return 0                      # the threshold
        return dmg

    def on_zero(self, src, crit):
        if self.phase == 1 and not self.sealed: self.phase_two(); return
        self.hp = 0; self._out = True

    # ---------- his attacks ----------
    def everyone(self, fight, dmg_dice, dc, dtype, ab="Dex", rider=None):
        for e in list(fight.enemies(self)):
            saved = e.save(ab, dc)
            dmg = e.dex_damage(saved, roll(dmg_dice, 10)) if ab == "Dex" else roll(dmg_dice, 10) // (2 if saved else 1)
            if dmg: e.take(dmg, dtype, self.name, ignore_res=(self.phase == 2))
            if not saved and rider and e.alive(): rider(e)

    def strike(self, fight, tgt, lim=False):
        if self.phase == 1:
            attack(fight, self, tgt, 16, lambda c: roll(6 if c else 3, 10) + 9, "bludgeoning", True)
        else:
            attack(fight, self, tgt, 18, lambda c: roll((6 if c else 3) if lim else (8 if c else 4), 10) + 9,
                   "bludgeoning" if lim else "force", not lim, adv=lim, ignore_res=True, ignore_imm=True)

    def held(self, e):
        e.dread = True
        def free(c): c.dread = False; return False
        e.effects.append(free)

    def turn(self, fight):
        enemies = fight.enemies(self)
        if not enemies: return
        if self.phase == 1:
            self.hp = min(self.maxhp, self.hp + 50)                       # the Edo body regrows
            if not self.perfect and self.hp < self.maxhp // 2: self.perfect = True
            if self.meteors and (self.meteor_cast or fight.round == 1):
                self.meteor_cast = True; self.meteors -= 1                 # Tengai Shinsei: one, then the second on it
                self.everyone(fight, 18, 24, "bludgeoning"); return
            if self.pollen and len(enemies) >= 3:
                self.pollen = False
                for e in enemies:
                    if not e.save("Con", 24): e.asleep = True
                return
            if not self.flame and d(6) >= 5: self.flame = True
            if self.flame and len(enemies) >= 3:
                self.flame = False; self.everyone(fight, 14, 24, "fire"); return
            if self.perfect:
                for e in enemies[:4]:                                       # the Susanoo's sword through a line of them
                    saved = e.save("Dex", 24); dmg = e.dex_damage(saved, roll(12, 10))
                    if dmg: e.take(dmg, "force", self.name)
                return
            for i in range(3):
                tgt = fight.pick_target(self)
                if not tgt: return
                self.strike(fight, tgt)
                if fight.over(): return
            return
        # Phase 2
        self.p2_turns += 1
        self.hp = min(self.maxhp, self.hp + 30)
        if self.p2_turns == 4:
            self.infinite_tsukuyomi(fight); return
        if not self.chibaku and d(6) >= 5: self.chibaku = True
        if self.chibaku and len(enemies) >= 2:
            self.chibaku = False; self.everyone(fight, 18, 25, "bludgeoning", rider=self.held); return
        for i in range(3):
            tgt = fight.pick_target(self)
            if not tgt: return
            self.strike(fight, tgt)
            if fight.over(): return

    def infinite_tsukuyomi(self, fight):
        fight.note("the moon rises: the Infinite Tsukuyomi")
        shelter = set()
        for e in fight.enemies(self):
            if e.susanoo:               # a Susanoo under the moonlight, like Sasuke's over Team 7
                shelter.add(e)
                others = sorted([x for x in fight.allies(e) if not x.summon], key=lambda x: -x.danger)[:2]
                shelter.update(others)
        for e in list(fight.enemies(self)):
            if e not in shelter: e.out = True

    def legendary_action(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        if self.phase == 1 and self.la_left >= 2 and not tgt.dread and d(2) == 1:
            self.la_left -= 2                                              # the Wood Dragon
            if not tgt.save("Str", 24):
                self.held(tgt); dmg = tgt.take(roll(4, 10), "necrotic", self.name); self.hp = min(self.maxhp, self.hp + dmg)
            return
        self.la_left -= 1
        self.strike(fight, tgt, lim=(self.phase == 2))                     # a gunbai strike, or a Limbo shadow
