# Sheet Arena

D&D 5e (2024 rules) character sheets for fictional characters, built canon-first, and a dice-driven arena that fights them against each other.

Fourteen fighters, one sheet each: Goblin Slayer, Guts, Kyle Crane, Itachi Uchiha, Adam Smasher, Jin Sakai, Might Guy (the canon merge), the Doom Slayer, Link the Hero of Time, Battle Beast, Alexander Anderson, Arthur Morgan, Spike Spiegel, Talion. The sheets are PDFs in `sheets/pdf/`; the scripts that render the ones Claude built are in `sheets/build/` (reportlab). Caleb's sheets (Smasher, Jin, Crane, Battle Beast, Arthur, Talion) are PDFs only.

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
- Itachi fights with his whole slot table (4/3/3/3/2/1/1/1/1) and concentration: genjutsu first (Tsukuyomi on whoever will probably fail it), Susanoo when what is coming would kill him, then Totsuka or Yasaka Magatama inside it, Amaterasu for the one who can't be reached, and once Susanoo is gone Dominate Person, Hold Person, Phantasmal Killer or Phantasmal Force. Shadow Clone every time he has a spare 4th-level slot (the clone opens with Mind Sliver before his save spells, and enemies can't tell which Itachi is real), Mislead when he's low, Mirror Image, Shield and Illusory Self, Hypnotic Pattern and Fireball for groups, Counterspell against 3rd-level spells and up (Anderson's Haste and Hold Monster, Talion's Steel Wind Strike and Conjure Barrage). Each Mangekyo casting costs a level of exhaustion (-2 on his d20 tests; six is death) and Susanoo ending costs two, as his sheet says; he never spends the level that would kill him. Left out: what does nothing on open sand (Misty Step, Disguise Self, Silent Image, Dispel Magic, the rituals) and what is strictly worse than something he has (Scorching Ray and the kunai below Fire Bolt, Tidal Wave below Fireball, Summon Beast and Summon Fey, whose concentration he always has a better use for).
- Battle Beast by his sheet: charm and fear immunity only while raging (no stun immunity), +27 on a natural 20, Hew after a crit or a kill, his Worthy Opponent has disadvantage attacking anyone else, Intimidating Presence (DC 22, a save each turn) on everyone not immune, paid for with Rage uses after the free one, and Glorious Death: one last swing at the worthy opponent who drops him for good.
- Talion has no army here: Brand works only on orcs and beasts, and his sheet says it doesn't matter against one foe. Every arena fighter counts as a named captain, so Execution's kill gives them a Con save.

## Where the ladder stood on 6 Nov 2026 (300 fights per 1v1 cell, 500 free-for-alls)

1v1, by average win rate: Doom Slayer 91%, Link 84%, Anderson 79%, Smasher 66%, Guy 62%, Battle Beast 59%, Jin 59%, Itachi 57%, Guts 46%, Arthur 38%, Crane 24%, Spike 19%, Talion 8%, Goblin Slayer 4%.

What breaks the pattern:
- Link and Anderson draw every time: Nayru's Love against a body that keeps getting up.
- Itachi is the upset machine. Tsukuyomi on a low Wisdom save ends a fight before it starts, so he beats the Slayer (79%), Anderson (81%), Battle Beast (93%), Guts (72%) and Talion (85%). He still loses to Smasher (Mage Slayer and the ICE, 1%), Arthur (who kills him before he casts, 0%) and Link (5%).
- Talion's 224 HP behind AC 17 and a +3 Con save are the trouble: Spike and Crane stun him out of his turns, and every hit he takes costs two Might, so Elven Rage rarely comes up against anyone who attacks often. He beats Goblin Slayer (88%) and sometimes Itachi.

Free-for-all with everyone: Link 62%, Anderson 6%, Smasher 6%, draws 20%. Nobody beats the rest of the roster at once (solo is 0% for everyone; the crowd ends it in the first round).

## How the code is shaped

- `sim/engine.py`: dice, the `Combatant` base class, `attack()` and `Fight`. Anything one fighter does to another's attack, save or turn is a hook on `Combatant` (listed at the top of the file): `incoming_attack`, `immune`/`ignore_imm`, `answer_standoff`, `retaliate` and the rest. Nothing patches the engine from outside.
- `sim/fighters/`: one file per sheet. Rules that other sheets check are traits on the class (`caster`, `evil`, `evasion`, `never_stunned`, `shrugs_stunning_strike`, `averts_eyes`, `humanoid`, `danger`...), not name lists. Conditions (charmed, frightened, dread, invisible, sapped...) and summons are handled by the engine for everyone.
- `sim/roster.py`: command-line names onto fighters.
- `sim/duels/`: the narrated single-fight loggers from the first bouts, kept for the round-by-round output format. Standalone.

To add a fighter: a new file in `sim/fighters/`, a line in `sim/fighters/__init__.py`, a name in `roster.py`, and the key in `ROSTER` in `battle.py`.

The flattening (Nov 2026) changed no results: on 5,564 seeded fights (every 1v1 pairing, both free-for-alls, every solo and 400 random teams) the old chain and the new layout produced the same winner, rounds, final HP and dice count for every fight. The rule fixes (Izanami, Evasion, Anderson) and the move to one sheet per character came after it, in a separate commit.

## Sheets

    cd sheets/build && python build_slayer.py      # writes ../pdf/Doom_Slayer_5e_Build.pdf

Needs `pip install reportlab pypdf` and the DejaVu fonts (`fonts-dejavu` on Debian/Ubuntu). Each build script is self-contained except the Guy, Slayer, Link, Anderson and Spike ones, which `exec` the shared fonts, styles and helpers in `sheet_style.py`.

## Tests

    pip install pytest && pytest
