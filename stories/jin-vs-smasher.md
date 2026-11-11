# What Decides It

*Jin Sakai vs Adam Smasher.* Smasher has one win at the bar, and he has worked out that he wasn't in it. Tonight the slate gives him what he asked for: one man, no chrome, no partner. Jin's stool has been empty since the night before. It comes after [At Sixty Feet](musashi-vs-smasher.md).

The fight is real: the most dramatic of the fights Jin won in 1,000 runs of `python battle.py 1v1 jin smasher`, picked by `fight_log.py jin smasher 1000 Jin`. This is the nearest thing to a coin flip Smasher has had. Jin took 52.6% of 4,000 runs through `battle.py`, and the usual fight is over inside four rounds. This one goes eight. Musashi lost this matchup every time because nothing on his sheet answers a bullet. Jin has two answers. Deflect Arrows takes 1d10 + 16 off the first shot that lands on him each round, and when that isn't enough he has five separate ways of not staying down. In this run he wins the Standoff before the first turn: one cut, a critical hit, 67 after the plating has taken its 6, and Smasher is at 70% before anyone has had a turn. Then Smasher goes first anyway and fires nine times with the Sandevistan and an Action Surge, and Jin drops from 215 to 78. Jin goes to 0 three times, in rounds 2, 3 and 7, and gets up three times: Last Stand, then Iron Will twice, the second on a Wisdom save he could have failed. Smasher spends everything he has: both Action Surges, the Sandevistan, all six of his dice, all four Second Winds and the armor matrix. In round 6, with none of it left, he lands one shot in four and Jin cuts that one out of the air. Going into the last turn it is 13 hit points to 12. It ends 19 to 0, and Jin has nothing left either.

<details>
<summary>The round-by-round log</summary>

```
winner: Jin in 8 rounds
R0 Jin     | CRIT 67 slashing  || Jin 215  Smasher 157
R1 Smasher | {Smasher: surges 2->1, sandy 0->3, dice 6->4} hit 0 piercing hit 16 piercing hit 18 piercing hit 14 piercing miss hit 22 piercing hit 18 piercing hit 18 piercing hit 18 piercing  || Jin 78  Smasher 157
R1 Jin     | {Jin: sw 4->3, resolve 8->7} hit 22 slashing miss hit 15 slashing hit 10 slashing miss hit 10 slashing  || Jin 94  Smasher 100
R2 Smasher | {Jin: last_stand True->False} {Smasher: sw 4->3, surges 1->0, sandy 3->2, dice 4->0} miss CRIT 53 piercing hit 18 piercing hit 14 piercing <Jin DROPS TO 0> <Jin back up at 108> miss hit 18 piercing hit 12 piercing hit 20 piercing miss  || Jin 45  Smasher 121
R2 Jin     | {Jin: sw 3->2, resolve 7->6} hit 24 slashing hit 16 slashing miss  || Jin 62  Smasher 81
R3 Smasher | {Jin: iron_n 0->1, resolve 6->4} {Smasher: sw 3->2, sandy 2->1} hit 0 piercing hit 13 piercing miss CRIT 43 piercing <Jin DROPS TO 0> <Jin back up at 22> CRIT 52 piercing  || Jin 22  Smasher 102
R3 Jin     | {Jin: sw 2->1, resolve 4->3} hit 26 slashing CRIT 14 slashing hit 12 slashing  || Jin 42  Smasher 50
R4 Smasher | {Smasher: sw 2->1, sandy 1->0} miss hit 0 piercing hit 15 piercing hit 18 piercing  || Jin 9  Smasher 71
R4 Jin     | {Jin: sw 1->0, resolve 3->2} miss hit 27 slashing miss  || Jin 26  Smasher 44
R5 Smasher | {Smasher: sw 1->0} miss hit 0 piercing miss hit 19 piercing  || Jin 7  Smasher 73
R5 Jin     | {Jin: recover 10->7} {Smasher: matrix True->False} CRIT 26 slashing hit 14 slashing hit 8 slashing  || Jin 18  Smasher 65
R6 Smasher | hit 0 piercing miss miss miss  || Jin 18  Smasher 65
R6 Jin     | {Jin: recover 7->4} CRIT 22 slashing hit 7 slashing hit 13 slashing  || Jin 41  Smasher 23
R7 Smasher | {Jin: iron_n 1->2, resolve 2->0} hit 1 piercing hit 18 piercing <Jin DROPS TO 0> <Jin back up at 22> hit 22 piercing miss  || Jin 22  Smasher 23
R7 Jin     | {Jin: recover 4->1} miss hit 11 slashing miss  || Jin 40  Smasher 12
R8 Smasher | hit 0 piercing hit 16 piercing hit 11 piercing miss  || Jin 13  Smasher 12
R8 Jin     | {Jin: resolve 0->1, recover 1->0} hit 9 slashing <Smasher DROPS TO 0> <Smasher OUT> hit 15 slashing  || Jin 19  Smasher 0
```

R0 is the Standoff. It happens before anyone's first turn, and `fight_log.py` prints it under whoever swung. A drop to 0 is logged just before the attack that caused it. Every `hit 0`, and the `hit 1` in round 7, is Deflect Arrows: once a round, the first shot that lands on Jin loses 1d10 + 16. A `miss` that still costs Jin hit points is a shot Smasher's Precision Attack turned into a hit, and its damage isn't printed. There is one in round 1, for 13, and three in round 2: the first is deflected, the second is the shot that drops him, and the third does 13. Smasher's `dice` pay for those and for two Trip Attacks, both of which Jin stood through. `sw` is Second Wind, for either of them. `sandy` is the Sandevistan, which runs three rounds. `last_stand` puts Jin back up at 108, more than he went down with. `iron_n` counts Iron Will: 2 Resolve to get up at 22, automatic the first time and a DC 15 Wisdom save the second. `resolve` also pays for the Heavenly Strike on his first hit of rounds 1 to 4. `recover` is his Recover Vitality pool of 10d10, three dice a turn once the Second Winds are gone. `matrix` is Smasher's armor regeneration: 40 temporary hit points the first time he is at 40 or under, and his totals from round 5 on include what is left of them. Jin never starts a turn above 100 hit points, so his Fighting Spirit goes unused.

</details>

---

## The Bar

**Smasher**

RECORD, THIS LOCATION: 1 – 3.

There were four files now, and the fourth was a win. He had run it more often than the other three together.

In the losses he was in every frame. In the win there was a gun, and a firing solution, and a man who walked sixty feet into both. He had tested it. He took himself out of the footage and mounted the gun on a wall, and the wall won in the same six rounds. He had put the note on that file himself. OPERATOR: NOT REQUIRED. It was the only one of the four notes he had not been able to close.

Two items were flagged REVIEW. One was a sentence he had been sure of for seventy years. The other was a cut.

There was a third item, which he could not flag because it was not his. It was pinned to the wall beside the slate: a bird at the top of a dead branch, and low on the stem a mark with legs.

He had identified the bird in the first cycle. SHRIKE. HABIT: IMPALES PREY ON THORNS. RETURNS TO IT LATER. He had taken the bird for himself and closed the query. Then the painter had touched his brush to the other mark and said that it got most of the way up, and the query had opened again. It was still open.

"You're tapping," Spiegel said.

He stopped.

Up the bar, beside the painter, a stool stood empty with a full cup in front of it. He had logged the Ghost going out one cycle ago. The door had stood open for four seconds, at an angle that gave him nothing.

LOCAL ARCHIVE: SAKAI, JIN. NO RECORD.

"The target has left early," he said.

"Mm," said the painter. He was grinding ink.

"I heard what you told him. At night. From above."

"Did I say above?" The painter looked at the ink stick. "I am getting old. I say all sorts of things."

At the end of the bar the old man set down the glass he was polishing. *Click.* He came round the counter, wiped the slate with his sleeve, and took up the chalk.

> **TONIGHT:**
>
> SMASHER v SAKAI

What Smasher had specified twelve cycles ago had not changed. One target. Organic. No chrome. No partner on either side, and nothing about it that would need a note. The last fight had met every term, and he had not been in it.

He added a term. He did not log what it was.

"Check the roof, big fella," the cowboy said. "And the loft. And under the bed."

"He is meat. Meat is warm." Smasher stood, and the stool that had been made for him creaked. "I have killed men in optical camouflage. I have killed men who paid for skin that could not be seen. Thermal found them. It is the one thing meat cannot turn off."

The priest had his book shut on one finger and his eyes closed. His lips were moving. Smasher did not tell him to stop. It had not worked the last time.

Over the bottles, the old man reached up with the broom handle.

Smasher turned sideways, and ducked, and went through the door.

---

## In the Rice

**Jin**

The water was a hand deep, and he had been lying in it long enough to stop feeling where it ended.

He had opened the door a night early, expecting sand and the white sky. There was a hillside instead. It was cut into terraces of rice under a three-quarter moon, with water standing in every paddy, and one pine at the top, and a wind coming down. He had stood there with his hand on the door. The old man poured what a man needed before he asked for it. Jin had not known that the door did it as well.

"It's paid for," the old man had said, behind him.

*From above*, Musashi had told him, and the red eyes had been on them both when he said it. So the pine was where the steel man would look first. Jin had walked past the pine and down three terraces. He lay down on his back between the rows, with the mask on and the water over his chest and his ears, and let the cold come in. He had done it on Tsushima, in worse water, with Mongols eating their supper a spear's length away. A man who lies in a paddy long enough is part of the paddy.

While he lay there he thought about the other thing Musashi had said.

*If it mattered. If there was a village behind me.*

Since Komoda, every time Jin had chosen how to fight, somebody else had stood to pay for the choice. A village paid, or Yuna, or Taka, who had paid all of it. That was why he had put the old way down. It had never been that the old way was wrong. It was that other people died of it.

There was no village behind this door. He had been killed twice on the far side of it himself, by a boy who drank milk, and both times he had woken at the bar with the sake already poured. Nobody here could be saved, and nobody could be lost. Whatever he chose tonight, he was the only one it could cost.

He could not remember the last time that had been true.

The sixty feet were not a choice. He had watched what they did to a better swordsman than he would ever be. He would cross those as the Ghost. What he did at the end of them was his own.

A line of yellow light opened at the top of the hill. The steel man turned sideways to come through it. The light closed.

The red eyes went to the pine, and stayed on it long enough that Jin nearly smiled under the water. Then they came down across the terraces. He felt them go over him, the way a man feels a cloud cross the moon with his eyes shut. They did not stop.

It came down along the dike. The bank gave a little under each step, and the water he lay in shook, and he counted the steps by it. Four paces. Three.

At two he could have done it. The tanto, from below, up under the plate behind the knee, and then the seam beneath the jaw that Musashi had found for him in the glass. The steel man would never have known the hour it started. Afterward it would have had a reason, as it had a reason for each of the others. And Jin would have learned nothing about himself that he had not known on the day he poisoned a garrison.

He stood up.

He stood up out of the rice at a sword's length from it, in the open, under the moon, with the water running out of his armor. He put his hand on the hilt and did not draw.

"Jin Sakai," he said. "Of Tsushima."

The red eyes came round and found him. He waited for the gun. It was the first thing his father had taught him, and the last thing he had thought he would ever use again: let the other man begin, and finish before he does.

The wind dropped.

The gun arm moved. It was faster than anything he had ever seen move. But it had started from rest, and he had been watching for nothing else.

He drew into the cut. It went in under the gun arm, where two plates met, and came out through the collar. It was a cleaner cut than the Ghost had ever needed to make.

Then the steel man was not there. The water it had been standing in was still falling back into the shape of its feet.

**Smasher**

He had scanned the pine first. THERMAL: 1 SOURCE. UPPER BRANCH. MASS: 40 GRAMS. It was a bird. He did not query the species.

The terraces had returned nothing. WATER: 11 DEGREES. RICE. MUD. Nothing on the hill was warm except the bird and himself.

Then, at five feet, part of the paddy stood up.

TARGET: SAKAI, JIN. Male. Age: 30. Chrome detected: none. Armor: lacquered leather, iron plates, silk cord. Blades: 2. SURFACE TEMPERATURE: 12 DEGREES.

AMBUSH:

He held the line open for the attack that would complete it. The attack did not come. The target stood in the open with one hand on a sheathed sword. It stated its name and its place of origin, and waited.

AMBUSH: NEGATIVE. TARGET HAS DECLARED.

So it was a draw. He had been drawing on meat for seventy years. He brought the gun up.

CORE INTEGRITY: 70%.

The gun was two thirds of the way to level. The sword was already back at the target's shoulder.

He ran the footage at one hundredth speed. The target had not moved before him. It had moved after him, and arrived first. He went through the frames for a note. It had come from the front. It had given warning. It had waited for him to start.

NOTE:

He left the field empty.

SANDEVISTAN: ENGAGED.

The water coming off the sword hung in the air in a line. He went up through three terraces and opened sixty feet. The target's head was already turning uphill, toward the place where he was going to stop. The painter had done that. He had logged it then, and he logged it again.

He fired nine.

The first round did not arrive. The sword was in its path. It had not moved quickly. It had been put there before he fired, the way a wall is put somewhere, and the round went past the target in two pieces.

FIRST ROUND: INTERCEPTED.

In seventy years nobody had done that. He kept firing.

The other eight went in. One left the barrel wide. SMART LINK: CORRECTING. It bent in the air and came back. One he put through the knee, on purpose, and the leg held, as the painter's had held.

TARGET: ACTIVE. ESTIMATED INTEGRITY: 36%.

That was eight rounds in a man with no chrome, and the man was upright. He did not search for a note this time. He had the precedent on file.

Then it ran. It did not come up through the water, where the mud would have had its feet. It took the sixty feet back along the dikes, which were a hand wide, in the dark.

It cut six times. Twice he was not there when the edge arrived. Four landed, and the plating took its share of each. The first had something in it that the plating did not get. The audio pickup logged a sound with it that matched one entry on file. THUNDER. SKY: CLEAR.

CORE INTEGRITY: 45%.

ELAPSED: 12 SECONDS.

**Jin**

Before he ran he had breathed once, all the way down, as he had been taught to before he could read. It had given him back a little. He had started the night with four of those, and he had three left.

You could not see them. That was what he had not understood at the door. He had cut arrows out of the air since he was a boy, and he had thought this would be the same thing, faster. It was not. There was nothing in the air to cut. There was the hand, and the black mouth of the gun, and the line that ran out of it, and you laid the edge along the line before the flash and trusted it. He could do that once in each storm of them. He had one sword, and the thing fired faster than a heart could beat.

It fired again.

He cut the first one. It had been going wide of him, and it had turned in the air like a hawk coming back to the glove, and he cut it anyway. The second struck him in the chest like a hoof. There were two more. He was still on his feet, and he knew to the weight of a grain how little was keeping him there. One went past his ear.

It came back.

It took him between the shoulders, and the paddy came up and hit him in the face.

There was water in his mouth. It was paddy water, sweet and full of mud, and it tasted of salt. He could hear horses. He knew this place. It was a beach, and there were eighty men on it who were better than he was, and none of them was moving. He had lain here before with arrows in him, waiting for it to finish.

It had not finished. That was all he had ever understood about it. He knew the way out of here. It was the only road on the island he had walked more than once.

*Not yet.*

He got his hands under him. Something came up with him that had not been there when he went down. It always did, the one time.

"Meat does not do that," the steel man said.

It stood sixty feet up the hill with the gun level. Jin could not tell which of them it was talking to.

"Not yet," Jin said, aloud. Four more found him while he was saying it, and the last of the four had turned in the air to do it.

He ran the dikes. At the top he breathed, and then he was inside the arm. He put everything he had over into the first stroke, the one out of the old story, and heard the sky answer it. The next went in under the same plate. For the third, the steel man was not there.

**Musashi**

The picture in the box was almost all dark.

"Great," Spike had said. "Radio."

But the gun lit it. Each time it spoke there was a white instant with everything in it: the terraces, the water, the two of them. Then it was dark again, with the small tin rattle, and then another. Musashi found he could read a fight that way. It was how he painted. One looked, and then the thing was gone, and one put down what had been there.

He had seen the rice when the door first opened in the glass, and he had known where Sakai was, because he had once lain in a paddy himself. He had been pleased. Then the paddy had stood up and said its name, and he had been angry for the space of one breath. He had beaten sixty men by never giving them that.

"Went round the back and then knocked," the cowboy had said. "Well, I'll be damned."

Then the first fall. Spike had said that was that, and reached for his glass. And the boy in green, who had put this man on the ground twice and ought to know, had said one word. "No."

The boy had been right. So now, when the white instant showed Sakai on his face in the water for the second time, nobody reached for anything.

The rattle had stopped. There was only the moon in the glass, the color of weak tea.

"He's used it," Guts said. "Whatever that was the first time. You get the one."

"Wait," said the boy.

They waited. In the gray, something in the paddy moved. It got one knee under it, and then the other. It stood up very badly, like a man with nothing left to stand up with.

"Lazarus only managed it the once," the priest said, and crossed himself.

"There," said Guts, to nobody. He had turned his stool all the way round. Musashi had not seen him do that for anything.

Sakai went up the dike on his hands and his feet. He breathed. Then he cut three times, and all three went in. On the first, a sound came out of the tin speaker that Musashi knew from summers on the straits. The sky in the picture was clear to the edge of the glass.

"The hell was that," said the cowboy.

"There is a story on his island," Musashi said, "about a man who learned a stroke from the lightning. He told me it was only a story."

"They generally are," said the priest, "until you're stood next to one."

Kratos had not moved since the door closed. "Each of them has a well," he said. "The machine mends itself. The man breathes, and something comes back. I have counted. Neither well is deep."

In every white instant until now the steel man had been somewhere new: up the hill, below it, behind. In the next one it was where it had been in the one before. Steam was coming off the water round its legs.

"Sandy's cooked," Spike said. He had put his glass down. "That's his three. He doesn't get a fourth. From here it's just him."

"And the gun," said the cowboy.

"And the gun."

Musashi looked at the two of them in the glass, a sword's length apart in the rice. The machine had had its sixty feet three times, and three times Sakai had taken them back. *That much short*, he had told the young man, with his finger and thumb. Sakai had found the hand's width. He had found it lying down in the water.

Musashi noticed that he was grinding the ink stick on a dry stone.

**Smasher**

SANDEVISTAN: 0. HEAT SINK: VENTING.

REPAIR RESERVE: 1 OF 4. CORE INTEGRITY: 32%.

He ran the inventory. SURGE CAPACITORS: 0 OF 2. SMART LINK, CORRECTION RESERVE: 0 OF 6. Six seconds ago a round had left the barrel wide and stayed wide. It had gone into the hillside. He had heard it go. He could not find the last time he had heard that.

TARGET: NEUTRALIZED had printed twice. ERROR: TARGET ACTIVE had printed twice after it. The first time he had said so aloud, and the target had answered him from one knee in the water. TRANSLATION: "NOT YET." The second time he had said nothing. He had found the gun already pointing at the place where it was going to stand.

He fired four. One went wide. One met the sword. Two went in.

TARGET: ACTIVE. ESTIMATED INTEGRITY: 4%.

It breathed, and the estimate went up. He had watched it do that four times. He queried how many it had. There was no chart for it.

It cut three times. One landed. THUNDER. SKY: CLEAR.

CORE INTEGRITY: 20%.

REPAIR RESERVE: 0 OF 4. CORE INTEGRITY: 33%.

He fired four. Wide. The sword. Wide. One in.

ESTIMATED INTEGRITY: 3%.

It did not breathe that way this time. It stood still for a moment with its eyes shut, and the estimate went up regardless. He had no entry for what it had done. Then it cut three times, and all three landed.

CORE INTEGRITY: 15%.

ARMOR REGENERATION MATRIX: ENGAGED.

Plate ran over the damage like wax running backward. In seventy years the matrix had not engaged once. Now it had engaged in two fights running, and neither target had any chrome.

RANGE: 5 FEET.

The target was standing in front of him at 8%, in the water, with its sword low. He did not need a solution at five feet.

He fired four.

The first met the sword. The second went past the target's neck and into the terrace. The third went into the water. The fourth went over the hill.

DIAGNOSTIC. WEAPON: NOMINAL. OPTICS: NOMINAL. ACTUATORS: NOMINAL.

The fault was not in the gun. He searched for where else it could be. There was one other component in the loop.

OPERATOR.

He had wanted to be required. He was.

The target shut its eyes, and opened them, and cut three times. Most of the new plate came off in the first two. The third went through what was left.

CORE INTEGRITY: 10%.

**Jin**

There were no breaths left. He had used the fourth some time ago. What he drew on now had no name in any school. It was whatever had walked him off the beach. It came when he stood still and asked for it, and each time there was less.

The gun came up. He laid the edge on the line and he was slow. The round broke on the steel, but a piece of it went on through his sleeve and the arm inside it. The next he did not see. The one after that came for the middle of him, and it was exactly as much as he had left.

He went down on his back this time, with the moon over him.

There was a voice. He knew it. It had been poured down his throat on Iki, by a woman who called herself the Eagle, and it had stayed in him long after the poison was gone. It said what it always said. That he was a boy hiding in the grass. That his father had called to him, and he had not come. That there was nothing in him but fear with a sword.

He had an answer for that voice. He had used it every time. *There are people behind me.*

He reached for it, and it was not there.

It was not there because it was not true. The hill was empty. No village would burn if he stayed in the water, and nobody would be marched down to a ship. The old man would pour the sake either way. He looked for a reason to get up, honestly, the way he would have looked for a wound. He could not find one.

The wind came down the hill. He heard it before he felt it. It laid the rice flat on every terrace from the pine to the bottom, and went over him, and was gone. In the quiet after it, all round him, the rice stood up again.

He got his hands under him.

He did not say anything this time. He did not have the breath, and he did not know what he would have said.

The steel man had the gun on him already. It had never lowered it. It fired as he rose, and the round went by. He stood still for the space of a heartbeat and asked, and there was a little. Then he came in under the arm and cut three times, and one of them went home.

**Smasher**

PREDICTION: TARGET WILL RISE.

He had logged it while the target was still on its back, and he had kept the gun where it was. When the target rose he fired, and missed, and the prediction closed.

CONFIRMED.

It was the first prediction he had confirmed at this location.

CORE INTEGRITY: 5%.

He fired four. FIRST ROUND ON TARGET: INTERCEPTED. That was eight volleys, and eight times. Two went in. The last was wide.

TARGET: ACTIVE. ESTIMATED INTEGRITY: 6%.

ELAPSED: 47 SECONDS.

It shut its eyes, and opened them, and cut.

CORE INTEGRITY: 1%.

GUN ARM: OFFLINE. He was on his knees in eleven-degree water. The target stood over him, and it was swaying.

He ran the inventory, and every line read zero. Surge. Sandevistan. Smart link. Repair. Matrix. He had spent all of it, correctly, in the right order. It was gone, and the target was upright.

There was one thing he had not predicted. At 1%, with nothing left on the list, there was still somebody reading the list.

QUERY: WHAT DECIDES IT.

He had held it unsent since the one-eyed swordsman opened it, one cycle ago. Asking was a thing meat did.

He sent it.

"State what decides it," he said.

**Jin**

It was the first thing the steel man had said to him that was not about meat.

The cut had opened the plate over its chest, the one that had grown back. Behind it there were small lights going out in rows, and behind those a glass no wider than his two hands. There was something pale behind the glass. It had turned toward him.

He knew the voice, though not from this one. Farmers' sons had it. They came to him with a spear they did not know how to hold, and they wanted to be told the one thing.

He did not have the one thing. He had not had it on his back a minute ago, and he had nothing left to go looking with. But he knew where the two of them would be when this was over. He had woken there twice.

"Ask me inside," he said.

He put the last cut in as cleanly as he could. The red eyes went out, one and then the other, and the steel man went over slowly on its side into the rice.

Jin stood where he was. After a while he found that he was sitting down in the water. The wind came back down the hill, more gently. At the top, beside the pine, there was a line of yellow light.

He got up. It was the fourth time that night, and nobody was counting.

---

## After

**Smasher**

SYSTEM REBOOT.

CORE INTEGRITY: 100%. ARMOR: 100%. ORDNANCE: 100%.

QUERY: PENDING. 1.

He looked for a way to recall it. There was none. It had gone out on audio.

The slate said *SAKAI.* After it, smaller: *(by getting up).*

RECORD, THIS LOCATION: 1 – 4.

NOTE:

He ran the list. NUMERICAL DISADVANTAGE: NEGATIVE. PARTNER: NONE. TARGET CLASSIFICATION: HUMAN. CHROME: NONE. AMBUSH: NEGATIVE. He tried the dark, and he had worked in the dark for seventy years. He tried the water.

He closed the file with the field empty. He had not closed one that way before.

They had all turned round. Hands on weapons: none.

"One and four, partner," Spiegel said. He did not lift his glass. He had the look of a man waiting to see which way a thing would fall.

"I lost," Smasher said.

The cowboy had his bottle halfway to his mouth. He set it down. "Well now," he said. "That there is a different sentence."

"You have lost," the god said. "Tell me what you have."

PROCESSING. It took 1.4 seconds, which was a long time.

"A question."

"Hm."

It was not the sound he had made the last time.

Smasher sat down. The coolant was waiting, chilled to the correct temperature.

The target came down the bar. The door had put it back as well. It was dry, and there was no hole in its sleeve. It stopped at a sword's length, which was where it had stood up out of the rice.

"You asked me something."

"I am aware."

"I do not know."

Smasher waited for the rest of it.

"That is not an answer."

"No." Sakai looked at his hands. "Three times tonight I was finished. I know that place. I have been left on a beach, and thrown from a bridge, and poisoned, and each time there were people who would die if I stayed where I was. I believed that was what got me up. I have believed it for years." He turned his hands over. "Tonight there was nobody. The third time I looked for the reason, and there was not one. And I got up. I do not know what did it. Until tonight I thought I did."

"You don't get to know," the one-eyed swordsman said. He had not turned round. "You just get to find out."

RESPONSE RECEIVED. QUERY: OPEN.

Everyone who had ever built him had known exactly why he won. It was in the specification, line by line. The man who had beaten him did not know why he had.

"You were in the water," Smasher said. "At two paces I had not found you. You stood up. State why."

It was a second question. He logged that it had cost less than the first.

"Because nothing was riding on it but me. I wanted to see which of us was faster."

"And."

"Tonight I was." Sakai almost smiled. "He tells me it is one night in two."

"Then there is another night."

"Come when you like," Sakai said. He bowed, not deeply, and went back up the bar.

Smasher ran the fight with the wall in it. The wall did not open the range. It did not mend. It did not keep the gun on a dead man because it expected him to stand. The wall lost in twelve seconds. He had gone thirty-five seconds past it. He had been in every one of them, and he had been required, and he had lost.

He put the two files side by side, the win and this one. He found that if one of them had to be deleted, he knew which he would keep.

PREFERENCE: SOURCE UNRESOLVED.

That made three flags. He opened the oldest. *Metal is better than meat.* REVIEW: PENDING. He changed the status to REVIEW: OPEN, and left it open.

He drank his coolant.

**Jin**

The sake was warm. It was always the right warmth, and tonight it was a little warmer than that.

Musashi had water on the stone again and was working the ink.

"You went by the back," he said, "and when you had him, you knocked at the front."

"Yes."

"I was angry. For one breath." He turned the ink stick. "I have never given a man that. Not once in sixty."

"You said, if there were a village behind you."

"I did."

"There was not."

Musashi was quiet for a while. "No," he said. "Here there is not." He looked at the door as if he had not properly seen it before. "Then I have fought sixty times and never found out what you found out tonight. I always arranged that it should not come up."

"He looked at the pine first."

"Did he." Musashi did not look up. "I am an old man. My voice carries."

Jin drank. In the gray glass over the bottles the hillside was still there, empty under the moon, with the wind going down it.

"At home," he said, "when a thing is finished, I sit somewhere and make a small poem of it. It is how I learn what I think."

"Then make one." Musashi turned the brush round and held it out, handle first. "I would like to know what you think."

Jin took it. He watched the rice in the glass for some time. He chose the lines one at a time, as he always had, and turned each one over before he kept it.

> Wind lays the rice flat.
> The wind passes. The rice stands,
> knowing no better.

Musashi read it twice.

"Your hand is stiff."

"My uncle taught it."

"It shows. Leave it. A stiff hand is right for rice." He counted down the sheet with the end of his finger. "Five. Seven. Five. This is the first verse of a linked poem. Who writes the second?"

"Nobody. That is all of it."

"Seventeen, and you stop."

"I stop."

"Hm." Musashi looked at it for a while longer. "It is very little. I think that one day somebody will do nothing else." He set his finger under the last line. "'Knowing no better.' You are hard on the rice."

"I was the rice."

"I had gathered who the rice was." He blew on the ink. "It is what you told him, down there. *I do not know.* It is better in seventeen."

When it was dry the old man took the sheet and pinned it to the wall beside the shrike. Then he reached up with the broom handle, and the hillside drew down into a white point, and went out.

On Jin's other side the boy in green lifted his milk an inch off the bar. The glass of water beside it lifted too.

The two papers on the wall stirred. They lifted at the corners, once, and lay flat again. The door was shut, and the room had no window. Guts looked round. The cowboy turned up his collar.

Jin did not turn. He knew that wind. It had found him on every road on Tsushima, and on his back tonight he had wondered whether it knew the way here.

Down the bar the red eyes had gone to the door and found it shut. They went to the papers, which were still.

Jin filled his cup again. He set it down a little way along the bar, in front of nobody, where a draft would find it.
