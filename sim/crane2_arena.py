from slayer_arena import *
import slayer_arena

class Crane2(C):
    """Brother's retuned Crane: Barbarian (Path of the Beast, homebrew) 14 / Rogue (Thief) 5 / Fighter 1. Meter starts empty after a rest."""
    def __init__(s):
        super().__init__("Crane2"); s.hp = s.maxhp = 233; s.ac = 16
        s.saves = dict(Str=11, Dex=3, Con=9, Int=-1, Wis=0, Cha=-1); s.indom_bonus = 0
        s.meter = 0; s.beast = False; s.rel_dc = 10; s.sw = 2; s.bandages = 4; s.rare = 2; s.morphine = 1
        s.regen = 0; s.dmg_boost = False; s.melee = True; s.hit_this_turn = False; s.dmg_this_round = False; s.miss_this_round = False
        s.stun_immune = False
    def init(s): return d20(adv=True) + 3
    def ac_now(s): return s.ac
    def save_adv(s, ab, spell): return ab == "Dex" or (ab == "Str" and s.beast)
    def fill(s, n):
        if not s.beast: s.meter = min(6, s.meter + n)
    def modify_incoming(s, dmg, dtype, src, from_attack, melee, ignore_res):
        if s.beast and dtype in ("slashing", "piercing", "bludgeoning") and not ignore_res: dmg //= 2
        if from_attack and s.reaction: s.reaction = False; dmg //= 2
        return dmg
    def after_damage(s, dmg, dtype, src, melee):
        if not s.dmg_this_round: s.dmg_this_round = True; s.fill(1)
    def defend_ac(s, att, total, melee, crit):
        if not crit and total < s.ac and not s.miss_this_round: s.miss_this_round = True; s.fill(1)
        return 0
    def on_zero(s, src, crit):
        if s.beast and d(20) + 9 >= s.rel_dc: s.rel_dc += 5; s.hp = 28; return
        s.out = True
    def start_turn(s):
        super().start_turn(); s.dmg_this_round = False; s.miss_this_round = False; s.hit_this_turn = False
    def unleash(s, fight, full):
        s.beast = True; s.reckless = True
        if full:
            s.hp = s.maxhp
            for e in fight.enemies(s):
                if e.melee and not e.out and not getattr(e, "stun_immune", False) and e.name not in ("Guts",):
                    if not e.save("Con", 19): e.paralyzed = True; e.stun_until = fight.round
    def turn(s, fight):
        tgt = fight.pick_target(s)
        if not tgt: return
        if s.regen > 0: s.regen -= 1; s.hp = min(s.maxhp, s.hp + 5)
        bonus = False
        if s.beast:
            s.meter -= 1
            if s.meter <= 0: s.beast = False; s.meter = 0; s.ending = True
        if not s.beast and s.meter >= 6: s.unleash(fight, True); bonus = True
        elif not s.beast and s.meter >= 3 and s.hp < 80: s.unleash(fight, False); bonus = True
        if s.beast:
            first = False
            for i in range(3):
                if tgt.out: tgt = fight.pick_target(s)
                if not tgt: return
                brutal = (i == 2) and not s.disadv_attacks and not s.poisoned
                def dmg(crit, sav=not first, br=brutal):
                    w = roll(2 if crit else 1, 10)
                    if sav: w = max(w, roll(2 if crit else 1, 10))
                    return w + 8 + (2 if s.dmg_boost else 0) + (roll(2 if crit else 1, 10) if br else 0)
                def extra(crit, dealt, t=tgt):
                    if dealt:
                        s.hp = min(s.maxhp, s.hp + 7)
                        if 0 < t.hp + t.thp <= 15: t.hp = 0; t.on_zero("Crane2", False)
                hit, crit, dealt = attack(fight, s, tgt, 11, dmg, "slashing", True, adv=not brutal, extra=extra)
                if hit: first = True
                if fight.over(): return
            return
        # human form
        if not bonus:
            if s.regen == 0 and not getattr(s, "booster_used", False): s.booster_used = True; s.regen = 10; s.dmg_boost = True; bonus = True
            elif s.hp <= 150 and s.rare > 0: s.rare -= 1; s.hp = min(s.maxhp, s.hp + roll(4, 8) + 8); bonus = True
            elif s.hp <= 150 and s.bandages > 0: s.bandages -= 1; s.hp = min(s.maxhp, s.hp + roll(2, 8) + 4); bonus = True
            elif s.hp <= 100 and s.morphine > 0: s.morphine -= 1; s.hp = min(s.maxhp, s.hp + roll(6, 8) + 12); bonus = True
            elif s.hp <= 150 and s.sw > 0: s.sw -= 1; s.hp = min(s.maxhp, s.hp + d(10) + 1); bonus = True
        s.reckless = True
        first = False
        for i in range(2):
            if tgt.out: tgt = fight.pick_target(s)
            if not tgt: break
            def dmg(crit, sav=not first):
                w = roll(2 if crit else 1, 6)
                if sav: w = max(w, roll(2 if crit else 1, 6))
                return w + 7 + (2 if s.dmg_boost else 0) + roll(2 if crit else 1, 6)
            def extra(crit, dealt, t=tgt, f=not first):
                if dealt:
                    s.fill(2 if f else 1)
                    if not t.burning: t.burning_small = True
            hit, crit, dealt = attack(fight, s, tgt, 11, dmg, "slashing", True, adv=True, sneak=3, extra=extra)
            if hit: first = True
            if fight.over(): return
        if not bonus and s.meter >= 6: s.unleash(fight, True)
    def on_miss(s, *a): pass
    def on_hit(s, *a): pass

MAKERS["Crane2"] = Crane2; DANGER["Crane2"] = 2

if __name__ == "__main__":
    n = int(sys.argv[1]); base = ["Smasher","Guts","Jin","Itachi","GS","GuyC","Slayer","Crane"]
    print("Retuned Crane, 1v1 (wins %, avg rounds)")
    for b in base:
        w = Counter(); rr = 0
        for _ in range(n):
            res, r = Fight([[Crane2()], [MAKERS[b]()]]).run(); w[res] += 1; rr += r
        lab = {"GuyC": "Guy", "Crane": "old Crane"}.get(b, b)
        print(f"  vs {lab:9s} {100*w[0]/n:5.1f}%   avg {rr/n:.1f} rounds")
    names = ["Crane2","Smasher","Guts","Jin","Itachi","GS","GuyC","Slayer"]; w = Counter()
    for _ in range(n):
        res, r = Fight([[MAKERS[x]()] for x in names]).run(); w[names[res] if res is not None else "none"] += 1
    print("Eight-way FFA:", {({"GuyC":"Guy","Crane2":"Crane"}).get(k,k): f"{100*v/n:.0f}%" for k, v in sorted(w.items(), key=lambda kv: -kv[1])})
    w = Counter()
    for _ in range(n):
        res, r = Fight([[Crane2(), Jin()], [Guts(), GS()]]).run(); w[res] += 1
    print(f"Crane + Jin vs Guts + Goblin Slayer: {100*w[0]/n:.1f}%")
