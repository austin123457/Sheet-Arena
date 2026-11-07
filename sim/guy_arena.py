from arena import *
import arena

class Guy(C):
    def __init__(s):
        super().__init__("Guy"); s.hp = s.maxhp = 203; s.ac = 21
        s.saves = dict(Str=7, Dex=13, Con=9, Int=5, Wis=10, Cha=5); s.indom_bonus = 0
        s.focus = 20; s.gate = 0; s.gate8_turn = None; s.night_used = False; s.sup_def = False; s.melee = True
        s.stun_immune = False; s.eyes_averted = True; s.dead_after = False
    def init(s): return d(20) + 7
    def ac_now(s): return s.ac + (2 if s.gate >= 5 else 0)
    def save(s, ab, dc, spell=False, source=None):
        if s.gate >= 8 and ab in ("Wis", "Con"): pass
        ok = super().save(ab, dc, spell, source)
        if not ok and s.focus > 0:
            s.focus -= 1; nat = d20(); ok = nat + s.saves[ab] >= dc
        return ok
    def defend_ac(s, att, total, melee, crit):
        # Seventh gate: attacks against him have disadvantage (handled in attack via reckless-like flag)
        return 0
    def modify_incoming(s, dmg, dtype, src, from_attack, melee, ignore_res):
        if s.sup_def and dtype != "force" and not ignore_res: dmg //= 2
        if from_attack and s.reaction:
            s.reaction = False; dmg = max(0, dmg - (d(10) + 27))
        return dmg
    def take(s, dmg, dtype, src, **kw):
        if s.gate >= 8 and src != "gate":
            before = s.hp; r = super().take(dmg, dtype, src, **kw)
            if s.hp <= 0: s.hp = 1; s.out = False
            return r
        return super().take(dmg, dtype, src, **kw)
    def on_zero(s, src, crit):
        if s.gate >= 8: s.hp = 1; return
        s.out = True
    def gate_dice(s):
        return 6 if s.gate >= 8 else 3 if s.gate >= 7 else 2 if s.gate >= 6 else 1 if s.gate >= 3 else 0
    def to_hit(s):
        return 13 + (5 if s.gate >= 8 else 4 if s.gate >= 7 else 2 if s.gate >= 5 else 0)
    def turn(s, fight):
        tgt = fight.pick_target(s)
        if not tgt: return
        # gate bill
        if s.gate >= 8:
            if fight.round - s.gate8_turn >= 10 or s.dead_after: s.out = True; return
        elif s.gate >= 7: s.hp -= roll(3, 10)
        elif s.gate >= 6: s.hp -= roll(2, 10)
        elif s.gate >= 4: s.hp -= d(10)
        if s.hp <= 0: s.out = True; return
        # open gates: 6 on turn 1, 7 on turn 2 if the target is still healthy, 8 if losing
        if s.gate < 6: s.gate = 7 if DANGER.get(tgt.name, 0) >= 5 else 6; s.hp = min(s.maxhp, s.hp + 20)
        elif s.gate < 7 and (tgt.hp + tgt.thp) > 0.4 * tgt.maxhp: s.gate = 7
        elif s.gate < 8 and s.hp < 70 and (tgt.hp + tgt.thp) > 0.15 * tgt.maxhp:
            s.gate = 8; s.gate8_turn = fight.round; s.stun_immune = True
        if not s.sup_def and s.focus >= 3: s.sup_def = True; s.focus -= 3
        bonus = 13 + 0
        hit_bonus = s.to_hit()
        gd = s.gate_dice()
        # action
        if s.gate >= 8:
            if not s.night_used and (tgt.hp + tgt.thp) <= 250:
                s.night_used = True; s.dead_after = True
                dmg = roll(30, 12)
                if tgt.save("Con", 25): dmg //= 2
                tgt.take(dmg, "force", "Night Guy", ignore_res=True)
                return
            # Evening Elephant
            for k in range(1, 6):
                if tgt.out: tgt = fight.pick_target(s)
                if not tgt: return
                attack(fight, s, tgt, 18, (lambda crit, kk=k: roll(4 * kk * (2 if crit else 1), 12)), "force", True, adv=True)
                if fight.over(): return
            return
        if s.gate >= 7 and not getattr(s, "tiger_used", False) and (tgt.hp + tgt.thp) > 120:
            s.tiger_used = True; s.hp -= roll(4, 10)
            if s.hp <= 0: s.out = True; return
            dmg = roll(20, 10)
            if tgt.save("Con", 18): dmg //= 2
            else: tgt.prone = True
            tgt.take(dmg, "force", "Daytime Tiger")
            if fight.over(): return
            strikes = 3
        elif s.gate >= 6:
            strikes = 6 + 3  # Morning Peacock + Flurry
            tgt.reaction = False
        else:
            strikes = 3 + 3
        s.focus = max(0, s.focus - 1)
        first = False
        for i in range(strikes):
            if tgt.out: tgt = fight.pick_target(s)
            if not tgt: return
            peacock = (s.gate >= 6 and i < 6)
            def dmg(crit, sav=not first, pk=peacock, g=gd):
                w = roll(2 if crit else 1, 12)
                if sav: w = max(w, roll(2 if crit else 1, 12))
                v = w + 7
                if g: v += roll(g * (2 if crit else 1), 12)
                if pk: v += roll(4 if crit else 2, 6)
                return v
            def extra(crit, dealt, t=tgt, i=i):
                if dealt and not first and s.focus > 0 and not getattr(t, "stun_immune", False) and t.name not in ("Guts", "Smasher") and not t.paralyzed:
                    s.focus -= 1
                    if not t.save("Con", 18): t.paralyzed = True  # stunned until his next turn, modeled as paralysis for one round
                    t.stun_until = fight.round
                if dealt and i >= 1 and not t.prone and not getattr(t, "susanoo", False):
                    if not t.save("Dex", 18): t.prone = True
            hit, crit, dealt = attack(fight, s, tgt, hit_bonus, dmg, "bludgeoning", True, extra=extra)
            if hit: first = True
            if fight.over(): return
    def on_miss(s, *a): pass
    def on_hit(s, *a): pass

# seventh gate disadvantage: patch attack() via reckless-style flag
_orig_attack = arena.attack
def attack(fight, att, tgt, bonus, dmg_fn, dtype, melee=True, adv=False, dis=False, **kw):
    if getattr(tgt, "gate", 0) >= 7: dis = True
    return _orig_attack(fight, att, tgt, bonus, dmg_fn, dtype, melee, adv, dis, **kw)
arena.attack = attack
# stun wears off at the start of the stunned creature's next turn after Guy's
_orig_start = C.start_turn
def start_turn(s):
    _orig_start(s)
    if getattr(s, "stun_until", None) is not None and s.paralyzed and s.name != "Guy":
        pass
C.start_turn = start_turn
_orig_end = C.end_turn
def end_turn(s, fight):
    if getattr(s, "stun_until", None) is not None and s.paralyzed:
        s.paralyzed = False; s.stun_until = None; return
    _orig_end(s, fight)
C.end_turn = end_turn

MAKERS["Guy"] = Guy
DANGER["Guy"] = 7
# Itachi's eye-contact spells cannot reach him: Tsukuyomi is skipped against Guy
_orig_cast = Itachi.turn
def itachi_turn(s, fight):
    enemies = fight.enemies(s)
    if any(e.name == "Guy" for e in enemies) and s.tsukuyomi:
        s.tsukuyomi = False  # he never bothers; Guy is watching his feet
    return _orig_cast(s, fight)
Itachi.turn = itachi_turn

if __name__ == "__main__":
    n = int(sys.argv[1])
    print("Guy 1v1 (wins %, and how many of those wins used the Eighth Gate)")
    for b in NAMES:
        w = Counter(); g8 = 0; night = 0; rounds = 0
        for _ in range(n):
            g = Guy(); o = MAKERS[b]()
            res, r = Fight([[g], [o]]).run(); w[res] += 1; rounds += r
            if res == 0 and g.gate >= 8: g8 += 1
            if res == 0 and g.night_used: night += 1
        print(f"  vs {b:8s} Guy wins {100*w[0]/n:5.1f}%   (Eighth Gate in {100*g8/n:4.1f}% of all fights; Night Guy {100*night/n:4.1f}%)  avg {rounds/n:.1f} rounds")
    print("\nSeven-way free-for-all")
    w = Counter(); g8 = 0
    names = ["Guy"] + NAMES
    for _ in range(n):
        teams = [[MAKERS[x]()] for x in names]
        res, r = Fight(teams).run(); w[names[res] if res is not None else "none"] += 1
    print(" ", dict(w))
    print("\nGuy alone vs the other six: ", end="")
    w = Counter()
    for _ in range(n):
        res, r = Fight([[Guy()], [MAKERS[x]() for x in NAMES]]).run(); w[res] += 1
    print(f"wins {100*w[0]/n:.1f}%")
    print("Guy + Jin vs Smasher + Guts: ", end="")
    w = Counter()
    for _ in range(n):
        res, r = Fight([[Guy(), Jin()], [Smasher(), Guts()]]).run(); w[res] += 1
    print(f"Guy+Jin win {100*w[0]/n:.1f}%")
