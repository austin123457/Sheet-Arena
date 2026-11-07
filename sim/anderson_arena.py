from bb_arena import *
import bb_arena

class Anderson(C):
    def __init__(s):
        super().__init__("Anderson"); s.hp = s.maxhp = 284; s.ac = 17
        s.saves = dict(Str=9, Dex=9, Con=10, Int=3, Wis=12, Cha=14); s.indom_bonus = 0
        s.down = False; s.radiant_taken = 0; s.haste = False; s.vow = None; s.slots = {5: 2, 4: 3, 3: 3, 2: 3, 1: 4}
        s.hold_used = False; s.melee = True; s.fright_immune = True; s.nail = False; s.nail_broken = False; s.down_dmg = 0
    def init(s): return d(20) + 11
    def ac_now(s): return s.ac + (2 if s.haste else 0)
    def save_adv(s, ab, spell): return ab == "Dex" and s.haste
    def modify_incoming(s, dmg, dtype, src, from_attack, melee, ignore_res):
        if s.nail and dtype in ("slashing", "piercing", "bludgeoning") and not ignore_res: dmg //= 2
        if dtype in ("radiant", "fire"): s.radiant_taken += dmg
        if s.down: s.down_dmg += dmg
        return dmg
    def on_zero(s, src, crit):
        if s.hp <= -s.maxhp: s.out = True; return        # a single blow for his whole pool
        s.hp = 0; s.down = True
    def take(s, dmg, dtype, src, **kw):
        if s.down and not s.nail:
            s.down_dmg += dmg
            return dmg
        before = s.hp
        r = super().take(dmg, dtype, src, **kw)
        if s.down and s.nail and s.down_dmg >= 40: s.out = True; s.nail_broken = True
        return r
    def start_turn(s):
        super().start_turn()
    def turn(s, fight):
        tgt = fight.pick_target(s)
        if not tgt: return
        # regeneration
        if s.down:
            if s.radiant_taken >= 20:
                s.radiant_taken = 0; return             # nothing regrows this turn
            s.down = False; s.hp = 60 if s.nail else 30; s.down_dmg = 0; s.radiant_taken = 0
            s.prone = False
        else:
            s.hp = min(s.maxhp, s.hp + (60 if s.nail else 30)); s.radiant_taken = 0
        if s.vow is None: s.vow = tgt
        # the Nail: desperation
        if not s.nail and getattr(s, "times_down", 0) >= 3 and (tgt.hp + tgt.thp) > 0.5 * tgt.maxhp:
            s.nail = True; s.hp = min(284, s.hp + 60); return
        if not s.haste and s.slots[3] > 0 and not (tgt.saves.get("Wis", 0) <= 3 and not s.hold_used and s.slots[5] > 0):
            s.slots[3] -= 1; s.haste = True; return
        if not s.hold_used and tgt.saves.get("Wis", 0) <= 3 and s.slots[5] > 0 and not tgt.paralyzed and tgt.name not in ("Smasher",):
            s.hold_used = True; s.slots[5] -= 1
            if not tgt.save("Wis", 18, spell=True): tgt.paralyzed = True; tgt.hold = True
            return
        if s.nail:
            for e in fight.enemies(s):
                if e.melee and not e.out: e.take(roll(2, 8), "radiant", "Holy Thorns")
        n = (3 if s.nail else 3) + (1 if s.haste else 0)
        smited = False; first = False
        for i in range(n):
            if tgt.out: tgt = fight.pick_target(s)
            if not tgt: return
            adv = (tgt is s.vow) or tgt.paralyzed
            def dmg(crit, sm=not smited, nail=s.nail):
                v = (roll(4 if crit else 2, 8) + 5) if nail else (roll(2 if crit else 1, 6) + 5)
                v += roll(2 if crit else 1, 8)           # Radiant Strikes
                if sm:
                    lvl = next((L for L in (5, 4, 3, 2, 1) if s.slots[L] > 0), None)
                    if lvl: s.slots[lvl] -= 1; v += roll((2 + lvl - 1) * (2 if crit else 1), 8)
                return v
            hit, crit, dealt = attack(fight, s, tgt, 11, dmg, "radiant", True, adv=adv, crit_range=1 if tgt.paralyzed else 20)
            if hit: first = True; smited = True
            if fight.over(): return
    def end_turn(s, fight):
        if getattr(s, "hold", False): pass
        super().end_turn(fight)
    def on_miss(s, *a): pass
    def on_hit(s, *a): pass

_orig_take_track = Anderson.on_zero
def on_zero(s, src, crit):
    s.times_down = getattr(s, "times_down", 0) + 1
    _orig_take_track(s, src, crit)
Anderson.on_zero = on_zero
MAKERS["Anderson"] = Anderson; DANGER["Anderson"] = 6

# Hold Monster: the paralyzed flag already repeats a DC 19 Wis save at the target's end of turn in the base engine (DC 18 here is close enough)

if __name__ == "__main__":
    n = int(sys.argv[1]); base = ["Smasher","Guts","Jin","Itachi","GS","Crane2","GuyC","Slayer","Link","Beast"]
    print("Anderson, 1v1 (wins %, draws %, avg rounds)")
    for b in base:
        w = Counter(); rr = 0; to = 0
        for _ in range(n):
            f = Fight([[Anderson()], [MAKERS[b]()]]); res, r = f.run(); rr += r
            if r >= 40: to += 1
            else: w[res] += 1
        print(f"  vs {({'Crane2':'Crane','GuyC':'Guy'}).get(b,b):8s} {100*w[0]/n:5.1f}%   draws {100*to/n:3.0f}%   avg {rr/n:.1f} rounds")
    names = ["Anderson"] + base; w = Counter()
    for _ in range(n):
        res, r = Fight([[MAKERS[x]()] for x in names]).run(); w[names[res] if res is not None else "draw"] += 1
    print("Eleven-way FFA:", {({"GuyC":"Guy","Crane2":"Crane"}).get(k,k): f"{100*v/n:.0f}%" for k, v in sorted(w.items(), key=lambda kv: -kv[1])})
    w = Counter()
    for _ in range(n):
        res, r = Fight([[Anderson(), Jin()], [Smasher(), BattleBeast()]]).run(); w[res] += 1
    print(f"Anderson + Jin vs Smasher + Beast: {100*w[0]/n:.1f}%")
