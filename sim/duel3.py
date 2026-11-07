import secrets, sys

LOG = []
VERBOSE = True


def log(s):
    if VERBOSE:
        LOG.append(s)


def d(n):
    return secrets.randbelow(n) + 1


def roll(n, sides, gwf=False):
    r = [d(sides) for _ in range(n)]
    if gwf:
        r = [3 if x <= 2 else x for x in r]
    return r


def fmt_d20(adv, disadv):
    r1, r2 = d(20), d(20)
    if adv and disadv:
        adv = disadv = False
    if adv:
        return max(r1, r2), f"2d20 ({r1},{r2}) high"
    if disadv:
        return min(r1, r2), f"2d20 ({r1},{r2}) low"
    return r1, f"d20 {r1}"


def fight(verbose=True):
    global VERBOSE, LOG
    VERBOSE = verbose
    LOG = []
    kc = dict(hp=227, maxhp=227, ac=16, raging=False, rages=4, fury=6, reaction=True, relentless_dc=10,
              greater=2, potions=4, sw=2, disadv=False, mode="claws", lit=False, down=False)
    gu = dict(hp=236, maxhp=236, ac=18, raging=False, surge=1, sw=3, reaction=True, relentless_dc=10,
              death_fail=0, death_succ=0, hew=False, down=False, prone=False)
    dist = 60
    rnd = 0
    winner = None

    # ---- initiative: both have advantage ----
    k1, k2 = d(20), d(20)
    g1, g2 = d(20), d(20)
    kc_init = max(k1, k2) + 3
    gu_init = max(g1, g2) + 2
    log(f"INITIATIVE  Crane 2d20 ({k1},{k2}) high +3 = {kc_init}   |   Guts 2d20 ({g1},{g2}) high +2 = {gu_init}")
    order = ["kc", "gu"] if kc_init >= gu_init else ["gu", "kc"]

    # ---------------- damage handlers ----------------
    def damage_guts(amount, src, dtype="slashing", crit=False):
        nonlocal winner
        taken = amount
        note = ""
        if gu["raging"] and dtype != "psychic":
            taken = amount // 2
            note = f" (halved to {taken} by the armor)"
        if gu["down"]:
            gu["death_fail"] += 2 if crit else 1
            log(f"      Guts is at 0: {src} is {'two failed death saves' if crit else 'a failed death save'} ({gu['death_fail']}/3)")
            if gu["death_fail"] >= 3:
                winner = "Kyle Crane"
            return
        gu["hp"] -= taken
        log(f"      Guts takes {taken}{note} -> {max(gu['hp'],0)} HP")
        if gu["hp"] <= 0:
            if gu["raging"]:
                s = d(20); dc = gu["relentless_dc"]; gu["relentless_dc"] += 5
                log(f"      Guts drops to 0. RELENTLESS RAGE: d20 {s} +9 = {s+9} vs DC {dc}")
                if s + 9 >= dc:
                    gu["hp"] = 24; log("      ...he stays up at 24 HP.")
                else:
                    gu["hp"] = 0; gu["down"] = True
                    log("      ...failed. The armor holds the body up: he keeps fighting at 0 HP, making death saves.")
            else:
                gu["hp"] = 0; winner = "Kyle Crane"

    def damage_crane(amount, src, dtype="slashing", on_guts_turn=False):
        nonlocal winner
        taken = amount
        note = ""
        if kc["raging"] and dtype in ("slashing", "piercing", "bludgeoning"):
            taken = amount // 2
            note = f" (halved to {taken} by Rage)"
        if on_guts_turn and kc["reaction"]:
            kc["reaction"] = False
            taken = taken // 2
            note += f", UNCANNY DODGE halves it again to {taken}"
        kc["hp"] -= taken
        log(f"      Crane takes {taken}{note} -> {max(kc['hp'],0)} HP")
        if kc["raging"] and kc.get("surge_ready") and 0 < kc["hp"] < 113:
            kc["surge_ready"] = False
            before = kc["hp"]; kc["hp"] = min(kc["hp"] + 44, kc["maxhp"])
            log(f"      BEAST MODE SURGE (the meter fills): +{kc['hp']-before} -> Crane {kc['hp']} HP")
        if kc["hp"] <= 0:
            if kc["raging"]:
                s = d(20); dc = kc["relentless_dc"]; kc["relentless_dc"] += 5
                log(f"      Crane drops to 0. RELENTLESS RAGE: d20 {s} +9 = {s+9} vs DC {dc}")
                if s + 9 >= dc:
                    kc["hp"] = 22; log("      ...he gets back up at 22 HP.")
                else:
                    kc["hp"] = 0; winner = "Guts"
            else:
                kc["hp"] = 0; winner = "Guts"

    # ---------------- Guts's swing ----------------
    def guts_swing(adv, label, brutal=False, frenzy=False, savage=True, can_hew=True, on_guts_turn=True):
        nonlocal winner
        disadv = gu["prone"]
        nat, shown = fmt_d20(adv, disadv)
        total = nat + 13
        crit = nat >= 19
        hit = crit or (nat != 1 and total >= kc["ac"])
        if not hit:
            log(f"   {label}: {shown} +13 = {total} vs AC 16: MISS")
            return False
        n = 8 if crit else 4
        w1 = roll(n, 6, gwf=True); wsum = sum(w1)
        txt = f"4d6{'x2' if crit else ''} {w1}={wsum}"
        if savage:
            w2 = roll(n, 6, gwf=True)
            if sum(w2) > wsum:
                txt += f", Savage reroll {w2}={sum(w2)} (kept)"; wsum = sum(w2)
            else:
                txt += f", Savage reroll {w2}={sum(w2)} (discarded)"
        bonus = 16 if gu["raging"] else 13
        dmg = wsum + bonus
        if frenzy:
            fr = roll(6 if crit else 3, 6); txt += f", Frenzy 3d6{'x2' if crit else ''} {fr}={sum(fr)}"; dmg += sum(fr)
        if brutal:
            br = roll(2 if crit else 1, 10); txt += f", Brutal Strike d10{'x2' if crit else ''} {br}={sum(br)}"; dmg += sum(br)
        log(f"   {label}: {shown} +13 = {total} vs AC 16: {'CRITICAL HIT' if crit else 'hit'} -> {txt} +{bonus} = {dmg}")
        if crit:
            kc["disadv"] = True
            if can_hew: gu["hew"] = True
            log("      Slasher crit: Crane has disadvantage on attacks until Guts's next turn." + (" Hew is up." if can_hew else ""))
        damage_crane(dmg, label, "slashing", on_guts_turn=on_guts_turn)
        return True

    # ---------------- Crane's attacks ----------------
    def crane_claw(adv, label, brutal=False, savage=False):
        nonlocal winner
        nat, shown = fmt_d20(adv, kc["disadv"])
        total = nat + 11
        crit = nat == 20
        hit = crit or (nat != 1 and total >= gu["ac"])
        if not hit:
            log(f"   {label}: {shown} +11 = {total} vs AC 18: MISS")
            return False
        w = roll(2 if crit else 1, 6); wsum = sum(w)
        txt = f"1d6{'x2' if crit else ''} {w}"
        if savage:
            w2 = roll(2 if crit else 1, 6)
            if sum(w2) > wsum: txt += f", Savage reroll {w2} (kept)"; wsum = sum(w2)
            else: txt += f", Savage reroll {w2} (discarded)"
        dmg = wsum + 8
        if brutal:
            br = roll(2 if crit else 1, 10); txt += f", Brutal Strike d10{'x2' if crit else ''} {br}"; dmg += sum(br)
        log(f"   {label}: {shown} +11 = {total} vs AC 18: {'CRITICAL HIT' if crit else 'hit'} -> {txt} +8 = {dmg} slashing")
        damage_guts(dmg, label, "slashing", crit=crit)
        if kc["hp"] < kc["maxhp"]:
            before = kc["hp"]; kc["hp"] = min(kc["hp"] + 6, kc["maxhp"])
            log(f"      Beast Unleashed: +{kc['hp']-before} -> Crane {kc['hp']} HP")
        if winner: return True
        if kc["fury"] > 0:
            kc["fury"] -= 1
            sv = d(20)
            if sv + 7 >= 17:
                log(f"      Infectious Fury ({kc['fury']} left): Guts Wis save d20 {sv} +7 = {sv+7} vs DC 17: resists")
            else:
                p = roll(4 if crit else 2, 12)
                log(f"      Infectious Fury ({kc['fury']} left): Guts Wis save d20 {sv} +7 = {sv+7} vs DC 17: FAILS -> 2d12{'x2' if crit else ''} {p} = {sum(p)} psychic, straight through the armor")
                damage_guts(sum(p), "Infectious Fury", "psychic", crit=crit)
        # Retaliation
        if winner is None and gu["reaction"] and gu["raging"]:
            gu["reaction"] = False
            log("      RETALIATION (reaction):")
            guts_swing(True, "   Guts, Retaliation", savage=True, can_hew=False, on_guts_turn=False)
        return True

    def crane_blade(adv, label, sa_available, brutal=False, savage=False):
        nonlocal winner
        nat, shown = fmt_d20(adv, kc["disadv"])
        eff_adv = adv and not kc["disadv"]
        total = nat + 11
        crit = nat == 20
        hit = crit or (nat != 1 and total >= gu["ac"])
        if not hit:
            log(f"   {label}: {shown} +11 = {total} vs AC 18: MISS")
            return False, False
        w = roll(2 if crit else 1, 6); wsum = sum(w)
        txt = f"1d6{'x2' if crit else ''} {w}"
        if savage:
            w2 = roll(2 if crit else 1, 6)
            if sum(w2) > wsum: txt += f", Savage reroll {w2} (kept)"; wsum = sum(w2)
            else: txt += f", Savage reroll {w2} (discarded)"
        slash = wsum + 10
        fire = roll(4 if crit else 2, 6); txt += f" +10 slashing, 2d6{'x2' if crit else ''} fire {fire}"
        sa_used = False
        if sa_available and eff_adv:
            s = roll(8 if crit else 4, 6); slash += sum(s); txt += f", Sneak Attack 4d6{'x2' if crit else ''} {s}={sum(s)}"; sa_used = True
        if brutal:
            br = roll(2 if crit else 1, 10); slash += sum(br); txt += f", Brutal Strike d10 {br}"
        log(f"   {label}: {shown} +11 = {total} vs AC 18: {'CRITICAL HIT' if crit else 'hit'} -> {txt} = {slash} slashing + {sum(fire)} fire")
        damage_guts(slash, label, "slashing", crit=crit)
        if winner is None:
            damage_guts(sum(fire), label + " (fire)", "fire")
        if winner is None and gu["reaction"] and gu["raging"]:
            gu["reaction"] = False
            log("      RETALIATION (reaction):")
            guts_swing(True, "   Guts, Retaliation", savage=True, can_hew=False, on_guts_turn=False)
        return True, sa_used

    # ---------------- turns ----------------
    while winner is None and rnd < 40:
        rnd += 1
        log(f"\n===== ROUND {rnd} =====  Crane {kc['hp']}/227 | Guts {gu['hp']}/236{' (0 HP, armor)' if gu['down'] else ''}")
        for who in order:
            if winner: break
            if who == "kc":
                kc["reaction"] = True
                log(f"-- Crane's turn ({kc['hp']} HP, Fury {kc['fury']}, {'Beast Mode' if kc['raging'] else 'not raging'})")
                bonus_used = False
                if not kc["raging"]:
                    kc["raging"] = True; kc["rages"] -= 1; bonus_used = True
                    log("   BEAST MODE (bonus action): Rage, claws out. Resistance to slashing. Instinctive Pounce 20 ft.")
                    kc["surge_ready"] = True
                    if kc["hp"] < 113:
                        kc["surge_ready"] = False
                        before = kc["hp"]; kc["hp"] = min(kc["hp"] + 44, kc["maxhp"])
                        log(f"   Beast Mode heal on activation (meter full): +{kc['hp']-before} -> {kc['hp']} HP")
                    else:
                        log("   (The Beast Mode heal is banked: it fires the first time he drops below half.)")
                    if dist > 5: dist = 0; log("   Closes the 60 ft.")
                elif dist > 5:
                    dist = 0; log("   Moves to Guts.")
                # choose mode
                # revised: Beast Unleashed heals per claw hit, so he stays on the claws
                if kc["mode"] == "blade" and not kc["lit"] and not bonus_used:
                    kc["lit"] = True; bonus_used = True
                    log("   Lights the Inferno Machete (bonus action): +2d6 fire.")
                if not bonus_used:
                    if kc["hp"] <= 150 and kc["greater"] > 0:
                        kc["greater"] -= 1; h = sum(roll(4, 4)) + 4; kc["hp"] = min(kc["hp"] + h, kc["maxhp"])
                        log(f"   Drinks a Potion of Greater Healing (bonus action): 4d4+4 = {h} -> {kc['hp']} HP")
                    elif kc["hp"] <= 150 and kc["potions"] > 0:
                        kc["potions"] -= 1; h = sum(roll(2, 4)) + 2; kc["hp"] = min(kc["hp"] + h, kc["maxhp"])
                        log(f"   Drinks a Potion of Healing (bonus action): 2d4+2 = {h} -> {kc['hp']} HP")
                    elif kc["hp"] <= 150 and kc["sw"] > 0:
                        kc["sw"] -= 1; h = d(10) + 1; kc["hp"] = min(kc["hp"] + h, kc["maxhp"])
                        log(f"   Second Wind (bonus action): 1d10+1 = {h} -> {kc['hp']} HP")
                log("   Reckless Attack.")
                adv = True  # his own Reckless (and Guts's)
                if kc["mode"] == "claws":
                    first_hit = False
                    for i in range(3):
                        if winner: break
                        brutal = (i == 2) and not kc["disadv"]
                        hit = crane_claw(adv and not brutal, f"Claw {i+1}{' (Brutal Strike)' if brutal else ''}", brutal=brutal, savage=not first_hit)
                        if hit: first_hit = True
                else:
                    sa_avail = True; first_hit = False
                    for i in range(2):
                        if winner: break
                        brutal = (i == 1)
                        hit, sa_used = crane_blade(adv and not brutal, f"Machete {i+1}{' (Brutal Strike)' if brutal else ''}", sa_avail, brutal=brutal, savage=not first_hit)
                        if sa_used: sa_avail = False
                        if hit: first_hit = True
            else:
                gu["reaction"] = True
                kc["disadv"] = False
                if gu["down"]:
                    ds1, ds2 = d(20), d(20); ds = max(ds1, ds2)
                    if ds == 20:
                        gu["hp"] = 1; gu["down"] = False; gu["death_fail"] = 0
                        log(f"-- Guts's turn: DEATH SAVE 2d20 ({ds1},{ds2}) high = 20! Back to 1 HP.")
                    elif ds >= 10:
                        gu["death_succ"] += 1
                        log(f"-- Guts's turn: death save 2d20 ({ds1},{ds2}) high = {ds}: success ({gu['death_succ']} successes, {gu['death_fail']} failures). The armor keeps him moving.")
                    else:
                        gu["death_fail"] += 1
                        log(f"-- Guts's turn: death save 2d20 ({ds1},{ds2}) high = {ds}: FAILURE ({gu['death_fail']}/3)")
                        if gu["death_fail"] >= 3:
                            winner = "Kyle Crane"; break
                log(f"-- Guts's turn ({gu['hp']} HP)")
                bonus_used = False
                if gu["prone"]:
                    gu["prone"] = False; log("   Stands up.")
                if not gu["raging"]:
                    gu["raging"] = True; bonus_used = True
                    log("   RAGE (bonus action). The Berserker Armor bites down: resistance to everything but psychic.")
                    if dist > 5: dist = 0; log("   Instinctive Pounce 20 ft + 40 ft: closes the gap.")
                elif dist > 5:
                    dist = 0; log("   Moves to Crane.")
                swings = 2
                if gu["surge"] > 0 and gu["raging"]:
                    gu["surge"] = 0; swings = 4
                    log("   ACTION SURGE. Reckless Attack. Four swings.")
                else:
                    log("   Reckless Attack.")
                first_hit = False
                for i in range(swings):
                    if winner: break
                    brutal = (i == 1)
                    hit = guts_swing(not brutal, f"Swing {i+1}{' (Brutal Strike)' if brutal else ''}", brutal=brutal, frenzy=not first_hit, savage=not first_hit)
                    if hit: first_hit = True
                if winner: break
                if not bonus_used and gu["hew"]:
                    gu["hew"] = False; bonus_used = True
                    log("   HEW (bonus action after the crit):")
                    guts_swing(True, "Swing, Hew", savage=False)
                elif not bonus_used and gu["hp"] <= 128 and gu["sw"] > 0 and not gu["down"]:
                    h = d(10) + 8; gu["sw"] -= 1; gu["hp"] = min(gu["hp"] + h, gu["maxhp"])
                    log(f"   Second Wind (bonus action): 1d10+8 = {h} -> {gu['hp']} HP")
                gu["hew"] = False
    return winner, rnd


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "mc":
        n = int(sys.argv[2])
        wins = {"Guts": 0, "Kyle Crane": 0, None: 0}; rounds = []
        for _ in range(n):
            w, r = fight(verbose=False); wins[w] += 1; rounds.append(r)
        print(wins, "avg rounds", sum(rounds) / len(rounds))
    else:
        w, r = fight(verbose=True)
        print("\n".join(LOG)); print(f"\nWINNER: {w} after {r} rounds")
