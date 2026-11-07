# Sheet Arena

D&D 5e (2024 rules) character sheets for fictional characters, built canon-first, and a dice-driven arena that fights them against each other.

Thirteen fighters, one sheet each: Goblin Slayer, Guts, Kyle Crane, Itachi Uchiha, Adam Smasher, Jin Sakai, Might Guy (the canon merge), the Doom Slayer, Link the Hero of Time, Battle Beast, Alexander Anderson, Arthur Morgan, Spike Spiegel. Talion's sheet is in `sheets/pdf/` too but he isn't in the arena yet. The sheets are PDFs in `sheets/pdf/`; the scripts that render the ones Claude built are in `sheets/build/` (reportlab). Caleb's sheets (Smasher, Jin, Crane, Battle Beast, Arthur, Talion) are PDFs only.

## Run a fight

    python battle.py 1v1 slayer link -n 400
    python battle.py team slayer+guy smasher+jin
    python battle.py ffa                      # the whole roster
    python battle.py matrix -n 200            # every 1v1
    python battle.py solo link                # Link vs everyone at once
    python battle.py list

Dice come from the OS (`secrets`), nothing is seeded, and a fight caps at 40 rounds and counts as a draw.

## The rulings the arena uses

- Open sand, daylight, 60 ft apart, everyone fresh off a long rest, no surprise. The walls are out of bounds.
- Teams and free-for-alls coordinate on "the wizard first, then the lowest."
- "Ignores Resistance" (Smasher's and Battle Beast's Irresistible Offense) does not pierce immunity. Only Night Guy and the Crucible are written to.
- Guy's Gate of Death and Anderson's Nail are desperation moves (under 70 HP); Crane's Beast Meter starts empty after a rest; the Fierce Deity's Mask only works in a boss's lair, so Link never has it here; Izanami needs the target to have struck Itachi on two separate turns, and then it ends the fight.
- Evasion works for everyone whose sheet has it (Jin, Guy, Spike): nothing on a made Dex save, half on a failed one, unless they're incapacitated.
- Anderson dies only to a single blow for his full 284 hit points (heart-tearing isn't modelled: nobody here grapples) or once the Nail is in and breaks. Down, he gets up at 30 at the start of his turn unless 20 radiant or fire landed on him since his last one.
- Peak versions: living, healthy Itachi (the Edo body can't lose to anyone without a seal); canon Guy with Night Guy at 60d12.
- Itachi in the arena uses Susanoo (Yata Mirror, Totsuka), Tsukuyomi, Amaterasu, Izanami, Hold Person, Fireball, Mirror Image, Shield, Illusory Self and Fire Bolt. Not yet modelled from his sheet: Dominate Person, Phantasmal Killer, Mislead, Shadow Clone, Yasaka Magatama, Counterspell, Hypnotic Pattern and the Sneak Attack kunai.

## Where the ladder stood on 6 Nov 2026 (300 fights per 1v1 cell, 500 free-for-alls)

1v1, by average win rate: Doom Slayer 95%, Link 83%, Anderson 77%, Smasher 63%, Guy 60%, Jin 57%, Battle Beast 55%, Itachi 52%, Guts 41%, Arthur 32%, Crane 18%, Spike 13%, Goblin Slayer 2%.

What breaks the pattern:
- Link and Anderson draw every time: Nayru's Love against a body that keeps getting up.
- Itachi with Izanami working beats Anderson and Battle Beast (88%), Guts (76%) and Guy (56%), and takes the Slayer 19% of the time. He still loses to Smasher (Mage Slayer and the ICE, 2%), and Arthur and Spike usually kill him before he casts (Arthur wins 95%).
- Anderson, Itachi and Guy are the only ones who beat the Slayer with any regularity (14–20%).

Free-for-all with everyone: Link 68%, Smasher 8%, Anderson 5%, draws 15%; the Slayer almost never survives the crowd that goes for him. Nobody beats the rest of the roster at once (solo is 0% for everyone; twelve fighters end it in the first round).

## How the code is shaped

- `sim/engine.py`: dice, the `Combatant` base class, `attack()` and `Fight`. Anything one fighter does to another's attack, save or turn is a hook on `Combatant` (listed at the top of the file): `incoming_attack`, `immune`/`ignore_imm`, `answer_standoff`, `retaliate` and the rest. Nothing patches the engine from outside.
- `sim/fighters/`: one file per sheet. Rules that other sheets check are traits on the class (`caster`, `evil`, `evasion`, `never_stunned`, `shrugs_stunning_strike`, `averts_eyes`, `danger`...), not name lists.
- `sim/roster.py`: command-line names onto fighters.
- `sim/duels/`: the narrated single-fight loggers from the first bouts, kept for the round-by-round output format. Standalone.

To add a fighter: a new file in `sim/fighters/`, a line in `sim/fighters/__init__.py`, a name in `roster.py`, and the key in `ROSTER` in `battle.py`.

The flattening (Nov 2026) changed no results: on 5,564 seeded fights (every 1v1 pairing, both free-for-alls, every solo and 400 random teams) the old chain and the new layout produced the same winner, rounds, final HP and dice count for every fight. The rule fixes (Izanami, Evasion, Anderson) and the move to one sheet per character came after it, in a separate commit.

## Sheets

    cd sheets/build && python build_slayer.py      # writes ../pdf/Doom_Slayer_5e_Build.pdf

Needs `pip install reportlab pypdf` and the DejaVu fonts (`fonts-dejavu` on Debian/Ubuntu). Each build script is self-contained except the Guy, Slayer, Link, Anderson and Spike ones, which `exec` the shared fonts, styles and helpers in `sheet_style.py`.

## Tests

    pip install pytest && pytest
