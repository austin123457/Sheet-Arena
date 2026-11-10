"""One file per sheet. To add a fighter: write a Combatant subclass in its own file, import it
here, add it to ALL, and give it a command-line name in roster.py."""
from .anderson import Anderson
from .arthur import Arthur
from .battle_beast import BattleBeast
from .crane import Crane
from .goblin_slayer import GoblinSlayer
from .guts import Guts
from .guy import Guy
from .itachi import Itachi
from .jin import Jin
from .link import Link
from .slayer import Slayer
from .smasher import Smasher
from .spike import Spike
from .talion import Talion
from .v import V
from .kratos import Kratos
from .madara import Madara
from .piccolo import Piccolo
from .musashi import Musashi

ALL = [GoblinSlayer, Guts, Crane, Itachi, Smasher, Jin, Guy, Slayer, Link, BattleBeast, Anderson, Arthur, Spike, Talion, V, Kratos, Musashi, Madara, Piccolo]
