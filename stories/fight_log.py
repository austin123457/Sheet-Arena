"""Run n fights between two fighters, keep a turn-by-turn log of each, and print the most dramatic one:
the raw material for the stories in this folder.

    python stories/fight_log.py beast might-guy 400
    python stories/fight_log.py spike arthur 2000 Spike     # only fights Spike won
    python stories/fight_log.py spike+arthur smasher 400     # teams: join names with +

"Dramatic" scores long fights, Relentless Rage-style comebacks, Night Guy, and a winner left low.
It wraps the engine's attack() and take() to record them; the fights themselves are the arena's own.
A Reaction queued with fight.after_turn (a Riposte, Dark Link's Answer) lands once the turn is over:
it's printed on the turn that drew it, after "then:". Anything that happens before the first turn (Jin's
Standoff) is printed as R0, under the name of whoever attacked."""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sim.engine as E
from sim.roster import make, Fight
import importlib, pkgutil, sim.fighters
MODS = [importlib.import_module('sim.fighters.' + m.name) for m in pkgutil.iter_modules(sim.fighters.__path__)]

LOG = []; DEPTH = [0]
orig_attack = E.attack
def logged_attack(fight, att, tgt, bonus, dmg_fn, dtype, melee=True, **kw):
    DEPTH[0] += 1
    try: res = orig_attack(fight, att, tgt, bonus, dmg_fn, dtype, melee, **kw)
    finally: DEPTH[0] -= 1
    hit, crit, dealt = res
    LOG.append(("atk", att.name, tgt.name, dtype, hit, crit, dealt, tgt.hp))
    return res
for m in [E] + MODS:
    if hasattr(m, 'attack'): m.attack = logged_attack

orig_take = E.Combatant.take
def logged_take(self, dmg, dtype, src, **kw):
    r = orig_take(self, dmg, dtype, src, **kw)
    if not kw.get("from_attack") or not DEPTH[0]:      # a hit dealt outside an attack roll (Peerless Aim) is logged too
        LOG.append(("dmg", src, self.name, dtype, r, self.hp))
    return r
E.Combatant.take = logged_take

# resources and conditions worth narrating: a change in any of them shows up in the log
WATCH = ("luck", "nine", "deadeye", "boxes", "sw", "wob", "snake", "miracle", "surges", "paralyzed", "prone",
         "hades", "fairies", "second_heart", "frightened", "raging", "gate", "sandy", "shorted", "matrix",
         "nayru", "red", "blue", "last_stand", "iron_n", "bfg", "crucible", "blood", "hammer", "rbd", "legacy", "runic", "valor",
         "haste", "nail", "times_down", "down", "hold_used", "death_fail", "dice", "one_cut", "nuts", "triforce", "clanks", "translucent",
         "resolve", "fs", "recover",
         "decoys", "invisible", "items", "stored", "shield_up", "flash", "fate")


def run_one(a, b):
    LOG.clear()
    A, B = [make(k) for k in a.split("+")], [make(k) for k in b.split("+")]
    everyone = A + B
    f = Fight([A, B], verbose=True)
    on = f.note
    def note(text, on=on): LOG.append(("note", text)); on(text)
    f.note = note
    turns = []; seen = [0]
    def snap(): return [{k: getattr(c, k) for k in WATCH if hasattr(c, k)} for c in everyone]
    def late():        # whatever happened since the last turn ended belongs to that turn
        if not turns and LOG:       # before anyone's first turn: the Standoff
            s = snap(); who = next((e[1] for e in LOG if e[0] == "atk"), "start")
            turns.append((0, who, s, s, LOG[:], [(e.name, e.hp + e.thp) for e in everyone]))
        elif turns and len(LOG) > seen[0]:
            rnd, name, before, _, events, _ = turns[-1]
            turns[-1] = (rnd, name, before, snap(), events + [("then",)] + LOG[seen[0]:], [(e.name, e.hp + e.thp) for e in everyone])
        seen[0] = len(LOG)
    for c in everyone:
        ot, oz, om = c.turn, c.on_zero, c.on_massive
        def wrapped(fight, c=c, ot=ot):
            late()
            start, before = len(LOG), snap()
            ot(fight)
            turns.append((fight.round, c.name, before, snap(), LOG[start:], [(e.name, e.hp + e.thp) for e in everyone]))
            seen[0] = len(LOG)
        c.turn = wrapped
        def zero(src, crit, c=c, oz=oz):
            LOG.append(("zero", c.name, src))
            oz(src, crit)
            LOG.append(("after_zero", c.name, c.hp, c.out, getattr(c, "down", None)))
        c.on_zero = zero
        def massive(src, c=c, om=om):
            LOG.append(("massive", c.name, src))
            om(src)
        c.on_massive = massive
    w, r = f.run()
    late()
    return w, r, turns, (A, B)


a, b = sys.argv[1], sys.argv[2]
n = int(sys.argv[3]) if len(sys.argv) > 3 else 400
want = sys.argv[4] if len(sys.argv) > 4 else None      # a fighter's name: keep only fights their side won
team = len(a.split("+")) + len(b.split("+")) > 2
best = None
for i in range(n):
    w, r, turns, (A, B) = run_one(a, b)
    if want and (w is None or want not in [c.name for c in (A, B)[w]]): continue
    night = any(e[0] == "dmg" and e[1] == "Night Guy" for t in turns for e in t[4])
    relentless = sum(1 for t in turns for e in t[4] if e[0] == "after_zero" and not e[3])
    fallen = 0 if w is None else sum(c.out for c in (A, B)[w])        # a winner who lost someone on the way
    close = 0 if w is None else -sum(c.hp for c in (A, B)[w]) / 20
    score = r + 6 * night + 4 * relentless + 5 * fallen + close + random.random()
    if best is None or score > best[0]:
        best = (score, w, r, turns, (A, B))
if best is None: sys.exit(f"no fight in {n} went to {want}")
score, w, r, turns, (A, B) = best
names = [c.name for c in A + B]
print(f"winner: {' + '.join(c.name for c in (A, B)[w]) if w is not None else 'draw'} in {r} rounds")
for rnd, name, before, after, events, hps in turns:
    bits = []
    for who, s0, s1 in zip(names, before, after):
        ch = [f"{k} {s0[k]}->{s1[k]}" for k in s0 if s0[k] != s1[k]]
        if ch: bits.append(f"{{{who}: {', '.join(ch)}}}")
    for e in events:
        if e[0] == "atk":
            _, at, tg, dt, hit, crit, dealt, thp = e
            bits.append(f"{'CRIT' if crit else 'hit' if hit else 'miss'}{'' if not hit else f' {dealt} {dt}'}{f' >{tg}' if team else ''}{f' ({at})' if team and at != name else ''}")
        elif e[0] == "dmg":
            bits.append(f"[{e[1]} -> {e[2]}: {e[4]} {e[3]}]")
        elif e[0] == "note":
            bits.append(f"** {e[1]} **")
        elif e[0] == "then":
            bits.append("then:")
        elif e[0] == "massive":
            bits.append(f"<{e[1]} KILLED OUTRIGHT by {e[2]}>")
        elif e[0] == "zero":
            bits.append(f"<{e[1]} DROPS TO 0>")
        elif e[0] == "after_zero":
            bits.append(f"<{e[1]} {'OUT' if e[3] else ('DOWN' if e[4] else f'back up at {e[2]}')}>")
    print(f"R{rnd} {name:7s} | {' '.join(bits)}  || " + "  ".join(f"{n_} {h}" for n_, h in hps))
