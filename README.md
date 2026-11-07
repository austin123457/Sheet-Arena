# Sheet Arena

D&D 5e (2024 rules) character sheets for fictional characters, built canon-first, and a dice-driven arena that fights them against each other.

Thirteen fighters so far: Goblin Slayer, Guts, Kyle Crane, Itachi Uchiha, Adam Smasher, Jin Sakai, Might Guy (three versions: mine, Caleb's, and the canon merge), the Doom Slayer, Link the Hero of Time, Battle Beast, Alexander Anderson, Arthur Morgan, Spike Spiegel. The sheets are PDFs in `sheets/pdf/`; the scripts that render them are in `sheets/build/` (reportlab).

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
- Guy's Gate of Death and Anderson's Nail are desperation moves (under 70 HP); Crane's Beast Meter starts empty after a rest; the Fierce Deity's Mask only works in a boss's lair, so Link never has it here; Izanami needs the target to have struck Itachi on two separate turns.
- Peak versions: living, healthy Itachi (the Edo body can't lose to anyone without a seal); canon Guy with Night Guy at 60d12.

## Where the ladder stood on 6 Nov 2026 (300–400 fights per cell)

1v1, roughly: Doom Slayer, then Link, then Anderson, then Guy and Smasher, then Battle Beast and Jin, then Guts, then Itachi, then Crane, Arthur and Spike, then Goblin Slayer. The three that break the pattern: Link and Anderson draw every time (immunity vs regeneration), Itachi beats Guts and Crane with genjutsu, Arthur and Spike each kill Itachi before he casts.

Free-for-all with everyone: Link about 70–90%, the Slayer most of the rest. Nobody beats the rest of the roster at once.

## How the code is shaped

- `sim/engine.py`: dice, the `Combatant` base class, `attack()` and `Fight`. Anything one fighter does to another's attack, save or turn is a hook on `Combatant` (listed at the top of the file): `incoming_attack`, `immune`/`ignore_imm`, `answer_standoff`, `retaliate` and the rest. Nothing patches the engine from outside.
- `sim/fighters/`: one file per sheet. Rules that other sheets check are traits on the class (`caster`, `evil`, `evasion`, `never_stunned`, `shrugs_stunning_strike`, `averts_eyes`, `danger`...), not name lists.
- `sim/roster.py`: command-line names onto fighters.
- `sim/duels/`: the narrated single-fight loggers from the first bouts, kept for the round-by-round output format. Standalone.

To add a fighter: a new file in `sim/fighters/`, a line in `sim/fighters/__init__.py`, a name in `roster.py`, and the key in `ROSTER` in `battle.py`.

The flattening (Nov 2026) changed no results: on 5,564 seeded fights (every 1v1 pairing, both free-for-alls, every solo and 400 random teams) the old chain and the new layout produced the same winner, rounds, final HP and dice count for every fight. The known quirks it preserved are marked `NOTE:` in the fighter files.

## Sheets

    cd sheets/build && python build_slayer.py      # writes ../pdf/Doom_Slayer_5e_Build.pdf

Needs `pip install reportlab pypdf` and the DejaVu fonts (`fonts-dejavu` on Debian/Ubuntu). Each build script is self-contained except the Guy, Slayer, Link, Anderson and Spike ones, which `exec` the style header from `build_guy.py`.

## Tests

    pip install pytest && pytest
