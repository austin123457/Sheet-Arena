"""Adam Smasher, Caleb's sheet: Fighter (Battle Master) 20 in the Dragoon frame. Sheet: Adam_Smasher_5e_Build.pdf.
224 HP, AC 20, a smart gun at +15 for 2d8+7 that ignores resistance (not immunity), Studied Attacks,
Precision and Trip from a die pool, missiles, Mage Slayer, and an ICE that burns anyone who casts at him.
Experimental Sandevistan: 3 rounds of +2 AC, advantage on Dex saves and an extra shot a turn; switched on
as a Reaction when an enemy speeds up first (Counter-Sandevistan); no Reactions on the turn it runs out.
Weakness: 20+ lightning from one source shorts him out: no Reactions and no Sandevistan until the end of
his next turn."""
from ..engine import Combatant, MENTAL, attack, d, roll


class Smasher(Combatant):
    name = "Smasher"; danger = 6
    evil = True
    poison_immune = True; charm_immune = True; fright_immune = True; shrugs_stunning_strike = True

    def __init__(self):
        super().__init__()
        self.hp = self.maxhp = 224; self.ac = 20
        self.saves = dict(Str=14, Dex=5, Con=11, Int=0, Wis=0, Cha=1); self.indomitable = 3; self.indom_bonus = 20
        self.mage_slayer = True; self.matrix = True; self.sandy = 0; self.sandy_used = False; self.surges = 2; self.sw = 4
        self.dice = 6; self.studied = set(); self.missiles_ready = True; self.shorted = False; self.turns = 0

    def init(self): return d(20) + 11
    def overclocked(self): return self.sandy > 0 and not self.shorted
    def ac_now(self): return self.ac + (2 if self.overclocked() else 0)
    def save_adv(self, ab, spell): return spell or ab == "Con" or (ab == "Dex" and self.overclocked())

    def shrug_off_save(self, ab, spell):
        if spell and ab in MENTAL and self.mage_slayer:
            self.mage_slayer = False; return True
        return False

    def on_targeted_by_spell(self, fight, caster):
        # the ICE: a caster who reaches into his head takes 4d10 psychic, Int save for half
        if self.reaction and self.alive():
            self.reaction = False
            if not caster.save("Int", 19): caster.take(roll(4, 10), "psychic", "ICE")
            else: caster.take(roll(4, 10) // 2, "psychic", "ICE")

    def modify_incoming(self, dmg, dtype, src, from_attack, melee, ignore_res):
        if from_attack and dtype in ("slashing", "piercing", "bludgeoning"): dmg = max(0, dmg - 6)
        if dtype in ("acid", "radiant", "necrotic"): dmg //= 2
        if dtype == "poison": dmg = 0
        return dmg

    def after_damage(self, dmg, dtype, src, melee):
        if self.matrix and 0 < self.hp <= 40: self.matrix = False; self.thp += 40
        if dtype == "lightning" and dmg >= 20:
            self.shorted = self.turns + 1; self.reaction = False       # shorted out until the end of his next turn

    def on_enemy_speeds_up(self, fight, who):
        if self.reaction and not self.sandy_used and not self.shorted and self.alive() and not self.incapacitated():
            self.reaction = False; self.sandy_used = True; self.sandy = 3

    def start_turn(self):
        super().start_turn()
        if self.shorted: self.reaction = False

    def end_turn(self, fight):
        super().end_turn(fight)
        self.turns += 1
        if self.shorted and self.turns >= self.shorted: self.shorted = False

    def answer_standoff(self, fight, jin):
        attack(fight, self, jin, 15, lambda c: roll(4 if c else 2, 8) + 7, "piercing", False, ignore_res=True)

    def attack_advantage(self, target): return target.name in self.studied
    def natural_bonus(self, nat): return 20 if nat == 20 else 0

    def turn(self, fight):
        if self.sandy > 0:
            self.sandy -= 1
            if self.sandy == 0: self.reaction = False       # heat sink
        if not self.missiles_ready and d(6) >= 5: self.missiles_ready = True
        tgt = fight.pick_target(self)
        if not tgt: return
        if not self.sandy_used and not self.shorted: self.sandy_used = True; self.sandy = 3
        elif self.hp <= 150 and self.sw > 0: self.sw -= 1; self.hp = min(self.maxhp, self.hp + d(10) + 20)
        enemies = fight.enemies(self)
        actions = 1 + (1 if self.surges > 0 else 0)
        if self.surges > 0: self.surges -= 1
        extra_shot = 1 if self.overclocked() else 0
        for a in range(actions):
            if self.missiles_ready and len(enemies) >= 2:
                self.missiles_ready = False
                for e in enemies[:4]:
                    if e.out: continue
                    f = roll(4, 6); b = roll(4, 6)
                    saved = e.save("Dex", 19)
                    f = e.dex_damage(saved, f); b = e.dex_damage(saved, b)
                    if f: e.take(f, "fire", "Missiles")
                    if b: e.take(b, "bludgeoning", "Missiles", ignore_res=True)
                continue
            first = False
            for i in range(4):
                if tgt.out: tgt = fight.pick_target(self)
                if not tgt: return
                def dmg(crit, sav=not first):
                    w = roll(4 if crit else 2, 8)
                    if sav: w = max(w, roll(4 if crit else 2, 8))
                    return w + 7
                hit, crit, dealt = attack(fight, self, tgt, 15, dmg, "piercing", melee=False, ignore_res=True)
                if hit: first = True
                if fight.over(): return
        for i in range(extra_shot):
            if tgt and not tgt.out:
                attack(fight, self, tgt, 15, lambda crit: roll(4 if crit else 2, 8) + 7, "piercing", melee=False, ignore_res=True)

    def on_miss(self, fight, tgt, total, ac, melee):
        self.studied.add(tgt.name)
        # Precision Attack: add d12 if it turns the miss into a hit
        if self.dice > 0 and total + 12 >= ac:
            self.dice -= 1
            if total + d(12) >= ac:
                dmg = roll(2, 8) + 7
                dmg = tgt.reduce_hit(dmg, False)
                tgt.take(dmg, "piercing", self.name, from_attack=True, melee=False, ignore_res=True)

    def on_hit(self, fight, tgt, crit, dealt, melee):
        self.studied.discard(tgt.name)
        # trip the melee brute once per turn with a die
        if self.dice > 0 and tgt.melee and not tgt.prone and not tgt.trip_done and dealt:
            self.dice -= 1; tgt.trip_done = True
            if not tgt.save("Str", 22): tgt.prone = True
