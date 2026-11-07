import secrets, sys

LOG = []
VERBOSE = True


def log(s):
    if VERBOSE:
        LOG.append(s)


def d(n):
    return secrets.randbelow(n) + 1


def roll(n, sides, gwf=False, minval=None):
    r = [d(sides) for _ in range(n)]
    if gwf:
        r = [3 if x <= 2 else x for x in r]
    if minval:
        r = [max(x, minval) for x in r]
    return r


def d20(adv=False, disadv=False):
    r1, r2 = d(20), d(20)
    if adv and disadv:
        adv = disadv = False
    if adv:
        return max(r1, r2), f"2d20 ({r1},{r2}) high"
    if disadv:
        return min(r1, r2), f"2d20 ({r1},{r2}) low"
    return r1, f"d20 {r1}"


# =====================================================================
#  ITACHI vs GUTS
# =====================================================================
def fight_guts(verbose=True, policy="susanoo_first"):
    global VERBOSE, LOG
    VERBOSE = verbose
    LOG = []
    it = dict(hp=85, maxhp=85, base_ac=19, shield_slots=4, illusory_self=True, susanoo=False, thp=0, yata=0,
              tsukuyomi=True, amaterasu=True, mirror=0, mirror_cast=False, reaction=True, disadv=False, dist=60,
              shield_up=False, susanoo_turns=0, susanoo_cast=0)
    gu = dict(hp=236, maxhp=236, ac=18, raging=False, surge=1, sw=3, reaction=True, relentless_dc=10, death_fail=0,
              hew=False, down=False, burning=False, unconscious=False, sealed=False)
    winner = None
    rnd = 0
    i1, i2 = d(20), d(20); g1, g2 = d(20), d(20)
    it_init = max(i1, i2) + 10; gu_init = max(g1, g2) + 2
    log(f"INITIATIVE  Itachi 2d20 ({i1},{i2}) high +10 = {it_init}   |   Guts 2d20 ({g1},{g2}) high +2 = {gu_init}")
    order = ["it", "gu"] if it_init >= gu_init else ["gu", "it"]

    def itachi_ac():
        ac = it["base_ac"]
        if it["susanoo"]:
            ac = max(ac, 21)
        if it["shield_up"]:
            ac += 5
        return ac

    def concentration(dmg):
        if not it["susanoo"]:
            return
        dc = max(10, dmg // 2)
        nat, shown = d20(adv=True)
        if nat >= dc:
            log(f"      Concentration (War Caster): {shown} vs DC {dc}: holds")
        else:
            it["susanoo"] = False; it["thp"] = 0; it["yata"] = 0
            log(f"      Concentration: {shown} vs DC {dc}: FAILS. Susanoo comes apart.")

    def damage_itachi(dmg, src):
        nonlocal winner
        note = ""
        if it["susanoo"]:
            dmg = dmg // 2
            note = f" (halved by Susanoo to {dmg})"
        absorbed = min(it["thp"], dmg)
        it["thp"] -= absorbed
        rest = dmg - absorbed
        it["hp"] -= rest
        log(f"      Itachi takes {dmg}{note}: {absorbed} off the Susanoo ({it['thp']} left), {rest} to him -> {max(it['hp'],0)} HP")
        if it["hp"] <= 0:
            winner = "Guts"; return
        concentration(dmg)

    def damage_guts(dmg, src, dtype):
        nonlocal winner
        taken = dmg if dtype == "psychic" or not gu["raging"] else dmg // 2
        note = "" if taken == dmg else f" (halved by the armor to {taken})"
        if gu["down"]:
            gu["death_fail"] += 1
            log(f"      Guts at 0: {src} is a failed death save ({gu['death_fail']}/3)")
            if gu["death_fail"] >= 3: winner = "Itachi"
            return
        gu["hp"] -= taken
        log(f"      Guts takes {taken}{note} -> {max(gu['hp'],0)} HP")
        if gu["hp"] <= 0:
            s = d(20); dc = gu["relentless_dc"]; gu["relentless_dc"] += 5
            log(f"      Guts drops to 0. RELENTLESS RAGE: d20 {s} +9 = {s+9} vs DC {dc}")
            if s + 9 >= dc:
                gu["hp"] = 24; log("      ...up at 24.")
            else:
                gu["hp"] = 0; gu["down"] = True; log("      ...failed. The armor keeps him moving at 0 HP.")

    def guts_swing(adv, label, brutal=False, frenzy=False, savage=True, can_hew=True):
        nonlocal winner
        if it["mirror"] > 0:
            m = d(20)
            need = {3: 6, 2: 8, 1: 11}[it["mirror"]]
            if m >= need:
                it["mirror"] -= 1
                log(f"   {label}: Mirror Image d20 {m} (needs {need}): the swing goes through a duplicate ({it['mirror']} left)")
                return False
        nat, shown = d20(adv)
        total = nat + 13
        crit = nat >= 19
        hit = crit or (nat != 1 and total >= itachi_ac())
        if hit and it["reaction"]:
            if it["susanoo"] and it["yata"] > 0:
                it["yata"] -= 1; it["reaction"] = False
                log(f"   {label}: {shown} +13 = {total}: would hit. YATA MIRROR: the swing is repelled outright ({it['yata']} uses left)")
                return False
            if it["shield_slots"] > 0 and not it["shield_up"]:
                it["shield_slots"] -= 1; it["reaction"] = False; it["shield_up"] = True
                if not crit and total < itachi_ac():
                    log(f"   {label}: {shown} +13 = {total}: SHIELD (AC {itachi_ac()}), and the swing misses")
                    return False
                log(f"   {label}: {shown} +13 = {total}: SHIELD goes up (AC {itachi_ac()}) but this one still lands")
            elif it["illusory_self"]:
                it["illusory_self"] = False; it["reaction"] = False
                log(f"   {label}: {shown} +13 = {total}: ILLUSORY SELF. The Itachi he hit scatters into crows.")
                return False
        if not hit:
            log(f"   {label}: {shown} +13 = {total} vs AC {itachi_ac()}: MISS")
            return False
        n = 8 if crit else 4
        w = roll(n, 6, gwf=True); wsum = sum(w); txt = f"4d6{'x2' if crit else ''}={wsum}"
        if savage:
            w2 = roll(n, 6, gwf=True)
            if sum(w2) > wsum: wsum = sum(w2); txt += f", reroll {wsum} kept"
        dmg = wsum + (16 if gu["raging"] else 13)
        if frenzy:
            fr = roll(6 if crit else 3, 6); dmg += sum(fr); txt += f", Frenzy {sum(fr)}"
        if brutal:
            br = roll(2 if crit else 1, 10); dmg += sum(br); txt += f", Brutal {sum(br)}"
        log(f"   {label}: {shown} +13 = {total} vs AC {itachi_ac()}: {'CRITICAL HIT' if crit else 'hit'} -> {txt} = {dmg}")
        if crit:
            it["disadv"] = True
            if can_hew: gu["hew"] = True
        damage_itachi(dmg, label)
        return True

    while winner is None and rnd < 30:
        rnd += 1
        log(f"\n===== ROUND {rnd} =====  Itachi {it['hp']}/85 (+{it['thp']} Susanoo) | Guts {gu['hp']}/236")
        for who in order:
            if winner: break
            if who == "it":
                it["reaction"] = True; it["shield_up"] = False
                log(f"-- Itachi's turn ({it['hp']} HP, Susanoo {'up, ' + str(it['thp']) + ' temp' if it['susanoo'] else 'down'})")
                if it["susanoo"]:
                    it["susanoo_turns"] += 1
                    if it["susanoo_turns"] > 1:
                        it["hp"] -= 5; log(f"   Susanoo's upkeep: 5 HP -> {it['hp']}")
                        if it["hp"] <= 0: winner = "Guts"; break
                if it["dist"] <= 5:
                    it["dist"] = 15; log("   Cunning Action: Disengage, and ten feet back. The Totsuka's reach is fifteen.")
                if gu["burning"]:
                    b = roll(4, 10); log(f"   Amaterasu keeps burning: 4d10 {b} = {sum(b)}"); damage_guts(sum(b), "Amaterasu", "fire")
                    if winner: break
                want = None
                if policy == "susanoo_first":
                    if not it["susanoo"] and it["susanoo_cast"] == 0: want = "susanoo"
                    elif it["tsukuyomi"]: want = "tsukuyomi"
                    elif it["susanoo"]: want = "totsuka"
                else:
                    if it["tsukuyomi"]: want = "tsukuyomi"
                    elif not it["susanoo"] and it["susanoo_cast"] == 0: want = "susanoo"
                    elif it["susanoo"]: want = "totsuka"
                if want is None:
                    if not it["mirror_cast"]: want = "mirror"
                    elif it["amaterasu"] and not gu["burning"]: want = "amaterasu"
                    else: want = "firebolt"
                if want == "susanoo":
                    it["susanoo"] = True; it["thp"] = 150; it["yata"] = 3; it["susanoo_cast"] = 1; it["susanoo_turns"] = 1
                    log("   SUSANOO (9th level). A ribcage of chakra, then a warrior around him: 150 temporary HP, AC 21, resistance to everything, the Yata Mirror three times, the Sword of Totsuka.")
                elif want == "tsukuyomi":
                    it["tsukuyomi"] = False
                    nat = d(20)
                    log(f"   TSUKUYOMI (7th level). Guts has one eye, and it is looking at him. Wis save: d20 {nat} +7 = {nat+7} vs DC 19")
                    if nat + 7 >= 19:
                        p = roll(5, 10); log(f"      ...he grinds through it. Half damage: 5d10 {p} = {sum(p)} psychic, straight through the armor")
                        damage_guts(sum(p), "Tsukuyomi", "psychic")
                    else:
                        p = roll(10, 10); log(f"      ...FAILS. Seventy-two hours in a second: 10d10 {p} = {sum(p)} psychic, and he goes down, Unconscious for an hour.")
                        damage_guts(sum(p), "Tsukuyomi", "psychic")
                        gu["unconscious"] = True; winner = "Itachi"
                elif want == "totsuka":
                    nat, shown = d20(disadv=it["disadv"])
                    total = nat + 11
                    hit = nat == 20 or (nat != 1 and total >= gu["ac"])
                    if not hit:
                        log(f"   Sword of Totsuka: {shown} +11 = {total} vs AC 18: MISS")
                    else:
                        f = roll(12 if nat == 20 else 6, 8)
                        log(f"   Sword of Totsuka: {shown} +11 = {total} vs AC 18: hit -> 6d8 {f} = {sum(f)} force")
                        damage_guts(sum(f), "Totsuka", "force")
                        if winner is None:
                            s = d(20)
                            log(f"      Sealing: Guts Wis save d20 {s} +7 = {s+7} vs DC 19")
                            if s + 7 >= 19: log("      ...he wrenches free of the blade.")
                            else:
                                log("      ...FAILS. The sword drinks him into the gourd. Sealed."); gu["sealed"] = True; winner = "Itachi"
                elif want == "mirror":
                    it["mirror"] = 3; it["mirror_cast"] = True; log("   Mirror Image: three Itachis.")
                elif want == "amaterasu":
                    it["amaterasu"] = False
                    nat, shown = d20(adv=True)
                    log(f"   AMATERASU (6th level). Dex save (Danger Sense): {shown} +2 = {nat+2} vs DC 19")
                    if nat + 2 >= 19: log("      ...the black fire lands where he was standing.")
                    else:
                        b = roll(6, 10); log(f"      ...FAILS. Ignited: 6d10 {b} = {sum(b)} fire"); damage_guts(sum(b), "Amaterasu", "fire"); gu["burning"] = True
                elif want == "firebolt":
                    nat, shown = d20(disadv=it["disadv"]); total = nat + 11
                    if nat == 20 or (nat != 1 and total >= gu["ac"]):
                        b = roll(8 if nat == 20 else 4, 10, minval=2); log(f"   Fire Bolt: {shown} +11 = {total}: hit, {sum(b)} fire"); damage_guts(sum(b), "Fire Bolt", "fire")
                    else:
                        log(f"   Fire Bolt: {shown} +11 = {total}: miss")
            else:
                gu["reaction"] = True; it["disadv"] = False
                if gu["down"]:
                    ds, shown = d20(adv=True)
                    if ds == 20: gu["hp"] = 1; gu["down"] = False; gu["death_fail"] = 0; log(f"-- Guts: death save {shown} = 20, back to 1 HP")
                    elif ds < 10:
                        gu["death_fail"] += 1; log(f"-- Guts: death save {shown}: failure ({gu['death_fail']}/3)")
                        if gu["death_fail"] >= 3: winner = "Itachi"; break
                    else: log(f"-- Guts: death save {shown}: success; the armor keeps him moving")
                log(f"-- Guts's turn ({gu['hp']} HP)")
                bonus_used = False
                if not gu["raging"]:
                    gu["raging"] = True; bonus_used = True; log("   RAGE. The Berserker Armor bites down.")
                if it["dist"] > 5:
                    it["dist"] = 5; log("   Closes to Itachi." if rnd > 1 else "   Instinctive Pounce and the armor's speed: closes the sixty feet.")
                swings = 2
                if gu["surge"] > 0 and gu["raging"]:
                    gu["surge"] = 0; swings = 4; log("   ACTION SURGE. Reckless Attack. Four swings.")
                else:
                    log("   Reckless Attack.")
                first_hit = False
                for i in range(swings):
                    if winner: break
                    brutal = (i == 1)
                    hit = guts_swing(not brutal, f"Swing {i+1}{' (Brutal)' if brutal else ''}", brutal=brutal, frenzy=not first_hit, savage=not first_hit)
                    if hit: first_hit = True
                if winner: break
                if not bonus_used and gu["hew"]:
                    gu["hew"] = False; log("   HEW:"); guts_swing(True, "Swing, Hew", savage=False)
                elif not bonus_used and gu["hp"] <= 118 and gu["sw"] > 0 and not gu["down"]:
                    h = d(10) + 8; gu["sw"] -= 1; gu["hp"] = min(gu["hp"] + h, gu["maxhp"]); log(f"   Second Wind: +{h} -> {gu['hp']}")
                gu["hew"] = False
    return winner, rnd


# =====================================================================
#  ITACHI vs GOBLIN SLAYER  (silent, coarse but fair)
# =====================================================================
def fight_gs():
    it = dict(hp=85, ac=19, shield=4, illusory=True, reaction=True, prone=False)
    gs = dict(hp=220, ac=17, indom=2, sw=4, surge=1, doses=5, blade=True, dist=60, paralyzed=False, pk=False)
    spells = ["tsukuyomi", "dominate", "hold", "dominate", "hold", "hold", "pk", "pk", "pk"]
    si = 0
    i1, i2 = d(20), d(20); it_init = max(i1, i2) + 10; gs_init = d(20) + 8 + d(10)
    order = ["it", "gs"] if it_init >= gs_init else ["gs", "it"]
    winner = None; rnd = 0

    def gs_save(dc):
        nat = d(20); ok = nat + 8 >= dc
        if not ok and gs["indom"] > 0:
            gs["indom"] -= 1; nat = d(20); ok = nat + 8 >= dc
        return ok

    while winner is None and rnd < 40:
        rnd += 1
        for who in order:
            if winner: break
            if who == "it":
                it["reaction"] = True
                it["prone"] = False
                if gs["paralyzed"]:
                    nat = d(20); total = nat + 11
                    if nat == 20 or (nat != 1 and total >= gs["ac"]):
                        gs["hp"] -= sum(roll(8, 10, minval=2))
                        if gs["hp"] <= 0: winner = "Itachi"
                    continue
                if si < len(spells):
                    sp = spells[si]; si += 1
                    if sp == "tsukuyomi":
                        if not gs_save(19): winner = "Itachi"
                        else: gs["hp"] -= sum(roll(5, 10))
                    elif sp == "dominate":
                        if not gs_save(19): winner = "Itachi"
                    elif sp == "hold":
                        if not gs_save(19): gs["paralyzed"] = True
                    elif sp == "pk":
                        if not gs_save(19): gs["pk"] = True; gs["hp"] -= sum(roll(4, 10))
                else:
                    nat = d(20); total = nat + 11
                    if nat == 20 or (nat != 1 and total >= gs["ac"]):
                        gs["hp"] -= sum(roll(8 if nat == 20 else 4, 10, minval=2))
                if gs["hp"] <= 0: winner = "Itachi"
            else:
                if gs["paralyzed"]:
                    if d(20) + 8 >= 19: gs["paralyzed"] = False
                    continue
                if gs["pk"]:
                    if d(20) + 8 >= 19: gs["pk"] = False
                    else: gs["hp"] -= sum(roll(4, 10))
                    if gs["hp"] <= 0: winner = "Itachi"; break
                moved = False
                if gs["dist"] > 5: gs["dist"] = 5; moved = True
                bonus_adv = False
                if gs["hp"] <= 160 and gs["sw"] > 0: gs["sw"] -= 1; gs["hp"] = min(220, gs["hp"] + d(10) + 16)
                elif not gs["blade"] and gs["doses"] > 0: gs["doses"] -= 1; gs["blade"] = True
                elif not moved: bonus_adv = True
                attacks = 6 if gs["surge"] else 3
                gs["surge"] = 0
                sa = True; shield_up = False; bashed = False
                for a in range(attacks):
                    adv = it["prone"] or (bonus_adv and a == 0)
                    nat, _ = d20(adv)
                    ac = it["ac"] + (5 if shield_up else 0)
                    total = nat + 10
                    hit = nat == 20 or (nat != 1 and total >= ac)
                    if hit and it["reaction"] and it["shield"] > 0 and not shield_up:
                        it["shield"] -= 1; it["reaction"] = False; shield_up = True
                        if nat != 20 and total < it["ac"] + 5: hit = False
                    elif hit and it["reaction"] and it["illusory"]:
                        it["illusory"] = False; it["reaction"] = False; hit = False
                    if not hit: continue
                    dmg = sum(roll(2 if nat == 20 else 1, 6)) + 6
                    if sa and adv:
                        dmg += sum(roll(4 if nat == 20 else 2, 6)); sa = False
                    it["hp"] -= dmg
                    if gs["blade"]:
                        gs["blade"] = False
                        if d(20) < 14: it["hp"] -= sum(roll(2, 8))
                    if not bashed:
                        bashed = True
                        if d(20) - 1 < 18: it["prone"] = True
                    if it["hp"] <= 0: winner = "Goblin Slayer"; break
    return winner, rnd


# =====================================================================
#  ITACHI vs KYLE CRANE  (silent, coarse but fair)
# =====================================================================
def fight_crane():
    it = dict(hp=85, ac=19, shield=4, illusory=True, reaction=True)
    kc = dict(hp=227, ac=16, fury=6, dist=60, paralyzed=False)
    spells = ["tsukuyomi", "hold", "dominate", "hold", "dominate", "hold"]
    si = 0
    i1, i2 = d(20), d(20); it_init = max(i1, i2) + 10; k1, k2 = d(20), d(20); kc_init = max(k1, k2) + 3
    order = ["it", "kc"] if it_init >= kc_init else ["kc", "it"]
    winner = None; rnd = 0
    while winner is None and rnd < 40:
        rnd += 1
        for who in order:
            if winner: break
            if who == "it":
                it["reaction"] = True
                if kc["paralyzed"]:
                    nat = d(20); total = nat + 11
                    if nat == 20 or (nat != 1 and total >= kc["ac"]):
                        kc["hp"] -= sum(roll(8, 10, minval=2))
                        if kc["hp"] <= 0: winner = "Itachi"
                    continue
                if si < len(spells):
                    sp = spells[si]; si += 1
                    if d(20) < 19:
                        if sp in ("tsukuyomi", "dominate"): winner = "Itachi"
                        else: kc["paralyzed"] = True
                    elif sp == "tsukuyomi":
                        kc["hp"] -= sum(roll(5, 10))
                else:
                    nat = d(20); total = nat + 11
                    if nat == 20 or (nat != 1 and total >= kc["ac"]):
                        kc["hp"] -= sum(roll(8 if nat == 20 else 4, 10, minval=2))
                if kc["hp"] <= 0: winner = "Itachi"
            else:
                if kc["paralyzed"]:
                    if d(20) >= 19: kc["paralyzed"] = False
                    continue
                if kc["dist"] > 5: kc["dist"] = 5
                shield_up = False
                for a in range(3):
                    brutal = (a == 2)
                    nat, _ = d20(adv=not brutal)
                    ac = it["ac"] + (5 if shield_up else 0)
                    total = nat + 11
                    hit = nat == 20 or (nat != 1 and total >= ac)
                    if hit and it["reaction"] and it["shield"] > 0 and not shield_up:
                        it["shield"] -= 1; it["reaction"] = False; shield_up = True
                        if nat != 20 and total < it["ac"] + 5: hit = False
                    elif hit and it["reaction"] and it["illusory"]:
                        it["illusory"] = False; it["reaction"] = False; hit = False
                    if not hit: continue
                    dmg = sum(roll(2 if nat == 20 else 1, 6)) + 8 + (sum(roll(1, 10)) if brutal else 0)
                    it["hp"] -= dmg
                    if kc["fury"] > 0:
                        kc["fury"] -= 1
                        if d(20) + 7 < 17: it["hp"] -= sum(roll(2, 12))
                    if it["hp"] <= 0: winner = "Kyle Crane"; break
    return winner, rnd


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "narrate"
    if mode == "mc":
        n = int(sys.argv[2])
        for pol in ("susanoo_first", "tsukuyomi_first"):
            w = {"Itachi": 0, "Guts": 0, None: 0}; rs = []
            for _ in range(n):
                a, r = fight_guts(verbose=False, policy=pol); w[a] += 1; rs.append(r)
            print("vs Guts,", pol, w, "avg rounds", round(sum(rs) / n, 2))
        w = {"Itachi": 0, "Goblin Slayer": 0, None: 0}; rs = []
        for _ in range(n):
            a, r = fight_gs(); w[a] += 1; rs.append(r)
        print("vs Goblin Slayer", w, "avg rounds", round(sum(rs) / n, 2))
        w = {"Itachi": 0, "Kyle Crane": 0, None: 0}; rs = []
        for _ in range(n):
            a, r = fight_crane(); w[a] += 1; rs.append(r)
        print("vs Kyle Crane", w, "avg rounds", round(sum(rs) / n, 2))
    else:
        pol = sys.argv[2] if len(sys.argv) > 2 else "susanoo_first"
        w, r = fight_guts(verbose=True, policy=pol)
        print("\n".join(LOG)); print(f"\nWINNER: {w} after {r} rounds")
