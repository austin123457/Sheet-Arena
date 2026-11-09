# The Hero Nobody Remembers, and the Ghost Everybody Does

*Link, the Hero of Time, vs Jin Sakai.* The bar from [Dead or Alive](spike-arthur-vs-smasher.md), and a duel.

The fight is real, and it isn't close: Link won all 2,000 runs of `python battle.py 1v1 jin link`. This is the longest of 300, picked by `fight_log.py jin link 300`: 29 rounds. Jin's first turn takes Link from 224 to 84, the hardest anyone on the ladder hits him. Then Nayru's Love goes up, and for the next 28 rounds every one of Jin's blows lands for 0. Deku Nuts cost Jin four turns. Last Stand brings him back once and Iron Will four times, and Link never needs a fairy.

<details>
<summary>The round-by-round log</summary>

```
winner: Link in 29 rounds
R1 Jin     | hit 54 slashing hit 23 slashing hit 25 slashing hit 19 slashing miss hit 19 slashing  || Jin 225  Link 84
R1 Link    | {Link: sw 4->3, surges 2->1, nayru 0->10} miss miss miss  || Jin 225  Link 113
R2 Jin     | miss hit 0 slashing miss  || Jin 225  Link 113
R2 Link    | {Jin: paralyzed False->True, prone False->True} {Link: sw 3->2, surges 1->0, nayru 10->9} hit 9 slashing CRIT 17 slashing CRIT 19 slashing CRIT 34 slashing CRIT 20 slashing CRIT 16 slashing CRIT 14 slashing  || Jin 96  Link 135
R3 Link    | {Link: nayru 9->8} miss miss miss  || Jin 96  Link 135
R4 Jin     | {Jin: sw 4->3} hit 0 slashing hit 0 slashing hit 0 slashing  || Jin 115  Link 135
R4 Link    | {Jin: paralyzed False->True, prone False->True} {Link: nayru 8->7} miss CRIT 30 slashing CRIT 22 slashing  || Jin 63  Link 135
R5 Link    | {Link: nayru 7->6} miss miss miss  || Jin 63  Link 135
R6 Jin     | {Jin: sw 3->2} miss miss hit 0 slashing  || Jin 80  Link 135
R6 Link    | {Link: nayru 6->5} miss hit 15 slashing miss  || Jin 65  Link 135
R7 Jin     | {Jin: sw 2->1} CRIT 0 slashing miss miss  || Jin 85  Link 135
R7 Link    | {Jin: prone False->True} {Link: nayru 5->4} miss hit 11 slashing CRIT 25 slashing  || Jin 49  Link 135
R8 Jin     | {Jin: sw 1->0} hit 0 slashing hit 0 slashing hit 0 slashing  || Jin 64  Link 135
R8 Link    | {Jin: paralyzed False->True} {Link: nayru 4->3} miss miss hit 12 slashing  || Jin 52  Link 135
R9 Link    | {Jin: paralyzed False->True} {Link: nayru 3->2} miss miss hit 16 slashing  || Jin 36  Link 135
R10 Link    | {Jin: last_stand True->False} {Link: nayru 2->1} hit 8 slashing hit 17 slashing <Jin DROPS TO 0> <Jin back up at 108> hit 17 slashing  || Jin 108  Link 135
R11 Jin     | hit 0 slashing hit 0 slashing hit 0 slashing  || Jin 118  Link 135
R11 Link    | {Link: nayru 1->10}  || Jin 118  Link 135
R12 Jin     | miss hit 0 slashing miss  || Jin 118  Link 135
R12 Link    | {Link: nayru 10->9} hit 6 slashing hit 11 slashing miss miss  || Jin 101  Link 135
R13 Jin     | hit 0 slashing miss hit 0 slashing  || Jin 101  Link 135
R13 Link    | {Link: nayru 9->8} miss hit 12 slashing miss hit 13 slashing  || Jin 76  Link 135
R14 Jin     | hit 0 slashing miss hit 0 slashing  || Jin 88  Link 135
R14 Link    | {Link: nayru 8->7} miss hit 18 slashing miss hit 16 slashing  || Jin 54  Link 135
R15 Jin     | hit 0 slashing miss hit 0 slashing  || Jin 61  Link 135
R15 Link    | {Link: nayru 7->6} miss hit 13 slashing hit 14 slashing miss  || Jin 34  Link 135
R16 Jin     | hit 0 slashing hit 0 slashing hit 0 slashing  || Jin 50  Link 135
R16 Link    | {Link: nayru 6->5} miss miss miss miss  || Jin 50  Link 135
R17 Jin     | hit 0 slashing hit 0 slashing miss  || Jin 63  Link 135
R17 Link    | {Link: nayru 5->4} hit 6 slashing miss hit 18 slashing hit 11 slashing  || Jin 28  Link 135
R18 Jin     | hit 0 slashing hit 0 slashing hit 0 slashing  || Jin 34  Link 135
R18 Link    | {Link: nayru 4->3} miss miss miss hit 11 slashing  || Jin 23  Link 135
R19 Jin     | miss hit 0 slashing hit 0 slashing  || Jin 36  Link 135
R19 Link    | {Link: nayru 3->2} miss hit 16 slashing miss miss  || Jin 20  Link 135
R20 Jin     | miss hit 0 slashing hit 0 slashing  || Jin 33  Link 135
R20 Link    | {Jin: iron_n 0->1} {Link: nayru 2->1} hit 8 slashing hit 16 slashing <Jin DROPS TO 0> <Jin back up at 22> hit 12 slashing hit 18 slashing  || Jin 4  Link 135
R21 Jin     | hit 0 slashing CRIT 0 slashing hit 0 slashing  || Jin 14  Link 135
R21 Link    | {Link: nayru 1->10}  || Jin 14  Link 135
R22 Jin     | hit 0 slashing hit 0 slashing hit 0 slashing  || Jin 26  Link 135
R22 Link    | {Jin: iron_n 1->2} {Link: nayru 10->9} hit 7 slashing hit 11 slashing <Jin DROPS TO 0> <Jin back up at 22> hit 13 slashing hit 13 slashing  || Jin 9  Link 135
R23 Jin     | hit 0 slashing hit 0 slashing hit 0 slashing  || Jin 16  Link 135
R23 Link    | {Jin: iron_n 2->3} {Link: nayru 9->8} miss <Jin DROPS TO 0> <Jin back up at 22> hit 17 slashing miss miss  || Jin 22  Link 135
R24 Jin     | CRIT 0 slashing hit 0 slashing hit 0 slashing  || Jin 37  Link 135
R24 Link    | {Link: nayru 8->7} miss miss miss miss  || Jin 37  Link 135
R25 Jin     | hit 0 slashing hit 0 slashing hit 0 slashing  || Jin 51  Link 135
R25 Link    | {Link: nayru 7->6} hit 7 slashing hit 11 slashing hit 14 slashing hit 11 slashing  || Jin 8  Link 135
R26 Jin     | hit 0 slashing miss hit 0 slashing  || Jin 29  Link 135
R26 Link    | {Link: nayru 6->5} miss miss miss hit 12 slashing  || Jin 17  Link 135
R27 Jin     | miss CRIT 0 slashing hit 0 slashing  || Jin 25  Link 135
R27 Link    | {Link: nayru 5->4} miss hit 6 slashing hit 16 slashing <Jin DROPS TO 0> <Jin back up at 22> hit 14 slashing  || Jin 22  Link 135
R28 Jin     | CRIT 0 slashing hit 0 slashing hit 0 slashing  || Jin 36  Link 135
R28 Link    | {Link: nayru 4->3} miss CRIT 18 slashing miss hit 14 slashing  || Jin 4  Link 135
R29 Jin     | miss hit 0 slashing hit 0 slashing  || Jin 23  Link 135
R29 Link    | {Link: nayru 3->2} miss hit 18 slashing <Jin DROPS TO 0> <Jin OUT> hit 11 slashing  || Jin 0  Link 135
```

A drop to 0 is logged just before the attack that caused it. Jin's HP includes his 10 temporary HP. Every "hit 0" is a blow into Nayru's Love. The rounds where Jin has no line are rounds he lost to a Deku Nut. Jin's healing between Link's turns is Second Wind, then Resolve, then Recovery dice.

</details>

---

## The Bar

**Jin**

The bar was quiet when Jin Sakai stepped into it.

He did not remember the door. One moment there had been the cliffs of Tsushima, gray sea and gray sky, and his uncle's voice still ringing in his ears. The next there was a low wooden room with lamps burning, a long counter and an old bartender with a face like a weathered post.

There was an ashtray on the counter with two cigarette ends in it, side by side. Someone had left them there carefully.

At the far end of the counter sat a young man in green.

He was perhaps eighteen or twenty. He had fair hair under a long pointed cap and ears that came to points, like the kami in old scroll paintings. A sword was strapped across his back with a violet hilt, the hilt of a blade that had been made by something other than men. Leaning against his stool was a shield painted with a red bird and three golden triangles.

He was drinking a glass of milk.

Jin sat down two stools away. The bartender set a cup of sake in front of him without being asked.

They sat in silence for a while. It was a good silence. Jin had not had one of those in a long time.

"That sword," Jin said at last. "It is very old."

The young man looked at him. His eyes were blue and very calm, and much older than his face.

"Yes," he said.

"And you are very young to carry it."

The young man considered this.

"Not really," he said.

Jin waited, but that seemed to be all.

"I am Jin," he said. "Of Clan Sakai. Once." He turned the sake cup in his fingers. "Now they call me the Ghost."

The young man tilted his head.

"I made a choice," Jin said. He had not meant to say it. Perhaps it was the sake, or the quiet. "The Mongols came to my island. They burned the villages and killed the samurai, all of them, in one morning on the beach. My uncle and I were all that was left. He told me there was only one way to fight: face to face, with honor, the way our ancestors had." He drank. "But the way our ancestors fought was dying on that beach. So I learned another way. I struck from the shadows, and I used poison, and fear. I saved my people."

"And they hate you," the young man said quietly.

Jin looked at him.

"The Shogun has named me a traitor," he said. "My uncle was ordered to kill me. The people I saved whisper my name like a curse, or a prayer. I do not know which is worse." He set the cup down. "What about you?"

The young man was quiet for so long that Jin thought he would not answer.

"Saved them," he said finally.

"Who?"

"Everyone. My kingdom." A pause. "Then they sent me back. Before it happened."

Jin frowned. "Back?"

"Seven years." The young man turned his glass slowly on the counter. "So it never happened. Nobody remembers."

Jin was silent.

"Then another place," the young man said. "A moon falling. Three days, over and over." He shrugged a little. "Saved them too."

"And they don't remember either."

"No."

The lamps flickered. Somewhere in the back the bartender was polishing glasses.

"You have saved two worlds," Jin said slowly, "and nobody knows your name."

"Link," the young man said.

Jin looked at him for a long time. Then, very slowly, he began to laugh. It was not a happy laugh, but it was not a bitter one either.

"Link," he said. "I saved one island, and everyone knows mine. You saved two worlds, and no one knows yours." He shook his head. "The gods are strange."

Link almost smiled.

"What are you looking for?" Jin asked. "Here, in this place. Everyone who comes here is looking for something."

Link's hand went to an empty bottle hanging on his belt, a small glass bottle with a cork. Jin had noticed it earlier and assumed it was for water.

"A friend," Link said.

Jin did not ask. He understood looking for someone who was not coming back.

He stood. He bowed, a full bow, the formal one he had not given anyone since the beach at Komoda.

"Link of the forgotten kingdom," he said. "I have not fought an honorable duel since the day I became the Ghost. No one will face me openly anymore. They think I will put a knife in their back." He straightened. "Would you do me the honor?"

Link looked at him for a long moment.

Then he finished his milk, stood, and slung the shield onto his arm.

He nodded once.

---

## The Duel

**Jin**

Open sand under a white sky. Thirty paces between them, and wind.

Jin stood with his hand on Sakai Clan steel and breathed. He let the world narrow to the man in green: his feet, his shoulders, the place his weight sat. This was the Standoff, the old way, the way his father had taught him. Two men, one breath, and whoever moved second died.

The wind dropped.

Jin *moved*.

He was across the sand before the young man's hand had closed on his hilt. The first cut was the Heavenly Strike, everything he had, a blow that could split armor and the man inside it. It caught Link across the chest and threw him back a step.

Jin did not stop. He would not have been alive if he had ever stopped.

The second cut, the third, the fourth: the old forms his uncle had taught him, flowing one into the next like water down a mountain. He felt each one land. Link's green tunic went dark, and the shield came up too late. On the fifth the young man's knees buckled.

When Jin stepped back, Link was on one knee in the sand, and his blood was soaking into it.

*It is over*, Jin thought. *He is very good, but it is over.*

Link looked up at him and *raised his hand*.

**Link**

That hurt.

He'd been hurt worse. Ganon had hurt him worse, and Majora had. But not often, and not that fast. He had not even seen the first cut.

*Good*, he thought. *He's good.*

He breathed and felt his body steady, a little. Enough. Then he raised his hand and called on Nayru.

The light came down around him like water, a great diamond of blue crystal, clear as ice and humming faintly. He stood inside it, bleeding, and looked out at the Ghost through the blue.

He reached into his pouch and threw a Deku Nut.

The flash went off like a thunderclap, and the Ghost froze mid-step, stunned. Link went in.

He didn't fight with forms. He'd never had a teacher, only a forest and a sword and a great many monsters. But he had done this for seven years that didn't exist and three days that happened a hundred times. He knew where to put the blade.

He struck seven times. Most were clean, and some were perfect.

**Jin**

He came back to himself on his knees, with blood in his mouth and the world spinning. The young man was standing over him inside a cage of blue light.

*Sorcery.*

He rose and cut.

The blade stopped against the blue light like it had struck a mountain. There was no sound, no spark. The edge simply *stopped*, and the young man inside did not even flinch.

He cut again, and again, the best cuts of his life. He felt each one land and *stop*, as if he were cutting the sea.

Then a flash. The world went white, and when it came back he was on the ground again, and the young man's sword was coming down.

**Link**

He didn't stay down.

That was the thing Link kept noticing. The Ghost went down, and got up. He went down again, and got up. He'd bring something to his lips, or breathe deep and steady himself somehow, and then he was cutting again. Every cut stopped dead on Nayru's light, and he kept cutting anyway.

At the tenth exchange, Link put him down for real. The Ghost hit the sand and lay still.

Then he sat up and stood, with blood running down his face and something burning in his eyes.

"*Not yet*," the Ghost said.

He came again.

**Jin**

*Not yet.*

He did not know how many times he had cut the blue light now. Fifty, a hundred. His arms were lead. His katana was nicked, the edge his father had given it ground away against something no blade could touch.

He thought of the beach at Komoda, of eighty samurai charging into the Mongol lines in the old way, and dying. He thought of Taka, who had believed in him and been killed for it. He thought of Yuna and Lady Masako, of Sensei Ishikawa and Kenji, and of his uncle's face when he'd said *you have disgraced our family*.

He'd broken everything for them. His code, his name, his uncle's love. He had made himself into something that walked in the dark, so that they could walk in the light.

He could not cut through the blue light. He knew that now. He had known it for a long time.

He cut it anyway.

**Link**

Twenty exchanges. The light faded around him, and he called it back. The Ghost didn't even pause.

Link knew this man. Not his face. He knew the *thing* in him, the thing that would not stop. He'd seen it in a mirror in the Temple of Time, in the face of a boy who didn't know the world was going to forget him. He had it himself.

The Ghost went down, and got up. He went down a third time, and got up. A fourth time, his whole body shaking. He came up with his sword, with nothing left but the refusal, and cut the blue light one more time. It stopped, as it always did.

Link felt something tighten in his chest that wasn't a wound.

He thought of the masked boy in Termina, and the Happy Mask Salesman, and a moon with a face. He thought of a fairy who had flown away through a window and never come back. He thought of all the people he'd saved who had never known, and the swordsmanship he'd learned that no one would ever learn from him.

*Someday*, he thought. *Someday I'll teach someone.*

He struck the last time, clean and quick, across the back of the knee.

The Ghost fell, and this time he did not get up.

**Link**

The blue light faded.

Link knelt beside the Ghost. He was breathing, barely: shallow, ragged and slowing. His hand was still on his sword. His eyes were open, looking at the white sky.

Link looked at him for a long moment.

Then he reached for his belt and unhooked one of the bottles. Not the empty one, one of the full ones. A small pink light was pulsing inside.

He'd been saving it. You always saved one, for when you needed it most. That was the rule. He'd learned it the hard way, in a hundred dark dungeons.

He pulled the cork.

The fairy came out in a spiral of pink light and chiming bells, and circled once around Link's head as if asking a question. Link nodded toward the man on the ground.

It went.

**Jin**

He was warm.

That was the first thing. He'd been cold, so cold, the cold of the sea and the dark. Now there was warmth and light and a sound like small bells. Something was circling over his chest, leaving a trail of pink light behind it. Every time it passed, he felt a wound close.

He sat up.

Link was kneeling beside him, holding an empty bottle. The young man looked very tired.

"Why?" Jin asked.

Link looked at the bottle in his hand, then at Jin.

"You'd have done it," he said.

Jin opened his mouth, and closed it again.

He thought of all the times he'd knelt beside someone dying, a peasant or a samurai or a child the Mongols had left behind. He thought of how many times he'd given away the last of his medicine.

"Yes," he said quietly. "I would have."

Link stood and offered his hand. Jin took it and rose, and found that his legs held.

They walked back to the bar in silence. It was a good silence again.

The bartender had set out two cups: sake for Jin, and another glass of milk. On the counter between them sat a small glass bottle, corked, glowing pink.

Link looked at it, surprised. He looked at the bartender, who didn't look up from his polishing.

Link picked up the bottle and hung it back on his belt, next to the empty one. He put his hand on the empty one for a moment.

Jin raised his cup.

"To the people who will never know our names," he said. "Or who will only remember the wrong ones."

Link raised his milk.

They drank.
