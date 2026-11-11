"""The roster: command-line names -> fighters."""
from collections import Counter  # noqa: F401  (battle.py imports it from here)

from .engine import Fight, d, d20, roll  # noqa: F401
from .fighters import ALL

MAKERS = {cls.name: cls for cls in ALL}
DANGER = {cls.name: cls.danger for cls in ALL}


def _v_with(os):
    from .fighters.v import V
    def make():
        v = V(); v.os = os; return v
    return make


MAKERS["V-sandy"] = _v_with("sandy"); MAKERS["V-deck"] = _v_with("deck")      # V with his OS chosen for him


def _dark_link_in_his_room():
    from .fighters.dark_link import DarkLink
    s = DarkLink(); s.translucent = 10; return s


MAKERS["Dark Link-room"] = _dark_link_in_his_room       # translucent for the first minute, as in the Water Temple

NAMES = {
    "gs": "GS", "goblin-slayer": "GS", "guts": "Guts", "crane": "Crane", "itachi": "Itachi",
    "smasher": "Smasher", "jin": "Jin", "guy": "Guy", "might-guy": "Guy",
    "slayer": "Slayer", "doomslayer": "Slayer", "link": "Link", "hero-of-time": "Link", "beast": "Beast",
    "battle-beast": "Beast", "anderson": "Anderson", "arthur": "Arthur", "spike": "Spike", "talion": "Talion",
    "kratos": "Kratos", "musashi": "Musashi", "miyamoto-musashi": "Musashi", "dark-link": "Dark Link", "darklink": "Dark Link",
    "dark-link-room": "Dark Link-room", "madara": "Madara", "piccolo": "Piccolo", "v": "V", "v-sandy": "V-sandy", "v-deck": "V-deck",
}


def make(key):
    k = key.lower().strip()
    name = NAMES.get(k, key)
    if name not in MAKERS: raise SystemExit(f"unknown fighter {key!r}; try: {', '.join(sorted(NAMES))}")
    return MAKERS[name]()
