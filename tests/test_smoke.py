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


def test_a_shadow_clone_never_wins_the_fight_for_a_dead_itachi():
    from sim.fighters.itachi import ShadowClone
    it, gs = make("itachi"), make("gs")
    f = Fight([[it], [gs]]); clone = ShadowClone(it); f.add(clone, it.team)
    it.out = True
    assert not clone.alive() and f.over()


def test_battle_beast_shrugs_off_charm_and_fear_only_while_raging():
    b = make("beast")
    assert not b.charm_immune and not b.fright_immune
    b.raging = True
    assert b.charm_immune and b.fright_immune


def test_hypnotic_pattern_breaks_on_any_damage():
    g = make("guts"); g.charmed = {"mode": "pattern", "by": None, "dc": 19}
    g.take(5, "fire", "test")
    assert g.charmed is None


def test_mangekyo_costs_exhaustion():
    it = make("itachi"); it.exhaust(2)
    assert it.saves["Wis"] == 7 - 4 and it.atk() == 11 - 4


def test_talion_loses_might_when_hit():
    t = make("talion"); t.might = 5
    t.take(10, "slashing", "test", from_attack=True)
    assert t.might == 4


def test_freeflow_counter_turns_a_melee_hit_into_a_miss_but_not_a_crit():
    t, g = make("talion"), make("guts")
    f = Fight([[t], [g]])
    assert t.defend_ac(g, 30, True, False) is None and t.might == 1
    assert t.defend_ac(g, 30, True, True) == 0


def test_cranes_perfect_block_only_when_six_more_ac_would_stop_it():
    c, g = make("crane"), make("guts")
    assert c.defend_ac(g, 25, True, False) == 0 and c.reaction
    assert c.defend_ac(g, 18, True, False) == 6 and not c.reaction


def test_v_picks_his_operating_system_before_the_fight():
    v, j = make("v"), make("jin")
    Fight([[v], [j]]).run()
    assert v.os == "deck"
    v, s = make("v"), make("smasher")
    f = Fight([[v], [s]]); v.before_first_round(f)
    assert v.os == "sandy" and v.scalpel


def test_twenty_lightning_shorts_smasher_out():
    s = make("smasher"); Fight([[s], [make("v")]])
    s.take(25, "lightning", "test")
    assert s.shorted and not s.reaction and not s.overclocked()


def test_kratos_can_finish_a_downed_anderson_the_way_his_sheet_allows():
    k, a = make("kratos"), make("anderson")
    f = Fight([[k], [a]]); a.take(200, "slashing", "test"); a.take(200, "slashing", "test")
    assert a.down and not a.out
    for _ in range(40):
        k.tear_heart(f, a)
        if a.out: break
    assert a.out


def test_madara_phase_one_cant_be_killed_only_sealed():
    m = make("madara"); f = Fight([[m], [make("itachi")]])
    m.take(5000, "force", "test")
    assert m.phase == 2 and m.alive() and m.hp == 900
    m2 = make("madara"); Fight([[m2], [make("itachi")]]); m2.seal(f)
    assert m2.sealed and not m2.alive()


def test_the_jinchuriki_ignores_small_hits_spells_and_instant_kills():
    m = make("madara"); Fight([[m], [make("guy")]]); m.phase_two()
    assert m.take(99, "bludgeoning", "test") == 0 and m.take(150, "force", "Night Guy") == 150
    assert m.save("Wis", 30, spell=True) and m.negates_spells()
    m.out = True
    assert m.alive()
