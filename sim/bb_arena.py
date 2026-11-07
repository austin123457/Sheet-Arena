from link_arena import *
import link_arena

class BattleBeast(C):
    def __init__(s):
        super().__init__("Beast"); s.hp = s.maxhp = 265; s.ac = 19
        s.saves = dict(Str=14, Dex=0, Con=12, Int=0, Wis=1, Cha=-1); s.indom_bonus = 0
        s.raging = False; s.rel_dc = 10; s.hew = False; s.worthy = None; s.melee = True; s.presence = True
        s.charm_immune = True; s.fright_immune = True; s.glorious = True
    def init(s): return d20(adv=True) + 0
    def ac_now(s): return s.ac
    def save_adv(s, ab, spell): return ab == "Dex" or (ab == "Str" and s.raging)
    def save(s, ab, dc, spell=False, source=None):
        if ab == "Str": return True if 27 >= dc else super().save(ab, dc, spell, source)
        return super().save(ab, dc, spell, source)
    def modify_incoming(s, dmg, dtype, src, from_attack, melee, ignore_res):
        if s.raging and dtype in ("slashing", "piercing", "bludgeoning") and not ignore_res: return dmg // 2
        if dtype == "cold": return dmg // 2
        return dmg
    def on_zero(s, src, crit):
        if s.raging and d(20) + 12 >= s.rel_dc: s.rel_dc += 5; s.hp = 40; return
        s.rel_dc += 5; s.out = True
    def retaliate(s, fight, att):
        if s.reaction and att.alive() and s.raging:
            s.reaction = False; s.swing(fight, att, adv=True, frenzy=False, savage=True, can_hew=False)
    def swing(s, fight, tgt, adv, frenzy, savage, brutal=False, can_hew=True):
        def dmg(crit):
            n = 8 if crit else 4
            w = roll(n, 6)
            if savage: w = max(w, roll(n, 6))
            v = w + (20 if s.raging else 16)
            if frenzy: v += roll(8 if crit else 4, 6)
            if brutal: v += roll(4 if crit else 2, 10)
            return v
        cr = 19 if (tgt is s.worthy) else 20
        hit, crit, dealt = attack(fight, s, tgt, 16, dmg, "slashing", True, adv=adv, crit_range=cr, ignore_res=True)
        if not hit and not tgt.out: tgt.take(8, "slashing", "Graze", ignore_res=True)   # Graze
        if crit and can_hew: s.hew = True
        return hit
    def turn(s, fight):
        tgt = fight.pick_target(s)
        if not tgt: return
        bonus = False
        if not s.raging:
            s.raging = True; s.reckless = True; bonus = True
            s.worthy = max(fight.enemies(s), key=lambda e: DANGER.get(e.name, 0))
        elif s.presence and not getattr(tgt, "fright_immune", False) and tgt.name not in ("Guts","Smasher","Link","Slayer","GuyC"):
            s.presence = False; bonus = True
            if not tgt.save("Wis", 22): tgt.frightened = True
        if s.worthy is not None and not s.worthy.out: tgt = s.worthy
        first = False
        for i in range(2):
            if tgt.out: tgt = fight.pick_target(s)
            if not tgt: break
            brutal = (i == 1) and not s.poisoned and not s.disadv_attacks
            hit = s.swing(fight, tgt, adv=not brutal, frenzy=not first, savage=not first, brutal=brutal)
            if hit: first = True
            if fight.over(): return
        if not bonus and s.hew and tgt and not tgt.out: s.hew = False; s.swing(fight, tgt, True, False, False, can_hew=False)
        s.hew = False
    def on_miss(s, *a): pass
    def on_hit(s, *a): pass

# Guts's retaliation hook in Fight.run only looks for name "Guts"; give the Beast the same hook
_orig_run = Fight.run
def run(self):
    for c in self.all:
        if c.name == "Beast":
            c.name = "Guts"; c._beast = True
    res = _orig_run(self)
    for c in self.all:
        if getattr(c, "_beast", False): c.name = "Beast"
    return res
Fight.run = run
MAKERS["Beast"] = BattleBeast; DANGER["Beast"] = 6; DANGER["Guts"] = 5

if __name__ == "__main__":
    n = int(sys.argv[1]); base = ["Smasher","Guts","Jin","Itachi","GS","Crane2","GuyC","Slayer","Link"]
    print("Battle Beast, 1v1 (wins %, avg rounds)")
    for b in base:
        w = Counter(); rr = 0
        for _ in range(n):
            res, r = Fight([[BattleBeast()], [MAKERS[b]()]]).run(); w[res] += 1; rr += r
        print(f"  vs {({'Crane2':'Crane','GuyC':'Guy'}).get(b,b):8s} {100*w[0]/n:5.1f}%   avg {rr/n:.1f} rounds")
    names = ["Beast"] + base; w = Counter()
    for _ in range(n):
        teams = [[MAKERS[x]()] for x in names]
        res, r = Fight(teams).run(); w[names[res] if res is not None else "none"] += 1
    print("Ten-way FFA:", {({"GuyC":"Guy","Crane2":"Crane"}).get(k,k): f"{100*v/n:.0f}%" for k, v in sorted(w.items(), key=lambda kv: -kv[1])})
    w = Counter()
    for _ in range(n):
        res, r = Fight([[BattleBeast(), Smasher()], [Slayer(), Link()]]).run(); w[res] += 1
    print(f"Battle Beast + Smasher vs Slayer + Link: {100*w[0]/n:.1f}%")
    w = Counter()
    for _ in range(n):
        res, r = Fight([[BattleBeast(), Guts()], [Jin(), GuyC()]]).run(); w[res] += 1
    print(f"Battle Beast + Guts vs Jin + Guy: {100*w[0]/n:.1f}%")
