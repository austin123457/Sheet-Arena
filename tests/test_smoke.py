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


def test_evasion_takes_nothing_on_a_save_and_half_on_a_failure():
    spike, guts = make("spike"), make("guts")
    assert (spike.dex_damage(True, 40), spike.dex_damage(False, 40)) == (0, 20)
    assert (guts.dex_damage(True, 40), guts.dex_damage(False, 40)) == (20, 40)
    spike.paralyzed = True
    assert spike.dex_damage(False, 40) == 40


def test_anderson_gets_up_unless_one_blow_takes_his_whole_pool():
    a = make("anderson"); a.take(200, "slashing", "test"); a.take(200, "slashing", "test")
    assert a.down and not a.out
    a.take(250, "slashing", "test")
    assert not a.out
    a = make("anderson"); a.take(284, "slashing", "test")
    assert a.out


def test_fire_on_a_downed_anderson_keeps_him_down():
    a = make("anderson"); a.take(200, "slashing", "test"); a.take(200, "slashing", "test")
    a.take(25, "fire", "test")
    assert a.radiant_taken >= 20


def test_izanami_counts_separate_turns():
    it, gs = make("itachi"), make("gs")
    f = Fight([[it], [gs]])
    for rnd in (1, 1, 2):
        f.round = rnd; it.struck_on.setdefault(gs, set()).add(rnd)
    assert it.turns_struck_by(gs) == 2
