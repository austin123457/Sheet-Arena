# Sheet Arena

D&D 5e (2024 rules) character sheets for fictional characters, built canon-first, and a dice-driven arena that fights them against each other.

Sixteen fighters, one sheet each: Goblin Slayer, Guts, Kyle Crane, Itachi Uchiha, Adam Smasher, Jin Sakai, Might Guy (the canon merge), the Doom Slayer, Link the Hero of Time, Battle Beast, Alexander Anderson, Arthur Morgan, Spike Spiegel, Talion, V, and Kratos. The sheets are PDFs in `sheets/pdf/`; the scripts that render the ones Claude built are in `sheets/build/` (reportlab). Caleb's sheets (Smasher, Jin, Crane v3, Battle Beast, Arthur, Talion v2) are PDFs only.

## Run a fight

    python battle.py 1v1 slayer link -n 400
    python battle.py team slayer+guy smasher+jin
    python battle.py ffa                      # the whole roster
    python battle.py matrix -n 200            # every 1v1
    python battle.py solo link                # Link vs everyone at once
    python battle.py 1v1 v smasher            # V picks his OS; v-sandy / v-deck force it
    python battle.py list

Dice come from the OS (`secrets`), nothing is seeded, and a fight caps at 40 rounds and counts as a draw.

## The rulings the arena uses

- Open sand, daylight, 60 ft apart, everyone fresh off a long rest, no surprise. The walls are out of bounds.
- Teams and free-for-alls coordinate on "the wizard first, then the lowest."
- "Ignores Resistance" (Smasher's and Battle Beast's Irresistible Offense) does not pierce immunity. Only Night Guy and the Crucible are written to.
- Guy's Gate of Death and Anderson's Nail are desperation moves (under 70 HP); Crane's Beast Meter starts empty after a rest; the Fierce Deity's Mask only works in a boss's lair, so Link never has it here; Izanami needs the target to have struck Itachi on two separate turns, and then it ends the fight.
- Evasion works for everyone whose sheet has it (Jin, Guy, Spike): nothing on a made Dex save, half on a failed one, unless they're incapacitated.
- Anderson dies only to a single blow for his full 284 hit points, his heart torn out (see Kratos), or once the Nail is in and breaks. Down, he gets up at 30 at the start of his turn unless 20 radiant or fire landed on him since his last one.
- Kratos is the one fighter who uses the heart clause on Anderson's sheet: once Anderson is down, he grapples him and wins a Strength contest. His Blades of Chaos keep the fire coming so nothing regrows in between.
- Peak versions: living, healthy Itachi (the Edo body can't lose to anyone without a seal); canon Guy with Night Guy at 60d12.
- Itachi fights with his whole slot table (4/3/3/3/2/1/1/1/1) and concentration: genjutsu first (Tsukuyomi on whoever will probably fail it), Susanoo when what is coming would kill him, then Totsuka or Yasaka Magatama inside it, Amaterasu for the one who can't be reached, and once Susanoo is gone Dominate Person, Hold Person, Phantasmal Killer or Phantasmal Force. Shadow Clone every time he has a spare 4th-level slot (the clone opens with Mind Sliver before his save spells, and enemies can't tell which Itachi is real), Mislead when he's low, Mirror Image, Shield and Illusory Self, Hypnotic Pattern and Fireball for groups, Counterspell against 3rd-level spells and up (Anderson's Haste and Hold Monster, Talion's Steel Wind Strike and Conjure Barrage). Each Mangekyo casting costs a level of exhaustion (-2 on his d20 tests; six is death) and Susanoo ending costs two, as his sheet says; he never spends the level that would kill him. Left out: what does nothing on open sand (Misty Step, Disguise Self, Silent Image, Dispel Magic, the rituals) and what is strictly worse than something he has (Scorching Ray and the kunai below Fire Bolt, Tidal Wave below Fireball, Summon Beast and Summon Fey, whose concentration he always has a better use for).
- Battle Beast by his sheet: charm and fear immunity only while raging (no stun immunity), +27 on a natural 20, Hew after a crit or a kill, his Worthy Opponent has disadvantage attacking anyone else, Intimidating Presence (DC 22, a save each turn) on everyone not immune, paid for with Rage uses after the free one, and Glorious Death: one last swing at the worthy opponent who drops him for good.
- Talion has no army here: Brand works only on orcs and beasts, and his sheet says it doesn't matter against one foe. He plays it the sheet's way: mark first, Freeflow Counter every melee blow, bank six Might for Elven Rage, and spend a single Execution only on a foe at 30 HP or fewer.
- Crane's finisher (a claw hit that leaves an ordinary creature at 15 HP or fewer kills it) never fires here: his sheet excludes bosses, and everyone in this arena is one. The same goes for V's Suicide, System Collapse, Cyberpsychosis and Memory Wipe.
- V has one Operating System slot and picks before each fight: the Sandevistan by default, the cyberdeck against Jin, Battle Beast and Itachi (where it tested better). `v-sandy` and `v-deck` force one. Against Smasher he takes the Scalpel, because Smasher's sheet says 20 lightning from one source shorts him out (no Reactions, no Sandevistan until the end of his next turn), and Smasher's Counter-Sandevistan answers anyone who speeds up first (Anderson's Haste counts).

## Where the ladder stood on 6 Nov 2026 (300 fights per 1v1 cell, 500 free-for-alls)

1v1, by average win rate: Doom Slayer 91%, Link 86%, Anderson 75%, Smasher 65%, Kratos 63%, Guy 61%, V 57%, Battle Beast 55%, Itachi 54%, Talion 44%, Jin 42%, Crane 33%, Guts 30%, Arthur 27%, Spike 9%, Goblin Slayer 3%.

What breaks the pattern:
- Link and Anderson draw every time: Nayru's Love against a body that keeps getting up.
- Itachi is the upset machine. Tsukuyomi on a low Wisdom save ends a fight before it starts, so he beats the Slayer (79%), Anderson (84%), Battle Beast (90%), Guts (73%) and Talion (79%). He still loses to Smasher (Mage Slayer and the ICE), Arthur (who kills him before he casts) and Link.
- Talion v2's Freeflow Counter turns melee hits into misses and feeds his Might, so he beats the melee middle of the ladder: Guts (97%), Spike (100%), Crane (91%), Jin (78%), Battle Beast (66%), and Guy about half the time. Anything that shoots him (Smasher, Arthur) or out-hits his counters (the Slayer, Anderson, Link) still wins.
- Crane v3's claws (2d10+8, ignoring resistance, plus a bite) beat Jin and Guts about three times in four.
- V vs Adam Smasher is close to a coin flip (V about 40%), the fight his whole game builds to.
- Kratos beats Anderson nine times in ten (fire, then the heart) and V every time (V's blades can't get through Rage resistance and the shield Parry). He loses to the Slayer, Link, Battle Beast, Guy and Smasher.

Free-for-all with everyone: Link 71%, V 12%, Smasher 5%. Nobody beats the rest of the roster at once (solo is 0% for everyone; the crowd ends it in the first round).

## Raid bosses

Above the ladder sits the raid tier: everything from past the god-killers up to the moon, built as 5e monsters to fight a party, with Legendary Resistance, Legendary Actions and phases. They stay out of the ladder's matrix and free-for-all.

    python battle.py raid madara                    # the boss vs all sixteen at once
    python battle.py raid madara guy+itachi+slayer  # vs a party

- **Madara Uchiha** (`Madara_Uchiha_Raid.pdf`), CR 30 in two phases. Phase 1 is the Edo Tensei body: 700 HP regrowing 50 a turn, never killed by damage (at 0 it's pinned and Phase 2 starts), ended only by a seal: Itachi's Totsuka, through three Legendary Resistances. Phase 2 is the Ten-Tails jinchūriki: 900 HP, spells don't take, nothing under 100 damage in one hit does anything (Night Guy does), no instant kills, and on his fourth turn the Infinite Tsukuyomi takes everyone not under a Susanoo.
- Against the whole ladder he wins every time: the party burns Phase 1 too fast for the seal and can't finish Phase 2 before the moon. Slow parties stall into forty-round draws, and Itachi's seal lands about once in a hundred. Ten-Tails Madara fought on even terms with Six Paths Naruto, who tanks a moon-splitting beam in *The Last*, so the ladder isn't the tier that beats him.
- The raid tier is sized to the moon: next up are the Raditz-saga Z fighters (Roshi blew up the moon, and Yamcha by then out-powers him). Planet-level and above (Saiyan saga Vegeta onward, Frieza, Gurren Lagann) would be a third, cosmic division.

## How the code is shaped

- `sim/engine.py`: dice, the `Combatant` base class, `attack()` and `Fight`. Anything one fighter does to another's attack, save or turn is a hook on `Combatant` (listed at the top of the file): `incoming_attack`, `immune`/`ignore_imm`, `answer_standoff`, `retaliate` and the rest. Nothing patches the engine from outside.
- `sim/fighters/`: one file per sheet. Rules that other sheets check are traits on the class (`caster`, `evil`, `evasion`, `never_stunned`, `shrugs_stunning_strike`, `averts_eyes`, `humanoid`, `danger`...), not name lists. Conditions (charmed, frightened, dread, invisible, sapped...) and summons are handled by the engine for everyone.
- `sim/roster.py`: command-line names onto fighters.
- `sim/duels/`: the narrated single-fight loggers from the first bouts, kept for the round-by-round output format. Standalone.

To add a fighter: a new file in `sim/fighters/`, a line in `sim/fighters/__init__.py`, a name in `roster.py`, and the key in `ROSTER` in `battle.py`.

The flattening (Nov 2026) changed no results: on 5,564 seeded fights (every 1v1 pairing, both free-for-alls, every solo and 400 random teams) the old chain and the new layout produced the same winner, rounds, final HP and dice count for every fight. The rule fixes (Izanami, Evasion, Anderson) and the move to one sheet per character came after it, in a separate commit.

## Sheets

    cd sheets/build && python build_slayer.py      # writes ../pdf/Doom_Slayer_5e_Build.pdf

Needs `pip install reportlab pypdf` and the DejaVu fonts (`fonts-dejavu` on Debian/Ubuntu). Each build script is self-contained except the Guy, Slayer, Link, Anderson, Spike, V, Kratos and Madara ones, which `exec` the shared fonts, styles and helpers in `sheet_style.py`. Without the DejaVu fonts (Windows) it falls back to Calibri and Georgia, which is how `V_5e_Build.pdf` and `Kratos_5e_Build.pdf` were built.

## Tests

    pip install pytest && pytest
