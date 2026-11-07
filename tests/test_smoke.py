import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from sim.engine import ROUND_CAP
from sim.roster import make, Fight, MAKERS, NAMES


def test_every_fighter_builds():
    for k in NAMES:
        assert make(k).hp > 0


def test_every_sheet_has_a_command_line_name():
    assert set(NAMES.values()) == set(MAKERS)


def test_a_fight_finishes():
    res, r = Fight([[make("guts")], [make("gs")]]).run()
    assert res in (0, 1) and 1 <= r <= ROUND_CAP


def test_link_is_immune_under_nayrus_love():
    L = make("link"); L.nayru = 5
    assert L.take(50, "slashing", "test", from_attack=True, melee=True) == 0


def test_night_guy_and_the_crucible_go_through_nayrus_love():
    L = make("link"); L.nayru = 5; L.reaction = False
    assert L.take(50, "force", "Night Guy", ignore_res=True, ignore_imm=True) == 50


def test_the_seventh_gate_gives_attackers_disadvantage():
    g = make("guy"); g.gate = 7
    assert g.incoming_attack(make("gs"), 10, False, False) == (False, True)
