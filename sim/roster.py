"""The roster: command-line names -> fighters."""
from collections import Counter  # noqa: F401  (battle.py imports it from here)

from .engine import Fight, d, d20, roll  # noqa: F401
from .fighters import ALL

MAKERS = {cls.name: cls for cls in ALL}
DANGER = {cls.name: cls.danger for cls in ALL}

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
