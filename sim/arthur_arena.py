from anderson_arena import *
import anderson_arena

class Arthur(C):
    """Caleb's sheet: Fighter (Dead Eye) 19 / Rogue 1, open sand (no cover)"""
    def __init__(s, cover=0):
        super().__init__("Arthur"); s.hp = s.maxhp = 223; s.ac = 16 + cover
        s.saves = dict(Str=9, Dex=5, Con=9, Int=0, Wis=1, Cha=0); s.indomitable = 3; s.indom_bonus = 19
        s.boxes = 6; s.deadeye = False; s.surges = 2; s.sw = 4; s.snake = 2; s.cures = 3; s.potent = 1; s.miracle = 1
        s.dyn = 4; s.melee = False; s.refund_turn = -1
    def init(s): return d(20) + 11
    def ac_now(s): return s.ac
    def modify_incoming(s, dmg, dtype, src, from_attack, melee, ignore_res): return dmg
    def on_zero(s, src, crit): s.out = True
    def shot(s, fight, tgt, sa_ok):
        def dmg(crit):
            v = roll(4 if crit else 2, 6) + 5
            if sa_ok and not getattr(s, "sa_used", False): v += roll(2 if crit else 1, 6); s.sa_used = True
            return v
        def extra(crit, dealt, t=tgt):
            if dealt and s.deadeye and crit and 0 < (t.hp + t.thp) <= 50 and not t.out:
                t.hp = 0; t.on_zero("Arthur", True)                # Fatal Areas
            if dealt and (crit or t.out) and s.refund_turn != fight.round:
                s.refund_turn = fight.round; s.boxes = min(6, s.boxes + 1)
        cr = 18 if s.deadeye else 20
        hit, crit, dealt = attack(fight, s, tgt, 13, dmg, "piercing", melee=False, adv=s.deadeye, crit_range=cr, extra=extra)
        if not hit and getattr(s, "prowess", True):
            s.prowess = False
            dealt = tgt.take(dmg(False), "piercing", "Arthur", from_attack=True, melee=False)   # Peerless Aim
            return True
        return hit
    def turn(s, fight):
        tgt = fight.pick_target(s)
        if not tgt: return
        s.prowess = True; s.sa_used = False
        if s.deadeye:
            if s.boxes > 0: s.boxes -= 1
            else: s.deadeye = False
        # bonus action
        bonus = None
        if s.hp <= 100 and s.sw > 0: s.sw -= 1; s.hp = min(s.maxhp, s.hp + d(10) + 19); bonus = "sw"
        elif s.boxes == 0 and not s.deadeye and s.snake > 0: s.snake -= 1; s.boxes = 3; bonus = "snake"
        elif not s.deadeye and s.boxes >= 1:
            s.boxes -= 1; s.deadeye = True; bonus = "de"; s.shot(fight, tgt, True)          # the free shot
            if fight.over(): return
        elif s.hp <= 150 and s.miracle: s.miracle = 0; s.hp = min(s.maxhp, s.hp + roll(4, 4) + 4); s.boxes = min(6, s.boxes + 2); bonus = "t"
        elif s.hp <= 150 and s.potent: s.potent = 0; s.hp = min(s.maxhp, s.hp + roll(4, 4) + 4); bonus = "t"
        elif s.hp <= 150 and s.cures: s.cures -= 1; s.hp = min(s.maxhp, s.hp + roll(2, 4) + 2); bonus = "t"
        # action: Painting when he can afford a big turn, else four shots
        shots = 4
        if s.deadeye and s.boxes >= 3 and s.surges > 0:
            n = s.boxes; s.boxes = 0
            for i in range(n):
                if tgt.out: tgt = fight.pick_target(s)
                if not tgt: return
                s.shot(fight, tgt, True)
                if fight.over(): return
        else:
            for i in range(shots):
                if tgt.out: tgt = fight.pick_target(s)
                if not tgt: return
                s.shot(fight, tgt, True)
                if fight.over(): return
        if s.surges > 0:
            s.surges -= 1
            for i in range(shots):
                if tgt.out: tgt = fight.pick_target(s)
                if not tgt: return
                s.shot(fight, tgt, True)
                if fight.over(): return
    def on_miss(s, *a): pass
    def on_hit(s, *a): pass

MAKERS["Arthur"] = Arthur; DANGER["Arthur"] = 3

if __name__ == "__main__":
    n = int(sys.argv[1]); base = ["Smasher","Guts","Jin","Itachi","GS","Crane2","GuyC","Slayer","Link","Beast","Anderson"]
    for cover, label in ((0, "open sand, AC 16"), (2, "fighting from half cover, AC 18")):
        print(f"Arthur Morgan, 1v1 ({label})")
        for b in base:
            w = Counter(); rr = 0; to = 0
            for _ in range(n):
                f = Fight([[Arthur(cover)], [MAKERS[b]()]]); res, r = f.run(); rr += r
                if r >= 40: to += 1
                else: w[res] += 1
            print(f"  vs {({'Crane2':'Crane','GuyC':'Guy'}).get(b,b):9s} {100*w[0]/n:5.1f}%   draws {100*to/n:3.0f}%   avg {rr/n:.1f} rounds")
    names = ["Arthur"] + base; w = Counter()
    for _ in range(n):
        res, r = Fight([[MAKERS[x]()] for x in names]).run(); w[names[res] if res is not None else "draw"] += 1
    print("Twelve-way FFA:", {({"GuyC":"Guy","Crane2":"Crane"}).get(k,k): f"{100*v/n:.0f}%" for k, v in sorted(w.items(), key=lambda kv: -kv[1])})
    w = Counter()
    for _ in range(n):
        res, r = Fight([[Arthur(), GS()], [Crane2(), Itachi()]]).run(); w[res] += 1
    print(f"Arthur + Goblin Slayer vs Crane + Itachi: {100*w[0]/n:.1f}%")
