"""Run n fights between two fighters, keep a turn-by-turn log of each, and print the most dramatic one:
the raw material for the stories in this folder.

    python stories/fight_log.py beast might-guy 400
    python stories/fight_log.py spike arthur 2000 Spike     # only fights Spike won

"Dramatic" scores long fights, Relentless Rage-style comebacks, Night Guy, and a winner left low.
It wraps the engine's attack() and take() to record them; the fights themselves are the arena's own."""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sim.engine as E
from sim.roster import make, Fight
import importlib, pkgutil, sim.fighters
MODS = [importlib.import_module('sim.fighters.' + m.name) for m in pkgutil.iter_modules(sim.fighters.__path__)]

LOG = []
orig_attack = E.attack
def logged_attack(fight, att, tgt, bonus, dmg_fn, dtype, melee=True, **kw):
    res = orig_attack(fight, att, tgt, bonus, dmg_fn, dtype, melee, **kw)
    hit, crit, dealt = res
    LOG.append(("atk", att.name, tgt.name, dtype, hit, crit, dealt, tgt.hp))
    return res
for m in [E] + MODS:
    if hasattr(m, 'attack'): m.attack = logged_attack

orig_take = E.Combatant.take
def logged_take(self, dmg, dtype, src, **kw):
    r = orig_take(self, dmg, dtype, src, **kw)
    if not kw.get("from_attack"):
        LOG.append(("dmg", src, self.name, dtype, r, self.hp))
    return r
E.Combatant.take = logged_take

def run_one(a, b):
    LOG.clear()
    x, y = make(a), make(b)
    f = Fight([[x], [y]], verbose=True)
    turns = []
    for c in (x, y):
        ot, oz = c.turn, c.on_zero
        def wrapped(fight, c=c, ot=ot):
            start = len(LOG)
            before = dict(gate=getattr(c, "gate", None), raging=getattr(c, "raging", None), hp=c.hp, down=getattr(c, "down", None), fr=[e.frightened for e in (x, y)], st=snap((x, y)))
            ot(fight)
            after = dict(gate=getattr(c, "gate", None), raging=getattr(c, "raging", None), hp=c.hp, down=getattr(c, "down", None), fr=[e.frightened for e in (x, y)], st=snap((x, y)))
            turns.append((fight.round, c.name, before, after, LOG[start:], x.hp, y.hp))
        c.turn = wrapped
        def zero(src, crit, c=c, oz=oz):
            LOG.append(("zero", c.name, src))
            oz(src, crit)
            LOG.append(("after_zero", c.name, c.hp, c.out, getattr(c, "down", None)))
        c.on_zero = zero
        om = c.on_massive
        def massive(src, c=c, om=om):
            LOG.append(("massive", c.name, src))
            om(src)
        c.on_massive = massive
    w, r = f.run()
    return w, r, turns, (x, y)

a, b = sys.argv[1], sys.argv[2]
n = int(sys.argv[3]) if len(sys.argv) > 3 else 400
want = sys.argv[4] if len(sys.argv) > 4 else None
# resources and conditions worth narrating: a change in any of them shows up in the log
WATCH = ("luck", "nine", "deadeye", "boxes", "sw", "wob", "snake", "miracle", "surges", "paralyzed", "prone", "hades", "fairies", "second_heart")
def snap(cs): return [{k: getattr(c, k) for k in WATCH if hasattr(c, k)} for c in cs]
best = None
for i in range(n):
    w, r, turns, (x, y) = run_one(a, b)
    if want and (w is None or [x, y][w].name != want): continue
    night = any(e[0] == "dmg" and e[1] == "Night Guy" for t in turns for e in t[4])
    relentless = sum(1 for t in turns for e in t[4] if e[0] == "after_zero" and not e[3])
    close = 0 if w is None else -[x, y][w].hp / 20
    score = r + 6 * night + 4 * relentless + close + random.random()
    if best is None or score > best[0]:
        best = (score, w, r, turns, x.name, y.name)
if best is None: sys.exit(f"no fight in {n} went to {want}")
score, w, r, turns, xn, yn = best
print(f"winner: {[xn, yn][w] if w is not None else 'draw'} in {r} rounds")
for rnd, name, before, after, events, hx, hy in turns:
    bits = []
    if before["gate"] != after["gate"] and after["gate"] is not None: bits.append(f"gates {before['gate']}->{after['gate']}")
    if before["raging"] != after["raging"]: bits.append("RAGE")
    for who, b0, b1 in zip((xn, yn), before['fr'], after['fr']):
        if b0 != b1: bits.append(f"<{who} {'FRIGHTENED' if b1 else 'no longer frightened'}>")
    for who, s0, s1 in zip((xn, yn), before['st'], after['st']):
        ch = [f"{k} {s0[k]}->{s1[k]}" for k in s0 if s0[k] != s1[k]]
        if ch: bits.append(f"{{{who}: {', '.join(ch)}}}")
    for e in events:
        if e[0] == "atk":
            _, at, tg, dt, hit, crit, dealt, thp = e
            bits.append(f"{'CRIT' if crit else 'hit' if hit else 'miss'}{'' if not hit else f' {dealt} {dt}'}")
        elif e[0] == "dmg":
            bits.append(f"[{e[1]} -> {e[2]}: {e[4]} {e[3]}]")
        elif e[0] == "massive":
            bits.append(f"<{e[1]} KILLED OUTRIGHT by {e[2]}>")
        elif e[0] == "zero":
            bits.append(f"<{e[1]} DROPS TO 0>")
        elif e[0] == "after_zero":
            bits.append(f"<{e[1]} {'OUT' if e[3] else ('DOWN' if e[4] else f'back up at {e[2]}')}>")
    print(f"R{rnd} {name:5s} | {' '.join(bits)}  || {xn} {hx}  {yn} {hy}")
