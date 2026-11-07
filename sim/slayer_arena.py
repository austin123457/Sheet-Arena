from guy_canon import *
import guy_canon

class Slayer(C):
    def __init__(s):
        super().__init__("Slayer"); s.hp = s.maxhp = 298; s.thp = 60; s.ac = 20
        s.saves = dict(Str=13, Dex=4, Con=12, Int=-1, Wis=1, Cha=-1); s.indom_bonus = 0
        s.raging = False; s.rages = 5; s.bfg = 3; s.crucible = 3; s.blood = 2; s.hammer = 1; s.surge = 1; s.sw = 3
        s.rel_dc = 10; s.ff = True; s.melee = True; s.ice_cd = 0; s.flame_cd = 0; s.rbd = False; s.death_fail = 0
        s.fright_immune = False
    def init(s): return d20(adv=True) + 4
    def ac_now(s): return s.ac
    def save_adv(s, ab, spell): return ab == "Dex"
    def save(s, ab, dc, spell=False, source=None):
        ok = super().save(ab, dc, spell, source)
        if not ok and s.ff and s.raging:
            s.ff = False; ok = d20(adv=s.save_adv(ab, spell)) + s.saves[ab] + 3 >= dc
        return ok
    def modify_incoming(s, dmg, dtype, src, from_attack, melee, ignore_res):
        if not ignore_res and ((s.raging and dtype in ("slashing", "piercing", "bludgeoning")) or dtype in ("fire", "radiant")): dmg //= 2
        if from_attack and s.reaction:
            s.reaction = False; dmg = max(0, dmg - (d(10) + 13))
        return dmg
    def on_zero(s, src, crit):
        if s.rbd:
            s.death_fail += 2 if crit else 1
            if s.death_fail >= 3: s.out = True
            return
        if s.raging and d(20) + 12 >= s.rel_dc: s.rel_dc += 5; s.hp = 28; return
        if s.raging: s.rel_dc += 5; s.rbd = True; s.hp = 0; return
        s.out = True
    def shoot(s, fight, tgt, fury):
        def dmg(crit, f=fury):
            w = roll(8 if crit else 4, 8); w = max(w, roll(8 if crit else 4, 8))
            return w + (roll(2 if crit else 1, 6) + 7 if f else 0)
        return attack(fight, s, tgt, 12, dmg, "piercing", melee=False, crit_range=19)
    def turn(s, fight):
        if s.rbd:
            r = d20()
            if r == 20: s.hp = 1; s.rbd = False; s.death_fail = 0
            elif r < 10:
                s.death_fail += 1
                if s.death_fail >= 3: s.out = True; return
        enemies = fight.enemies(s)
        if not enemies: return
        tgt = fight.pick_target(s)
        if s.ice_cd: s.ice_cd -= 1
        if s.flame_cd: s.flame_cd -= 1
        bonus_used = False
        if not s.raging: s.raging = True; s.rages -= 1; s.reckless = True; bonus_used = True
        actions = 1 + (1 if s.surge else 0); s.surge = 0
        fury = True
        for a in range(actions):
            if tgt is None or tgt.out: tgt = fight.pick_target(s)
            if not tgt: return
            cur = tgt.hp + tgt.thp
            if s.hammer and len([e for e in enemies if e.melee and not e.out]) >= 2:
                s.hammer = 0
                for e in enemies:
                    if e.out or not e.melee: continue
                    e.take(roll(6, 10), "force", "Hammer")
                    if not e.save("Con", 19) and e.name not in ("Guts",) and not getattr(e, "stun_immune", False): e.paralyzed = True; e.stun_until = fight.round
            elif s.bfg > 0 and (len(enemies) >= 2 or cur > 150):
                s.bfg -= 1
                for e in list(enemies):
                    if e.out: continue
                    dmg = roll(20, 10)
                    if e.save("Dex", 18):
                        if e.name in ("Jin", "Crane", "Guy", "Guy2", "GuyC"): continue
                        dmg //= 2
                    e.take(dmg, "force", "BFG")
            elif s.crucible > 0 and cur <= 240:
                s.crucible -= 1
                frozen = tgt.paralyzed
                def dmg(crit): return roll(24 if crit else 12, 12) + 7 + 3
                def extra(crit, dealt, t=tgt):
                    if dealt and not t.out and (t.hp + t.thp) <= 150: t.out = True; fight.note("Crucible")
                import link_arena as _la
                _la.PIERCE_IMMUNITY = True
                try:
                    hit, crit, dealt = attack(fight, s, tgt, 13, dmg, "slashing", True, adv=True, crit_range=1 if frozen else 19, extra=extra, ignore_res=True)
                finally:
                    _la.PIERCE_IMMUNITY = False
                fury = False
            else:
                for i in range(2):
                    if tgt.out: tgt = fight.pick_target(s)
                    if not tgt: return
                    if s.blood > 0 and i == 0 and tgt.paralyzed:
                        s.blood -= 1
                        attack(fight, s, tgt, 13, (lambda crit: roll(16 if crit else 8, 10) + 10), "bludgeoning", True, adv=True, crit_range=1)
                    else:
                        hit, crit, dealt = s.shoot(fight, tgt, fury)
                        if hit: fury = False
                    if fight.over(): return
            if fight.over(): return
        # bonus action
        if not bonus_used:
            if s.hp <= 150 and s.sw > 0: s.sw -= 1; s.hp = min(s.maxhp, s.hp + d(10) + 6)
            elif s.ice_cd == 0 and tgt and not tgt.out and not tgt.paralyzed and tgt.name not in ("Guts",):
                s.ice_cd = 4
                if not tgt.save("Dex", 18) and not getattr(tgt, "stun_immune", False): tgt.paralyzed = True; tgt.stun_until = fight.round
            elif s.flame_cd == 0 and tgt and not tgt.out:
                s.flame_cd = 3; tgt.take(roll(2, 6), "fire", "Flame Belch"); s.thp = min(60, s.thp + 10)
    def on_miss(s, *a): pass
    def on_hit(s, *a): pass

MAKERS["Slayer"] = Slayer; DANGER["Slayer"] = 8

if __name__ == "__main__":
    n = int(sys.argv[1]); base = ["Smasher","Guts","Jin","Itachi","Crane","GS","GuyC"]
    print("Doom Slayer, 1v1 (wins %, avg rounds)")
    for b in base:
        w = Counter(); rr = 0
        for _ in range(n):
            res, r = Fight([[Slayer()], [MAKERS[b]()]]).run(); w[res] += 1; rr += r
        print(f"  vs {('Guy' if b=='GuyC' else b):8s} {100*w[0]/n:5.1f}%   avg {rr/n:.1f} rounds")
    names = ["Slayer"] + base; w = Counter()
    for _ in range(n):
        res, r = Fight([[MAKERS[x]()] for x in names]).run(); w[names[res] if res is not None else "none"] += 1
    print("Eight-way FFA:", {("Guy" if k=="GuyC" else k): f"{100*v/n:.0f}%" for k, v in sorted(w.items(), key=lambda kv: -kv[1])})
    w = Counter()
    for _ in range(n):
        res, r = Fight([[Slayer()], [MAKERS[x]() for x in base]]).run(); w[res] += 1
    print(f"Slayer alone vs the other seven: {100*w[0]/n:.1f}%")
    w = Counter()
    for _ in range(n):
        res, r = Fight([[Slayer(), GuyC()], [Smasher(), Jin()]]).run(); w[res] += 1
    print(f"Slayer + Guy vs Smasher + Jin: {100*w[0]/n:.1f}%")
