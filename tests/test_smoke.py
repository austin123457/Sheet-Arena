import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sim"))
from roster import make, Fight, MAKERS

def test_every_fighter_builds():
    for k in ("gs","guts","crane","itachi","smasher","jin","guy","slayer","link","beast","anderson","arthur","spike"):
        assert make(k).hp > 0

def test_a_fight_finishes():
    res, r = Fight([[make("guts")], [make("gs")]]).run()
    assert res in (0, 1) and 1 <= r <= 40

def test_link_is_immune_under_nayrus_love():
    L = make("link"); L.nayru = 5
    assert L.take(50, "slashing", "test", from_attack=True, melee=True) == 0
