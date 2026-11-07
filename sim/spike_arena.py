from arthur_arena import *
import arthur_arena

class Spike(C):
    def __init__(s):
        super().__init__("Spike"); s.hp = s.maxhp = 183; s.ac = 17
        s.saves = dict(Str=6, Dex=11, Con=8, Int=6, Wis=8, Cha=6); s.indom_bonus = 0
        s.focus = 14; s.luck = 6; s.nine = True; s.melee = True; s.wob = 4
    def init(s): return d20(adv=True) + 11
    def ac_now(s): return s.ac
    def save(s, ab, dc, spell=False, source=None):
        ok = super().save(ab, dc, spell, source)
        if not ok and s.focus > 0: s.focus -= 1; ok = d20() + s.saves[ab] >= dc
        if not ok and s.luck > 0: s.luck -= 1; ok = d20(adv=True) + s.saves[ab] >= dc
        return ok
    def defend_ac(s, att, total, melee, crit):
        # Lucky: disadvantage on an attack that would hit him
        if (crit or total >= s.ac) and s.luck > 0:
            s.luck -= 1
            if d(20) + (total - (total - 0)) * 0 + 0 and False: pass
            re = d(20); re_total = re + (total - (crit and 20 or (total - 0)))  # placeholder, replaced below
        return 0
    def modify_incoming(s, dmg, dtype, src, from_attack, melee, ignore_res):
        if from_attack and s.reaction: s.reaction = False; dmg = max(0, dmg - (d(10) + 19))
        return dmg
    def on_zero(s, src, crit):
        if s.nine: s.nine = False; s.hp = 1; return
        s.out = True
    def turn(s, fight):
        tgt = fight.pick_target(s)
        if not tgt: return
        if s.hp <= 90 and s.wob > 0: s.wob -= 1; s.hp = min(s.maxhp, s.hp + roll(2, 10) + 2)
        first_round = fight.round == 1 and not tgt.acted
        adv = first_round or tgt.reckless or tgt.prone or tgt.paralyzed
        sa = True
        for i in range(2):      # the Jericho
            if tgt.out: tgt = fight.pick_target(s)
            if not tgt: return
            def dmg(crit, fr=first_round):
                v = roll(2 if crit else 1, 10) + 5
                return v
            def extra(crit, dealt, t=tgt, fr=first_round):
                nonlocal sa
                if dealt and sa and (adv): t.take(roll(6 if crit else 3, 6) + (6 if fr else 0), "piercing", "Spike"); sa = False
            attack(fight, s, tgt, 11, dmg, "piercing", melee=False, adv=adv, extra=extra)
            if fight.over(): return
        if s.focus > 0:          # Flurry of three, Stunning Strike on the first hit, Topple on the rest
            s.focus -= 1; stunned = False
            for i in range(3):
                if tgt.out: tgt = fight.pick_target(s)
                if not tgt: return
                def dmg(crit): return roll(2 if crit else 1, 10) + 5
                def extra(crit, dealt, t=tgt):
                    nonlocal stunned
                    if dealt and not stunned and s.focus > 0 and t.name not in ("Guts","Smasher") and not getattr(t, "stun_immune", False) and not t.paralyzed:
                        s.focus -= 1; stunned = True
                        if not t.save("Con", 16): t.paralyzed = True; t.stun_until = fight.round
                    elif dealt and not t.prone and not getattr(t, "susanoo", False) and not t.save("Dex", 16): t.prone = True
                attack(fight, s, tgt, 11, dmg, "bludgeoning", True, adv=(tgt.reckless or tgt.prone or tgt.paralyzed), extra=extra)
                if fight.over(): return
    def on_miss(s, *a): pass
    def on_hit(s, *a): pass

# Lucky as a clean reroll-to-lower on a hit (2014-style), applied in the attack wrapper
_prev_attack = arthur_arena.attack
def attack(fight, att, tgt, bonus, dmg_fn, dtype, melee=True, adv=False, dis=False, **kw):
    if tgt.name == "Spike" and getattr(tgt, "luck", 0) > 0 and not dis:
        # peek: if the straight roll would hit, spend a point for disadvantage
        nat = d20(adv=adv)
        if nat + bonus >= tgt.ac_now() and nat != 1:
            tgt.luck -= 1; dis = True; adv = False
    return _prev_attack(fight, att, tgt, bonus, dmg_fn, dtype, melee, adv, dis, **kw)
for mod in (arena, guy_arena, guy2_arena, guy_canon, slayer_arena, crane2_arena, link_arena, bb_arena, anderson_arena, arthur_arena):
    mod.attack = attack
Spike.defend_ac = lambda s, att, total, melee, crit: 0
MAKERS["Spike"] = Spike; DANGER["Spike"] = 3

if __name__ == "__main__":
    n = int(sys.argv[1]); base = ["Arthur","GS","Itachi","Crane2","Jin","Guts","Beast","Smasher","GuyC","Slayer","Link","Anderson"]
    print("Spike Spiegel, 1v1 (wins %, avg rounds)")
    for b in base:
        w = Counter(); rr = 0; to = 0
        for _ in range(n):
            f = Fight([[Spike()], [MAKERS[b]()]]); res, r = f.run(); rr += r
            if r >= 40: to += 1
            else: w[res] += 1
        print(f"  vs {({'Crane2':'Crane','GuyC':'Guy'}).get(b,b):9s} {100*w[0]/n:5.1f}%   draws {100*to/n:3.0f}%   avg {rr/n:.1f} rounds")
    w = Counter()
    for _ in range(n):
        res, r = Fight([[Spike(), Arthur()], [GS(), Crane2()]]).run(); w[res] += 1
    print(f"Spike + Arthur vs Goblin Slayer + Crane: {100*w[0]/n:.1f}%")
    names = ["Spike","Arthur","GS","Itachi","Crane2"]; w = Counter()
    for _ in range(n):
        res, r = Fight([[MAKERS[x]()] for x in names]).run(); w[names[res] if res is not None else "draw"] += 1
    print("The mortals' free-for-all (Spike, Arthur, Goblin Slayer, Itachi, Crane):", {({"Crane2":"Crane"}).get(k,k): f"{100*v/n:.0f}%" for k, v in sorted(w.items(), key=lambda kv: -kv[1])})
