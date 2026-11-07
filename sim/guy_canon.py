from guy2_arena import *
import guy2_arena

class GuyC(Guy2):
    """Canon merge: the second sheet's chassis, Night Guy 25d12+15, Daytime Tiger 14d12+7 for crowds"""
    def __init__(s):
        super().__init__(); s.name = "GuyC"; s.g8_adv = True
    def turn(s, fight):
        enemies = fight.enemies(s)
        if not enemies: return
        cluster = [e for e in enemies if e.melee]
        # crowd: seven gates open, 3+ Focus, two or more melee enemies -> Daytime Tiger instead of the Attack action
        if s.gate == 7 and s.g8 is None and s.focus >= 3 and len(cluster) >= 2 and s.hp >= 70:
            s.hp -= (14 if s.gate >= 6 else s.gate)
            if s.hp <= 0: s.out = True; return
            s.focus -= 3; s.hp -= roll(4, 10)
            if s.hp <= 0: s.out = True; return
            for e in cluster:
                dmg = roll(30, 12) + 7
                if e.save("Dex", 16):
                    if e.name in ("Jin", "Crane"): continue
                    dmg //= 2
                else: e.prone = True
                e.take(dmg, "force", "Daytime Tiger")
            return
        return super().turn(fight)

# Night Guy at 25d12+15
_src = open(guy2_arena.__file__).read()
import types
def night(s, tgt): tgt.take(roll(60, 12) + 15, "force", "Night Guy", ignore_res=True)
_old_turn = Guy2.turn
def turn_patch(s, fight):
    if s.gate >= 8 and s.g8 != fight.round and s.g8 != "spent":
        tgt = fight.pick_target(s)
        if not tgt: return
        s.night_used = True; night(s, tgt); s.g8 = "spent"
        if fight.over(): return
        s.hp = 0; s.out = True; return
    return _old_turn(s, fight)
Guy2.turn = turn_patch
MAKERS["GuyC"] = GuyC; DANGER["GuyC"] = 7
_o = Itachi.turn
def it(s, fight):
    if any(e.name == "GuyC" for e in fight.enemies(s)) and s.tsukuyomi: s.tsukuyomi = False
    return _o(s, fight)
Itachi.turn = it

if __name__ == "__main__":
    n = int(sys.argv[1])
    print("Canon Guy, 1v1 (wins %; share decided by the Gate of Death)")
    for b in NAMES + ["Guy2", "Guy"]:
        w = Counter(); g8 = 0; rr = 0
        for _ in range(n):
            g = GuyC(); o = MAKERS[b]()
            res, r = Fight([[g], [o]]).run(); w[res] += 1; rr += r
            if res == 0 and g.gate >= 8: g8 += 1
        label = {"Guy2": "brother's", "Guy": "mine"}.get(b, b)
        print(f"  vs {label:9s} wins {100*w[0]/n:5.1f}%   (Gate of Death {100*g8/n:4.1f}%)  avg {rr/n:.1f} rounds")
    print("\nSeven-way free-for-all (canon Guy in place of the other two)")
    names = ["GuyC"] + NAMES; w = Counter()
    for _ in range(n):
        res, r = Fight([[MAKERS[x]()] for x in names]).run(); w[names[res] if res is not None else "none"] += 1
    print(" ", {k: f"{100*v/n:.0f}%" for k, v in sorted(w.items(), key=lambda kv: -kv[1])})
    print("\nCanon Guy + Jin vs Smasher + Guts: ", end="")
    w = Counter()
    for _ in range(n):
        res, r = Fight([[GuyC(), Jin()], [Smasher(), Guts()]]).run(); w[res] += 1
    print(f"{100*w[0]/n:.1f}%")
    print("Canon Guy alone vs the other six: ", end="")
    w = Counter()
    for _ in range(n):
        res, r = Fight([[GuyC()], [MAKERS[x]() for x in NAMES]]).run(); w[res] += 1
    print(f"{100*w[0]/n:.1f}%")
