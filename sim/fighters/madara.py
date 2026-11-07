"""Madara Uchiha, raid boss. Sheet: Madara_Uchiha_Raid.pdf. Built as a monster in two phases, off the ladder.

Phase 1 is exponent 1, at the top of the ladder (Str 24, Dex 26, Con 26, Int 22, Wis 24, Cha 22). Phase 2 is
exponent 2, in moon units (Str 26, Dex 26, Con 26; the mind untiered: Int 24, Wis 30, Cha 24): Piccolo hits harder
and takes it better (the moon is his, on the page), Madara is quicker and carries the hax. Proficiency +9.
Sharingan genjutsu in both phases (recharge 5-6, an action): a creature that can see his eyes makes a Wis save
(DC 24, then 27) or loses its next turn to the illusion. Long-term control (Kurama, Yagura) is set up outside a
fight; inside one, a gaze buys a moment, and the victim tears out of it. Anyone with averted eyes (Guy) is immune.

Phase 1, the Edo Tensei Madara who beat the Five Kage (ch 560-591): 700 HP, AC 22, Legendary Resistance (3),
three Legendary Actions a round. The reanimated body regrows 50 HP at the start of each of his turns and can't
be killed: at 0 HP, or put down by a genjutsu, the Edo body is pinned and Phase 2 begins. Only a seal ends him
here (Itachi's Totsuka). Gunbai and kama (+16, 3d10+7, three a turn), Tengai Shinsei once (two meteors on two
turns: 18d10 to everyone, Dex 25 half), Great Fire Annihilation (recharge 5-6: 14d10 fire to everyone, Dex 25
half), the pollen of the Advent of a World of Flowering Trees once (Con 25 or asleep until hurt), and Perfect
Susanoo below half HP (AC 25; its sword cuts a line through up to four enemies for 12d10, Dex 25 half).
Legendary Actions: a gunbai strike (1); the Wood Dragon (2): Str 24 or held, 4d10 drained into him.

Phase 2, revived as the Ten-Tails jinchuriki (ch 663-677), at raid scale (moon-level by the scaling chain):
246 HP, AC 18, regrows 10 HP a turn (Hashirama's cells and the God
Tree: he recovered from being cut in half), flies. Six Paths
Senjutsu: spells and quickhacks don't take, spell saves always succeed, nothing kills him outright (the
Crucible, an Execution); ladder hits convert to almost nothing (the Seventh Gate punch did nothing and Daytime
Tiger only pushed him back), and Night Guy, an E2 technique, took half his body. Truth-Seeking Balls (+17, 2d10+3
force, three a turn, cancelling resistance and Nayru's Love alike), Chibaku Tensei (recharge 5-6: 6d10 to
everyone, Dex 25 half, and held), Limbo's shadows as his Legendary Actions (+17, 2d6+2, unseen); the
shadows time out after three of his turns and need two to come back (ch 674), and in between his Legendary
Actions throw a Truth-Seeking Ball (costs 2). The first energy blast he sees coming each round is eaten by a
Truth-Seeking Ball (in Phase 1 the Preta Path drinks it and heals him 30); not while he's held or blinded. At the start
of his fourth Phase 2 turn the moon rises: the Infinite Tsukuyomi takes everyone who isn't under a Rinnegan
or Susanoo's cover. Itachi's Susanoo shelters him and two others, the way Sasuke's sheltered Team 7.
"""
from ..engine import Combatant, attack, d, d20, roll


class Madara(Combatant):
    name = "Madara"; danger = 10; caster = True
    raid_boss = True; legendary_actions = 3

    @property
    def tier(self): return 2 if getattr(self, "phase", 1) == 2 else 1      # the Edo body is ladder-top; the jinchuriki is the moon

    def __init__(self):
        super().__init__()
        self.phase = 1; self.sealed = False; self._out = False
        self.hp = self.maxhp = 700; self.ac = 22
        self.saves = dict(Str=7, Dex=17, Con=17, Int=15, Wis=16, Cha=6)
        self.legendary_resist = 3
        self.meteors = 2; self.meteor_cast = False; self.flame = True; self.pollen = True; self.perfect = False
        self.chibaku = True; self.p2_turns = 0; self.dreamed = False; self.limbo = 0; self.gaze = True

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
        self.phase = 2; self.hp = self.maxhp = 246; self.ac = 18; self.thp = 0
        self.saves = dict(Str=8, Dex=17, Con=17, Int=16, Wis=19, Cha=7); self.limbo = 0; self.gaze = True
        self.paralyzed = False; self.asleep = False; self.charmed = None; self.burning = False; self.dread = False
        self.effects = []; self.p2_turns = 0; self.perfect = False

    def before_first_round(self, fight):
        # raid against raid is the strongest version: the jinchuriki. The revival was Black Zetsu's doing, not his.
        if any(e.tier >= 2 for e in fight.enemies(self)): self.phase_two()

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

    def defend_ac(self, att, total, melee, crit):
        # the first energy blast at him each round: the Preta Path drinks it, or a Truth-Seeking Ball eats it
        if not melee and self.reaction and getattr(att, "energy", False) and not self.incapacitated() and not self.dread:
            self.reaction = False
            if self.phase == 1: self.hp = min(self.maxhp, self.hp + 30)
            return None
        return 0

    def needs_moon(self): return self.phase == 2

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
            attack(fight, self, tgt, 16, lambda c: roll(6 if c else 3, 10) + 7, "bludgeoning", True)
        else:
            attack(fight, self, tgt, 17, lambda c: (roll(4 if c else 2, 6) + 2) if lim else (roll(4 if c else 2, 10) + 3),
                   "bludgeoning" if lim else "force", not lim, adv=lim, ignore_res=True, ignore_imm=True)

    def genjutsu(self, fight, enemies):
        """The Sharingan: one creature that meets his eyes, trapped until its own will gets it out."""
        if not self.gaze and d(6) >= 5: self.gaze = True
        marks = [e for e in enemies if not e.averts_eyes and e.charmed is None and not e.incapacitated()]
        if not self.gaze or not marks: return False
        tgt = max(marks, key=lambda e: e.danger); self.gaze = False
        dc = 24 if self.phase == 1 else 27
        if not tgt.save("Wis", dc, kind="illusion"):
            tgt.charmed = {"mode": "genjutsu", "by": self, "dc": dc}; fight.note(f"Madara's genjutsu takes {tgt.name}")
        return True

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
                self.everyone(fight, 18, 25, "bludgeoning"); return
            if self.genjutsu(fight, enemies): return
            if self.pollen and len(enemies) >= 3:
                self.pollen = False
                for e in enemies:
                    if not e.save("Con", 25): e.asleep = True
                return
            if not self.flame and d(6) >= 5: self.flame = True
            if self.flame and len(enemies) >= 3:
                self.flame = False; self.everyone(fight, 14, 25, "fire"); return
            if self.perfect:
                for e in enemies[:4]:                                       # the Susanoo's sword through a line of them
                    saved = e.save("Dex", 25); dmg = e.dex_damage(saved, roll(12, 10))
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
        self.limbo = (self.limbo + 1) % 5          # shadows out for three turns, then two to come back
        self.hp = min(self.maxhp, self.hp + 10)
        if self.p2_turns >= 4 and fight.moon and not self.dreamed:
            self.dreamed = True; self.infinite_tsukuyomi(fight); return
        if self.genjutsu(fight, enemies): return
        if not self.chibaku and d(6) >= 5: self.chibaku = True
        if self.chibaku and len(enemies) >= 2:
            self.chibaku = False; self.everyone(fight, 6, 25, "bludgeoning", rider=self.held); return
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
        if self.phase == 2 and not (1 <= self.limbo <= 3):
            if self.la_left >= 2: self.la_left -= 2; self.strike(fight, tgt)   # a thrown Truth-Seeking Ball
            else: self.la_left = 0
            return
        self.la_left -= 1
        self.strike(fight, tgt, lim=(self.phase == 2))                     # a gunbai strike, or a Limbo shadow
