import secrets, itertools, sys
from collections import Counter

def d(n): return secrets.randbelow(n) + 1
def roll(n, s, gwf=False, minv=None):
    r = [d(s) for _ in range(n)]
    if gwf: r = [3 if x <= 2 else x for x in r]
    if minv: r = [max(x, minv) for x in r]
    return sum(r)
def d20(adv=False, dis=False):
    a, b = d(20), d(20)
    if adv and dis: adv = dis = False
    return max(a, b) if adv else (min(a, b) if dis else a)

DANGER = {"Smasher": 6, "Guts": 5, "Jin": 4, "Itachi": 3, "Crane": 2, "GS": 1}

class C:
    def __init__(s, name):
        s.name = name; s.out = False; s.team = None
        s.thp = 0; s.prone = False; s.paralyzed = False; s.poisoned = False; s.frightened = False
        s.reckless = False; s.reaction = True; s.disadv_attacks = False; s.hits_on = Counter()
        s.melee = False; s.burning = False; s.hold_dc = 0; s.indomitable = 0
        s.last_hit_by_melee = None; s.surge_used = False; s.down = False; s.death_fail = 0
    def alive(s): return not s.out
    def can_act(s): return s.alive() and not s.paralyzed
    # ---------- saves ----------
    def save(s, ab, dc, spell=False, source=None):
        adv = s.save_adv(ab, spell)
        if s.paralyzed and ab in ("Str", "Dex"): return False
        nat = d20(adv=adv); tot = nat + s.saves[ab]
        ok = tot >= dc
        if not ok and s.name == "Smasher" and spell and ab in ("Int", "Wis", "Cha") and s.mage_slayer:
            s.mage_slayer = False; return True
        if not ok and s.indomitable > 0:
            s.indomitable -= 1
            nat = d20(adv=adv); tot = nat + s.saves[ab] + s.indom_bonus
            ok = tot >= dc
        return ok
    def save_adv(s, ab, spell): return False
    # ---------- damage ----------
    def take(s, dmg, dtype, src, from_attack=False, melee=False, crit=False, ignore_res=False):
        if s.out: return 0
        dmg = s.modify_incoming(dmg, dtype, src, from_attack, melee, ignore_res)
        if dmg <= 0: return 0
        a = min(s.thp, dmg); s.thp -= a; rest = dmg - a
        s.hp -= rest
        s.after_damage(dmg, dtype, src, melee)
        if s.hp <= 0: s.hp = 0; s.on_zero(src, crit)
        return dmg
    def modify_incoming(s, dmg, dtype, src, from_attack, melee, ignore_res): return dmg
    def after_damage(s, dmg, dtype, src, melee): pass
    def on_zero(s, src, crit): s.out = True
    # ---------- reactions to an incoming attack: return ac bonus, or None to negate ----------
    def defend_ac(s, attacker, total, melee, crit): return 0
    def reduce_hit(s, dmg, melee): return dmg
    def start_turn(s):
        s.reaction = True; s.disadv_attacks = False; s.sa_used = False
        if s.name == "Guy":
            for e in getattr(s, "_fight_all", []):
                if getattr(e, "stunned_by_guy", False): e.paralyzed = False; e.stunned_by_guy = False
        if s.prone: s.prone = False
        if s.burning: s.take(roll(4, 10), "fire", "Amaterasu", ignore_res=True)
    def end_turn(s, fight):
        if s.paralyzed and not getattr(s, "stunned_by_guy", False):
            if s.save("Wis", 19, spell=True): s.paralyzed = False

def attack(fight, att, tgt, bonus, dmg_fn, dtype, melee=True, adv=False, dis=False, crit_range=20, label="", sneak=0, extra=None, ignore_res=False):
    """returns (hit, crit, dmg_dealt)"""
    if tgt.out: return (False, False, 0)
    if tgt.reckless or tgt.prone or tgt.paralyzed or getattr(tgt, "asleep", False): adv = True
    if att.poisoned or att.disadv_attacks or att.prone or (att.frightened and melee is not None): dis = True
    if att.name == "Smasher" and tgt.name in att.studied: adv = True
    nat = d20(adv=adv, dis=dis)
    total = nat + bonus
    crit = nat >= crit_range
    acb = tgt.defend_ac(att, total, melee, crit)
    if acb is None: return (False, False, 0)  # negated
    ac = tgt.ac_now() + acb
    hit = crit or (nat != 1 and total >= ac)
    if not hit:
        if att.name == "Smasher": att.studied.add(tgt.name)
        att.on_miss(fight, tgt, total, ac, melee)
        return (False, False, 0)
    if att.name == "Smasher": att.studied.discard(tgt.name)
    dmg = dmg_fn(crit)
    if sneak and not getattr(att, "sa_used", False) and ((adv and not dis) or any(a.alive() and a is not att and a.melee for a in fight.allies(att))):
        dmg += roll(sneak * (2 if crit else 1), 6); att.sa_used = True
    if nat == 20 and att.name == "Smasher": dmg += 20
    dmg = tgt.reduce_hit(dmg, melee)
    dealt = tgt.take(dmg, dtype, att.name, from_attack=True, melee=melee, crit=crit, ignore_res=ignore_res)
    tgt.hits_on[att.name] += 0
    if melee or att.name in getattr(tgt, "adjacent", set()): tgt.last_hit_by_melee = att
    if melee: att.adjacent = getattr(att, "adjacent", set()) | {tgt.name}; tgt.adjacent = getattr(tgt, "adjacent", set()) | {att.name}
    if extra: extra(crit, dealt)
    att.on_hit(fight, tgt, crit, dealt, melee)
    return (True, crit, dealt)

# ---------------------------------------------------------------- GOBLIN SLAYER
class GS(C):
    def __init__(s):
        super().__init__("GS"); s.hp = s.maxhp = 220; s.ac = 17
        s.saves = dict(Str=10, Dex=2, Con=9, Int=0, Wis=8, Cha=-1); s.indomitable = 2; s.indom_bonus = 0
        s.sw = 4; s.dice = 5; s.doses = 5; s.blade = True; s.hitdice = 10; s.melee = True; s.moved = True
    def init(s): return d(20) + 8 + d(10)
    def ac_now(s): return s.ac
    def defend_ac(s, att, total, melee, crit): return 0
    def reduce_hit(s, dmg, melee):
        if melee and s.reaction and s.dice > 0:
            s.reaction = False; s.dice -= 1; return max(0, dmg - (d(10) + 4))
        return dmg
    def turn(s, fight):
        tgt = fight.pick_target(s)
        if not tgt: return
        bonus = None
        if s.hp <= 160 and s.sw > 0: s.sw -= 1; s.hp = min(s.maxhp, s.hp + d(10) + 16); bonus = "sw"
        elif not s.blade and s.doses > 0 and not getattr(tgt, "poison_immune", False): s.doses -= 1; s.blade = True; bonus = "poison"
        elif s.hp <= 200 and s.hitdice > 0 and s.hp <= 120: s.hitdice -= 1; s.hp = min(s.maxhp, s.hp + d(10) + 3); bonus = "hd"
        steady = (bonus is None and fight.round > 1)
        n = 3 + (3 if (fight.round == 1 and not s.surge_used) else 0); s.surge_used = True
        first_hit = False
        for i in range(n):
            if tgt.out: tgt = fight.pick_target(s)
            if not tgt: break
            adv = steady and i == 0
            def dmg(crit): return roll(2 if crit else 1, 6) + 6
            def extra(crit, dealt, t=tgt):
                nonlocal first_hit
                if dealt and s.blade and not getattr(t, "poison_immune", False):
                    s.blade = False
                    if not t.save("Con", 14): t.take(roll(2, 8), "poison", "GS"); t.poisoned = True
                if dealt and not first_hit and not getattr(t, "susanoo", False):
                    first_hit = True
                    if not t.save("Str", 18): t.prone = True
            attack(fight, s, tgt, 10, dmg, "piercing", True, adv=adv, label="stab", sneak=2, extra=extra)
            if fight.over(): return
    def on_miss(s, *a): pass
    def on_hit(s, *a): pass

# ---------------------------------------------------------------- GUTS
class Guts(C):
    def __init__(s):
        super().__init__("Guts"); s.hp = s.maxhp = 236; s.ac = 18
        s.saves = dict(Str=11, Dex=2, Con=9, Int=-1, Wis=7, Cha=-1); s.indom_bonus = 0
        s.raging = False; s.sw = 3; s.rel_dc = 10; s.hew = False; s.melee = True
        s.charm_immune = True; s.fright_immune = True
    def init(s): return d20(adv=True) + 2
    def ac_now(s): return s.ac
    def save_adv(s, ab, spell): return (ab == "Str" and s.raging) or ab == "Dex"
    def modify_incoming(s, dmg, dtype, src, from_attack, melee, ignore_res):
        if s.raging and dtype != "psychic" and not ignore_res: return dmg // 2
        return dmg
    def after_damage(s, dmg, dtype, src, melee):
        pass
    def on_zero(s, src, crit):
        if s.down:
            s.death_fail += 2 if crit else 1
            if s.death_fail >= 3: s.out = True
            return
        if s.raging:
            if d(20) + 9 >= s.rel_dc: s.rel_dc += 5; s.hp = 24; return
            s.rel_dc += 5; s.down = True; s.hp = 0; return
        s.out = True
    def retaliate(s, fight, att):
        if s.reaction and att.alive() and s.raging:
            s.reaction = False; s.swing(fight, att, adv=True, frenzy=False, savage=True, can_hew=False)
    def swing(s, fight, tgt, adv, frenzy, savage, brutal=False, can_hew=True):
        def dmg(crit):
            n = 8 if crit else 4
            w = roll(n, 6, gwf=True)
            if savage: w = max(w, roll(n, 6, gwf=True))
            v = w + (16 if s.raging else 13)
            if frenzy: v += roll(6 if crit else 3, 6)
            if brutal: v += roll(2 if crit else 1, 10)
            return v
        hit, crit, dealt = attack(fight, s, tgt, 13, dmg, "slashing", True, adv=adv, crit_range=19)
        if crit:
            tgt.disadv_attacks = True
            if can_hew: s.hew = True
        if hit and s.team is not None:
            others = [e for e in fight.enemies(s) if e is not tgt and e.melee]
            if others: others[0].take(roll(4, 6, gwf=True), "slashing", "Guts cleave", from_attack=True, melee=True)
        return hit
    def turn(s, fight):
        if s.down:
            r = d20(adv=True)
            if r == 20: s.hp = 1; s.down = False; s.death_fail = 0
            elif r < 10:
                s.death_fail += 1
                if s.death_fail >= 3: s.out = True; return
        tgt = fight.pick_target(s)
        if not tgt: return
        bonus = False
        if not s.raging: s.raging = True; s.reckless = True; bonus = True
        n = 2 + (2 if not s.surge_used else 0); s.surge_used = True
        first = False
        for i in range(n):
            if tgt.out: tgt = fight.pick_target(s)
            if not tgt: break
            brutal = (i == 1) and not s.poisoned and not s.disadv_attacks
            hit = s.swing(fight, tgt, adv=not brutal, frenzy=not first, savage=not first, brutal=brutal)
            if hit: first = True
            if fight.over(): return
        if not bonus and s.hew and tgt and not tgt.out: s.hew = False; s.swing(fight, tgt, True, False, False, can_hew=False)
        elif not bonus and s.hp <= 118 and s.sw > 0 and not s.down: s.sw -= 1; s.hp = min(s.maxhp, s.hp + d(10) + 8)
        s.hew = False
    def on_miss(s, *a): pass
    def on_hit(s, *a): pass

# ---------------------------------------------------------------- CRANE
class Crane(C):
    def __init__(s):
        super().__init__("Crane"); s.hp = s.maxhp = 227; s.ac = 16
        s.saves = dict(Str=11, Dex=3, Con=9, Int=-1, Wis=0, Cha=-1); s.indom_bonus = 0
        s.raging = False; s.fury = 6; s.rel_dc = 10; s.greater = 2; s.potions = 4; s.sw = 2; s.surge = True; s.melee = True
    def init(s): return d20(adv=True) + 3
    def ac_now(s): return s.ac
    def save_adv(s, ab, spell): return ab == "Dex" or (ab == "Str" and s.raging)
    def modify_incoming(s, dmg, dtype, src, from_attack, melee, ignore_res):
        if s.raging and dtype in ("slashing", "piercing", "bludgeoning") and not ignore_res: dmg //= 2
        if from_attack and s.reaction and not s.paralyzed:
            s.reaction = False; dmg //= 2
        return dmg
    def after_damage(s, dmg, dtype, src, melee):
        if s.raging and s.surge and 0 < s.hp < 113: s.surge = False; s.hp = min(s.maxhp, s.hp + 44)
    def on_zero(s, src, crit):
        if s.raging and d(20) + 9 >= s.rel_dc: s.rel_dc += 5; s.hp = 22; return
        s.out = True
    def turn(s, fight):
        tgt = fight.pick_target(s)
        if not tgt: return
        bonus = False
        if not s.raging: s.raging = True; s.reckless = True; bonus = True
        if not bonus:
            if s.hp <= 150 and s.greater: s.greater -= 1; s.hp = min(s.maxhp, s.hp + roll(4, 4) + 4)
            elif s.hp <= 150 and s.potions: s.potions -= 1; s.hp = min(s.maxhp, s.hp + roll(2, 4) + 2)
            elif s.hp <= 150 and s.sw: s.sw -= 1; s.hp = min(s.maxhp, s.hp + d(10) + 1)
        first = False
        for i in range(3):
            if tgt.out: tgt = fight.pick_target(s)
            if not tgt: break
            brutal = (i == 2) and not s.disadv_attacks and not s.poisoned
            def dmg(crit, sav=not first, br=brutal):
                w = roll(2 if crit else 1, 6)
                if sav: w = max(w, roll(2 if crit else 1, 6))
                return w + 8 + (roll(2 if crit else 1, 10) if br else 0)
            def extra(crit, dealt, t=tgt):
                if dealt:
                    s.hp = min(s.maxhp, s.hp + 6)
                    if s.fury > 0 and not t.out:
                        s.fury -= 1
                        if not t.save("Wis", 17, spell=True): t.take(roll(4 if crit else 2, 12), "psychic", "Fury")
            hit, crit, dealt = attack(fight, s, tgt, 11, dmg, "slashing", True, adv=not brutal, extra=extra)
            if hit: first = True
            if fight.over(): return
    def on_miss(s, *a): pass
    def on_hit(s, *a): pass

# ---------------------------------------------------------------- ITACHI
class Itachi(C):
    def __init__(s):
        super().__init__("Itachi"); s.hp = s.maxhp = 85; s.ac = 19
        s.saves = dict(Str=-1, Dex=4, Con=0, Int=11, Wis=7, Cha=0); s.indom_bonus = 0
        s.shield = 4; s.shield_up = False; s.illusory = True; s.susanoo = False; s.susanoo_cast = False; s.yata = 0
        s.tsukuyomi = True; s.amaterasu = True; s.izanami = True; s.hold = 2; s.dominate = 2; s.fireball = 3
        s.mirror = 0; s.mirror_cast = False; s.sus_turns = 0
    def init(s): return d20(adv=True) + 10
    def ac_now(s):
        ac = s.ac
        if s.susanoo: ac = max(ac, 21)
        if s.shield_up: ac += 5
        return ac
    def save_adv(s, ab, spell): return False
    def defend_ac(s, att, total, melee, crit):
        if s.mirror > 0:
            need = {3: 6, 2: 8, 1: 11}[s.mirror]
            if d(20) >= need: s.mirror -= 1; return None
        would_hit = crit or total >= s.ac_now()
        if would_hit and s.reaction:
            if s.susanoo and s.yata > 0: s.yata -= 1; s.reaction = False; return None
            if s.shield > 0 and not s.shield_up: s.shield -= 1; s.reaction = False; s.shield_up = True; return 0
            if s.illusory: s.illusory = False; s.reaction = False; return None
        return 0
    def modify_incoming(s, dmg, dtype, src, from_attack, melee, ignore_res):
        return dmg // 2 if s.susanoo else dmg
    def after_damage(s, dmg, dtype, src, melee):
        if s.susanoo:
            dc = max(10, dmg // 2)
            if d20(adv=True) < dc: s.susanoo = False; s.thp = 0; s.yata = 0
    def start_turn(s):
        super().start_turn(); s.shield_up = False
    def cast_on(s, fight, tgt):
        if tgt.name == "Smasher" and tgt.reaction and tgt.alive():
            tgt.reaction = False
            if not s.save("Int", 19): s.take(roll(4, 10), "psychic", "ICE")
            else: s.take(roll(4, 10) // 2, "psychic", "ICE")
    def turn(s, fight):
        if s.susanoo:
            s.sus_turns += 1
            if s.sus_turns > 1:
                s.hp -= 5
                if s.hp <= 0: s.hp = 0; s.out = True; return
        enemies = [e for e in fight.enemies(s)]
        if not enemies: return
        ready = [e for e in enemies if s.hits_on[e.name] >= 2]
        tgt = None; act = None
        if ready and s.izanami:
            tgt = max(ready, key=lambda e: DANGER[e.name]); act = "izanami"
        elif len(enemies) >= 2 and s.fireball > 0 and sum(1 for e in enemies if e.melee) >= 2:
            act = "fireball"
        elif not s.susanoo_cast and not (len(enemies) == 1 and enemies[0].name == "Crane"):
            act = "susanoo"
        else:
            cands = [e for e in enemies if not (e.name == "Smasher" and (e.mage_slayer or e.indomitable > 0)) and not (e.name == "Guy")]
            tgt = max(cands, key=lambda e: DANGER[e.name]) if cands else max(enemies, key=lambda e: DANGER[e.name])
            if s.tsukuyomi: act = "tsukuyomi"
            elif s.susanoo: act = "totsuka"
            elif s.hold > 0 and not getattr(tgt, "susanoo", False): act = "hold"
            elif s.amaterasu and not tgt.burning: act = "amaterasu"
            elif not s.mirror_cast: act = "mirror"
            else: act = "firebolt"
        if act == "izanami":
            s.izanami = False; s.cast_on(fight, tgt)
            if s.out: return
            tgt.out = True; fight.note(f"Izanami on {tgt.name}")
        elif act == "fireball":
            s.fireball -= 1
            for e in list(enemies):
                if e.melee or len(enemies) == 1:
                    s.cast_on(fight, e)
                    if s.out: return
                    dmg = roll(8, 6, minv=2)
                    if e.save("Dex", 19, spell=True):
                        if e.name in ("Jin", "Crane"): dmg = 0
                        else: dmg //= 2
                    e.take(dmg, "fire", "Fireball")
        elif act == "susanoo":
            s.susanoo = True; s.susanoo_cast = True; s.thp = 150; s.yata = 3; s.sus_turns = 1
        elif act == "tsukuyomi":
            s.tsukuyomi = False; s.cast_on(fight, tgt)
            if s.out: return
            if tgt.save("Wis", 19, spell=True): tgt.take(roll(5, 10), "psychic", "Tsukuyomi")
            else: tgt.take(roll(10, 10), "psychic", "Tsukuyomi"); tgt.out = True; fight.note(f"Tsukuyomi drops {tgt.name}")
        elif act == "totsuka":
            tgt = max(enemies, key=lambda e: DANGER[e.name])
            def dmg(crit): return roll(12 if crit else 6, 8)
            def extra(crit, dealt, t=tgt):
                if dealt and not t.out and not t.save("Wis", 19, spell=True): t.out = True; fight.note(f"Totsuka seals {t.name}")
            attack(fight, s, tgt, 11, dmg, "force", melee=False, extra=extra)
        elif act == "hold":
            s.hold -= 1; s.cast_on(fight, tgt)
            if s.out: return
            if not tgt.save("Wis", 19, spell=True): tgt.paralyzed = True
        elif act == "amaterasu":
            s.amaterasu = False; s.cast_on(fight, tgt)
            if s.out: return
            if not tgt.save("Dex", 19, spell=True): tgt.take(roll(6, 10), "fire", "Amaterasu", ignore_res=True); tgt.burning = True
        elif act == "mirror":
            s.mirror = 3; s.mirror_cast = True
        else:
            tgt = tgt or max(enemies, key=lambda e: DANGER[e.name])
            def dmg(crit): return roll(8 if crit else 4, 10, minv=2)
            attack(fight, s, tgt, 11, dmg, "fire", melee=False, adv=tgt.paralyzed)
    def end_turn(s, fight):
        super().end_turn(fight)
    def on_miss(s, *a): pass
    def on_hit(s, *a): pass

# ---------------------------------------------------------------- SMASHER
class Smasher(C):
    def __init__(s):
        super().__init__("Smasher"); s.hp = s.maxhp = 224; s.ac = 20
        s.saves = dict(Str=14, Dex=5, Con=11, Int=0, Wis=0, Cha=1); s.indomitable = 3; s.indom_bonus = 20
        s.mage_slayer = True; s.matrix = True; s.sandy = 0; s.sandy_used = False; s.surges = 2; s.sw = 4
        s.dice = 6; s.studied = set(); s.poison_immune = True; s.charm_immune = True; s.fright_immune = True
        s.missiles_ready = True; s.melee = False
    def init(s): return d(20) + 11
    def ac_now(s): return s.ac + (2 if s.sandy > 0 else 0)
    def save_adv(s, ab, spell): return spell or ab == "Con" or (ab == "Dex" and s.sandy > 0)
    def modify_incoming(s, dmg, dtype, src, from_attack, melee, ignore_res):
        if from_attack and dtype in ("slashing", "piercing", "bludgeoning"): dmg = max(0, dmg - 6)
        if dtype in ("acid", "radiant", "necrotic"): dmg //= 2
        if dtype == "poison": dmg = 0
        return dmg
    def after_damage(s, dmg, dtype, src, melee):
        if s.matrix and 0 < s.hp <= 40: s.matrix = False; s.thp += 40
    def on_zero(s, src, crit): s.out = True
    def turn(s, fight):
        if s.sandy > 0: s.sandy -= 1
        if not s.missiles_ready and d(6) >= 5: s.missiles_ready = True
        tgt = fight.pick_target(s)
        if not tgt: return
        bonus = False
        if not s.sandy_used: s.sandy_used = True; s.sandy = 3; bonus = True
        elif s.hp <= 150 and s.sw > 0: s.sw -= 1; s.hp = min(s.maxhp, s.hp + d(10) + 20); bonus = True
        enemies = fight.enemies(s)
        actions = 1 + (1 if s.surges > 0 else 0)
        if s.surges > 0: s.surges -= 1
        extra_shot = 1 if s.sandy > 0 else 0
        for a in range(actions):
            if s.missiles_ready and len(enemies) >= 2:
                s.missiles_ready = False
                for e in enemies[:4]:
                    if e.out: continue
                    f = roll(4, 6); b = roll(4, 6)
                    if e.save("Dex", 19):
                        if e.name in ("Jin", "Crane"): continue
                        f //= 2; b //= 2
                    e.take(f, "fire", "Missiles"); e.take(b, "bludgeoning", "Missiles", ignore_res=True)
                continue
            shots = 4
            first = False
            for i in range(shots):
                if tgt.out: tgt = fight.pick_target(s)
                if not tgt: return
                def dmg(crit, sav=not first):
                    w = roll(4 if crit else 2, 8)
                    if sav: w = max(w, roll(4 if crit else 2, 8))
                    return w + 7
                hit, crit, dealt = attack(fight, s, tgt, 15, dmg, "piercing", melee=False, ignore_res=True)
                if hit: first = True
                if fight.over(): return
        for i in range(extra_shot):
            if tgt and not tgt.out:
                attack(fight, s, tgt, 15, lambda crit: roll(4 if crit else 2, 8) + 7, "piercing", melee=False, ignore_res=True)
    def on_miss(s, fight, tgt, total, ac, melee):
        # Precision Attack: add d12 if it turns the miss into a hit
        if s.dice > 0 and total + 12 >= ac:
            s.dice -= 1
            if total + d(12) >= ac:
                dmg = roll(2, 8) + 7
                dmg = tgt.reduce_hit(dmg, False)
                tgt.take(dmg, "piercing", s.name, from_attack=True, melee=False, ignore_res=True)
    def on_hit(s, fight, tgt, crit, dealt, melee):
        # Trip the melee brute once per turn with a die
        if s.dice > 0 and tgt.melee and not tgt.prone and not getattr(tgt, "trip_done", False) and dealt:
            s.dice -= 1; tgt.trip_done = True
            if not tgt.save("Str", 22): tgt.prone = True

# ---------------------------------------------------------------- JIN
class Jin(C):
    def __init__(s):
        super().__init__("Jin"); s.hp = s.maxhp = 215; s.ac = 19
        s.saves = dict(Str=7, Dex=5, Con=9, Int=0, Wis=8, Cha=-1); s.indomitable = 1; s.indom_bonus = 0
        s.resolve = 8; s.fs = 3; s.sw = 4; s.last_stand = True; s.iron_n = 0; s.recover = 10; s.hitdice = 11
        s.doses = 6; s.blade = True; s.dd_up = False; s.melee = True; s.surge = True; s.standoff_done = False
        s.darts = 3
    def init(s): return d20(adv=True) + 11
    def ac_now(s): return s.ac + (6 if s.dd_up else 0)
    def defend_ac(s, att, total, melee, crit):
        if melee and s.reaction and not crit and total < s.ac + 6 and total >= s.ac:
            s.reaction = False; s.dd_up = True; s.resolve += 1; return 0
        return 0
    def reduce_hit(s, dmg, melee):
        if s.reaction:
            if melee: s.reaction = False; return dmg // 2
            red = d(10) + 16
            s.reaction = False
            return max(0, dmg - red) if red >= dmg // 2 else dmg // 2
        return dmg
    def start_turn(s):
        super().start_turn(); s.dd_up = False
    def on_zero(s, src, crit):
        if s.last_stand: s.last_stand = False; s.hp = 108; return
        if s.resolve >= 2:
            if s.iron_n == 0 or d(20) + 8 >= 10 + 5 * s.iron_n:
                s.resolve -= 2; s.iron_n += 1; s.hp = 22; return
        s.out = True
    def turn(s, fight):
        tgt = fight.pick_target(s)
        if not tgt: return
        adv_turn = False
        if s.hp <= 100 and s.sw > 0: s.sw -= 1; s.hp = min(s.maxhp, s.hp + d(10) + 11)
        elif s.hp <= 100 and s.resolve > 3: s.resolve -= 1; s.hp = min(s.maxhp, s.hp + roll(2, 8) + 2)
        elif s.hp <= 100 and s.recover > 0: k = min(3, s.recover); s.recover -= k; s.hp = min(s.maxhp, s.hp + roll(k, 10))
        elif s.fs > 0 and (fight.round <= 2 or DANGER[tgt.name] >= 4): s.fs -= 1; s.thp = max(s.thp, 10); adv_turn = True
        elif not s.blade and s.doses > 0 and not getattr(tgt, "poison_immune", False): s.doses -= 1; s.blade = True
        else: adv_turn = "steady"
        n = 3 + (3 if s.surge else 0); s.surge = False
        first = False
        for i in range(n):
            if tgt.out: tgt = fight.pick_target(s)
            if not tgt: break
            # sleep dart on a soft target once
            if i == 0 and s.darts > 0 and tgt.name in ("Itachi",) and not getattr(tgt, "poison_immune", False) and not getattr(tgt, "susanoo", False):
                s.darts -= 1
                if not tgt.save("Con", 19): tgt.asleep = True
                continue
            adv = adv_turn is True or (adv_turn == "steady" and i == 0) or (fight.round == 1 and not tgt.acted)
            heavenly = (not first) and s.resolve >= 3
            def dmg(crit, hv=heavenly, t=tgt):
                v = roll(2 if crit else 1, 10, gwf=True) + 7
                if hv: v += roll(6 if crit else 3, 10)
                if t.name in ("Smasher",) or getattr(t, "susanoo", False): v += roll(2 if crit else 1, 10)
                if fight.round == 1 and not t.acted: v += 9
                return v
            def extra(crit, dealt, t=tgt, hv=heavenly):
                if dealt and hv: s.resolve -= 1
                if dealt and s.blade and not getattr(t, "poison_immune", False):
                    s.blade = False
                    if not t.save("Con", 19): t.take(roll(2, 8), "poison", "Jin"); t.poisoned = True
                if dealt and getattr(t, "asleep", False): t.asleep = False
            hit, crit, dealt = attack(fight, s, tgt, 13, dmg, "slashing", True, adv=adv, sneak=5, extra=extra)
            if hit: first = True
            if tgt.out: s.resolve += 1
            if fight.over(): return
    def on_miss(s, *a): pass
    def on_hit(s, *a): pass


# ---------------------------------------------------------------- MIGHT GUY
class Guy(C):
    def __init__(s, max_gate=8):
        super().__init__("Guy"); s.hp = s.maxhp = 203; s.ac = 22
        s.saves = dict(Str=7, Dex=13, Con=9, Int=5, Wis=11, Cha=5); s.indom_bonus = 0
        s.focus = 20; s.gate = 0; s.max_gate = max_gate; s.wob = 5; s.melee = True; s.g8_turns = 0
        s.night_guy = True; s.eyes_immune = True; s.did_peacock = False; s.did_tiger = False; s.did_elephant = False
        s.stun_immune = False; s.deflects_left = 1
    def init(s): return d(20) + 7
    def ac_now(s): return 25 if s.gate >= 8 else 22
    def strmod(s): return {0: 1, 1: 4, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 9, 8: 10}[s.gate]
    def atk_mod(s): return max(7, s.strmod()) if s.gate < 8 else 10
    def save(s, ab, dc, spell=False, source=None):
        if s.gate >= 8 and ab in ("Str", "Dex", "Con"): bonus = 16
        else: bonus = s.saves[ab]
        adv = (ab in ("Str", "Dex") and s.gate >= 5)
        nat = d20(adv=adv); ok = nat + bonus >= dc
        if not ok and s.focus > 0:
            s.focus -= 1; nat = d20(adv=adv); ok = nat + bonus >= dc
        return ok
    def modify_incoming(s, dmg, dtype, src, from_attack, melee, ignore_res):
        if ignore_res: return dmg
        if s.gate >= 8: return dmg // 2
        if s.gate >= 7 and dtype != "force": return dmg // 2
        return dmg
    def reduce_hit(s, dmg, melee):
        if s.deflects_left > 0 and s.reaction:
            s.deflects_left -= 1
            if s.deflects_left == 0: s.reaction = False
            return max(0, dmg - (d(10) + 27))
        return dmg
    def start_turn(s):
        super().start_turn(); s.deflects_left = 2 if s.gate >= 7 else 1
    def open_to(s, g):
        g = min(g, s.max_gate)
        while s.gate < g:
            s.gate += 1
            if s.gate == 2: s.hp = min(s.maxhp, s.hp + 20); s.focus += 2
            if s.gate == 8: s.stun_immune = True; s.fright_immune = True
    def strike(s, fight, tgt, fire=False, extra=0, stun=False, topple=False, adv=False):
        def dmg(crit):
            v = roll(2 if crit else 1, 12) + s.atk_mod() + s.gate + extra
            if s.gate >= 6 or fire: v += roll(4 if crit else 2, 6) if fire else roll(1, 6)
            return v
        def ex(crit, dealt, t=tgt):
            if dealt and stun and s.focus > 0 and not getattr(t, "stun_immune", False) and not t.paralyzed:
                s.focus -= 1
                if not t.save("Con", 19): t.paralyzed = True; t.stunned_by_guy = True
            if dealt and topple and not t.prone and not getattr(t, "susanoo", False):
                if not t.save("Dex", 19): t.prone = True
        return attack(fight, s, tgt, 6 + s.atk_mod() + s.gate, dmg, "bludgeoning", True, adv=adv or s.gate >= 8, extra=ex)
    def turn(s, fight):
        tgt = fight.pick_target(s)
        if not tgt: return
        danger = DANGER.get(tgt.name, 3)
        # gate escalation
        if s.gate < 3: s.open_to(3)
        elif s.gate < 6 and (danger >= 3 or s.hp < 0.7 * s.maxhp): s.open_to(6)
        elif s.gate < 7 and (danger >= 4 or s.hp < 0.6 * s.maxhp): s.open_to(7)
        losing = (tgt.hp + tgt.thp) / tgt.maxhp > s.hp / s.maxhp + 0.2
        if s.max_gate >= 8 and s.gate < 8 and s.hp <= 80 and (losing or len(fight.enemies(s)) >= 2): s.open_to(8)
        if s.gate >= 8:
            s.g8_turns += 1
            if s.g8_turns > 10: s.out = True; s.died_g8 = True; return
        # techniques
        if s.gate >= 8 and not s.did_elephant:
            s.did_elephant = True; hits = 0
            for i in range(5):
                if tgt.out: break
                hit, crit, dealt = attack(fight, s, tgt, 6 + 10 + 8, lambda c: roll(16 if c else 8, 10), "force", False, adv=True)
                if hit: hits += 1
            if hits == 5 and not getattr(tgt, "stun_immune", False): tgt.paralyzed = True
        elif s.gate >= 8 and s.night_guy and not tgt.out:
            s.night_guy = False
            nat = d20(adv=True); total = nat + 24
            full = roll(40, 10) + 10
            if nat != 1 and total >= tgt.ac_now(): tgt.take(full, "force", "Night Guy", ignore_res=True)
            else: tgt.take(full // 2, "force", "Night Guy", ignore_res=True)
            fight.note("Night Guy")
        elif s.gate >= 7 and not s.did_tiger and s.focus >= 4:
            s.did_tiger = True; s.focus -= 4
            dmgv = roll(20, 10)
            if tgt.save("Dex", 23):
                if tgt.name in ("Jin", "Crane"): dmgv = 0
                else: dmgv //= 2
            else: tgt.prone = True
            tgt.take(dmgv, "force", "Daytime Tiger")
        elif s.gate >= 6 and not s.did_peacock and s.focus >= 2:
            s.did_peacock = True; s.focus -= 2; hits = 0
            for i in range(5):
                if tgt.out: break
                hit, crit, dealt = s.strike(fight, tgt, fire=True, stun=(i == 0))
                if hit: hits += 1
            if hits >= 3 and not getattr(tgt, "susanoo", False): tgt.prone = True
        else:
            n = 2
            flurry = 0
            if s.hp <= 50 and s.wob > 0 and s.gate < 8: s.wob -= 1; s.hp = min(s.maxhp, s.hp + d(12) + 5)
            elif s.focus > 0: s.focus -= 1; flurry = 3 + (1 if s.gate >= 4 else 0)
            first = False
            for i in range(n + flurry):
                if tgt.out: tgt = fight.pick_target(s)
                if not tgt: break
                hit, crit, dealt = s.strike(fight, tgt, stun=not first, topple=(i >= n))
                if hit: first = True
                if fight.over(): return
        # the gates' bill
        if s.gate >= 4 and not s.out:
            bill = roll(s.gate - 3, 6); s.hp -= bill
            if s.hp <= 0: s.hp = 0; s.out = True; s.died_g8 = (s.gate >= 8)
    def on_zero(s, src, crit): s.out = True
    def on_miss(s, *a): pass
    def on_hit(s, *a): pass

# ---------------------------------------------------------------- FIGHT
class Fight:
    def __init__(s, teams, verbose=False):
        s.teams = teams; s.all = [c for t in teams for c in t]
        for i, t in enumerate(teams):
            for c in t: c.team = i if len(t) > 1 or len(teams) > 2 else i; c.acted = False
        for c in s.all:
            if len([x for x in s.all if x.team == c.team]) == 1: c.team_solo = True
        s.round = 0; s.notes = []
        for c in s.all: c._fight_all = s.all
        s.verbose = verbose
    def note(s, m):
        if s.verbose: s.notes.append(f"R{s.round}: {m}")
    def enemies(s, c): return [e for e in s.all if e.alive() and e.team != c.team]
    def allies(s, c): return [a for a in s.all if a.alive() and a.team == c.team and a is not c]
    def pick_target(s, c):
        es = s.enemies(c)
        if not es: return None
        iz = [e for e in es if e.name == "Itachi"]
        if iz and c.name != "Itachi": return iz[0]
        return min(es, key=lambda e: (e.hp + e.thp) / (e.maxhp + 1))
    def over(s):
        teams_alive = {c.team for c in s.all if c.alive()}
        return len(teams_alive) <= 1
    def run(s):
        order = sorted(s.all, key=lambda c: c.init(), reverse=True)
        # Standoff: Jin vs his most dangerous enemy
        for j in [c for c in s.all if c.name == "Jin"]:
            es = s.enemies(j)
            if not es: continue
            foe = max(es, key=lambda e: DANGER[e.name])
            if d20(adv=True) + 11 >= foe.init():
                def dmg(crit): return roll(2 if crit else 1, 10, gwf=True) + 7 + 9 + (roll(1, 10) if foe.name == "Smasher" else 0)
                attack(s, j, foe, 13, dmg, "slashing", True, adv=True, crit_range=1, sneak=5)
                if foe.out: j.resolve += 3
            else:
                if foe.name == "Guts": foe.raging = True; foe.reckless = True; foe.swing(s, j, True, True, True)
                elif foe.name == "Smasher": attack(s, foe, j, 15, lambda c: roll(4 if c else 2, 8) + 7, "piercing", False, ignore_res=True)
                elif foe.name == "Crane": attack(s, foe, j, 11, lambda c: roll(2 if c else 1, 6) + 8, "slashing", True)
                elif foe.name == "GS": attack(s, foe, j, 10, lambda c: roll(2 if c else 1, 6) + 6, "piercing", True)
        while not s.over() and s.round < 40:
            s.round += 1
            for c in order:
                if s.over(): break
                if not c.alive(): continue
                c.start_turn()
                c.acted = True
                for e in s.all: e.trip_done = False
                if c.paralyzed or getattr(c, "asleep", False):
                    c.end_turn(s); continue
                c.turn(s)
                # Guts retaliation is handled as reaction on being hit in melee
                c.end_turn(s)
                # retaliation hook: any Guts hit in melee during this turn
                for g in s.all:
                    if g.name == "Guts" and g.alive() and g.last_hit_by_melee is c and c.alive() and g is not c:
                        g.retaliate(s, c); g.last_hit_by_melee = None
        alive_teams = {c.team for c in s.all if c.alive()}
        return (next(iter(alive_teams)) if alive_teams else None), s.round

MAKERS = {"GS": GS, "Guts": Guts, "Crane": Crane, "Itachi": Itachi, "Smasher": Smasher, "Jin": Jin, "Guy": Guy, "Guy7": lambda: Guy(7)}
NAMES = ["Smasher", "Guts", "Jin", "Itachi", "Crane", "GS", "Guy"]
DANGER["Guy"] = 5; DANGER["Guy7"] = 5

G8WINS = Counter()
def run_teams(team_names, n):
    """team_names: list of lists; returns win counts per team index (None = timeout)"""
    wins = Counter(); rounds = 0
    for _ in range(n):
        teams = [[MAKERS[x]() for x in t] for t in team_names]
        f = Fight(teams); w, r = f.run(); wins[w] += 1; rounds += r
        for c in f.all:
            if c.name == "Guy" and c.alive() and c.gate >= 8 and w == c.team: G8WINS[tuple(map(tuple, team_names))] += 1
    return wins, rounds / n

if __name__ == "__main__":
    mode = sys.argv[1]; n = int(sys.argv[2])
    if mode == "guy":
        for cap in ("Guy7", "Guy"):
            print(f"== Guy capped at gate {'7' if cap=='Guy7' else '8'} ==")
            for b in [x for x in NAMES if x != "Guy"]:
                w, r = run_teams([[cap], [b]], n)
                g8 = G8WINS.get(((cap,), (b,)), 0)
                print(f"   vs {b:8s} Guy wins {100*w[0]/n:5.1f}%  (avg {r:.1f} rounds{', ' + str(round(100*g8/n)) + '% of them at gate 8, which kills him after' if g8 else ''})")
    elif mode == "1v1":
        print("row beats column (%)")
        for a in NAMES:
            row = []
            for b in NAMES:
                if a == b: row.append("  -  "); continue
                w, _ = run_teams([[a], [b]], n); row.append(f"{100*w[0]/n:5.0f}")
            print(f"{a:8s}", " ".join(row))
    elif mode == "ffa":
        w, r = run_teams([[x] for x in NAMES], n)
        print({NAMES[k] if k is not None else "none": v for k, v in w.items()}, "avg rounds", round(r, 1))
    elif mode == "1v5":
        for a in NAMES:
            others = [x for x in NAMES if x != a]
            w, r = run_teams([[a], others], n)
            print(f"{a:8s} alone vs five: wins {100*w[0]/n:.1f}%  (avg {r:.1f} rounds)")
    elif mode == "2v2":
        duos = list(itertools.combinations(NAMES, 2)); score = Counter(); games = Counter()
        for i, A in enumerate(duos):
            for B in duos[i+1:]:
                if set(A) & set(B): continue
                w, _ = run_teams([list(A), list(B)], n)
                score[A] += w[0]; score[B] += w[1]; games[A] += n; games[B] += n
        for duo in sorted(duos, key=lambda x: -score[x] / max(1, games[x])):
            print(f"{'+'.join(duo):18s} {100*score[duo]/games[duo]:5.1f}% of its 2v2s")
    elif mode == "1v2":
        for a in NAMES:
            res = []
            for pair in itertools.combinations([x for x in NAMES if x != a], 2):
                w, _ = run_teams([[a], list(pair)], n); res.append((100 * w[0] / n, "+".join(pair)))
            res.sort(reverse=True)
            print(f"{a:8s}", ", ".join(f"{p}: {v:.0f}%" for v, p in res))
