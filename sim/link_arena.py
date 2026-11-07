from crane2_arena import *
import crane2_arena

EVIL = {"Smasher"}
PIERCE_IMMUNITY = False

class Link(C):
    def __init__(s):
        super().__init__("Link"); s.hp = s.maxhp = 224; s.ac = 20
        s.saves = dict(Str=8, Dex=5, Con=9, Int=0, Wis=3, Cha=-1); s.indomitable = 3; s.indom_bonus = 0
        s.magic = 12; s.nayru = 0; s.fairies = 2; s.red = 1; s.blue = 1; s.surges = 2; s.sw = 4
        s.dice = 6; s.nuts = 10; s.triforce = True; s.melee = True; s.fright_immune = True
    def init(s): return d(20) + 11
    def ac_now(s): return s.ac
    def save(s, ab, dc, spell=False, source=None):
        ok = super().save(ab, dc, spell, source)
        if not ok and s.triforce: s.triforce = False; ok = True
        return ok
    def modify_incoming(s, dmg, dtype, src, from_attack, melee, ignore_res):
        if s.nayru > 0 and not (src == "Night Guy" or PIERCE_IMMUNITY): return 0
        if from_attack and not melee and s.reaction: s.reaction = False; dmg = max(0, dmg - (d(10) + 11))
        elif from_attack and melee and s.reaction and s.dice > 0: s.reaction = False; s.dice -= 1; dmg = max(0, dmg - (d(12) + 5))
        return dmg
    def on_zero(s, src, crit):
        if s.fairies > 0: s.fairies -= 1; s.hp = 90; return
        s.out = True
    def turn(s, fight):
        tgt = fight.pick_target(s)
        if not tgt: return
        if s.nayru > 0: s.nayru -= 1
        # bonus action: potions
        if s.hp <= 80 and s.red: s.red = 0; s.hp = s.maxhp
        elif s.hp <= 80 and s.blue: s.blue = 0; s.hp = s.maxhp; s.magic = 12
        elif s.hp <= 120 and s.sw > 0: s.sw -= 1; s.hp = min(s.maxhp, s.hp + d(10) + 20)
        actions = 1 + (1 if s.surges > 0 else 0)
        if s.surges > 0: s.surges -= 1
        for a in range(actions):
            if s.nayru == 0 and s.magic >= 3 and DANGER.get(tgt.name, 0) >= 4:
                s.magic -= 3; s.nayru = 10; continue      # Nayru's Love: the action
            first = False
            for i in range(4):
                if tgt.out: tgt = fight.pick_target(s)
                if not tgt: return
                # Deku Nut on the first attack of the action when the target is upright and stunnable
                if i == 0 and s.nuts > 0 and not tgt.paralyzed and tgt.name not in ("Guts",) and not getattr(tgt, "stun_immune", False):
                    s.nuts -= 1
                    if not tgt.save("Con", 18): tgt.paralyzed = True; tgt.stun_until = fight.round
                    continue
                prone = tgt.prone
                use_die = s.dice > 0 and not first
                def dmg(crit, d_=use_die, t=tgt):
                    v = roll(2 if crit else 1, 8) + 10
                    if d_: v += roll(2 if crit else 1, 12)
                    if t.name in EVIL: v += roll(4 if crit else 2, 8)
                    return v
                def extra(crit, dealt, t=tgt, d_=use_die):
                    if dealt and d_:
                        s.dice -= 1
                        if not t.prone and not getattr(t, "susanoo", False) and not t.save("Str", 19): t.prone = True
                adv = tgt.paralyzed or tgt.prone or getattr(tgt, "reckless", False)
                hit, crit, dealt = attack(fight, s, tgt, 14, dmg, "slashing", True, adv=adv, crit_range=1 if prone else 20, extra=extra)
                if not hit and getattr(s, "prowess", True): s.prowess = False
                if hit: first = True
                if fight.over(): return
        s.prowess = True
    def on_miss(s, *a): pass
    def on_hit(s, *a): pass

# Night Guy ignores immunity: already ignore_res=True in the canon Guy; the Crucible is ignore_res too (Argent cuts anything)
MAKERS["Link"] = Link; DANGER["Link"] = 5

if __name__ == "__main__":
    n = int(sys.argv[1]); base = ["Smasher","Guts","Jin","Itachi","GS","Crane2","GuyC","Slayer"]
    print("Hero of Time, 1v1 (wins %, avg rounds)")
    for b in base:
        w = Counter(); rr = 0; to = 0
        for _ in range(n):
            f = Fight([[Link()], [MAKERS[b]()]]); res, r = f.run(); rr += r
            if r >= 40: to += 1
            else: w[res] += 1
        print(f"  vs {({'Crane2':'Crane','GuyC':'Guy'}).get(b,b):8s} {100*w[0]/n:5.1f}%   draws {100*to/n:.0f}%   avg {rr/n:.1f} rounds")
    names = ["Link"] + base; w = Counter()
    for _ in range(n):
        res, r = Fight([[MAKERS[x]()] for x in names]).run(); w[names[res] if res is not None else "none"] += 1
    print("Nine-way FFA:", {({"GuyC":"Guy","Crane2":"Crane"}).get(k,k): f"{100*v/n:.0f}%" for k, v in sorted(w.items(), key=lambda kv: -kv[1])})
    w = Counter()
    for _ in range(n):
        res, r = Fight([[Link()], [MAKERS[x]() for x in base]]).run(); w[res] += 1
    print(f"Link alone vs the other eight: {100*w[0]/n:.1f}%")
    w = Counter()
    for _ in range(n):
        res, r = Fight([[Link(), Jin()], [Slayer(), GuyC()]]).run(); w[res] += 1
    print(f"Link + Jin vs Slayer + Guy: {100*w[0]/n:.1f}%")
