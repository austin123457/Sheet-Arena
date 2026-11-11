# Until It Is Done

*Adam Smasher vs the Doom Slayer.* The chalkboard's first night is over, a stool that has stood empty since [The Rage That Does Not End](kratos-vs-slayer.md) is filled, and at the end somebody new comes through the door. It comes after [The Ledger](anderson-vs-kratos.md).

The fight is real: the most dramatic of 400 runs of `python battle.py 1v1 smasher slayer`, picked by `fight_log.py smasher slayer 400`. The Slayer wins about 99% of the time, usually inside three rounds. This one goes five. Smasher shoots first and takes 148 off him before he moves, makes all three saves against the BFG, and isn't there for the Crucible's first two swings. Relentless Rage holds twice and fails the third time, so the Slayer takes his last turn at 0 hit points with two death saves failed: Rage Beyond Death, and the Crucible's last charge. It hits for 88, and anything the Crucible leaves at 150 or fewer dies. The same line on his sheet says he dies when the Rage ends. The sim stops before that. The story doesn't.

The two bouts left on the chalkboard went the way the arena usually sends them: Arthur and Guts beat Spike and Smasher (72% of 1,000 runs), and Link beat Jin again (every run).

<details>
<summary>The round-by-round log</summary>

```
winner: Slayer in 5 rounds
R1 Smasher | {Smasher: surges 2->1, sandy 0->3, dice 6->5} {Slayer: prone False->True} hit 0 piercing hit 17 piercing hit 13 piercing CRIT 44 piercing hit 16 piercing hit 13 piercing hit 19 piercing hit 16 piercing hit 10 piercing  || Smasher 224  Slayer 210
R1 Slayer  | {Slayer: raging False->True, bfg 3->1} [BFG -> Smasher: 62 force] [BFG -> Smasher: 54 force]  || Smasher 108  Slayer 210
R2 Smasher | {Smasher: sw 4->3, surges 1->0, sandy 3->2, dice 5->4} CRIT 29 piercing hit 17 piercing hit 12 piercing hit 14 piercing hit 20 piercing hit 19 piercing hit 17 piercing hit 14 piercing hit 10 piercing  || Smasher 129  Slayer 58
R2 Slayer  | {Slayer: sw 3->2, crucible 3->2} miss  || Smasher 129  Slayer 66
R3 Smasher | {Smasher: sw 3->2, sandy 2->1, dice 4->3} {Slayer: prone False->True} hit 1 piercing CRIT 43 piercing hit 18 piercing <Slayer DROPS TO 0> <Slayer back up at 28> hit 12 piercing hit 14 piercing  || Smasher 150  Slayer 14
R3 Slayer  | {Slayer: sw 2->1, crucible 2->1} miss  || Smasher 150  Slayer 25
R4 Smasher | {Smasher: sw 2->1, sandy 1->0, dice 3->2} hit 3 piercing hit 21 piercing <Slayer DROPS TO 0> <Slayer back up at 28> hit 18 piercing hit 17 piercing  || Smasher 177  Slayer 11
R4 Slayer  | {Slayer: sw 1->0, bfg 1->0} [BFG -> Smasher: 64 force]  || Smasher 113  Slayer 24
R5 Smasher | {Smasher: sw 1->0, dice 2->1} {Slayer: rbd False->True, death_fail 0->1} hit 0 piercing hit 22 piercing <Slayer DROPS TO 0> <Slayer back up at 0> hit 14 piercing <Slayer DROPS TO 0> <Slayer back up at 0> hit 16 piercing  || Smasher 143  Slayer 0
R5 Slayer  | {Slayer: crucible 1->0, death_fail 1->2} ** Crucible ** hit 88 slashing  || Smasher 55  Slayer 0
```

HP includes temporary HP: the Slayer starts at 298 and 60. A drop to 0 is logged just before the attack that caused it. The hits for 0, 1 and 3 are the Slayer's Reaction taking most of a bullet. Smasher's HP climbing at the start of each of his turns is Second Wind, all four of them; the Slayer's `sw` is his own three. `sandy` is the Sandevistan's rounds, and Smasher's dice go on Trip Attacks (the Slayer is prone in rounds 1 and 3). The BFG's numbers are halves: Smasher made every save. "Back up at 0" in round 5 is Rage Beyond Death: at 0 hit points while raging, the Slayer keeps acting and makes death saves. The first failure is the bullet that hit him at 0, the second is the save at the start of his last turn. The Crucible's 88 leaves Smasher at 55, and the Crucible's own rule ends it.

</details>

---

## The Bar

**Smasher**

RECORD, THIS LOCATION: 0 – 2.

He had run the number every cycle since the chalk went up, and it had not changed. The slate by the door still showed the first night's card, and under each line the old man had added the result in his careful hand. Under SPIKE & SMASHER v ARTHUR & GUTS it said *ARTHUR & GUTS.* Under LINK v JIN it said *LINK,* and after it, *(again).* Under ANDERSON v KRATOS it said *KRATOS,* and after that, smaller, *(mostly).*

Twice now the cowboy had been on the other side of it. The cowboy was four stools down, coughing into a bottle of milk.

TARGET: MORGAN, ARTHUR. Chrome detected: none. Life expectancy: under six months. RECORD VS. SMASHER: 2 – 0.

"You're doing it again," said Spiegel, two stools down, without turning his head.

Smasher's fingers stopped tapping.

"Counting. You tap when you count." Spiegel blew smoke at the ceiling. "Look, partner. We lost. It happens to me all the time."

"Do not call me that."

"I'm just saying."

Smasher did not answer. He was looking at the ninth stool.

It stood at the far side of the god, and nobody sat on it. At the start of every cycle the old man set a glass in front of it. At the end of every cycle he poured it out untouched, rinsed it, and polished it with the others. Smasher had logged this eleven times. He had not asked. Asking was a thing meat did.

On the twelfth cycle the door opened.

THERMAL: 1 ORGANIC.

It had to turn its shoulders to get through the frame. It was plated head to foot in green, scarred and scorched, with a visor of gold glass and nothing showing behind it. One shoulder plate was a newer green than the rest. There was ash in the seams of the armor, and his spectrometer could not match it to anything that burned on Earth.

TARGET: UNKNOWN. Male. Armor: alloy not on file. Power source: not on file. Chrome detected:

The scan took longer than it should have.

None. Under the plate there was muscle, bone and blood, one hundred percent.

*Meat*, the software concluded. Then, because it had been patched twice since arriving at this location: THREAT ASSESSMENT: RECALCULATING.

The room had gone quiet, but not the way it had gone quiet for him. No hands went to weapons. The priest had stopped in the middle of a sentence and was looking at the green armor with his head a little to one side, like a man listening to something a long way off.

"That one's been in Hell," the priest said softly. "God help it."

The god had turned on his stool. It was the first time Smasher had seen him turn for anyone.

The armored man walked the length of the bar without a sound and sat down on the ninth stool. The glass was already there. He did not touch it.

"You were long at your hunt," the god said.

The helmet turned toward him. That was all.

"Hm," said the god, as if it had been an answer, and went back to his mead.

At the other end of the bar the old man set down the glass he was polishing. *Click.* He came out from behind the counter, wiped the slate clean with his sleeve, three lines and three results, and picked up the chalk.

> **TONIGHT:**
>
> SMASHER v THE SLAYER

Spiegel whistled, low.

"Partner."

"Do not—"

"No, I mean it this time. Listen." Spiegel was looking at the green helmet, and he wasn't smiling. "Whatever your computer's telling you about that guy, it's wrong."

"He does not stop," the god said, to his cup.

"Everything stops," said Smasher. "I have stopped everything I was ever pointed at. For seventy years."

"'Cept twice," the cowboy said mildly.

Smasher stood. The steel stool sighed. He walked down the bar until he was standing over the ninth stool, and he looked down at the gold visor from two feet above it.

"You are meat," he said, "in a can."

The helmet tilted up.

**The Slayer**

He had seen this before.

Hell did it to its own. It took a thing of flesh and bolted a launcher to its shoulders and a cannon to its arm. It plated the skull and lit the eyes red. The men who helped had called it progress, and they had given the results names. He had killed every one he could find.

Those had been made. Somebody had held them down.

Nobody had held this one down. This one had walked in and asked for it, and gone on asking until there was nothing left to cut away. It was proud of it.

The old man's glass sat where it was. There was nothing in a glass for this.

He stood up.

---

## Meat

**Smasher**

Sixty feet of sand, and a white sky.

SANDEVISTAN: ENGAGED.

The world stopped. A grain of sand kicked up by the green one's boot hung in the air and stayed there. Smasher had eighteen seconds of this, and he did not intend to need them.

He fired. Nine rounds left the chain gun in the time it took the meat to begin to lift its arm. The first one flattened on a forearm plate that had somehow got in the way, at that speed. The rest went in. He put one through the seam under the visor. He put one through the back of the knee, on purpose, and the leg folded.

The glow in the seams of the armor guttered and went out.

TARGET: PRONE. DAMAGE DEALT: 41%.

THREAT ASSESSMENT: LOW, the software decided.

**The Slayer**

Down.

Up.

Eight holes. The suit was telling him about each of them. He did not listen. The Rage came up, the thing from the deepest pit that had never stopped burning in him, and it washed the holes out of his mind like water off a fire.

The machine was fast. It had gone thin and bright at the edges, like something seen through heat. It did not matter how fast. He pulled the BFG off his back and fired at where it was, and then at where it went.

Green.

**Smasher**

He saw the first one coming. In the Sandevistan he saw everything coming. It was a ball of something his sensors returned as [NO VALUE], drifting across the sand at walking pace, and he stepped out of its path with room to spare.

It did not need to hit him. It went by twelve meters off, and the light came off it in ropes and found him anyway. Then the second one did the same.

CORE INTEGRITY: 48%.

He had been standing in Arasaka Tower in 2023 when the bomb went off. He still had the log from that day. He opened a new one.

REPAIR RESERVE: 3 OF 4.

He burned the second surge. Nine more rounds, and all nine hit. He watched each one go in. He watched blood come out of the far side of the suit, dark and ordinary.

TARGET INTEGRITY: 16%.

The meat was walking toward him. It had put the cannon away. There was something red in its hand.

**The Slayer**

The Crucible. Argent fire from the heart of Hell, with a hilt on it.

He swung, and the machine was not there. The blade took a long red bite out of the air, and the sand under it ran to glass.

He turned. Bullets. The knee again.

Down.

One through the chest, and something in there stopped.

The Rage started it again.

Up.

He swung. The machine was six feet to the left of where it had been, and the blade went past it.

Two swings. The blade held three.

**Smasher**

TARGET: NEUTRALIZED.

ERROR: TARGET ACTIVE.

He had seen that error once before, standing outside a wooden door. He had not liked it then.

He had the telemetry. A burst to the center of the chest, and the heart inside the suit had stopped. His audio had picked up the silence where it had been. Then it had started again, louder, and the meat had got up and swung that thing at him a second time.

SANDEVISTAN: 0. HEAT SINK: VENTING.

The world came back up to speed. The sand finished falling.

REPAIR RESERVE: 1 OF 4. CORE INTEGRITY: 79%.

He was winning. The numbers said so, 79 to 7. He fired four more. The heart stopped again.

It started again.

TARGET INTEGRITY: 3%. TARGET: ACTIVE.

**The Slayer**

The machine was mending. Every time he looked, there was less wrong with it.

One swing left in the blade. One swing would not be enough while it was whole.

He put the blade away and brought up the cannon. One cell.

Green.

**Smasher**

The jump boosters took him most of the way clear. Most.

CORE INTEGRITY: 50%.

REPAIR RESERVE: 0 OF 4. CORE INTEGRITY: 64%.

That was the last of it. It did not matter. Sixty-four to nothing was still arithmetic.

Four rounds. The first flattened on the forearm plate again. The second went in. The third went in, and the heart stopped.

He waited for it to start.

It did not start.

TARGET: NEUTRALIZED.

He waited for the error. It did not come. The software was satisfied. There was no pulse on audio and no pressure in the vessels on thermal. Most of the blood was in the sand. By every measure Adam Smasher owned, the thing in the green suit was dead.

It was standing up.

He put the fourth round through it to be sure. It rocked on its heels. It did not fall.

This was not a comeback. He knew what those looked like. He had the cowboy on file. There was nothing in there coming back. It was only not stopping.

*Metal is better than meat.* He had said it for seventy years, because meat quits. Meat gets tired. Meat gets scared, and bleeds out, and lies down. He had lain down once himself, in pieces, and when they offered him steel he had taken it and never looked back. Steel does not quit.

He ran the scan on the thing in front of him one more time, and found no steel in it anywhere.

**The Slayer**

Nothing left.

He knew this place. He had been here before. They had not been able to kill him then either. They had dropped a temple on him and shut him in a stone box, because it was all they could do.

There was no temple here.

Something on his left side went dark, and then something else. One more and that would be all. He counted it the way he counted shells.

The machine was not moving. It was looking at him. The lenses in the red eyes kept turning, like it was trying to read something written too small.

He drew the Crucible.

It did not step aside this time. Whatever had made it fast was spent.

The blade went in at the shoulder, under the launcher. It went through the cannon arm and into the chest, and the fire went looking, the way it always did. It had never cared what a thing was made of.

**Smasher**

CORE INTEGRITY: 24%.

ARMOR REGENERATION MATRIX: STANDING BY. THRESHOLD NOT MET.

It was a survivable hit. He had fought on with less than 24 percent. The matrix was waiting on a number he had not reached.

The fire did not wait. It was in the plating and it was moving. It was not melting the steel. The steel was simply *less*, a section at a time, as though it had never been there. It went through the frame like it knew the way. It was looking for something.

It found the biopod.

PAIN EDITOR: OFFLINE.

He had not felt anything since 2023. He had forgotten how loud it was.

The last thing his optics logged was the green suit, upright, with the red blade going dim in its hand and no pulse.

LAST LOG ENTRY: TARGET ACTIVE.

**The Slayer**

*Until it is done.*

It was done.

He stood over the machine while the fire finished. There was not much to stand over afterward.

He waited for the next one. There was always a next one. He listened for it. The sand was empty in every direction, and for once nothing, anywhere, was screaming.

The Rage looked for something to burn and did not find it. He knew what was holding him up, and he knew what would happen when it went.

The god had said something to him once, lying in this same sand with the same blade in him. *It will not end. Unless you let it.*

He got the photograph out. It took three tries, because the hand would not close. He looked at it until he could not see it.

Then he sat down in the sand with his back to what was left of the machine, and let it.

---

## After

**Smasher**

SYSTEM REBOOT.

CORE INTEGRITY: 100%. ARMOR: 100%. ORDNANCE: 100%.

RECORD, THIS LOCATION: 0 – 3.

A wooden door, and yellow light around the frame. He turned sideways and ducked.

They were all where he had left them. On the ninth stool sat the green suit, whole, with the glass in front of it. The slate by the door said *THE SLAYER.* After it, smaller, as if added later: *(standing).*

Smasher sat down. The coolant was waiting, chilled to the correct temperature. He did not drink it.

"Your heart stopped," he said.

Every head at the bar turned, and then the gold visor did.

"I have the log. Six seconds before you cut me. No pulse. No pressure." His fingers were tapping. He stopped them. "Meat does not do that."

The helmet looked at him for a long moment. Then it turned back to the bar. It was not an answer. Smasher logged it anyway.

"You have it backward," said the god.

He had not looked up from his mead. He was turning one hand over on the counter, the gray one, looking at the palm.

"You believe it is the steel that does not stop. It was never the steel." He closed the hand. "I have had none in me at all."

"Amen," said the priest, cheerfully, and the god gave him a look.

"This is where you say 'good fight,' partner," Spiegel said.

"Do not call me that."

Smasher queried the sentence. *Metal is better than meat.* It returned TRUE. It had returned TRUE every time for seventy years. It was the only line in him that he had written himself.

He did not delete it. He flagged it: REVIEW.

Then he noticed the glass in front of the ninth stool. It was half empty. Nobody in the room had seen the helmet come off. He checked his own footage, and found a gap in it eleven seconds long.

He drank his coolant.

**Link**

Link saw it in the glasses first.

The old man hung them over the bar when he had polished them, a long row, and each one held the room in it, small and upside down: the lamp, the red eyes of the steel man, the gold visor, Jin's sleeve beside him.

Beside Jin's sleeve, in every glass, there was an empty stool.

He looked down at his hands. They were there. He looked up at the glasses. They were not.

He had seen this once before, in water.

He put down his milk.

Something was coming in under the door. It was water, a thin clear sheet of it, spreading across the boards without a sound and without soaking in. It lay there an inch deep and perfectly flat, and the lamplight in it looked like a sky. The cowboy lifted his boots onto the rail of his stool and said a word under his breath.

The door opened.

It was Link's height. It had his cap and his tunic and his boots, his shield on its back and the hilt of his sword over its shoulder, and all of it was the same flat black, as if someone had cut his shape out of the room and left the hole standing in the doorway. Its eyes were red.

All down the bar, hands went to weapons. The priest's went into his coat, and the big swordsman's found his hilt. The one in green armor had come up off his stool without a sound. The steel man's cannon began its rising whine, and then it faltered.

"There is nothing there," the steel man said. "No heat. No mass."

"I'm looking right at it, partner," said Spike.

"So am I."

*Click.* The old man had set down his glass.

"Not in here," he said.

The shadow had not looked at any of them. It walked down the length of the bar, over the water, and left no ripple. There was a stool on Link's other side that had not been there a moment ago. It sat.

The old man looked at it a little longer than he looked at most people. Then he set a glass in front of it: water, full to the brim and perfectly still.

"It's paid for," he said.

Link looked into the shadow's glass. His own face looked back up at him out of it.

"Friend of yours?" Spike asked.

"Mine," said Link.

He reached for his milk. Beside him a black hand reached for the water, at the same moment, in the same way. He stopped. It stopped. He lifted the milk an inch off the bar, and the water rose an inch.

On his other side Jin, very quietly, moved his sake out of the way.

By the door, the old man was looking at the slate. He had not picked up the chalk.

Not yet.
