# The Chair

*Arthur Morgan vs FLLFFL.* The drawn man has laid his sword on the counter and taken his hand off it. Tonight the slate gives him the man who drew him, and he has to pick it back up. It comes after [Intermission: Epona's Song](intermission-eponas-song.md).

The fight is real: the most dramatic of three batches of 400 runs of `python battle.py 1v1 alfa arthur`, picked by `fight_log.py alfa arthur 400`. Alfa is the favorite: 69.6% of 4,000 through `battle.py`. In a separate count of 4,000 he won 2,829, 2,699 of them in the second round and 101 in the third, and only 16 times did he finish on 20 hit points or fewer. This is one of those. Arthur wins initiative and shoots first. He brings up Dead Eye with a free shot, paints five more, and Action Surges for four: ten shots. Alfa's Uncanny Dodge halves the first, Peerless Aim turns the one miss into a hit, and Alfa is at 89 of 217 before he has moved. Then Alfa takes a Second Wind, Action Surges, and makes six cuts without a miss, with the flame behind every one and a Sneak Attack and Assassinate's 7 on the second: 147, and Arthur is at 76. Round 2 is the same trade at half the size. Arthur spends his last Dead Eye box and his last Action Surge on eight shots (Alfa 19), and three cuts take him to 26. In round 3 Dead Eye is gone. Arthur's bonus action can drink the snake oil that would bring it back or take a Second Wind, and on 26 he breathes. Four plain shots leave Alfa on one hit point. Alfa breathes too, to 16, and cuts. The first cut takes Arthur to 26 again. The second takes him to 9 with the steel, and the flame on it is 9.

<details>
<summary>The round-by-round log</summary>

```
winner: Alfa in 3 rounds
R1 Arthur  | {Arthur: deadeye False->True, boxes 6->1, surges 2->1} ** Alfa: Uncanny Dodge ** hit 5 piercing hit 14 piercing hit 10 piercing hit 17 piercing hit 13 piercing CRIT 21 piercing hit 11 piercing hit 12 piercing miss [Arthur -> Alfa: 12 piercing] hit 13 piercing  || Alfa 89  Arthur 223
R1 Alfa    | {Alfa: sw 4->3, surges 1->0} [Alfa -> Arthur: 9 fire] hit 16 slashing [Alfa -> Arthur: 7 slashing] [Alfa -> Arthur: 8 fire] hit 23 slashing [Alfa -> Arthur: 7 fire] hit 11 slashing [Alfa -> Arthur: 4 fire] hit 11 slashing [Alfa -> Arthur: 12 fire] hit 18 slashing [Alfa -> Arthur: 6 fire] hit 15 slashing  || Alfa 108  Arthur 76
R2 Arthur  | {Arthur: boxes 1->0, sw 4->3, surges 1->0} ** Alfa: Uncanny Dodge ** hit 9 piercing hit 11 piercing hit 10 piercing hit 13 piercing hit 13 piercing hit 15 piercing hit 8 piercing hit 10 piercing  || Alfa 19  Arthur 98
R2 Alfa    | {Alfa: sw 3->2} [Alfa -> Arthur: 5 fire] hit 27 slashing [Alfa -> Arthur: 8 fire] hit 14 slashing [Alfa -> Arthur: 5 fire] hit 13 slashing  || Alfa 35  Arthur 26
R3 Arthur  | {Arthur: deadeye True->False, sw 3->2} ** Alfa: Uncanny Dodge ** hit 9 piercing hit 11 piercing miss [Arthur -> Alfa: 7 piercing] hit 7 piercing  || Alfa 1  Arthur 54
R3 Alfa    | {Alfa: sw 2->1} [Alfa -> Arthur: 4 fire] hit 24 slashing <Arthur DROPS TO 0> <Arthur OUT> [Alfa -> Arthur: 9 fire] hit 17 slashing  || Alfa 16  Arthur 0
```

The flame is logged as its own line, `[Alfa -> Arthur: N fire]`, just before the hit it rode in on. The `[Alfa -> Arthur: 7 slashing]` on the second cut of round 1 is Assassinate, the extra 7 on his first Sneak Attack of the fight. `** Alfa: Uncanny Dodge **` comes before the shot it halved: the first shot of every Arthur turn, the 5 in round 1 a 10. A `miss` followed by `[Arthur -> Alfa: N piercing]` is Peerless Aim, which makes one miss a turn a hit. `boxes` are Dead Eye: in round 1 Arthur spends one to bring it up with a free shot and five on the Painting, and gets one back for the critical hit. `sw` is Second Wind, and the totals after `||` already have it in them: Alfa ends round 1 on 108 because he was on 89 and breathed for 19. A drop to 0 is logged just before the attack that caused it. In round 3 it comes before `[Alfa -> Arthur: 9 fire]` and not after `hit 24`, because the fire did it: the second cut's steel, 17, had left Arthur standing on 9.

</details>

---

## The Bar

**Arthur**

The sword was still on the counter.

It had been there three nights now, between the tin of oil and the teacup, and the feller had not touched it except to wipe it down. Arthur had watched him do it. He'd lift the blade an inch, run the rag along it, and set it down again, and then take his hand back like a man taking his hand off a stove. The gray hand went to the cup after. It had found the cup the first night and it had not let go of it since.

Link's stool was empty. The shadow sat beside it with its glass of water, the same as always, and nobody sat in the stool. Down the bar the old Japanese gentleman had his paper out. Under the one mark he'd made the night the boy left, there were two columns now, and the brush was wet again.

Arthur coughed. It came up out of him the way it did lately, from a long way down, and he rode it out bent over the bar with his hat in his hand. When he looked up, the drawn man was watching him.

It wasn't the way most folks watched it. Most folks looked away, or looked at the handkerchief. The feller looked at Arthur's face the whole way through, without any pity in it. He looked like a man who had sat by a good many beds.

"How long," the feller said.

"Doc told me." Arthur put the handkerchief away. "Don't matter what he told me."

The green head nodded, once.

"That arm," Arthur said. "I been meaning to ask. It ain't the first thing I drew wrong, but I'd like to know what I drew."

"A man named Pulse."

"He still around?"

"He lost."

"Cost you an arm, to win."

"Yes."

Arthur turned his glass. "Seems to be about the price of most things worth winning."

The old man had come round the counter. He wiped the slate with his sleeve, and Arthur knew before the chalk touched it.

> **TONIGHT:**
>
> MORGAN v FLLFFL

"Fliffle again," Spike said.

"Alfa."

"I know. I just like saying it."

"Probability FLLFFL," said the machine at the end of the bar, "seventy percent."

Arthur laughed. It cost him a little, but he did it. "Then I got thirty. Mister, I've had worse. Most of my life was worse."

"Ooh, I'll take the seventy." The handsome face had come alive two stools down. "Spike. Buddy. Cowboy, ten thousand. You in?"

"I've got four woolongs and a bad attitude."

"Done. Shake on it. No, don't shake, I've seen where your hands have been."

The drawn man was looking at the sword.

His gray hand had come off the cup. It was over the grip, an inch off it, and it had stopped there. Arthur had seen men stop like that over a bottle. He had stopped like that himself.

"You gonna pick that up?" Arthur said.

"I'd decided not to."

"For how long?"

"I hadn't got that far."

"Well," Arthur said. "I'd sooner you did. I been shot at by men with no fight left in 'em, and it ain't no compliment to either party."

The old swordsman did not look up from his paper. "It is a sword," he said. "It is no better than the hand, and no worse. Pick it up as you would a tool. Not as an apology."

The gray hand closed on the grip. The blue flame came on at the back of the blade with a sound like silk tearing, and the whole bar looked at it, and then nobody did.

"I don't kill," Alfa said.

"So they tell me. Nobody does, in here." Arthur stood and settled his gunbelt. "I have, though. A whole lot. I ain't proud of most of it."

"I know."

"How's that?"

The green head tilted a little at the Schofield on his hip. "You wear it like it's heavy."

Arthur did not have anything to say to that. He went to the door and opened it.

It was sand. It was sand most nights: open sand, a sky too wide and too blue, and a mark sixty feet off. He'd stood on it the first night, against the feller in blue, and lost. He walked out to his mark. Behind him he heard the flame come through the door, tearing, and then he heard it stop moving, sixty feet away.

---

## The Sand

**Alfa**

He had moved first in every fight he could remember. That was the whole of how he fought. You lit the flame and you were there before the other man had finished deciding, and there were seven cuts, and it was over. Fourteen seconds.

The cowboy's hand moved before the flame was all the way lit.

Alfa saw the gun come up out of the holster, and he put the flat of the blade where it was pointing, and the bullet hit the steel and went half into the steel and half into his side. That was good. That was what he had expected.

Then the cowboy's eyes changed.

Alfa could not have said how. They went still, the way an animal's go in the moment before it moves, but they stayed that way. The hand was doing something to the hammer, very fast, and the gun went off five times in what sounded like one long sound. Alfa moved. He was moving the whole time. It made no difference. Each of the five was already where he was going to be. One of them broke a rib on the way through.

Then the man had both hands on it, and fanned it four more times, as if the first five had been somebody else's turn. The third of those four missed him by the width of a finger. He felt it go past. Then it was in his hip. He had not seen the man shoot again. He would think about that afterward, how a man could take a miss back.

Ten bullets, and he had not taken a step.

He was standing on the sand with less than half of himself, and the cowboy was reloading with the stillness gone out of his eyes. This was the other end of fourteen seconds. He had never been on it.

He breathed. It was a long breath, and it put him partway together again. Then he lit the jet all the way and went.

Sixty feet is nothing. He was on the cowboy before the cylinder closed. The first cut went in under the gun arm, and the flame came after it. The second came round the other way with the whole of his weight, low across the belly, and that was the one the cowboy would remember. Then four more, so fast they were one motion, the flame behind each, the jet throwing him round the man and back.

The cowboy's shirt was on fire. He stood there in it, and coughed, and did not fall.

Alfa had taken the measure of him in the bar. He had watched him cough. He knew what this man had, and how long, and it had made no difference to where the cuts went. It never did. He knocked men down. He did not decide how sick they were first.

---

**Arthur**

He'd seen a train come at him once, at night, on a trestle. You saw the light, and then you heard it, and then it was on you, and there was no part in between.

The drawn man came like that.

Arthur was a third of himself when it stopped. His shirt was burning in six places and he slapped at it with his hat, and the cough came, and he rode it out with the Schofield hanging off one finger. There was blood in it. There was always blood in it now. He spat, and looked up, and the feller was ten feet off with that sword held out to the side, and the flame tearing.

The feller was waiting for him to finish coughing. Arthur saw that, and it near made him laugh.

He found the breath. It was a trick he'd learned in camp, under a wagon, a long time ago: you breathed down past the pain to where there was still something left, and you brought it up with you. It got him back to his feet properly.

Then he spent the last of it.

There was a little Dead Eye left, the dregs. He let the world go slow. The sand went the color of old paper and the sky went the color of tin, and the feller came apart into the places a bullet could go. Eight of them. The first, the feller turned on the flat of that blade like a man brushing off a fly, and half of it went through him anyway. The other seven he didn't turn. They all went in.

The feller was very nearly done. Arthur could see it in how he stood.

So could the feller. He breathed, the way Arthur had, and came again.

There were only three this time. The first went deeper than any of the six before it, a cut that went in at the collarbone and came out somewhere south. The fire came after it. The second and third Arthur hardly felt. He was on his knees, and then he was up again, because getting up was the one thing he had always been good at.

---

**Spike**

The old man had the television on, and Spike had his four woolongs on the bar in a little stack, where Jack could see them.

He'd been on that sand with Arthur. He knew what the cowboy's eyes did right before. He'd seen the color go out of the man's face like somebody had turned down a lamp, and then there had been six bullets in the air at once, and he'd only gotten out from under about half of them. So when the glass went quiet for a second, and the brown mark on it went very still, Spike said, "Here it comes," and it came.

"Ten," Jin said quietly. "He took the miss back."

"He does that," Spike said. "It's rude."

Then the green mark was across the sand, and there was no more counting anything. Spike had been cut in his time. He had been cut by a man with a katana who was very good, more than once. That man had needed a lot of room. This one didn't need any. He came in, and there was a flash of blue, and he was round the far side of Arthur, and there was another, and he was back.

"Fifty-five," said the machine. "Revised."

"Revised to what?"

The red eyes did not leave the glass. "Insufficient data."

"Ha!" Jack slapped the bar. "That's my guy. Look at him. Look at that little rocket go. Spike, you can give me the woolongs now if you want, save us both the walk."

"Watch the show, Jack."

The second round went like the first, only smaller, as if both of them had been asked to do it again and had less to do it with. The cowboy went still and shot eight times. The green man came in three times. When it stopped they were both standing, and Spike, who had stood like that, could see that neither of them had any business doing it.

Anderson had his rosary out. He wasn't praying for anyone in particular. Spike didn't think he was, anyway.

"Who's ahead?" said Jack.

Nobody answered him. Down at the end of the bar, Link's shadow had turned on its stool to watch, and its hand was on its hilt again.

---

**Arthur**

There wasn't any more Dead Eye. He'd known that since the last of it went. The world stayed fast and bright and the color stayed in it, and the feller with the sword stood across from him with the flame tearing.

Arthur put his hand in the satchel and found two things.

One was the snake oil. Half a bottle. It would light the fire behind his eyes again, and the world would go slow, and he could paint that feller from the hat down. The other was not in the satchel at all. It was the last of the breath, the one under the wagon, and he could feel how little was left of it.

He couldn't do both. A man never could.

He was on his feet and not much else. He let go of the bottle, and breathed.

Then he did what he had always done, when there wasn't anything else: he shot straight, and he shot fast, and he hoped.

The first, the feller turned on the flat of the blade, the same as always, and some of it went in. The second went in clean. The third missed. Arthur saw the feller lean out from under it, the way a man leans out from under a branch on a horse. And Arthur, who had been taking misses back his whole life without ever knowing what it was he did, put another round down the same line before the feller could come back from the lean, and it took him where the third would have. The fourth went in too.

The feller swayed.

Arthur had shot a great many men. He knew what it looked like when there was nothing at all left in one. There was nothing left in this one. A strong wind would have done it. A harsh word would have done it.

He thumbed the hammer back, and the cough came up out of him.

It came from the bottom of everything. It folded him over where he stood, and he heard the Schofield hit the sand, and he could not stop it to pick it up. He coughed, and coughed, and through it he could hear the flame, and it was not moving. The feller was not coming. He was standing there with nothing left in him at all, and waiting for Arthur to be done.

When Arthur straightened up, with the gun back in his hand, the feller breathed.

---

**Alfa**

He had one breath left, and nothing else.

He did not know how he was standing. He had stood through a great deal in his life, but he had always known how. This time he simply was, the way a post stands in a field after the fence is gone. The cowboy had been coughing, and Alfa had waited, because the cough was not the cowboy and he did not fight it. Now the cowboy had straightened up, and the gun was back in his hand, and Alfa took the breath.

It gave him a little. Enough to lift the sword.

He went in. The first cut took the cowboy across the ribs, and the flame came after it, and the cowboy was still standing. That was all right. Alfa had felt him go down to his knees before and come up again.

The second cut he measured.

He had done this a thousand times. You learned it after the first man you nearly killed. You felt for the edge of what a man had left, and you put the steel just there, to the hair, and no further. The steel did as it was told. It went in at the shoulder and stopped where Alfa stopped it, and he felt in his hand that the cowboy had a little left. Nine, the smith in him would have said, if anyone had asked him to put a number to it. Enough to stay standing. Enough to fall down on his own, later, when he chose to.

Then the flame came after the steel, the way it always did.

He had never felt it separately before. It had always been one thing, the cut and the fire, the way the hammer and the ring are one thing. But the old swordsman had pulled them apart for him at the bar, and now he could not put them back. He felt his own cut stop. He felt the fire go on past where he had stopped it, along the cowboy's shoulder and up into his collar, and take the nine.

The cowboy looked at him with a sort of surprise. Then he sat down on the sand.

Alfa turned the blade away and held it out to the side, as far from the man as his arm would go. The flame went on tearing. It never went out. He had built it so.

"You waited on me," the cowboy said. He was lying back now, with his hat over his chest. "Twice."

"You were coughing."

"Most fellers'd take that."

"I fight the man," Alfa said. "Not what's wrong with him."

The cowboy thought about that. Then he laughed, very quietly, and it did not turn into a cough. "Well," he said. "That's a kindness I'll have to carry. I'm about full up."

His eyes closed.

Alfa sat down on the sand beside him, cross-legged, with the sword out to the side and the flame pointing away. He did not go back to the door. He sat there with the man until the man was gone, the way he would have sat by a bed.

---

## After

**Alfa**

The cowboy was on his stool with his hat over his face, and his chest going up and down. The old man had set a glass in front of him, and it was waiting.

Alfa had the stool beside him. He had taken it as soon as he came through the door, before the tea. The sword was on the counter between the oil and the cup, and his hand was not on it.

The slate said *FLLFFL.* After it, smaller: *(by one).*

"By one *what*?" Spike said.

"Hit point," said the machine. "Prediction confirmed. Margin: one."

Spike looked at the little stack of coins in front of him for a moment, and then pushed it two stools down. Jack picked one up and turned it over.

"What is this. What is a woolong."

"About a penny."

"About a *penny*." He held it up to the light. "I bet ten thousand against a penny."

"You took the bet, Jack."

Jack considered the coin a while longer. Then, to the general surprise, he put it in his breast pocket and patted it. "Best penny I ever made," he said. "I'm keeping this one. It's going in the museum."

The hat moved. The cowboy took it off his face and looked up at the ceiling, and then over at Alfa.

"You're doing the chair," the cowboy said.

"It's my part," Alfa said. "Last time I was on the other side of it."

"How long you been sitting there?"

"Since you came in."

The cowboy sat up slowly. He looked at the slate for a long time.

"One," he said.

"One."

"Hell." He picked up the glass, and drank, and set it down. "I had the gun up. I had the hammer back."

"I know."

"Didn't have the wind."

"No."

The cowboy laughed, and this time it did turn into a cough, and Alfa sat and waited for it to be done. It took a while.

"The second cut," Alfa said, when it was. "The steel left you standing. I measured it. You had nine."

"Then what put me down?"

"The fire."

The cowboy looked at the sword on the counter, and the blue flame at the back of it, tearing quietly to itself.

"Felt like all of it, from where I was," he said.

"It always does. From there." Alfa turned his cup. "I had never felt it apart from the cut before tonight. He showed me where to look." He did not have to say who. Down the bar the old swordsman went on writing, and did not look up, and Alfa thought that he had heard.

"It ain't part of you," the cowboy said slowly. "That's what you're saying. The fire."

"It's in the sword. I put it there. But it doesn't stop when I stop."

The cowboy was quiet for a while. His hand had gone to his chest, the way it did, without his seeming to notice.

"Well," he said. "I got one of them too."

He took the journal out of his satchel, and the pencil, and opened it to a clean page, and Alfa drank his tea and let him write.

---

*From the journal of Arthur Morgan, the page after the drawn man:*

> Lost today to the drawn feller, by one. One what I do not rightly know, but the machine says one and I believe it. I had the hammer back on the last of it and the cough come up and took the shot from me.
>
> He waited for me to finish coughing. Twice. Said he fights the man and not what is wrong with him. I never once in my life gave a man that, and I been given it now by a feller made of five lines, and I do not know where to put it.
>
> He says his fire is in the sword and is not part of him, on account of it don't stop when he stops. I have been thinking on it. I reckon the same goes for what is in my chest. It don't stop when I stop either. But it ain't me. I am going to try and remember that, for as long as I have got.
>
> He sat by me till I woke. Like kin.
