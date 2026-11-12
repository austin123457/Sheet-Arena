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


def test_the_exhibition_link_never_casts_nayrus_love():
    for _ in range(20):
        L, s = make("link-no-nayru"), make("dark-link"); f = Fight([[L], [s]])
        ot = L.turn
        def turn(fight, ot=ot):
            ot(fight); assert L.nayru == 0 and L.magic == 12
        L.turn = turn; f.run()
    assert make("link").no_nayru is False


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


def test_musashis_short_sword_guards_against_a_blade_and_not_a_bullet():
    m, a = make("musashi"), make("arthur")
    Fight([[m], [a]]); m.reaction = False
    assert m.defend_ac(a, 21, True, False) == 6 and m.defend_ac(a, 21, False, False) == 0


def test_holding_down_the_pillow_stops_a_blow_only_when_his_cut_lands():
    m, g = make("musashi"), make("gs")
    f = Fight([[m], [g]]); f.actor = g; m.one_cut = False
    stopped = 0
    for _ in range(200):
        m.reaction = True; g.hp = g.maxhp
        r = m.defend_ac(g, 30, True, False)
        assert not m.reaction and r in (None, 6)
        stopped += r is None
    assert 0 < stopped < 200
    m.reaction = True
    assert m.defend_ac(g, 30, True, True) == 6 and m.reaction      # a critical hit can't be stopped


def test_dark_link_mirrors_a_sword_in_one_hand_and_nothing_else():
    s, l, g, a = make("dark-link"), make("link"), make("guts"), make("arthur")
    f = Fight([[s], [l, g, a]]); f.round = 1; f.actor = l
    met = 0
    for _ in range(200):
        s.clanks = 0; s.reaction = False
        s.incoming_attack(l, 18, False, False, True)
        met += s.defend_ac(l, 20, True, False) is None          # a 2 on the hero's die: the shadow needs a 2
        s.incoming_attack(g, 14, False, False, True)
        assert s.defend_ac(g, 34, True, False) == 0             # the Dragonslayer takes both hands
        assert s.defend_ac(a, 34, False, False) == 0            # and a bullet isn't a swing
    assert 150 < met < 200
    s.prone = True
    assert s.defend_ac(l, 20, True, False) == 0


def test_dark_link_staggers_on_the_sixth_clank():
    s, l = make("dark-link"), make("link")
    f = Fight([[s], [l]]); f.round = 1; f.actor = l; s.reaction = False
    while s.staggered is None:
        s.incoming_attack(l, 18, False, False, True); s.defend_ac(l, 20, True, False)
    assert s.is_staggered() and s.clanks == 0
    assert s.incoming_attack(l, 18, False, False, True) == (True, False)
    assert s.defend_ac(l, 20, True, False) == 0
    f.round = 2
    assert not s.is_staggered()


def test_dark_link_sinks_under_the_second_swing_of_a_turn():
    s, g = make("dark-link"), make("guts")
    f = Fight([[s], [g]]); f.round = 1; f.actor = g; s.reaction = False
    assert s.incoming_attack(g, 14, False, False, True) == (False, False)
    s.take(20, "slashing", "Guts", from_attack=True, melee=True)
    assert s.incoming_attack(g, 14, False, False, True) == (False, True) and "Guts" in s.behind
    s.paralyzed = True; s.sunk = None                           # a Deku Nut: it can't sink while it can't move
    s.take(20, "slashing", "Guts", from_attack=True, melee=True)
    assert s.sunk is None


def test_dark_link_never_attacks_while_translucent():
    s, g = make("dark-link-room"), make("gs")
    f = Fight([[s], [g]]); f.round = 1; f.actor = s
    s.turn(f)
    assert s.translucent == 9 and g.hp == g.maxhp and s.surges == 2
    s.on_missed(f, g, True)
    assert s.reaction and not f.pending


def test_the_shadow_is_evil_has_no_pack_and_rolls_from_arrows():
    s, a = make("dark-link"), make("arthur")
    Fight([[s], [a]])
    assert s.evil and not s.humanoid and s.maxhp == make("link").maxhp
    assert not hasattr(s, "fairies") and not hasattr(s, "magic") and not hasattr(s, "sw")
    assert s.incoming_attack(a, 12, False, False, False) == (False, True)
    assert s.save_adv("Dex", False) and not s.save_adv("Dex", True)


def test_a_mirror_makes_kratos_and_v_change_weapons():
    k, v, s = make("kratos"), make("v"), make("dark-link")
    f = Fight([[s], [k, v]])
    k.before_first_round(f); v.before_first_round(f)
    assert k.blades and v.scalpel and not k.one_handed and not v.one_handed


def test_madara_phase_one_cant_be_killed_only_sealed():
    m = make("madara"); f = Fight([[m], [make("itachi")]])
    m.take(5000, "force", "test")
    assert m.phase == 2 and m.alive() and m.hp == 246
    m2 = make("madara"); Fight([[m2], [make("itachi")]]); m2.seal(f)
    assert m2.sealed and not m2.alive()


def test_the_jinchuriki_ignores_small_hits_spells_and_instant_kills():
    m = make("madara"); Fight([[m], [make("guy")]]); m.phase_two()
    assert m.take(99, "bludgeoning", "test") == 0 and m.take(150, "force", "Night Guy", exp=2) == 150
    assert m.save("Wis", 30, spell=True) and m.negates_spells()
    m.out = True
    assert m.alive()


def test_piccolo_blows_up_the_moon_madara_needs():
    p, m = make("piccolo"), make("madara")
    f = Fight([[p], [m]]); m.phase_two(); p.weights = False
    p.turn(f)
    assert not f.moon


def test_raid_against_raid_has_no_legendary_resistance():
    p, m = make("piccolo"), make("madara")
    f = Fight([[p], [m]]); f.run()
    assert p.legendary_resist == 0 and m.legendary_resist == 0


def test_a_genjutsu_costs_one_turn():
    g = make("guts"); g.charmed = {"mode": "genjutsu", "by": None, "dc": 27}
    g.take(50, "slashing", "test")
    assert g.charmed is not None and g.incapacitated()
    g.end_turn(None)
    assert g.charmed is None


def test_exponents_convert_damage_between_tiers():
    p, m, g = make("piccolo"), make("madara"), make("guts")
    Fight([[p], [m, g]]); m.phase_two()
    assert p.take(90, "slashing", "Guts") == 0          # 0.9 of a moon-unit point
    assert p.take(150, "slashing", "Guts") == 1         # a BFG-sized hit: 1.5, rounded down
    assert p.take(9, "force", "Madara") == 9            # same exponent: ordinary 5e
    assert g.take(2, "force", "Piccolo") == 200         # a moon-unit 2 on a ladder body


def test_massive_damage_kills_outright_but_a_fairy_still_answers_it():
    g, l, y = make("guts"), make("link"), make("might-guy")
    Fight([[y], [g, l]])
    g.raging = True; g.hp = 10
    g.take(600, "force", "Guy", ignore_res=True)       # 590 past 0 against 236 max: no Relentless Rage
    assert g.out and not g.down
    g2 = make("guts"); Fight([[y], [g2]]); g2.raging = True; g2.hp = 10
    g2.take(40, "force", "Guy", ignore_res=True)        # 30 past 0: Relentless Rage gets its save
    assert g2.down or g2.hp == 24
    f = l.fairies; l.take(5000, "force", "Guy", ignore_res=True, ignore_imm=True)
    assert l.alive() and l.fairies == f - 1 and l.hp == 90
    k, v = make("kratos"), make("v-sandy"); Fight([[y], [k, v]])
    k.take(9000, "force", "Guy", ignore_res=True); v.take(9000, "force", "Guy", ignore_res=True)
    assert k.alive() and k.hp == 1 and not v.alive()   # out of Hades; a second heart doesn't help


def test_jack_cheats_death_once_for_each_thing_he_built():
    j = make("jack"); Fight([[j], [make("arthur")]])
    for n in range(6):
        j.thp = 0; j.take(j.hp, "piercing", "test")
        assert j.alive() and j.hp == 20 and len(j.items) == 5 - n
    assert j.ac == 13 and j.atk() == 11 and j.saves["Con"] == 8      # the bracers, the ring, the cloak and the laser are gone
    j.take(20, "piercing", "test")
    assert not j.alive()


def test_a_digi_jack_takes_the_hit_and_one_comes_back_each_turn():
    j, a = make("jack"), make("arthur"); f = Fight([[j], [a]])
    j.before_first_round(f)
    assert j.decoys == 2
    j.reaction = False; j.fate = False                              # no Shield, no Boon of Fate: only the decoys
    seen = [j.defend_ac(a, 30, False, False) for i in range(40)]
    assert seen.count(None) == 2 and j.decoys == 0                  # two pop, and after that it's him
    j.start_turn()
    assert j.decoys == 1
    j.assets = 1; j.end_turn(f)
    assert j.decoys == 0                                            # the minute runs out


def test_jack_cloaks_when_the_other_one_drew_first():
    j, g = make("jack"), make("guts"); f = Fight([[j], [g]]); f.round = 1
    assert not j.wants_cloak(f, g)
    g.acted = True
    assert j.wants_cloak(f, g) and j.wants_cloak(f, make("arthur"))
    f.round = 2
    assert not j.wants_cloak(f, g)


def test_alfa_parries_a_blade_and_the_parry_stays_up_until_his_turn():
    a, g = make("alfa"), make("guts"); Fight([[a], [g]])
    assert a.defend_ac(g, 23, True, False) == 0 and a.reaction       # six wouldn't stop it: he keeps the Reaction
    assert a.defend_ac(g, 19, False, False) == 0 and a.reaction      # nobody parries a bullet
    assert a.defend_ac(g, 19, True, True) == 0 and a.reaction        # or a critical hit
    assert a.defend_ac(g, 19, True, False) == 6 and a.parry and not a.reaction
    assert a.defend_ac(g, 30, True, False) == 6                      # it's still up for the next blade
    a.start_turn()
    assert not a.parry and a.reaction


def test_alfa_dodges_a_bullet_or_a_big_blade_he_can_see_coming():
    a, g = make("alfa"), make("guts"); Fight([[a], [g]])
    assert a.reduce_hit(12, True) == 12 and a.reaction               # a small cut isn't worth it
    assert a.reduce_hit(12, False) == 6 and not a.reaction           # any bullet is
    assert a.reduce_hit(40, True) == 40                              # one Reaction a round
    a.start_turn()
    assert a.reduce_hit(40, True) == 20
    a.start_turn(); g.invisible = True
    a.defend_ac(g, 30, False, False)
    assert a.reduce_hit(40, False) == 40 and a.reaction              # he can't dodge what he can't see


def test_alfa_ripostes_with_a_die_and_a_fresh_sneak_attack():
    a, g = make("alfa"), make("guts"); f = Fight([[a], [g]]); f.round = 2
    a.sa_used = True
    a.on_missed(f, g, False)
    assert a.reaction and a.dice == 5 and not f.pending              # a bullet that misses is only a miss
    a.on_missed(f, g, True)
    assert not a.reaction and a.dice == 4 and len(f.pending) == 1
    hp = g.hp; g.ac = -50                                            # only a natural 1 misses now
    while g.hp == hp: a.sa_used = True; a.edge.add(g.name); a.cut(f, g, riposte=True)      # with advantage (Vex)
    assert a.sa_used and g.name in a.edge                            # the cut found its own Sneak Attack, and Vex


def test_alfa_takes_the_sword_in_both_hands_against_a_mirror():
    a = make("alfa"); f = Fight([[a], [make("guts")]]); a.before_first_round(f)
    assert a.one_handed and all(11 <= a.steel() <= 18 for i in range(200))
    a = make("alfa"); f = Fight([[a], [make("dark-link")]]); a.before_first_round(f)
    assert not a.one_handed and all(9 <= a.steel() <= 18 for i in range(200))


def test_the_jet_swords_flame_is_fire_and_not_steel():
    a, an = make("alfa"), make("anderson"); f = Fight([[a], [an]]); f.round = 2
    an.ac = -50
    while not an.radiant_taken: a.cut(f, an)
    assert 2 <= an.radiant_taken <= 24                               # the body that regrows feels the flame, not the edge
