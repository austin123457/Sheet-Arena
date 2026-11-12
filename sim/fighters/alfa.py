"""FLLFFL, "Alfa", the Rock Hard Gladiator with the Jet Sword: Human, Fighter (Battle Master) 13 / Rogue
(Assassin) 7. Sheet: FLLFFL_Alfa_5e_Build.pdf. 217 HP, AC 17, initiative +11 with advantage (Alert, Assassinate),
Evasion, Indomitable twice at +13.

The Jet Sword (homebrew, a +3 katana with a jet in the blunt end): +14 for 1d8+10 slashing, and 2d6 fire on every
hit. Three cuts per Attack action, Action Surge once for three more, and the Jet Lunge on his bonus action for one
last cut. Second Wind (four, 1d10 + 13) takes the bonus action instead once he's below half.

Advantage, which is what Sneak Attack (4d6, once a turn) needs:
  Assassinate: in the first round, against anyone who hasn't acted; a Sneak Attack that round deals 7 more.
  Vex: a cut that draws blood gives advantage on his next attack against that creature.
  Studied Attacks: so does a cut that misses.
So from the second swing on he almost always has it.

One Reaction a round, with three jobs, taken in the order the blows arrive:
  Parry (Defensive Duelist): a melee hit a +6 would stop is stopped, and the +6 stays up against melee until his
    next turn.
  Uncanny Dodge: halve a bullet, or a blade too big to parry (20 or more: a smaller one isn't worth the
    Reaction a Parry may still want), if he can see who it came from.
  Riposte: a superiority die (five d10) and a cut back when a blade misses him. It lands on somebody else's turn,
    so Sneak Attack is there again.
A die also turns a near miss into a hit on his own turn (Precision Attack).

The fire is dealt as its own damage after the steel (as Spike's Sneak Attack is), so armor that halves blades halves
the blade and not the flame, and a regenerating body feels it.

Against a mirror he takes the katana in both hands (Versatile: 1d10+8, and Dueling is gone): the arena's ruling is
that Dark Link can't copy a two-handed swing.

Not here: the shuriken (no flame, and nothing in the arena has to be reached), Cunning Strike, Feinting and
Disarming Attack, the Parry maneuver (Uncanny Dodge does the same job for no die), and losing the sword: nobody in
the arena disarms. His code (a foe he drops is knocked out, not killed) changes nothing here, where nobody stays
dead. He's a man: at 0 he's down, and nothing on the sheet brings him back."""
from ..engine import Combatant, attack, d, d20, roll

ATK = 14


class Alfa(Combatant):
    name = "Alfa"; danger = 3; melee = True
    evasion = True; one_handed = True

    heal_at = 108           # Second Wind below this
    near = 5                # how near a miss has to be
    dodge_at = 20           # a blade has to be this big before Uncanny Dodge takes the Reaction from Parry

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 217; self.ac = 17
        self.saves = dict(Str=6, Dex=5, Con=9, Int=0, Wis=8, Cha=-1); self.indomitable = 2; self.indom_bonus = 13
        self.dice = 5; self.sw = 4; self.surges = 1
        self.parry = False                          # Defensive Duelist is up
        self.edge = set()                           # who his next attack has advantage against (Vex, Studied Attacks)
        self.swung = False; self.short_by = 99; self.sees = True

    def init(self): return d20(adv=True) + 11

    def before_first_round(self, fight):
        if any(e.mirrors for e in fight.enemies(self)): self.one_handed = False       # both hands on the hilt

    def start_turn(self):
        super().start_turn(); self.parry = False; self.swung = False

    def end_turn(self, fight):
        super().end_turn(fight)
        if not self.swung: self.edge.clear()        # Vex and Studied Attacks last to the end of his next turn

    # ---------- the one Reaction ----------
    def defend_ac(self, att, total, melee, crit):
        self.sees = not att.invisible
        if not melee or self.incapacitated(): return 0
        if self.parry: return 6
        if self.reaction and not crit and self.ac <= total < self.ac + 6:
            self.reaction = False; self.parry = True
            if self.fight: self.fight.note("Alfa parries")
            return 6
        return 0

    def reduce_hit(self, dmg, melee):
        if self.reaction and self.sees and (dmg >= self.dodge_at or not melee) and not self.incapacitated():      # Uncanny Dodge
            self.reaction = False
            if self.fight: self.fight.note("Alfa: Uncanny Dodge")
            return dmg // 2
        return dmg

    def on_missed(self, fight, att, melee):
        if melee and self.reaction and self.dice > 0 and self.alive() and not self.incapacitated():      # Riposte
            self.reaction = False; self.dice -= 1
            fight.after_turn(lambda: att.alive() and self.alive() and self.cut(fight, att, riposte=True))

    def answer_standoff(self, fight, jin):
        self.cut(fight, jin, adv=True)

    # ---------- the Jet Sword ----------
    def on_miss(self, fight, tgt, total, ac, melee):
        self.short_by = 99 if total - ATK == 1 else ac - total      # a natural 1 is past saving

    def steel(self, crit=False):
        return roll(2 if crit else 1, 8) + 10 if self.one_handed else roll(2 if crit else 1, 10) + 8

    def cut(self, fight, tgt, adv=False, riposte=False):
        """One Jet Sword attack. Returns True on a hit."""
        self.swung = True
        if riposte: self.sa_used = False            # it isn't his turn: Sneak Attack is once a turn, not once a round
        adv = adv or tgt.name in self.edge or (fight.round == 1 and not tgt.acted)
        self.edge.discard(tgt.name)
        fresh = not self.sa_used
        def dmg(crit):
            return self.steel(crit) + (roll(2 if crit else 1, 10) if riposte else 0)
        def extra(crit, dealt, t=tgt):
            if dealt: self.edge.add(t.name)                                           # Vex
            if fresh and self.sa_used and fight.round == 1: t.take(7, "slashing", self.name)      # Assassinate
            t.take(roll(4 if crit else 2, 6), "fire", self.name)                      # the blue flame
        self.short_by = 99
        hit, crit, dealt = attack(fight, self, tgt, ATK, dmg, "slashing", True, adv=adv, sneak=4, extra=extra)
        if hit: return True
        # Precision Attack: a d10 on a near miss
        if not tgt.out and fight.actor is self and self.dice > 0 and self.short_by <= self.near:
            self.dice -= 1
            if d(10) >= self.short_by:
                fight.note("Alfa: Precision Attack")
                dealt = tgt.take(tgt.reduce_hit(self.steel(), True), "slashing", self.name, from_attack=True, melee=True)
                if dealt: self.edge.add(tgt.name)
                tgt.take(roll(2, 6), "fire", self.name)
                return True
        self.edge.add(tgt.name)                                                       # Studied Attacks
        return False

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        n = 3
        if self.surges > 0: self.surges -= 1; n += 3
        if self.hp <= self.heal_at and self.sw > 0: self.sw -= 1; self.hp = min(self.maxhp, self.hp + d(10) + 13)
        else: n += 1                                # the Jet Lunge
        for i in range(n):
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: break
            self.cut(fight, tgt)
            if fight.over(): return
