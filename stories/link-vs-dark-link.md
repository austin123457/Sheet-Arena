# Two of a Kind

*Link vs Dark Link, an exhibition.* The Slayer finally looks at the room he has walked into twice, the whole bar turns its stools around to watch, and the slate carries one rule: no Nayru's Love. It comes after [Until It Is Done](smasher-vs-slayer.md).

The fight is real: the most dramatic of 1,000 runs of `python battle.py 1v1 link-no-nayru dark-link`, picked by `fight_log.py link-no-nayru dark-link 1000`. `link-no-nayru` is the exhibition rule: Link as his sheet has him, with Nayru's Love left in the pack. It doesn't change who wins. Link takes all 3,000 of 3,000 without it, in under three rounds on average, and with it he also wins every time and takes a little longer (3.6 rounds), because the spell costs him an action. The Master Sword does extra damage to a creature of evil, he has two potions and two fairies, and nothing heals the shadow. This run is the far end of that: nine rounds. The shadow wins initiative and takes 186 off him before he moves. Not one of the ten Deku Nuts takes. From round 3 to round 6 Link swings twelve times and never touches it. He drinks both potions, uses all four Second Winds and loses a fairy, and he wins with 66 hit points and one fairy left.

<details>
<summary>The round-by-round log</summary>

```
winner: Link in 9 rounds
R1 Dark Link | {Link: prone False->True, dice 6->5, triforce True->False} {Dark Link: surges 2->1, dice 6->0} CRIT 22 slashing hit 27 slashing miss hit 24 slashing hit 26 slashing CRIT 42 slashing CRIT 29 slashing CRIT 16 slashing  || Link 38  Dark Link 224
R1 Link    | {Link: surges 2->1, red 1->0, dice 5->2, nuts 10->8} {Dark Link: clanks 0->3} miss miss hit 31 slashing hit 30 slashing miss miss then: hit 1 slashing  || Link 223  Dark Link 163
R2 Dark Link | {Dark Link: surges 1->0} CRIT 23 slashing hit 17 slashing miss hit 17 slashing hit 18 slashing miss miss hit 12 slashing  || Link 136  Dark Link 163
R2 Link    | {Link: surges 1->0, dice 2->0, nuts 8->6} {Dark Link: clanks 3->0} miss hit 28 slashing miss ** Dark Link staggers (Link) ** miss hit 31 slashing hit 30 slashing then: hit 17 slashing  || Link 119  Dark Link 74
R3 Dark Link | hit 11 slashing miss hit 17 slashing hit 16 slashing  || Link 75  Dark Link 74
R3 Link    | {Link: blue 1->0, nuts 6->5} miss miss miss then: miss  || Link 224  Dark Link 74
R4 Dark Link | hit 13 slashing hit 13 slashing miss hit 18 slashing  || Link 180  Dark Link 74
R4 Link    | {Link: nuts 5->4} {Dark Link: clanks 0->2} miss miss miss then: hit 15 slashing  || Link 165  Dark Link 74
R5 Dark Link | miss hit 18 slashing hit 18 slashing hit 18 slashing  || Link 111  Dark Link 74
R5 Link    | {Link: sw 4->3, nuts 4->3} {Dark Link: clanks 2->3} miss miss miss then: hit 15 slashing  || Link 121  Dark Link 74
R6 Dark Link | CRIT 23 slashing miss hit 12 slashing hit 16 slashing  || Link 70  Dark Link 74
R6 Link    | {Link: sw 3->2, nuts 3->2} miss miss miss then: hit 19 slashing  || Link 76  Dark Link 74
R7 Dark Link | CRIT 17 slashing hit 17 slashing miss CRIT 13 slashing  || Link 29  Dark Link 74
R7 Link    | {Link: sw 2->1, nuts 2->1} {Dark Link: clanks 3->0} ** Dark Link staggers (Link) ** miss hit 29 slashing hit 28 slashing  || Link 56  Dark Link 17
R8 Dark Link | hit 14 slashing CRIT 17 slashing miss CRIT 18 slashing  || Link 7  Dark Link 17
R8 Link    | {Link: sw 1->0, nuts 1->0} miss miss ** Dark Link staggers (Link) ** miss then: hit 14 slashing  || Link 16  Dark Link 17
R9 Dark Link | {Link: fairies 2->1} hit 12 slashing <Link DROPS TO 0> <Link back up at 90> hit 16 slashing hit 12 slashing hit 12 slashing  || Link 66  Dark Link 17
R9 Link    | miss miss <Dark Link DROPS TO 0> <Dark Link OUT> hit 28 slashing  || Link 66  Dark Link 0
```

The shadow's `dice` are Ending Blows, and all six go in round 1: the Triforce of Courage turns one failed save, the next puts Link prone, and a hit on a prone creature is a critical hit. `clanks` counts the times the blades have met. That is Mirror: Link's swing would land, the shadow makes the same swing, and the attack misses. On the sixth meeting it staggers (the note is logged just before the swing that did it), and attacks against it have advantage until the end of the turn. When Link is at a quarter of his hit points or less it staggers on the third instead, which is round 7 (56 of 224, with three already counted, so the first meeting does it) and round 8, where it comes on his last swing and he has nothing to follow it with. `then:` is the shadow's Answer, a Reaction that lands once Link's turn is over: Standing on the Blade when the blades met, a Jump Slash when he simply missed. `nuts` are Deku Nuts, `red` and `blue` the potions, `sw` Second Wind, and Link's own `dice` go on Trip Attacks and parries (the hits for 22 and 1). After Link's first hit in round 1 the shadow sinks into the floor and comes up behind him, so its first swing of round 2 has advantage. Its other critical hits after round 1 are natural 20s. A drop to 0 is logged just before the attack that caused it.

</details>

---

## The Bar

**The Slayer**

Nobody had sat back down.

The shadow had its glass of water and the boy had his milk, and the two of them were lifting them and lowering them an inch at a time, like a man testing a mirror. All down the bar, hands were coming off hilts and out of coats, slowly.

The Slayer looked at his own hands. They were empty. He had come up off the stool to kill something with them, and there was nothing in the black shape to kill. He knew what a thing looked like when something had moved into it. He knew what a thing looked like when it had been emptied and worn. This was neither. Nobody was home in it, and nobody ever had been. It was the boy's. The boy could have it.

That left him standing, for the first time, in a room with nothing in it that was his to do.

Twice he had walked in here. Both times there had been one thing in front of him, and he had looked at that and at nothing else: first the god, then the machine. He looked now, the way he looked at any room.

The boy carried a sword that hated what he hated. He had felt it when he came through the door, a pressure like a held breath, and it had felt him and let him pass. The priest's blades were the same, only more cheerful about it. The dying man was not afraid of anything here, which made him the most dangerous thing in the room for his size. The thin one with the cigarette had been dead once already and it had not suited him. The quiet one beside the boy had moved his cup before the trouble started. The machine was settled. The god was settled.

He got to the end of the bar, and stopped.

The swordsman sat at the corner, with the wall behind him and the door where he could see it. He had one eye. The other had been shut for years. His left arm was iron from the elbow down, held on with leather and buckles.

It was not like the machine's. Nobody had sold this man an arm. A smith had made it, by hand, to fit him, and had made it well. Somebody had wanted him to live. There was black powder packed in the forearm.

The sword leaned on the bar beside him. It was a slab of raw iron that somebody had put an edge on, because nothing smaller would do. The suit had flagged it when he first walked in, and he had not looked, because of the machine. He looked now. The readout was close to the one it gave him for the Crucible. That iron had been in so many of them, so deep and for so long, that it had stopped being only iron. There were things it could cut now that no sword should be able to touch.

He knew how many it took to do that to a blade.

Then the mark. It was on the side of the man's neck, a small raw brand, and a thread of blood ran from it down under his collar. It had been bleeding since the shadow came in. It had bled when *he* came in, too. He remembered it now: the man had put two fingers to his neck and looked up. He had not looked at the armor. He had looked at what was on it. Then he had gone back to his cup, and his hand had never gone near the sword.

The Slayer had a mark of his own. It was cut into the brow of his helmet, where the things he hunted could see it coming, and they ran from it.

This one was where the man who wore it could not see it, and nothing ran from it. They came to it. Somebody had hung a bell on him.

So he did not sleep. It was in the way he sat. The Slayer did not sleep either. But nothing had ever come looking for him in the dark. He went and found them. He had never once had to wait for it.

He stood there longer than he had ever stood anywhere without killing something.

It was like finding his own boot print in a place he had never walked.

**Guts**

The big green one was staring at him.

Guts let him. The Brand was beating, slow and hot, and he could no longer tell how much of it was the black thing down by the kid and how much was this. The man wasn't one of them. Guts had known that the first night. He just had it on him, soaked in to the knees and the elbows like a butcher. You couldn't wade in it that deep and not carry some out.

Guts knew, because his sword was the same.

He looked the man over the way he'd look over anyone he might have to fight, or stand next to. He stood square. His weight was even and his hands were open, and his feet were where a drillmaster would have put them. Somebody had *taught* this one. They had lined him up with a hundred others and shouted at him until he stood like that without thinking. They'd fed him regular, too, by the size of him. He'd had a flag once, and a number, and men on either side who were supposed to be there.

A soldier, then, a real one. Guts had been nine years old with a sword taller than he was, in a camp full of men who were paid by the day, raised by one who had never once wanted him.

And it hadn't made any difference. They had started at opposite ends of the world, and here was the same man standing in front of him anyway. Guts couldn't see through the gold glass. He didn't need to. He knew what the face was doing. He had seen it in still water.

"You're not one of them," Guts said. "You just smell like it."

The helmet dipped. It might have been a nod.

Then the man held out a hand, palm up, toward the sword.

Nobody touched it. That rule was older than the arm. Guts looked at the hand for a while. Then he tipped the hilt an inch toward it.

The green one lifted the Dragonslayer in one fist. Men had tried that. The few who could do it held it like a marvel, or a joke. This one held it like a shovel he had used all his life. He turned it to the lamp and ran his thumb down the edge, the way you check a thing you mean to use in the morning. He found the worst of the nicks and stopped on it. Then he set the sword back against the bar at the angle he had found it, to the inch.

He tapped the side of his own neck, once. Then he tapped the brow of his helmet, where something was cut into the metal.

"Yeah?" Guts looked at it. "Bet yours works the other way round."

Nothing.

"They run from you."

The helmet dipped.

"Figures." Guts drank. "Mine rings the dinner bell."

He turned the cup on the wood.

"How long have you been at it?"

No answer. The man did not even shrug. Guts waited, and after a while he understood that it wasn't a refusal. There was no number.

"That long," he said.

He did not know why he said the next part.

"I did two years. Just that. Kill them, walk, kill them. Nothing else in me, and I liked it that way. I had somebody waiting, and I left her in a cave to go and do it." He looked into the cup. "Nearly lost her."

The green hand moved. It went to a seam in the chest plate, where a man might keep something flat, and it stopped there.

"Yeah," Guts said. "Keep it."

He pushed the next stool out with his boot. It was the one on his right, on his blind side. He had not let anybody sit there in years.

The man looked at it. Down the bar, on the ninth stool, his glass stood where the old man had left it. Then it was standing in front of this stool instead, and nobody had seen it move.

He sat.

"Well, I'll be damned," the cowboy said. He was looking from the kid and his shadow to the two of them, and back. "Two of a kind. And two of a kind."

"That's two pair," said Spike. "Beats what I'm holding."

*Click.*

The old man had put down his glass. He went to the slate and wrote for some time.

> **EXHIBITION:**
>
> LINK v LINK
>
> *No Nayru's Love.*

He considered it. Then he put his thumb on the second name and rubbed until there was only a black smear where it had been.

"Exhibition," Spike read. "Means we get to watch."

"What's that last line?" said the cowboy.

"The blue light." Jin had not looked up from his sake. "He stands inside it, and nothing can touch him. I have fought it twice. I can tell you what it looks like from outside." He turned the cup a quarter turn. "It looks like waiting."

The kid was already digging in his pack. He came out with a blue crystal the size of a fist, with a light moving inside it, and set it on the bar. The old man turned a glass over it.

"Yes," said the kid.

The shadow had no pack to dig in. It had not moved.

The old man went to the door and opened it, and went on opening it. The wall came with it, lamp and slate and all, folding back like a shutter, until that whole side of the room stood open.

It wasn't sand out there.

---

## The Room Without Walls

**Link**

He knew the place.

An inch of water lay over pale sand as far as he could see, so still that the sky was in it. Mist stood where the walls should have been. Out in the middle was a low island with one dead tree on it. He had crossed this room once, a long time ago or not yet. He had stopped under that tree and looked down, and found nothing looking back.

Behind him the floorboards ended where the water began. They had turned their stools around. Somebody coughed.

The shadow stood on the far side of the tree with its sword already out.

Link drew.

He did not see it cross the water. It was there, and the first cut was already coming, and it was his cut, the one he always opened with. He got the shield to it late. He did not get to the second at all. The third went past his ear. The fourth hooked low behind the knee, the way he had hooked a hundred Stalfos, and he felt the leg start to go. The mark on the back of his left hand burned gold, and he kept his feet.

The fifth was the same hook. There was no gold left.

He hit the water on his back, and it was on him three times before he could roll.

*So that's what it's like*, he thought. He had never been on this end of it.

He got a hand to his belt, pulled the cork with his teeth and drank the red one, all of it. It went through him like a hot meal after a week of rain. The cuts closed. He stood up out of the water.

He threw a Deku Nut. It cracked white, and the shadow's arm was already across its eyes. It had been there before the nut left his hand. It knew when he threw them. It would have thrown one then too.

He went in. His cut met its cut, edge to edge, at the same angle with the same weight behind it, and stopped dead. He cut again, and it was the same. The third time he was a hair faster than himself, and the Master Sword went in. The black turned white where the blade touched it. The sword knew what it was for.

The shadow sank. It went straight down into an inch of water like a stone into a well, and the water closed over it without a ripple. Link was already turning, because he knew where he would have come up. He cut backhand and caught it rising.

Then it was his own guard again. One cut slid past it. One rang.

He thrust, and the weight on the end of his sword was wrong. He looked up.

It was standing on the blade.

It cut down at his face, and he got the shield there, barely.

Behind him, at the bar, somebody whistled.

**The Shadow**

It had no name. It had his.

It had his arm and his feet and the weight of his sword. It knew everything his hands knew, since they were the same hands. It knew nothing else. It had never been anywhere he had not. It had stood in a room with one tree for as long as there had been a room, and waited for the shape it was to walk in.

It did not hate him. There was nothing in it to hate with. He swung, so it swung. He was there, so it was.

There were bottles on its belt, because there were bottles on his. There was nothing in them.

It came up out of the water behind him and cut him across the back before he had finished turning. Then it did what he would have done: everything, at once, without stopping for breath. Eight cuts. He turned three of them. Five went in.

It did not feel that. It felt the two places where the bright sword had gone into it. Those did not close. Nothing here would close them. Only one thing ever had, and that was him walking out of the room.

They were the only things it had ever been given that were not his.

**Jin**

Jin had lost to that boy twice, and both times he had learned something. He was learning something now, and he did not like it.

"It's him," the big swordsman said, down the bar. "Every cut. Even the bad habits."

"He drops his shoulder before the thrust," said Jin.

"Yeah. So does it."

The cowboy had tried to get a wager going before the start, out of habit, and had found that nobody in the place had any money, himself included. Nobody had wanted the shadow anyway. Eight cuts later, nobody wanted the boy.

Out on the water the boy threw another of his nuts, and again the black arm was up before the flash.

Jin had been counting without meaning to. It was the kind of thing he counted. Three times in the first exchange the two swords had met edge to edge, perfectly, as no two swords ever met. Now they met a fourth time. The boy got one cut through, and the shadow dropped into the water and came up at his back. They met a fifth time.

"Six," Jin said, before it happened.

The sixth time, the black sword was late. It was not late by much. But it rang wide, and the whole body went after it, off its line and open from shoulder to hip.

The boy did not waste it. He cut twice, and the cuts went white. The shadow folded around the second one.

"How did you know?" said the cowboy.

"A mirror is never late," Jin said. "That is not a mirror. It is something doing what he does as fast as he does it. No one can keep that up. Not even him."

"I have fought myself," the god said, to his mead. "There was no audience."

Spike looked over. "How'd that go?"

"I am here."

The boy's last thrust carried him a step too far. When Jin looked back, the shadow was standing on his sword again, and this time the shield was nowhere near.

**The Shadow**

After that, nothing he did touched it.

It cut him, and he drank from the blue bottle and was whole. It cut him again. He stood still and breathed, and was a little more whole. It cut him.

He threw his nuts, and it covered its eyes. He swung, and it stepped where he would have stepped. He swung, and its sword was where his would have been. When he thrust, it stood on the blade and cut down. Twice it leapt and came down on him with both hands, as he would have. Once he was not under it. Once he was.

It could do this forever. It had never done anything else.

But each time it cut him there was less of him to cut. And something was happening that it had no way to know about, because he did not know it yet either.

**Smasher**

TARGET A (GREEN). SWINGS, LAST FOUR CYCLES: 12. HITS: 0.

CONSUMABLES: RED, EXPENDED. BLUE, EXPENDED. FLASH ORDNANCE: 2 OF 10. EFFECT ON TARGET: NONE.

INTEGRITY: 13%.

TARGET B (BLACK). NO HEAT. NO MASS. NO RETURN ON ANY BAND. INTEGRITY: [NO VALUE].

His sensors still said there was one fighter on the water, swinging at nothing and being cut to pieces by it. The cuts were real. He had magnified them.

PROJECTED WINNER: TARGET B.

"He is finished," Smasher said.

"He does this," said the samurai, who had not taken his eyes off the water.

"Does what?"

"Waits until there is almost nothing left of him."

"Partner," said Spiegel, "you're oh and three in this place. Maybe don't call it."

"Do not call me that."

**Link**

He had two nuts left, and two breaths, and two bottles with a light in them.

He took one of the breaths. It bought him a little.

He threw a nut, because his hand did it. The arm was up before the flash.

He swung, expecting his own sword in the way, and it was in the way. But it rang wrong. The black blade went wide. It had only met him once.

He did not stop to wonder. He cut it twice, and the white went deep.

It sank and rose and came for him, and he understood it while it was cutting him. It was his. It had his arm, and his arm was nearly done. It could not be more than he was. The less there was of him, the less there was of it.

So there was a way to win this, and it was to nearly lose.

Three of the four found him. He was on one knee, and the water around the knee was red.

He took the last breath. He threw the last nut. Nothing.

He swung, and the blades met. He swung, and they met. He swung with everything he had left, and they met, and the black sword flew wide, and the whole of it stood open in front of him.

His arm was at the end of its swing and would not come back.

One heartbeat. He had nothing to put in it.

Then the weight was on the end of his blade again.

**The Shadow**

One cut. Another.

He fell forward into the water and did not get up.

It stood over him with the sword raised, and the sword was hard to see. So was the hand that held it. It looked down for its feet and saw the sand through them.

It was a reflection, and what it reflected was gone. It had not known that it would go too.

It did not mind. It had nothing to mind with.

Then one of the bottles on his belt cracked, and a pink light came out of it, ringing, and went around him three times.

There were bottles on its own belt. It did not need to look.

He stood up. So it was solid again, and its arm came down.

**Link**

He could hear bells. They faded.

*You always save one.* He still had one saved.

The shadow cut him twice more as he rose, because that was what he would have done, and he let it, and got his feet under him.

He had no nuts, and no breath left that would buy him anything. He had the sword.

He cut, and it stepped where he would have stepped. He cut again, and it was not there either.

He did not aim the third. He had fought this whole fight the way he fought, and it knew the way he fought. Now he was too tired to fight like himself. The cut came out slow and ugly, from somewhere he would never have chosen, and the black sword went to where the good one would have been.

The Master Sword went through the middle of it.

It did not fall. It went thin, the way breath does on a window. He could see the tree through it, and then the mist. The red went last.

The water was still. He looked down.

His reflection looked up at him with its cap crooked, bleeding from the scalp and breathing hard.

Behind him the whole bar was on its feet, and the priest was pounding the counter with the flat of his hand.

---

## After

**Guts**

The wall was back, and the door in it was only a door. The slate said *LINK.* Under that, smaller: *(the green one).*

The kid sat with a rag pressed to his scalp and a fresh milk in front of him. The priest had offered to see to the cut, and had been turned down with a shake of the head, and had settled for telling the room at large what a fine fight it had been. The blue crystal had gone back into the pack.

The stool on the kid's far side was empty. The glass of water stood in front of it, full to the brim.

Guts had watched all of it. So had the man on his right, who had not moved the whole time, except once. When the kid went face down in the water, the green hand had closed on the edge of the bar, and the wood had cracked. The old man had not said anything about it.

"Hell of a thing," Guts said. "Having to fight yourself where people can watch."

The helmet turned.

"I've got one. It's a dog." He tapped his temple with an iron finger. "Big black one. It talks. Says all I need is the sword and something to use it on. Says everything else is weight." He picked up his cup. "It's not wrong about the weight."

He drank.

"I don't get to put a sword through mine. It doesn't come out. I just have to keep on not listening." He looked sidelong at the gold visor. "You?"

The man sat a while. Then he lifted his right hand off the bar and closed it, and looked at the fist. He opened it again and laid it flat on the wood.

"Yeah," Guts said. "That's the one."

The old man set down two cups. Guts took his.

A moment later, on his blind side, he heard a seal hiss.

He kept his eye on the lamp. A man was entitled.

**Link**

His head had stopped bleeding. He looked up at the row of glasses over the bar. There was the lamp in each of them, small and upside down. There were the steel man's red eyes, and Jin's sleeve.

Beside Jin's sleeve, in every glass, there was an empty stool.

Again.

He looked to his left.

It was sitting there. It had not come in by the door, and there was no water on the floor. It sat the way he was sitting, with a black hand around the glass.

Nobody reached for anything this time. The cowboy looked, and touched his hat, and went back to his drink.

"So that's how it is," Spike said. "He's staying."

Link thought about the room with the tree, and how long a thing might stand in it, waiting.

"Yes," he said.

He lifted his milk. Beside him the water rose with it. This time he did not stop.

They drank.
