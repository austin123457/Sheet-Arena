# At Sixty Feet

*Miyamoto Musashi vs Adam Smasher.* Smasher has lost to everyone he has met at the bar. Musashi comes through the door late, with two swords and no armor, and the old man switches on a television over the bottles that nobody had noticed. It comes after [Two of a Kind](link-vs-dark-link.md).

The fight is real: the most dramatic of 1,000 runs of `python battle.py 1v1 musashi smasher`, picked by `fight_log.py musashi smasher 1000`. Smasher has been beaten in every fight he has had here, and the dice would not do it to him again. He wins this matchup every time: 8,000 of 8,000 through `battle.py`, and when `fight_log.py` was asked for a fight Musashi won, another 12,000 went by without one. It ends in the second round 98 times in 100. Musashi's guard is his two swords, and it is a guard against a weapon in somebody's hand: AC 22 against melee, 16 against a shot, and no Reaction that does anything about a bullet. The smart gun is +15, ignores resistance, and fires nine times in a turn with the Sandevistan and an Action Surge. What Musashi can do is make one round of it close. He rolls initiative with advantage, every attack in the first round has advantage against someone who hasn't acted yet, and the first katana cut that lands is the One Cut. In this run all ten cuts of round 1 land, and the One Cut does 96 after the plating has taken its 6, which is 43% of Smasher in one stroke. They finish the round on 70 hit points each. In round 2 a critical hit takes Smasher to 33 of 224 and sets off his armor regeneration matrix, which happens in about one fight in eighteen (220 of 4,000). The lowest he got in any of those 4,000 was 29. Then he shoots six times.

<details>
<summary>The round-by-round log</summary>

```
winner: Smasher in 2 rounds
R1 Musashi | {Musashi: surges 2->1, dice 6->1, one_cut True->False} ** Musashi: One Cut on Smasher ** hit 96 slashing hit 3 slashing CRIT 16 slashing CRIT 10 slashing hit 4 slashing hit 6 slashing hit 7 slashing hit 4 slashing hit 3 slashing hit 5 slashing  || Musashi 204  Smasher 70
R1 Smasher | {Smasher: surges 2->1, sandy 0->3, dice 6->3} hit 13 piercing hit 17 piercing hit 11 piercing hit 14 piercing hit 16 piercing hit 16 piercing miss hit 15 piercing miss  || Musashi 70  Smasher 70
R2 Musashi | {Musashi: sw 4->3, surges 1->0} {Smasher: matrix True->False} hit 9 slashing hit 2 slashing hit 3 slashing hit 5 slashing miss miss CRIT 13 slashing hit 3 slashing miss  || Musashi 95  Smasher 70
R2 Smasher | {Smasher: sw 4->3, surges 1->0, sandy 3->2, dice 3->2} hit 21 piercing hit 12 piercing hit 12 piercing hit 20 piercing hit 19 piercing <Musashi DROPS TO 0> <Musashi OUT> hit 12 piercing  || Musashi 0  Smasher 96
```

A miss that a die turns into a hit is still logged `miss`, and its damage isn't printed, so it only shows in the totals. In round 1 Smasher's seven logged hits come to 102 and Musashi loses 134: both misses were pulled onto him by Precision Attack. Those are two of Smasher's three `dice` that turn. The third is a Trip that Musashi stood through, and so is the one in round 2. Smasher shoots at disadvantage in both rounds, because a critical hit from a Slasher does that to its target until the Slasher's next turn. In round 2 Musashi's logged hits come to 35 and Smasher loses 40: the first miss is the wakizashi, and Peerless Aim makes one miss a turn a hit. Every cut loses 6 to Smasher's plating, which is why a katana that does 1d8+7 is logged at 2, 3 and 4. The One Cut is logged as `hit`, though it is a critical hit by its own rule, and it takes five of Musashi's six `dice`. `sw` is Second Wind: Musashi goes from 70 to 95, Smasher from 33 to 59. The totals after `||` include temporary hit points. `matrix True->False` is the armor regeneration matrix, 40 temporary hit points the first time Smasher is at 40 or under, so the 70 beside his name after round 2 is 33 and 37, and the 96 at the end is 59 and 37. A drop to 0 is logged just before the attack that caused it. `sandy` counts the Sandevistan's rounds: +2 AC and an extra shot.

</details>

---

## The Bar

**Smasher**

RECORD, THIS LOCATION: 0 – 3.

PREDICTIONS, THIS LOCATION: 0 – 1.

He had the three losses on file, and each one had a note on it. The first: NUMERICAL DISADVANTAGE, TWO TO ONE. The second: PARTNER ASSIGNED: ORGANIC. The third: TARGET CLASSIFICATION: UNRESOLVED. They were good notes. Any one of them would have closed the file at Arasaka.

He ran the footage anyway. He had run it every cycle. In each of the three he had done what he was built to do, and the damage was on the log, and it was more than had been needed to end anything he had met in seventy years. Then each log ended the same way.

He scanned the room.

The cowboy was coughing into his milk. The priest was reading. The boy in green had a second boy beside him now, in black, who did not register on thermal. The green suit had left the ninth stool and sat on the blind side of the one-eyed swordsman, and the old man no longer set a glass at the ninth.

On the first night, when Smasher had turned sideways to come through that door, six hands had gone to six weapons. He had logged that as correct.

Now Spiegel called him partner. The cowboy touched his hat to him. The priest had started to pray for him, aloud and by name, and when Smasher told him to stop he had said that was between himself and his employer. The boy in green had looked at him once, for some time, and gone back to his milk. Smasher had not been able to classify the look. The nearest match on file was the one a ripperdoc gave a part that could not be saved.

THREAT RESPONSE, ROOM: NONE.

In Night City a room emptied when he came into it. Until this location he had not thought of that as something he owned.

"You're tapping," Spiegel said.

He stopped.

"Three's nothing. I got thrown out of a church window once. Nicest fight I ever lost."

"I do not lose."

"'Cept three times," the cowboy said mildly. He wiped his mouth. "I ain't crowing. You're the hardest thing I ever shot at, and I have shot at trains." He turned the bottle on the bar. "I rode twenty years with a man who had one sentence he was sure of. Losing never taught him a thing. He just said it louder."

"You're strong," said the one-eyed swordsman. He had not turned round. "So is a siege tower. Every damn thing I ever fought was stronger than me. That's not what decides it."

QUERY: WHAT DECIDES IT.

He did not send it. Asking was a thing meat did.

The god drank his mead and said nothing. He had said it already. The green suit did not turn its helmet.

What Smasher wanted was simple, and he had specified it eleven cycles ago. One target. Organic. No chrome. No partner on either side, and nothing about it that would need a note.

At the end of the bar the old man set down the glass he was polishing. *Click.* He came round the counter, wiped the slate with his sleeve, and took up the chalk.

> **TONIGHT:**
>
> SMASHER v MUSASHI

There was no line above it this time, and no rule under it.

LOCAL ARCHIVE: MUSASHI, MIYAMOTO. Swordsman, Japan. Born 1584. Died 1645. Author, one book. STATUS: DECEASED, 432 YEARS.

He knew the book. Saburo Arasaka had kept a copy on his desk and quoted it at board meetings. Smasher had never opened it. It was about swords.

"Musashi," Spiegel said. He had sat up. "Two swords, one in each hand. Sixty-some duels, never lost one. He's been dead four hundred years and change, which has never stopped anybody getting in here." He lit a cigarette. "They say he never took a bath, either. Didn't want to get caught without the swords."

TARGET: NOT PRESENT.

"Partner. It's a guy with two swords and no armor."

PROJECTED OUTCOME: SMASHER. CONFIDENCE: 100%.

He looked at the second line of his record, and did not say it aloud.

One cycle passed, and the door did not open. Then a second, and a third. The slate said TONIGHT.

"He's late on purpose," Spiegel said. "That's the other thing he was famous for. Shows up three hours after the bell. By then the other guy's so mad he can't see straight."

"I do not get angry."

"You're tapping."

On the fourth cycle the door opened.

THERMAL: 1 ORGANIC.

**Jin**

He knew the walk before he knew anything else about the man. It was the walk of home.

The man was about fifty, and tall. His hair had never been shaved back from the brow and was tied behind him anyhow. He wore a plain robe without a crest that had been slept in on the ground, and he had not bathed in some time and did not seem to know it. He had straw sandals on his feet, and two swords through his sash, the long one and the short one together.

He did not look at any face. He looked at the door behind him, which was the only one. He looked at the lamp, the floor, and the way the light fell. Then he looked at hands, and then at what was near the hands. Jin had been taught to enter a room that way. He had met very few men who could do it without being seen to.

The man stopped at the slab of iron that leaned beside Guts, and looked at it for some time.

"That is not a sword," he said. "That is a gate."

"It cuts," said Guts.

The man looked at the arm it belonged to, and the shoulder, and the iron hand. "Yes," he said. "I see that it would."

He went on down the bar. He passed the crack in the counter's edge and the green hand lying beside it, and did not stand near either. At the boy he stopped again. He looked at the hilt over the boy's shoulder, and inclined his head to it, a little, as a man does when he passes a shrine. He looked at the black shape on the next stool, and up at the glasses where the boy's reflection should have been. Then he moved on without a word, as if it happened wherever he drank.

Then he came to Jin, and stayed longest.

"That lacing," he said. It was the speech of home, with the corners worn differently, like a coin from another reign. "I have seen it in temple storehouses. On armor that nobody is allowed to touch."

"It was made for my father."

"What year is it, where you come from?"

"The eleventh year of Bun'ei."

The man was quiet a moment. "The eleventh year of Kan'ei," he said, of himself. "Three hundred and sixty years." He did not seem to find it strange. "Bun'ei. Then you know the beach at Komoda."

"I was on it."

"Eighty riders went down onto the sand against a fleet. The chronicle says none of them lived."

"The chronicle is nearly right."

The man looked him over again, and this time he looked at the rest. He saw the short blade at the back. He saw the bow, and the pouches at the belt with the smoke and the darts in them. They were the things Jin's uncle had not been able to look at.

"You carry more than a sword," the man said.

Jin waited for the rest. He had heard the rest before, from a man he loved.

"Good," the man said. "A man should not have a favorite weapon." He bowed, not deeply. "Miyamoto Musashi. Of Harima."

"Jin Sakai. Of Tsushima."

*Good.* Jin did not know what to do with the word. He had not been given it before.

Musashi had already turned. The steel man was on his feet, and the stool that had been made for him was still creaking.

"You are late," the steel man said.

"Yes."

Musashi looked at him the way a carpenter looks at a house he has been asked to pull down. He looked at the joints first, the knees, the place where the neck went into the shoulders. Then he looked at the gun, and he looked at it longer than he had looked at anything else in the room.

"I was sixteen at Sekigahara," he said, to nobody. "I know what that is. That is a large one."

The old man had set a cup on the bar. There was hot water in it, plain, with the steam going up.

"It's paid for."

Musashi looked at the cup. "After," he said.

The old man nodded, as if it had been ordered that way.

Musashi did not sit down. He walked to the door and opened it, and beyond it there was sand and a white sky. "Come when you like," he said to the steel man, and went out.

The steel man stood where he was for the space of a breath. Then he turned sideways, and ducked, and followed. The door closed.

The old man took the broom from the corner. He reached up with the handle, over the top shelf of bottles, and pushed something.

There was a box up there, bolted under the ceiling, with a face of gray glass. Jin had counted the bottles on that shelf more than once, and he had never counted a box. It hummed. A white point came up in the middle of the glass and opened into a picture: the sand, the sky, and two figures on it, small, the color of weak tea.

"Since when do we have a TV?" said Spike.

The old man put the broom back.

"That a window?" the cowboy asked.

"It's a television, Arthur."

"A what?"

"A window somebody else points."

The cowboy thought about it. "Don't care for that."

"Nobody does. We watch it anyway."

"I don't suppose it gets the football," said the priest.

Jin looked at the slate. For the boy and his shadow the wall itself had folded away, and the slate had said EXHIBITION. Tonight the wall was a wall, and the slate said only the two names. Whatever happened on that sand would be written under them and would stay there. The old man had only decided that they should see it.

In the glass, the smaller figure was walking. It had not stopped to bow, or to set its feet, or to draw. It had come out of the door and gone on toward the machine at the pace it had used to walk down the bar.

Jin understood it a moment before the others did. The fight was not about to begin. It had begun three days ago, when the man made the machine wait.

---

## One Cut

**Musashi**

Sixty feet of sand, and a white sky.

There was no grass and no tree, and no rock. There was no sun to put at his back. Whoever kept this ground had swept it of everything a man could use, and what was left was a gun's ground. He had been able to choose the hour, and nothing else. So he had spent the hour.

He did not stop walking.

Most of the men he had beaten were beaten before they knew it had started. There is a moment before a man's intention forms, and while he is in that moment he is standing still, however fast he is. The steel thing was waiting for a beginning. It wanted a bow, or a word, or a drawn sword. He gave it none of them. At forty feet his hands were empty. At twenty they still were. Then he saw the red eyes change, and the gun start to come up, faster than any arm he had ever watched.

But it had started late. That was the whole of the art, and he had been thirty-seven years learning it.

The long sword came out of the scabbard and into the cut in one motion.

There is a cut with everything in it. A man gets one of them in a fight, because afterward there is nothing left over to make another. It went in at the collar and came out at the hip. The plate was as thick as the banding on a castle gate, and it opened. Behind it there were wet lights and bundles of cord. Deeper in, behind a glass no wider than his two hands, there was something pale that was not steel.

*So there is someone at home.*

He cut nine times more, with both swords, because a fight is not one cut. All nine landed, and most of them did not matter. It was like cutting a temple bell. The hand rings, and afterward the bell is still a bell. Twice he found a seam. One was a bundle of cord under the jaw. The other was behind the eyes, and one of the red lights went out.

He could hear how much of it he had taken, the way a man hears it in a cask. Two parts in three.

Then it was not there.

**Smasher**

TARGET: MUSASHI, MIYAMOTO. Male. Age: 50. Chrome detected: none. Armor: none. Cloth. Blades: 2, carbon steel, hand-forged. THREAT ASSESSMENT: MINIMAL.

He had waited for the target to stop and begin. The target did not stop.

FIGHT START: NO SIGNAL ON FILE.

By the time the software reclassified an approach as an attack, the range was nine feet and the gun was a quarter of the way up.

CORE INTEGRITY: 57%.

It was one stroke. He ran the number again, and it was 57%. The thing from Hell had needed a blade made of [NO VALUE] to take forty points off him. This was 1.1 kilograms of folded iron.

PAIN EDITOR: ONLINE.

He felt nothing. He logged that he had checked.

Nine more impacts. PLATING: SURFACE DAMAGE, seven times. The other two went in. LEFT OPTIC: OFFLINE. TARGETING: DEGRADED.

CORE INTEGRITY: 31%.

ELAPSED: 5.8 SECONDS.

SANDEVISTAN: ENGAGED.

The world stopped. The sand the old man had kicked up hung in the air around his ankles. Smasher stepped back out of the reach of the swords, and kept stepping, and opened forty feet.

The man's head was turning to follow him. It turned slowly, as everything was slow. But it was not turning toward the place Smasher had been. It was turning toward the place he was going to stop.

He logged that.

He fired nine. With one optic the solution wandered, and two rounds left the barrel wide. SMART LINK: CORRECTING. They bent in the air and went back to the target. He put one through the knee, on purpose. The leg did not fold. The man put his weight on it as if he had been told that he could not, and had not agreed.

The target had not blocked, and it had not dodged. Meat with a sword always tried. This one kept the swords where they were and stood in it, nine rounds through cloth, and did not take its eyes off him.

TARGET: ACTIVE. ESTIMATED INTEGRITY: 34%.

He had put nine rounds into a man with no chrome, and the man was standing up. He searched for a note to put on that.

**Jin**

"Ten," Jin said.

He had counted them. Nobody asked him what.

"The first one wasn't like the rest," Guts said. He was leaning in toward the glass on his elbows. "He put everything on it. I've done that. You get the one."

"Mother of God," said the priest. "He's opened the brute like a tin of fish. With a *sword*."

Then the machine was forty feet from where it had been, with nothing in between, and a small tin rattle came out of the box. The figure in the robe jerked nine times. It did not go down.

"He's not blocking," Spike said.

"Can't block that," said the cowboy. "Only thing to do about a bullet is be someplace else. And there ain't no place else out there."

Jin was looking at a beach.

He had not meant to. But a man was walking upright over open sand toward a thing that did not fight the way he fought, and Jin had seen that before. Lord Adachi had ridden out alone at Komoda to offer single combat, as it had always been done. They had thrown oil on him and set him on fire.

"He knew," Jin said. "He saw what I carry and he said *good*. He knows what that weapon is. And then he went by the front."

Nobody answered him. Down the bar Kratos said, "Watch."

"Partner's down to a third," Spike said. "So's the old man. Call it even."

"It is not even," said Kratos. "One of them must cross the sand again."

In the glass the man in the robe breathed, once, all the way down. Jin could see it from here. Then he began to walk.

The boy in green was watching his feet. So was the shadow. The green helmet had tilted a degree toward the glass and stayed there.

The second walk was harder to watch than the first.

**Musashi**

At sixteen he had seen what a ball does to a man, and had lain under the dead until dark so as not to learn more. These were worse. They had turned in the air. Two of them had been going past him and had thought better of it.

He breathed. There is a breath that puts a man back together for a little while. He knew how to take it four times. He had never in his life needed the first.

The steel thing stood forty feet off. It was not slow now. It was bright at the edges, like a thing seen across a fire, and it was a little ahead of wherever he looked.

He had nothing left to steal. It knew when the fight was, now. So he walked.

The gun had gone quiet. Something in it was turning over. He had watched matchlock men swab and ram, and every gun yet made has a space like that in it somewhere. He walked into the space.

He made four cuts with the long sword. The first found the edge of the wound and took something out of it. The next three took paint.

The short sword went where the thing had been. He let the wrist turn it over, the way he had taught a hundred students and could not explain to one of them, and it came back onto the line and bit.

The long sword cut air.

Then for one part of a moment it was where it was. He put the long sword into the wound he had already made, to the depth of the glass. The glass starred. The point stopped a hand's width from the pale thing behind it.

The wound closed.

The edges of the plate went looking for each other and met, like wax running backward. He got the sword out before they did. He cut the new plate and it rang. He cut again, and the thing was somewhere else.

He stood with both swords and his breath going. He had nothing left of what makes a cut more than a cut.

*So that is how far it goes.*

He had wanted to know for thirty years. Nobody had been able to show him. It was farther than he had thought, and it was not far enough.

He kept the short sword in front of him and went on walking. A man can be shot walking toward a gun or walking away from it, and only one of those is the Way.

**Smasher**

CORE INTEGRITY: 15%.

ARMOR REGENERATION MATRIX: ENGAGED.

It had never engaged before. In seventy years, everything that could bring him to 15% had gone on to zero, and nothing else had come near it.

REPAIR RESERVE: 3 OF 4. CORE INTEGRITY: 26%.

LEFT OPTIC: OFFLINE.

The target was closing again. RANGE: FOURTEEN FEET. It was on the leg he had shot.

He fired. The first went through the knee again, and again the leg held. Two, center of mass. Three. Four. Five. The target was still coming. RANGE: FOUR FEET. The long sword had started to rise.

Six.

The target stopped. It did not fall the way meat fell. It went down onto one knee, and then onto its side, and the sword stayed in its hand.

TARGET: NEUTRALIZED.

He waited. In the last fight the next line had been ERROR: TARGET ACTIVE. He held the gun on the man for what was left of the eighteen seconds.

The line did not come.

RECORD, THIS LOCATION: 1 – 3.

He queried for whatever was supposed to arrive with that. He stood on sixty feet of sand at 26%, with new plate grown over a hole that a sword had made, and the query returned nothing.

**Musashi**

The sky was white. There was no sun in it, and no cloud.

It was like paper before the first stroke. He had always liked paper best then.

He had fought sixty times and more since he was thirteen, and he had never seen what was on this side of it. He had wondered. It looked like paper.

Somewhere close by, somebody had poured hot water. He could smell the steam.

---

## After

**Smasher**

The door put him back the way it put everyone back.

CORE INTEGRITY: 100%. ARMOR: 100%. ORDNANCE: 100%.

He checked the chest plate. There was no seam. He checked it again.

The slate said *SMASHER.* After it, smaller: *(at sixty feet).*

Over the bottles there was a box he had no record of, with a white point fading in the middle of the glass. LOCATION SCAN, PRIOR: NO SUCH OBJECT.

They had all turned round.

He scanned for it. Hands on weapons: none.

"One and three, partner," Spiegel said, and lifted his glass.

"That was shooting," said the cowboy, and touched his hat.

"He sends rain on the just and on the unjust," the priest said. "The odd win as well, it seems."

"He's fifty," said the one-eyed swordsman. That was all he said.

"You have won," said the god, to his mead. "Tell me what you have."

Smasher ran it. "A win."

"Hm," said the god.

"Do not call me that," Smasher said to Spiegel.

"You were slow on that one."

THREAT RESPONSE, ROOM: NONE.

He had projected that the win would bring it back. It had not. They were pleased for him. He searched for the classification of a room that was pleased for Adam Smasher, and found that the field had never been filled in.

The man with the swords was on a stool beside the samurai, with a cup of hot water in both hands. He was whole, and the robe was no cleaner. He put the cup down when Smasher came in, turned on the stool, and bowed from the waist.

"I lost," he said.

Smasher waited for the note.

The man had picked the cup up again.

"You have not qualified it," Smasher said.

"What is there to add?"

"The range. The ground. You had no armor. You are fifty."

"Yes," the man said. "Those are why I lost." He drank. "They do not make it something other than losing."

Smasher had three files with notes on them. He did not open them.

"How far does it throw true?" the man asked. He was looking at the gun as he had looked at it before, like a carpenter.

"Effective range: eight hundred meters."

"And I was given sixty feet. Then the place was kind to me, and I lost anyway. That is worth knowing." He nodded at the barrel. "The balls turned in the air."

"Smart rounds. Self-guided."

"Hm. From behind a wall nothing would equal it. I have said so for years. I have also been saying that once the swords are crossed, a gun is finished." He looked at the place on Smasher's chest where there was no seam. "I meant to write that down one day. I will write it differently."

He turned the cup in his hands.

"You stepped back. Most men who carry a gun forget that they have feet." He looked up, at the red eyes, and not at the gun. "I met your gun today. I would have liked to meet you. I came close, once."

BIOPOD PROXIMITY, MINIMUM: 9 CENTIMETERS.

"There is no difference," Smasher said. "I am the gun."

"Then you won," the man said agreeably, and turned back to the bar.

Smasher sat down. The coolant was waiting, chilled to the correct temperature.

He ran the fight again with a wall in his place. A wall with that gun on it, and a targeting loop, and nothing behind the loop. The wall won. He ran the three losses the same way, and the wall lost them, and it lost them faster than he had. He had been in every second of those. He could find very little of himself in this one.

He queried the sentence. *Metal is better than meat.* It returned TRUE, and today's file supported it. The flag on it said REVIEW. He moved to clear the flag.

SINGLE STRIKE. SOURCE: ORGANIC, AGE 50, NO AUGMENTATION. INSTRUMENT: CARBON STEEL, 1.1 KG, NO POWER SOURCE. RESULT: 43%.

He tried to file it under metal. The metal was a kilogram of iron that any forge on Earth could have turned out in the last two thousand years. He tried to file it under meat.

The flag did not clear. He added a second one beside it. ONE CUT: SOURCE UNRESOLVED.

"This is where you say 'good fight,'" Spiegel said.

Smasher said nothing for 3.2 seconds.

"The first cut," he said. The man looked round. "State what was in it."

"Everything," the man said. "That is why there is only one."

Smasher logged it. It did not resolve the flag.

He drank his coolant.

**Jin**

There was a stool beside him that he had not counted that morning, and Musashi was on it.

The old man took the empty cup away. In its place he set down an inkstone, a stick of ink, a brush, and one sheet of paper. He said nothing. Musashi said, "Ah," and wet the stone, and began to grind.

"You knew what the gun was," Jin said.

"Since I was sixteen."

"You saw what I carry, and you said *good*. Then you went out by the front, over open sand, as my uncle would have. As Lord Adachi did at Komoda. They burned him where he stood."

"Was there grass on that sand? A wall? Was it night?"

"No."

"No. Whoever keeps this place had swept it. I could not choose the ground or the light. I could choose the hour, so I was late. I could choose the first moment, so I took it." He turned the ink stick on the stone. "After that there was only the sword. I wanted to see how far it went."

"How far?"

Musashi held up his hand, with the fingers together. "That much short." He looked at the hand. "Sixty times, and I never found the end of it. Nobody could show me. It is a good thing to have seen once."

Jin watched the ink darken.

"My uncle would say you lost with honor."

"Did he die on that beach?"

"He lived. Long enough to tell me what I was."

Musashi picked up the brush and looked at the paper for a while without touching it.

"I have come late to a duel to make a man angry. More than once. Once I came early. I lay in the rice by a pine tree until the other side arrived. There were a hundred of them, with bows, and in the middle of them the head of their house, who was twelve years old. I cut the boy down first. Then I cut my way out." He set the brush to the bottom of the sheet. "Nobody calls me a ghost. They ask me to teach their sons."

"Is that honor?"

"I do not know what honor is. I know what winning is. I have never been sure it was the better thing to know."

He drew one line up the paper, from the bottom to the top, without lifting the brush. It leaned a little as it went.

"If I were sent against that one," he said, and did not look down the bar, "and it mattered, and there was a village behind me, I would not go by the front. I would go at night, from above, and I would have it finished before it knew there was a fight. You know how that is done. I have only watched."

"Would it work?"

"One time in two, I think." The brush stopped. "That is one in two better than the front."

Jin looked down the bar. The red eyes were already on him. The steel fingers had started to tap.

He looked away first, and was not ashamed of it. There would be a night for that.

"Tsushima," he said. "In your time."

"It stands. There are fishing villages, and a lord, and ships to Korea."

"And the Ghost?"

Musashi thought about it honestly. "There is no ghost in the chronicle. There are the eighty on the beach. Then the fleet went on to the mainland, and a wind sank it."

"It was not only the wind."

"It never is."

Jin sat with that. He had carried the name the Shogun gave him and had expected it to outlive him by a thousand years. It had not outlived him at all. Nothing had, not the name or the shame or the things he had done to earn them. Only the island had. He found he could not tell whether that was what he had wanted.

On his other side the boy in green had heard. He lifted his milk an inch off the bar. The glass of water beside it lifted too.

Jin remembered what the two of them had drunk to. *The people who will never know our names.* He had thought he was being generous.

"Welcome," the boy said.

Jin laughed. It surprised him. He raised his cup.

When he looked back, the line on the paper had become a dead branch. A bird sat at the very top of it, small and hunched, with a hooked beak. It was a shrike. Low on the stem there was a mark no bigger than a grain of rice, and it had legs. It was climbing.

"Which are you?" Jin asked.

"Today?" Musashi touched the end of the brush to the small mark. "It got most of the way up."

He blew on the ink. When it was dry the old man took the sheet and pinned it to the wall beside the slate, under *(at sixty feet).*

Down the bar the red eyes had left Jin. They were on the paper, and they stayed there a long time.
