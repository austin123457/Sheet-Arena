from guy_arena import *
import guy_arena, arena

class Guy2(C):
    """Brother's sheet: Monk (Warrior of the Eight Gates) 20"""
    def __init__(s):
        super().__init__("Guy2"); s.hp = s.maxhp = 263; s.ac = 19
        s.saves = dict(Str=9, Dex=13, Con=10, Int=6, Wis=8, Cha=5); s.indom_bonus = 0
        s.focus = 20; s.gate = 0; s.sup_def = False; s.melee = True; s.g8 = None; s.night_used = False
        s.stun_immune = False; s.eyes_averted = True
    def init(s): return d(20) + 13
    def ac_now(s): return s.ac + (2 if s.gate >= 4 else 0)
    def save(s, ab, dc, spell=False, source=None):
        ok = super().save(ab, dc, spell, source)
        if not ok and s.focus > 0:
            s.focus -= 1; ok = d20(adv=(ab == "Str" and s.gate >= 1)) + s.saves[ab] >= dc
        return ok
    def defend_ac(s, att, total, melee, crit): return 0
    def modify_incoming(s, dmg, dtype, src, from_attack, melee, ignore_res):
        if (s.sup_def and dtype != "force" or s.gate >= 8) and not ignore_res: dmg //= 2
        if from_attack and s.reaction:
            s.reaction = False; dmg = max(0, dmg - (d(10) + 27))
        return dmg
    def on_zero(s, src, crit): s.out = True
    def dmg_bonus(s): return 7 + (8 if s.gate >= 8 else s.gate)
    def turn(s, fight):
        tgt = fight.pick_target(s)
        if not tgt: return
        if s.g8 == "spent": s.out = True; return          # the Gate of Death closed: 0 HP, dying
        if 1 <= s.gate <= 7:
            s.hp -= (14 if s.gate >= 6 else s.gate)
            if s.hp <= 0: s.out = True; return
        bonus = None
        if s.gate == 0:
            s.gate = 7; bonus = "gates"
        elif s.gate == 7 and s.hp < 70 and (tgt.hp + tgt.thp) > 0.15 * tgt.maxhp:
            s.gate = 8; s.g8 = fight.round; s.stun_immune = True; bonus = "gates"
        if not s.sup_def and s.focus >= 3: s.sup_def = True; s.focus -= 3
        if s.gate >= 8:
            if s.g8 == fight.round:
                for k in range(1, 6):      # Evening Elephant
                    if tgt.out: tgt = fight.pick_target(s)
                    if not tgt: return
                    attack(fight, s, tgt, 13, (lambda crit, kk=k: roll(kk * (2 if crit else 1), 12) + 15), "force", True, adv=getattr(s, "g8_adv", False), crit_range=19, ignore_res=True)
                    if fight.over(): return
                return
            # Night Guy: auto, unreducible
            s.night_used = True
            tgt.take(roll(20, 12) + 15, "force", "Night Guy", ignore_res=True)
            s.g8 = "spent"
            if fight.over(): return
            s.hp = 0; s.out = True
            return
        # seven gates: Morning Peacock (5 fire strikes, 2 Focus) + free Flurry (3) + Stunning Strike on the first hit
        peacock = s.focus >= 2
        if peacock: s.focus -= 2
        strikes = (5 if peacock else 3) + (3 if bonus is None else 0)
        first = False; peacock_hits = 0
        for i in range(strikes):
            if tgt.out: tgt = fight.pick_target(s)
            if not tgt: return
            is_pk = peacock and i < 5
            def dmg(crit, pk=is_pk, de=(fight.round == 1 and not first)):
                v = roll(2 if crit else 1, 12) + s.dmg_bonus()
                if de: v += d(8)
                return v
            def extra(crit, dealt, t=tgt, pk=is_pk, i=i):
                nonlocal peacock_hits
                if dealt and pk: peacock_hits += 1
                if dealt and not first and s.focus > 0 and t.name not in ("Guts", "Smasher") and not getattr(t, "stun_immune", False) and not t.paralyzed:
                    s.focus -= 1
                    if not t.save("Con", 16): t.paralyzed = True; t.stun_until = fight.round
                if dealt and not pk and not t.prone and not getattr(t, "susanoo", False):
                    if not t.save("Dex", 16): t.prone = True
            hit, crit, dealt = attack(fight, s, tgt, 13, dmg, "fire" if is_pk else "bludgeoning", True, crit_range=19)
            if hit: first = True
            if fight.over(): return
        if peacock_hits >= 2 and tgt and not tgt.out: tgt.burning_small = True
    def on_miss(s, *a): pass
    def on_hit(s, *a): pass

MAKERS["Guy2"] = Guy2; DANGER["Guy2"] = 7
_orig = Itachi.turn
def itachi_turn(s, fight):
    if any(e.name == "Guy2" for e in fight.enemies(s)) and s.tsukuyomi: s.tsukuyomi = False
    return _orig(s, fight)
Itachi.turn = itachi_turn

if __name__ == "__main__":
    n = int(sys.argv[1])
    print("Brother's Guy, 1v1 (wins %; share of all fights decided by the Gate of Death)")
    for b in NAMES + ["Guy"]:
        w = Counter(); g8 = 0; rr = 0
        for _ in range(n):
            g = Guy2(); o = MAKERS[b]()
            res, r = Fight([[g], [o]]).run(); w[res] += 1; rr += r
            if res == 0 and g.gate >= 8: g8 += 1
        print(f"  vs {b:8s} wins {100*w[0]/n:5.1f}%   (Gate of Death wins {100*g8/n:4.1f}%)  avg {rr/n:.1f} rounds")
    print("\nEight-way free-for-all")
    names = ["Guy2", "Guy"] + NAMES; w = Counter()
    for _ in range(n):
        res, r = Fight([[MAKERS[x]()] for x in names]).run(); w[names[res] if res is not None else "none"] += 1
    print(" ", {k: f"{100*v/n:.0f}%" for k, v in sorted(w.items(), key=lambda kv: -kv[1])})
    print("\nBrother's Guy alone vs the other seven: ", end="")
    w = Counter()
    for _ in range(n):
        res, r = Fight([[Guy2()], [MAKERS[x]() for x in NAMES + ["Guy"]]]).run(); w[res] += 1
    print(f"{100*w[0]/n:.1f}%")
