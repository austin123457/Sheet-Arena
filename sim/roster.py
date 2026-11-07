import os, sys
_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path: sys.path.insert(0, _here)
from spike_arena import *          # noqa: pulls the whole chain
from spike_arena import MAKERS, DANGER, Fight, Counter, d, roll, d20

NAMES = {
    "gs": "GS", "goblin-slayer": "GS", "guts": "Guts", "crane": "Crane2", "crane-old": "Crane", "itachi": "Itachi",
    "smasher": "Smasher", "jin": "Jin", "guy": "GuyC", "guy-mine": "Guy", "guy-caleb": "Guy2",
    "slayer": "Slayer", "doomslayer": "Slayer", "link": "Link", "hero-of-time": "Link", "beast": "Beast",
    "battle-beast": "Beast", "anderson": "Anderson", "arthur": "Arthur", "spike": "Spike",
}
def make(key):
    k = key.lower().strip()
    name = NAMES.get(k, key)
    if name not in MAKERS: raise SystemExit(f"unknown fighter {key!r}; try: {', '.join(sorted(NAMES))}")
    return MAKERS[name]()
