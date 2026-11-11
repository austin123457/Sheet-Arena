"""Dark Link, the shadow of the Hero of Time (Ocarina of Time, the Water Temple). Sheet: Dark_Link_5e_Build.pdf.
A reflection of the hero at whatever level he walks in: on the ladder, Fighter (Battle Master) 20. It has his body,
his sword arm and the two things in his hands: 224 HP (two for every heart the hero has), AC 20, his saves,
initiative +11, and the shadow of the Master Sword at +14 for 1d8+10. Four swings a turn, Action Surge twice,
Indomitable three times, and six d12 superiority dice, every one of them an Ending Blow (Trip, and a hit on a prone
creature is a critical hit): it spends one on each hit until they're gone. The shadow of the Hylian Shield keeps
its Reaction, 1d10+11 off a ranged weapon attack. It doesn't Parry: its Reaction against a blade is the Answer.
It doesn't have the pack, the Magic Meter, the bottles, the fairies or the Triforce, the copy of the sword has no
Evil's Bane in it, and it has no Second Wind: nothing in the game heals it but the hero leaving the room.

What only the shadow does, all of it from the fight in the game:
  Mirror: when a creature it can see hits it with a melee weapon swung in one hand (one_handed), it makes the same
    swing. It rolls a d20, and if that equals or beats the number on the attacker's die, the blades meet and the
    attack misses. Nobody adds a bonus: it has yours. Not while prone, incapacitated or staggered.
  Stagger: the sixth time the blades meet, it staggers until the end of that turn: no Mirror, no Reaction, no
    sinking, and attacks against it have advantage. The third time, if the creature whose blade it met is down to
    a quarter of its hit points (the game halves the count when the hero is under five hearts).
  Answer (a Reaction, when a melee attack misses it): if the blades met it is Standing on the Blade, one sword
    attack with advantage; if the attack just missed it has side-hopped, and the answer is a Jump Slash for 2d8+10.
  Sink into the Floor: the first time on each turn that an attack damages it, it sinks and comes up behind the
    attacker. That creature's other attacks against it this turn have disadvantage, and its own first attack
    against that creature on its next turn has advantage.
  Shadow Roll: ranged weapon attacks against it have disadvantage, and it has advantage on Dexterity saves against
    anything that isn't a spell. Against magic it only raises its shield.

A shadow: a creature of evil (the Master Sword's extra damage applies), not a humanoid, and it can't be poisoned,
charmed or frightened. A Deku Nut stuns it like anyone else, and at 0 it fades.

translucent is the number of its turns left before it turns solid. In its own room it wakes translucent and takes a
minute (ten rounds) to turn solid, and until then it never attacks, on its turn or with its Reaction. On the ladder
it walks in solid (0)."""
from ..engine import Combatant, attack, d, roll


class DarkLink(Combatant):
    name = "Dark Link"; danger = 4; melee = True
    evil = True; humanoid = False; mirrors = True; one_handed = True
    poison_immune = True; charm_immune = True; fright_immune = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 224; self.ac = 20
        self.saves = dict(Str=8, Dex=5, Con=9, Int=0, Wis=3, Cha=-1); self.indomitable = 3
        self.surges = 2; self.dice = 6
        self.translucent = 0
        self.clanks = 0; self.staggered = None      # the turn it staggered on
        self.sunk = None; self.sunk_by = None       # the turn it last sank on, and whose blow sent it under
        self.behind = set()                         # who it has come up behind since its last turn
        self.bonus = 0                              # the attack bonus of the swing coming in

    def init(self): return d(20) + 11

    def now(self):
        f = self.fight
        return (f.round, id(f.actor)) if f else None

    def is_staggered(self): return self.staggered is not None and self.staggered == self.now()

    def save_adv(self, ab, spell): return ab == "Dex" and not spell and not self.incapacitated()

    # ---------- attacks against it ----------
    def incoming_attack(self, attacker, bonus, adv, dis, melee=True):
        self.bonus = bonus
        if not melee and not attacker.caster and not attacker.invisible and not self.incapacitated(): dis = True   # Shadow Roll
        if self.is_staggered(): adv = True
        elif self.sunk is not None and self.sunk == self.now() and attacker.name == self.sunk_by: dis = True
        return adv, dis

    def defend_ac(self, att, total, melee, crit):
        if not melee or not att.one_handed or att.invisible: return 0
        if self.prone or self.incapacitated() or self.is_staggered(): return 0
        nat = total - self.bonus
        if not crit and (nat == 1 or total < self.ac_now()): return 0       # a miss needs no answer
        if d(20) < nat: return 0
        self.clanks += 1                                                    # the blades meet
        if self.clanks >= (3 if att.hp * 4 <= att.maxhp else 6):
            self.clanks = 0; self.staggered = self.now()
            if self.fight: self.fight.note(f"Dark Link staggers ({att.name})")
        else: self.answer(att, jump=False)
        return None

    def on_missed(self, fight, att, melee):
        if melee and not self.is_staggered(): self.answer(att, jump=True)

    def answer(self, att, jump):
        f = self.fight
        if not f or not self.reaction or self.translucent > 0 or not self.can_act(): return
        self.reaction = False
        f.after_turn(lambda: att.alive() and self.can_act() and self.swing(f, att, adv=not jump, jump=jump))

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        if not from_attack or self.incapacitated(): return dmg
        if not melee and self.reaction: self.reaction = False; dmg = max(0, dmg - (d(10) + 11))     # the shield
        if dmg > 0 and self.fight and self.now() not in (self.sunk, self.staggered):   # Sink into the Floor
            self.sunk = self.now(); self.sunk_by = src; self.behind.add(src)
        return dmg

    # ---------- its own ----------
    def swing(self, fight, tgt, adv=False, jump=False, die=False):
        prone = tgt.prone
        def dmg(crit):
            v = roll((2 if crit else 1) * (2 if jump else 1), 8) + 10
            if die: v += roll(2 if crit else 1, 12)
            return v
        def extra(crit, dealt, t=tgt):
            if dealt and die:
                self.dice -= 1                                                      # Ending Blow
                if not t.prone and not t.susanoo and not t.save("Str", 19): t.prone = True
        return attack(fight, self, tgt, 14, dmg, "slashing", True, adv=adv, crit_range=1 if prone else 20, extra=extra)[0]

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        if self.translucent > 0: self.translucent -= 1; self.behind.clear(); return     # it only mirrors and evades
        actions = 1
        if self.surges > 0: self.surges -= 1; actions = 2
        for a in range(actions):
            for i in range(4):
                if tgt.out: tgt = fight.pick_target(self)
                if not tgt: return
                adv = tgt.name in self.behind; self.behind.discard(tgt.name)
                self.swing(fight, tgt, adv=adv, die=self.dice > 0)
                if fight.over(): return
        self.behind.clear()
