"""Handsome Jack, President of Hyperion, on the day he opened the Vault of the Warrior: Artificer (Artillerist) 20.
Sheet: Handsome_Jack_5e_Build.pdf. 143 HP, AC 17 (no armor: Bracers of Defense, a Ring and a Cloak of Protection,
and Half Cover from standing beside his own cannon), initiative +7 (Alert), spell attacks +13 through the wrist
laser (a Wand of the War Mage +2, carved as his Arcane Firearm), save DC 19.

What he does with a turn:
  the wrist laser: Fire Bolt, 4d10 + 1d8 fire (Ray of Frost against anything fire can't touch); with a 4th or 5th
    level slot, Scorching Ray instead (five or six rays of 2d6), or a Fireball into a crowd.
  the cloak: his Spell-Storing Item holds Invisibility, ten uses. An action; attacks against him have disadvantage
    until he fires (his next shot has advantage). Concentration: a Mind Sharpener holds it four times.
  two Eldritch Cannons on one bonus action (Fortified Position): Force Ballistas at +11 for 3d8 force, a
    Flamethrower (3d8 fire, Dex save for half) on anything standing close, and one turns Protector whenever his
    shield is down: 2d8 + 5 temporary hit points. The cannons firing don't open the cloak. Nobody in the arena
    spends a turn on a cannon (AC 18, 100 HP each), so they aren't modeled as targets.
  Expendable Assets (homebrew): two Digi-Jacks when initiative is rolled, for a minute. When an attack hits him, a
    d6 for each: on a 4+ it hit that one instead, and it pops. One comes back at the start of each of his turns.
    At the end of his turn each fires once: +11, 1d10 fire.

What keeps him alive: Shield on his low slots (a reaction, +5 AC until his next turn), Flash of Genius (five times,
+5 on a save he just failed), Lucky (six points: disadvantage on an attack against him, advantage on a save),
Boon of Fate (once, 2d4 off a roll that just hit him), and Soul of Artifice: each time he drops to 0 he
disintegrates one of the six things he built and stands at 20 instead. The bag first, the laser last.

Not here: Loaders, moonshots, Helios, the Warrior, a body double. Hyperion's are not his own two hands."""
from ..engine import Combatant, attack, d, roll

DC = 19

# who he opens cloaked against even when he's first to move, from arena testing (1,500 fights a policy, Nov 2026)
CLOAKS = {"Arthur", "Musashi", "Dark Link"}

# what he gives up to Cheat Death, cheapest first
ITEMS = ["Bag of Holding", "Mind Sharpener", "Cloak of Protection", "Ring of Protection", "Bracers of Defense", "wrist laser"]


class Jack(Combatant):
    name = "Jack"; danger = 3; caster = True; evil = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 143; self.ac = 17
        # Con and Int proficient; +2 from the ring and the cloak, and Half Cover's +2 on Dex
        self.saves = dict(Str=2, Dex=5, Con=10, Int=13, Wis=1, Cha=6)
        self.slots = {1: 3, 2: 3, 3: 3, 4: 3, 5: 2}       # one 1st-level slot already went into the second cannon
        self.items = list(ITEMS); self.stored = 10; self.sharp = 4; self.flash = 5; self.luck = 6; self.fate = True
        self.decoys = 0; self.assets = 0; self.shield_up = False
        self.thp = roll(2, 8) + 5                           # he walks in with the Protector's shield up

    def init(self): return d(20) + 7
    def ac_now(self): return self.ac + (5 if self.shield_up else 0)
    def atk(self): return 13 if "wrist laser" in self.items else 11
    def firearm(self, crit=False): return roll(2 if crit else 1, 8) if "wrist laser" in self.items else 0

    def before_first_round(self, fight):
        self.decoys = 2; self.assets = 10                   # Expendable Assets: on rolling initiative, for a minute

    # ---------- staying alive ----------
    def incoming_attack(self, attacker, bonus, adv, dis, melee=True):
        if self.luck > 0 and not dis and not self.invisible and (adv or self.hp <= self.maxhp // 2):
            self.luck -= 1; dis = True                      # Lucky
        return adv, dis

    def defend_ac(self, attacker, total, melee, crit):
        if not crit and total < self.ac_now(): return 0
        for i in range(self.decoys):                        # which Jack?
            if d(6) >= 4:
                self.decoys -= 1
                if self.fight: self.fight.note(f"{attacker.name} hits a Digi-Jack")
                return None
        if crit: return 0
        margin = total - self.ac_now()
        if not self.shield_up and self.reaction and margin < 5 and not self.incapacitated():
            lvl = next((l for l in (1, 2, 3) if self.slots[l]), None)
            if lvl: self.slots[lvl] -= 1; self.reaction = False; self.shield_up = True; return 0       # Shield
        if self.fate and margin < 4:
            self.fate = False; return roll(2, 4)            # Boon of Fate
        return 0

    def save(self, ab, dc, spell=False, kind=None, adv=False):
        need = dc - self.saves[ab]                          # what the d20 has to show
        if not adv and self.luck > 0 and need > 4: self.luck -= 1; adv = True          # Lucky
        ok = super().save(ab, dc, spell, kind, adv)
        if not ok and self.flash > 0 and self.reaction and not self.incapacitated() and 1 < need <= 25:
            # Flash of Genius: +5 after the roll. The roll was a failure, so somewhere in 1..need-1 (capped at 20)
            top = min(need - 1, 20); short = max(0, top - 5) if need <= 21 else top
            p = 1 - (short / top) ** (2 if adv else 1) if need <= 21 else max(0, 26 - need) / 20
            if d(1000) <= 1000 * p: self.flash -= 1; self.reaction = False; ok = True
        return ok

    def after_damage(self, dmg, dtype, src, melee):
        if self.invisible and self.hp > 0:                  # concentration on the cloak
            if d(20) + self.saves["Con"] < max(10, dmg // 2):
                if self.sharp > 0 and self.reaction and "Mind Sharpener" in self.items: self.sharp -= 1; self.reaction = False
                else: self.invisible = False

    def on_zero(self, src, crit):
        if not self.items: self.out = True; return
        gone = self.items.pop(0); self.hp = 20              # Soul of Artifice: Cheat Death
        if gone in ("Cloak of Protection", "Ring of Protection"):
            self.ac -= 1
            for k in self.saves: self.saves[k] -= 1
        elif gone == "Bracers of Defense": self.ac -= 2
        if self.fight: self.fight.note(f"Jack disintegrates his {gone} and stands at 20")

    # ---------- the turn ----------
    def start_turn(self):
        super().start_turn()
        self.shield_up = False
        if self.assets > 0 and self.decoys < 2: self.decoys += 1

    def bolt(self, fight, tgt, dice, sides, dtype, first):
        """One spell attack through the wrist laser; the Arcane Firearm's d8 rides on the first that hits."""
        def dmg(crit):
            v = roll(dice * (2 if crit else 1), sides)
            if first[0]: v += self.firearm(crit); first[0] = False
            return v
        hit, crit, dealt = attack(fight, self, tgt, self.atk(), dmg, dtype, melee=False)
        self.invisible = False                              # firing opens the cloak
        return hit

    def spell(self, fight, tgt, level):
        if not fight.cast(self, level): return False
        self.slots[level] -= 1; self.invisible = False
        return tgt.alive() and not tgt.negates_spells()

    def cannons(self, fight, tgt):
        """One bonus action for both. They aren't him: the cloak stays shut and gives them nothing."""
        cloak, self.invisible = self.invisible, False
        n = 2
        if self.thp < 7: self.thp = max(self.thp, roll(2, 8) + 5); n = 1          # Protector
        for i in range(n):
            if not tgt or not tgt.alive(): tgt = fight.pick_target(self)
            if not tgt: break
            p_hit = min(0.95, max(0.05, (32 - tgt.ac_now()) / 20))
            p_save = min(1.0, max(0.0, (21 - (DC - tgt.saves["Dex"])) / 20))
            if tgt.melee and not tgt.evasion and not tgt.immune("fire") and 1 - p_save / 2 > p_hit:
                saved = tgt.save("Dex", DC, spell=True)                           # Flamethrower
                tgt.take(tgt.dex_damage(saved, roll(3, 8)), "fire", "Eldritch Cannon")
            else:
                attack(fight, self, tgt, 11, lambda c: roll(6 if c else 3, 8), "force", melee=False)
            if fight.over(): break
        self.invisible = cloak and self.alive()

    def turn(self, fight):
        tgt = fight.pick_target(self)
        if not tgt: return
        es = fight.enemies(self)
        fire = not tgt.immune("fire")
        high = next((l for l in (5, 4) if self.slots[l]), None)
        if not self.invisible and self.stored > 0 and self.wants_cloak(fight, tgt):
            self.stored -= 1; self.invisible = True         # the Spell-Storing Item: Invisibility
        elif high and len(es) >= 2:
            if self.spell(fight, tgt, high):                # Fireball into the crowd
                first = [True]
                for e in es:
                    if not e.alive() or e.negates_spells(): continue
                    dmg = roll(8 + high - 3, 6) + (self.firearm() if first[0] else 0); first[0] = False
                    e.take(e.dex_damage(e.save("Dex", DC, spell=True), dmg), "fire", "Fireball")
        elif high and fire:
            if self.spell(fight, tgt, high):                # Scorching Ray, upcast
                first = [True]
                for i in range(high + 1):
                    if not tgt.alive(): tgt = fight.pick_target(self)
                    if not tgt: break
                    self.bolt(fight, tgt, 2, 6, "fire", first)
        elif fire: self.bolt(fight, tgt, 4, 10, "fire", [True])           # Fire Bolt
        else: self.bolt(fight, tgt, 4, 8, "cold", [True])                 # Ray of Frost
        if fight.over() or not self.alive(): return
        self.cannons(fight, tgt if tgt and tgt.alive() else None)
        if fight.over() or not self.alive(): return
        for i in range(self.decoys):                        # the Digi-Jacks fire
            tgt = fight.pick_target(self)
            if not tgt: break
            cloak, self.invisible = self.invisible, False
            attack(fight, self, tgt, 11, lambda c: roll(2 if c else 1, 10), "fire", melee=False)
            self.invisible = cloak
            if fight.over(): break

    def wants_cloak(self, fight, tgt):
        """The cloak costs him a turn of the laser, so he uses it once: at the top, when the other one got the drop
        on him or is somebody the arena says it pays against."""
        return fight.round == 1 and (tgt.acted or tgt.name in CLOAKS)

    def end_turn(self, fight):
        super().end_turn(fight)
        if self.assets > 0:
            self.assets -= 1
            if self.assets == 0: self.decoys = 0
