"""One file per sheet. To add a fighter: write a Combatant subclass in its own file, import it
here, add it to ALL, and give it a command-line name in roster.py."""
from .anderson import Anderson
from .arthur import Arthur
from .battle_beast import BattleBeast
from .crane import Crane
from .crane_beast import CraneBeast
from .goblin_slayer import GoblinSlayer
from .guts import Guts
from .guy import Guy
from .guy_caleb import GuyCaleb
from .guy_canon import GuyCanon
from .itachi import Itachi
from .jin import Jin
from .link import Link
from .slayer import Slayer
from .smasher import Smasher
from .spike import Spike

ALL = [GoblinSlayer, Guts, Crane, Itachi, Smasher, Jin, Guy, GuyCaleb, GuyCanon, Slayer, CraneBeast, Link,
       BattleBeast, Anderson, Arthur, Spike]
