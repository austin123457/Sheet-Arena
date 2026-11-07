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


def fight(verbose=True):
    global VERBOSE, LOG
    VERBOSE = verbose
    LOG = []
    gs = dict(name="Goblin Slayer", hp=220, maxhp=220, ac=17, sw=4, dice=5, surge=1, doses=5, blade_poisoned=True,
              hitdice=10, reaction=True, disadv_until_guts_turn=False, dist=60)
    gu = dict(name="Guts", hp=256, maxhp=256, ac=18, raging=False, sw=3, surge=1, reaction=True, poisoned=False,
              death_fail=0, death_succ=0, relentless_dc=10, prone=False, hew=False, down=False)
    # ---- initiative ----
    gs_i_roll, amb = d(20), d(10)
    gs_init = gs_i_roll + 8 + amb
    gu_rolls = (d(20), d(20))
    gu_init = max(gu_rolls) + 2
    log(f"INITIATIVE  Goblin Slayer d20 {gs_i_roll} +8, Ambush d10 {amb} = {gs_init}   |   Guts 2d20 {gu_rolls} take high +2 = {gu_init}")
    order = ["gs", "gu"] if gs_init >= gu_init else ["gu", "gs"]
    dist = 60
    rnd = 0
    winner = None

    def damage_guts(amount, src, crit=False):
        nonlocal winner
        taken = amount // 2 if gu["raging"] else amount
        note = f" (halved to {taken} by the armor)" if gu["raging"] and amount else ""
        if gu["hp"] <= 0 and gu["down"]:
            gu["death_fail"] += 2 if crit else 1
            log(f"      Guts is at 0: {src} counts as {'two failed death saves' if crit else 'a failed death save'} ({gu['death_fail']}/3)")
            if gu["death_fail"] >= 3:
                winner = "Goblin Slayer"
            return
        gu["hp"] -= taken
        log(f"      Guts takes {taken}{note} -> {max(gu['hp'],0)} HP")
        if gu["hp"] <= 0:
            if gu["raging"]:
                s = d(20)
                dc = gu["relentless_dc"]
                log(f"      Guts drops to 0. RELENTLESS RAGE: d20 {s} +10 = {s+10} vs DC {dc}")
                gu["relentless_dc"] += 5
                if s + 10 >= dc:
                    gu["hp"] = 24
                    log("      ...he stays on his feet at 24 HP.")
                else:
                    gu["hp"] = 0
                    gu["down"] = True
                    log("      ...failed. The armor holds the body up anyway: he keeps fighting at 0 HP, making death saves.")
            else:
                gu["hp"] = 0
                winner = "Goblin Slayer"

    def damage_gs(amount, src):
        nonlocal winner
        gs["hp"] -= amount
        log(f"      Goblin Slayer takes {amount} -> {max(gs['hp'],0)} HP")
        if gs["hp"] <= 0:
            gs["hp"] = 0
            winner = "Guts"

    def guts_swing(adv, label, brutal=False, frenzy=False, savage=True, can_hew=True):
        """Returns True if it hit."""
        nonlocal winner
        disadv = gu["poisoned"] or gu["prone"]
        if adv and disadv:
            adv = False
            disadv = False
        r1, r2 = d(20), d(20)
        if adv:
            nat = max(r1, r2); shown = f"2d20 ({r1},{r2}) high"
        elif disadv:
            nat = min(r1, r2); shown = f"2d20 ({r1},{r2}) low"
        else:
            nat = r1; shown = f"d20 {r1}"
        total = nat + 13
        crit = nat >= 19
        hit = crit or (nat != 1 and total >= gs["ac"])
        if not hit:
            log(f"   {label}: {shown} +13 = {total} vs AC 17: MISS")
            if gs["reaction"] and gs["dice"] > 0 and winner is None:
                gs["reaction"] = False
                gs["dice"] -= 1
                log(f"      RIPOSTE (reaction, one die; dice left {gs['dice']}):")
                gs_stab(gu["raging"], "   Goblin Slayer, Riposte", False, riposte=True)
            return False
        n = 8 if crit else 4
        w1 = roll(n, 6, gwf=True)
        txt = f"4d6{'x2' if crit else ''} {w1}={sum(w1)}"
        wsum = sum(w1)
        if savage:
            w2 = roll(n, 6, gwf=True)
            if sum(w2) > wsum:
                txt += f", Savage reroll {w2}={sum(w2)} (kept)"
                wsum = sum(w2)
            else:
                txt += f", Savage reroll {w2}={sum(w2)} (discarded)"
        bonus = 16 if gu["raging"] else 13
        total_dmg = wsum + bonus
        if frenzy:
            fr = roll(6 if crit else 3, 6)
            txt += f", Frenzy 3d6{'x2' if crit else ''} {fr}={sum(fr)}"
            total_dmg += sum(fr)
        if brutal:
            br = roll(2 if crit else 1, 10)
            txt += f", Brutal Strike d10{'x2' if crit else ''} {br}={sum(br)}"
            total_dmg += sum(br)
        log(f"   {label}: {shown} +13 = {total} vs AC 17: {'CRITICAL HIT' if crit else 'hit'} -> {txt} +{bonus} = {total_dmg}")
        if crit:
            gs["disadv_until_guts_turn"] = True
            if can_hew:
                gu["hew"] = True
            log("      Slasher crit: Goblin Slayer has disadvantage on attacks until Guts's next turn." + (" Hew is up." if can_hew else ""))
        # Goblin Slayer's reaction: Parry
        if gs["reaction"] and gs["dice"] > 0:
            p = d(10)
            red = p + 4
            gs["reaction"] = False
            gs["dice"] -= 1
            total_dmg = max(total_dmg - red, 0)
            log(f"      PARRY: d10 {p} +4 = {red} off -> {total_dmg} gets through (dice left {gs['dice']})")
        damage_gs(total_dmg, label)
        return True

    def gs_stab(adv, label, sa_available, melee=True, riposte=False):
        """Returns (hit, sa_used)."""
        nonlocal winner
        disadv = gs["disadv_until_guts_turn"]
        if adv and disadv:
            adv = False; disadv = False
        r1, r2 = d(20), d(20)
        if adv:
            nat = max(r1, r2); shown = f"2d20 ({r1},{r2}) high"
        elif disadv:
            nat = min(r1, r2); shown = f"2d20 ({r1},{r2}) low"
        else:
            nat = r1; shown = f"d20 {r1}"
        total = nat + 10
        crit = nat == 20
        hit = crit or (nat != 1 and total >= gu["ac"])
        if not hit:
            log(f"   {label}: {shown} +10 = {total} vs AC 18: MISS")
            return False, False
        w = roll(2 if crit else 1, 6)
        dmg = sum(w) + 6
        txt = f"1d6{'x2' if crit else ''} {w} +6"
        sa_used = False
        if riposte:
            rp = roll(2 if crit else 1, 10)
            dmg += sum(rp)
            txt += f", Riposte d10{'x2' if crit else ''} {rp}"
        if sa_available and adv and not disadv:
            s = roll(4 if crit else 2, 6)
            dmg += sum(s)
            txt += f", Sneak Attack 2d6{'x2' if crit else ''} {s}={sum(s)}"
            sa_used = True
        log(f"   {label}: {shown} +10 = {total} vs AC 18: {'CRITICAL HIT' if crit else 'hit'} -> {txt} = {dmg}")
        damage_guts(dmg, label, crit=crit)
        if winner:
            return True, sa_used
        # poison
        if gs["blade_poisoned"]:
            gs["blade_poisoned"] = False
            sv = d(20)
            if sv + 10 >= 14:
                log(f"      Poison: Guts Con save d20 {sv} +10 = {sv+10} vs DC 14: resists")
            else:
                p = roll(4 if crit else 2, 8)
                log(f"      Poison: Guts Con save d20 {sv} +10 = {sv+10} vs DC 14: FAILS -> 2d8 {p} = {sum(p)} poison, and he is Poisoned until the end of Goblin Slayer's next turn")
                damage_guts(sum(p), "poison")
                gu["poisoned"] = True
                gu["poison_clears_after_gs_turn"] = rnd + 1
        # Guts's reaction: Retaliation
        if winner is None and gu["reaction"]:
            gu["reaction"] = False
            log("      RETALIATION (reaction):")
            guts_swing(gu["raging"], "   Guts, Retaliation", savage=True, can_hew=False)
        return True, sa_used

    while winner is None and rnd < 30:
        rnd += 1
        log(f"\n===== ROUND {rnd} =====  GS {gs['hp']}/{gs['maxhp']} | Guts {gu['hp']}/{gu['maxhp']}{' (0 HP, armor)' if gu['down'] else ''}")
        for who in order:
            if winner:
                break
            if who == "gs":
                # ---------- Goblin Slayer's turn ----------
                gs["reaction"] = True
                gs["disadv_until_guts_turn"] = gs["disadv_until_guts_turn"]  # persists until Guts's turn
                log(f"-- Goblin Slayer's turn ({gs['hp']} HP, dice {gs['dice']}, Second Wind {gs['sw']})")
                bonus_used = False
                if dist > 5:
                    dist = 0
                    bonus_used = True
                    log("   Cunning Action: Dash (bonus action) and closes 60 ft to Guts.")
                if not bonus_used:
                    if gs["hp"] <= 160 and gs["sw"] > 0:
                        h = d(10) + 16
                        gs["sw"] -= 1
                        gs["hp"] = min(gs["hp"] + h, gs["maxhp"])
                        log(f"   Second Wind (bonus action): 1d10+16 = {h} -> {gs['hp']} HP")
                    elif not gs["blade_poisoned"] and gs["doses"] > 0:
                        gs["doses"] -= 1
                        gs["blade_poisoned"] = True
                        log(f"   Applies a fresh dose of poison to the blade (bonus action). Doses left {gs['doses']}.")
                    elif gs["hp"] <= 200 and gs["hitdice"] > 0:
                        h = d(10) + 3
                        gs["hitdice"] -= 1
                        gs["hp"] = min(gs["hp"] + h, gs["maxhp"])
                        log(f"   Durable (bonus action): spends a Hit Die, 1d10+3 = {h} -> {gs['hp']} HP")
                attacks = 3
                if gs["surge"] > 0:
                    gs["surge"] = 0
                    attacks = 6
                    log("   ACTION SURGE: six attacks this turn.")
                sa_available = True
                vex = False
                shield_bash_done = False
                for i in range(attacks):
                    if winner:
                        break
                    adv = gu["raging"] or vex
                    hit, sa_used = gs_stab(adv, f"Stab {i+1}", sa_available)
                    if sa_used:
                        sa_available = False
                    if hit:
                        vex = True
                        if not shield_bash_done and not gu["down"]:
                            shield_bash_done = True
                            s1, s2 = d(20), d(20)
                            s = max(s1, s2) if gu["raging"] else s1
                            if s + 11 >= 18:
                                log(f"      Shield Master bash: Guts Str save {'2d20 (' + str(s1) + ',' + str(s2) + ') high' if gu['raging'] else 'd20 ' + str(s1)} +11 = {s+11} vs DC 18: holds his footing")
                            else:
                                gu["prone"] = True
                                log(f"      Shield Master bash: Guts Str save {'2d20 (' + str(s1) + ',' + str(s2) + ') high' if gu['raging'] else 'd20 ' + str(s1)} +11 = {s+11} vs DC 18: FAILS, Guts is knocked prone")
                # poison set this turn clears at the end of NEXT turn; poison set last turn clears now
                if gu["poisoned"] and gu.get("poison_clears_after_gs_turn", 99) <= rnd:
                    gu["poisoned"] = False
                    log("   (The poison wears off Guts at the end of this turn.)")
            else:
                # ---------- Guts's turn ----------
                gu["reaction"] = True
                gs["disadv_until_guts_turn"] = False
                if gu["down"]:
                    ds1, ds2 = d(20), d(20)
                    ds = max(ds1, ds2)  # Durable: advantage on death saves
                    if ds == 20:
                        gu["hp"] = 1; gu["down"] = False; gu["death_fail"] = 0
                        log(f"-- Guts's turn: DEATH SAVE 2d20 ({ds1},{ds2}) high = 20! He comes back to 1 HP.")
                    elif ds >= 10:
                        gu["death_succ"] += 1
                        log(f"-- Guts's turn: death save 2d20 ({ds1},{ds2}) high = {ds}: success ({gu['death_succ']} successes, {gu['death_fail']} failures). The armor keeps him moving.")
                    else:
                        gu["death_fail"] += 1
                        log(f"-- Guts's turn: death save 2d20 ({ds1},{ds2}) high = {ds}: FAILURE ({gu['death_fail']}/3)")
                        if gu["death_fail"] >= 3:
                            winner = "Goblin Slayer"
                            break
                log(f"-- Guts's turn ({gu['hp']} HP{', poisoned' if gu['poisoned'] else ''})")
                bonus_used = False
                if gu["prone"]:
                    gu["prone"] = False
                    log("   Stands up (half his movement).")
                if not gu["raging"]:
                    gu["raging"] = True
                    bonus_used = True
                    log("   RAGE (bonus action). The Berserker Armor bites down: resistance to everything but psychic, nothing can stop him.")
                    if dist > 5:
                        dist = 0
                        log("   Instinctive Pounce 20 ft + 40 ft of movement: closes the gap.")
                elif dist > 5:
                    dist = 0
                    log("   Moves to Goblin Slayer.")
                swings = 2
                surge_now = False
                if gu["surge"] > 0 and dist <= 5 and gu["raging"]:
                    gu["surge"] = 0
                    swings = 4
                    surge_now = True
                    log("   ACTION SURGE. Reckless Attack. Four swings.")
                else:
                    log("   Reckless Attack.")
                first_hit = False
                for i in range(swings):
                    if winner:
                        break
                    brutal = (i == 1) and not gu["poisoned"]
                    adv = not brutal
                    hit = guts_swing(adv, f"Swing {i+1}{' (Brutal Strike)' if brutal else ''}", brutal=brutal, frenzy=not first_hit, savage=not first_hit)
                    if hit:
                        first_hit = True
                if winner:
                    break
                if not bonus_used and gu["hew"]:
                    gu["hew"] = False
                    bonus_used = True
                    log("   HEW (bonus action after the crit):")
                    guts_swing(True, "Swing, Hew", savage=False)
                elif not bonus_used and gu["hp"] <= 128 and gu["sw"] > 0 and not gu["down"]:
                    h = d(10) + 8
                    gu["sw"] -= 1
                    gu["hp"] = min(gu["hp"] + h, gu["maxhp"])
                    log(f"   Second Wind (bonus action): 1d10+8 = {h} -> {gu['hp']} HP")
                gu["hew"] = False
    return winner, rnd


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "mc":
        n = int(sys.argv[2])
        wins = {"Guts": 0, "Goblin Slayer": 0, None: 0}
        rounds = []
        for _ in range(n):
            w, r = fight(verbose=False)
            wins[w] += 1
            rounds.append(r)
        print(wins, "avg rounds", sum(rounds) / len(rounds))
    else:
        w, r = fight(verbose=True)
        print("\n".join(LOG))
        print(f"\nWINNER: {w} after {r} rounds")
