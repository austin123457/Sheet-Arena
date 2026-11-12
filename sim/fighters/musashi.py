"""Miyamoto Musashi at fifty: Human, Fighter (Battle Master) 20. Sheet: Miyamoto_Musashi_5e_Build.pdf.
204 HP, AC 16 with no armor (10 + Dex + Wis) and 22 against melee while he holds both swords. Two swords at +13:
the katana for 1d8+7 (Sap), the wakizashi for 1d6+7.

Six attacks a turn (four, the Nick cut, and Dual Wielder's bonus action), Action Surge twice, Second Wind four times.
Six d12 superiority dice, and Relentless gives a free d8 once on every turn, his or anyone else's: Trip on his own,
Parry or Riposte on theirs. Precision, Studied Attacks, Peerless Aim (one miss a turn becomes a hit), and Slasher
(a critical hit leaves its target attacking at disadvantage until his next turn).

Niten Ichi-ryu, from the sheet's five rings:
  Two swords, two Reactions. The short sword receives: +6 AC against melee all the time, and its Reaction is Parry
    on a hit or Riposte on a miss. The long sword's Reaction is Holding Down the Pillow: when a melee attack would
    hit him, he cuts first, and if that cut hits, the attack misses.
  Ken no sen: advantage on initiative, and on attacks in the first round against anyone who hasn't acted.
  Rhythm: from the third round, the first attack each creature makes at him on its turn has disadvantage, and his
    first attack each turn has advantage.
  One Cut, once: a katana hit becomes a critical hit, ignores resistance, and takes every superiority die but one.
  The Way of Walking Alone: can't be frightened, advantage against charms and illusions; Indomitable three times
    at +20.

He's a man: at 0 he's down, and nothing on the sheet brings him back."""
from ..engine import Combatant, attack, d, d20, roll

DC = 19


class Musashi(Combatant):
    name = "Musashi"; danger = 4; melee = True
    fright_immune = True; one_handed = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 204; self.ac = 16
        self.saves = dict(Str=11, Dex=3, Con=8, Int=1, Wis=9, Cha=-1); self.indomitable = 3; self.indom_bonus = 20
        self.dice = 6; self.sw = 4; self.surges = 2; self.one_cut = True
        self.short = True                           # the wakizashi's Reaction; self.reaction is the katana's
        self.slashed = set()                        # Slasher: who a critical hit has left swinging at disadvantage
        self.free = None; self.seen = set(); self.prowess = True; self.studied = set(); self.short_by = 99

    def init(self): return d20(adv=True) + 9

    def save(self, ab, dc, spell=False, kind=None, adv=False):
        return super().save(ab, dc, spell, kind, adv or kind in ("charm", "illusion"))

    def start_turn(self):
        super().start_turn(); self.short = True; self.slashed = set()

    # ---------- the dice ----------
    def die(self, spend=True):
        """A superiority die: Relentless's free d8 once on each turn (anyone's), then a d12 from the pool."""
        f = self.fight; key = (f.round, id(f.actor)) if f else None
        if key != self.free: self.free = key; return d(8)
        if spend and self.dice > 0: self.dice -= 1; return d(12)
        return 0

    def rhythm(self): return self.fight is not None and self.fight.round >= 3

    # ---------- attacks against him ----------
    def incoming_attack(self, attacker, bonus, adv, dis, melee=True):
        if id(attacker) in self.slashed: dis = True
        if self.rhythm() and not self.incapacitated():
            key = (id(attacker), self.fight.round, id(self.fight.actor))
            if key not in self.seen: self.seen.add(key); dis = True
        return adv, dis

    def defend_ac(self, att, total, melee, crit):
        if not melee or self.incapacitated(): return 0
        # Holding Down the Pillow: the long sword cuts into a blow that would land; if the cut hits, the blow doesn't
        if self.reaction and not crit and total >= self.ac + 6 and att.alive():
            self.reaction = False
            if self.cut(self.fight, att, long=True, pillow=True): return None
        return 6                                    # the short sword is always in the way

    def reduce_hit(self, dmg, melee):
        if melee and self.short and not self.incapacitated():      # Parry: the smacking parry
            r = self.die(spend=dmg >= 20 and self.dice > 2)
            if r:
                self.short = False
                if self.fight: self.fight.note(f"Musashi parries {min(dmg, r + 5)}")
                return max(0, dmg - (r + 5))
        return dmg

    def on_missed(self, fight, att, melee):
        if melee and self.short and self.alive() and not self.incapacitated():      # Riposte, with the short sword
            self.short = False
            fight.after_turn(lambda: att.alive() and self.alive() and self.cut(fight, att, long=False, riposte=True))

    def answer_standoff(self, fight, jin):
        self.cut(fight, jin, long=True, adv=True)

    # ---------- his own ----------
    def attack_advantage(self, target): return target.name in self.studied

    def on_miss(self, fight, tgt, total, ac, melee):
        self.studied.add(tgt.name); self.short_by = ac - total

    def cut(self, fight, tgt, long=True, adv=False, riposte=False, trip=False, pillow=False):
        """One sword attack. Returns True on a hit."""
        one = long and self.one_cut and not riposte and self.dice >= 4
        state = {}
        def dmg(crit):
            c = crit or one
            v = roll(2 if c else 1, 8 if long else 6) + 7
            if one:
                self.one_cut = False; n = self.dice - 1; self.dice = 1; v += roll(2 * n, 12); state["one"] = True
                fight.note(f"Musashi: One Cut on {tgt.name}")
            if riposte: v += self.die(spend=self.dice > 2) * (2 if c else 1)
            if trip and not tgt.prone and not tgt.susanoo and not tgt.trip_done:
                r = self.die(spend=False)
                if r: v += r * (2 if c else 1); state["trip"] = True
            return v
        def extra(crit, dealt, t=tgt):
            if dealt and long and not t.out: t.sapped = True
            if state.get("trip") and not t.out:
                t.trip_done = True
                if not t.save("Str", DC): t.prone = True
        self.short_by = 99
        hit, crit, dealt = attack(fight, self, tgt, 13, dmg, "slashing", True, adv=adv, extra=extra, ignore_res=one)
        if hit and (crit or state.get("one")): self.slashed.add(id(tgt))
        if hit: self.studied.discard(tgt.name); return True
        # Peerless Aim turns one miss a turn into a hit; after that, Precision Attack when a d12 could
        saved = False
        if not tgt.out and fight.actor is self:
            if self.prowess: self.prowess = False; saved = True
            elif self.dice > 1 and self.short_by <= 12:
                self.dice -= 1; saved = d(12) >= self.short_by
        if saved:
            v = tgt.reduce_hit(roll(1, 8 if long else 6) + 7, True)
            dealt = tgt.take(v, "slashing", self.name, from_attack=True, melee=True)
            if dealt and long and not tgt.out: tgt.sapped = True
            self.studied.discard(tgt.name); return True
        return False

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        self.prowess = True
        bonus = True
        if self.hp <= 120 and self.sw > 0: self.sw -= 1; self.hp = min(self.maxhp, self.hp + d(10) + 20); bonus = False
        n = 4
        if self.surges > 0: self.surges -= 1; n += 4
        n += 1 + (1 if bonus else 0)          # the Nick cut with the short sword, then Dual Wielder's
        first = True; tripped = False
        for i in range(n):
            if tgt.out: tgt = fight.pick_target(self)
            if not tgt: break
            long = i % 3 != 1                 # the long sword leads; the short one takes every third cut
            adv = (first and self.rhythm()) or (fight.round == 1 and not tgt.acted)
            hit = self.cut(fight, tgt, long=long, adv=adv, trip=not tripped and tgt.melee)
            first = False
            if hit and tgt.trip_done: tripped = True
            if fight.over(): return
