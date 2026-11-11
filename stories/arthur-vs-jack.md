# Expendable Assets

*Arthur Morgan vs Handsome Jack.* The bar has had one villain, and he has started asking questions. A new one comes through the door in the middle of a sentence, wearing a mask of his own face, and tells the room he is the hero. The slate has him against the man who coughs. It comes after [What Decides It](jin-vs-smasher.md).

The fight is real: the most dramatic of the fights Arthur won in 1,200 runs of `python battle.py 1v1 arthur jack`, picked by `fight_log.py arthur jack 1200 Arthur`. Arthur is the favorite here, which he almost never is: he took 62.9% of 4,000 runs through `battle.py`, and the usual fight is over in about five rounds. This one goes eight and he finishes it with 2 hit points. He opens in Dead Eye with ten shots. Jack spends all six of his luck in that one turn and both his holograms, and still goes from 155 to 64. Jack cloaks. Arthur puts six more into a man he can't see, and Jack is at 3 with the cloak still up. Then Jack starts firing. Twenty-three of his twenty-seven Scorching Rays land, a cannon puts his shield back every single turn, and Arthur takes 324 damage in seven rounds on a sheet with 223 hit points: all four Second Winds go into the gap. Jack goes to 0 seven times. Six times he burns one of the six things he built and stands at 20: the storage deck, the Mind Sharpener, the jacket, the ring, the bracers, the wrist laser, in that order, two of them in one turn. In every one of Arthur's eight turns Peerless Aim turns his first miss into a hit, and seven of those eight are a bullet that had just popped a Digi-Jack. Jack's last turn, with no laser and no slots worth the name, takes Arthur from 48 to 2. The seventh time, there is nothing left to burn.

<details>
<summary>The round-by-round log</summary>

```
winner: Arthur in 8 rounds
R1 Arthur  | {Arthur: deadeye False->True, boxes 6->1, surges 2->1} {Jack: luck 6->0, decoys 2->0, shield_up False->True} ** Jack's luck ** hit 18 piercing ** Jack's luck ** ** Arthur hits a Digi-Jack ** miss [Arthur -> Jack: 12 piercing] ** Jack's luck ** ** Arthur hits a Digi-Jack ** miss ** Jack's luck ** miss ** Jack's luck ** hit 8 piercing ** Jack's luck ** CRIT 20 piercing CRIT 14 piercing ** Jack's Shield ** miss miss CRIT 19 piercing  || Arthur 223  Jack 64
R1 Jack    | {Jack: invisible False->True, stored 10->9} ** Jack cloaks ** ** a cannon puts Jack's shield back: 15 ** hit 7 force hit 3 fire  || Arthur 213  Jack 79
R2 Arthur  | {Arthur: boxes 1->0, surges 1->0} {Jack: decoys 1->0, shield_up False->True, fate True->False} hit 14 piercing hit 17 piercing ** Arthur hits a Digi-Jack ** miss [Arthur -> Jack: 13 piercing] hit 12 piercing hit 8 piercing ** Jack's Shield ** miss ** Boon of Fate ** miss hit 12 piercing  || Arthur 213  Jack 3
R2 Jack    | {Jack: invisible True->False} hit 13 fire hit 3 fire hit 7 fire hit 6 fire hit 9 fire hit 10 fire ** a cannon puts Jack's shield back: 21 ** hit 7 force hit 8 fire  || Arthur 150  Jack 24
R3 Arthur  | {Arthur: deadeye True->False, boxes 0->3, snake 2->1} {Jack: decoys 1->0} ** Arthur hits a Digi-Jack ** miss [Arthur -> Jack: 14 piercing] <Jack DROPS TO 0> ** Jack disintegrates his Bag of Holding and stands at 20 ** <Jack back up at 20> hit 10 piercing hit 13 piercing miss  || Arthur 150  Jack 7
R3 Jack    | hit 7 fire hit 7 fire hit 2 fire hit 9 fire hit 10 fire hit 7 fire ** a cannon puts Jack's shield back: 13 ** CRIT 18 force hit 1 fire  || Arthur 89  Jack 20
R4 Arthur  | {Arthur: sw 4->3} {Jack: decoys 1->0, shield_up False->True} ** Arthur hits a Digi-Jack ** miss [Arthur -> Jack: 14 piercing] <Jack DROPS TO 0> ** Jack disintegrates his Mind Sharpener and stands at 20 ** <Jack back up at 20> hit 11 piercing hit 9 piercing ** Jack's Shield ** miss  || Arthur 118  Jack 11
R4 Jack    | hit 15 fire hit 3 fire CRIT 9 fire hit 8 fire miss ** a cannon puts Jack's shield back: 17 ** hit 10 force miss  || Arthur 73  Jack 28
R5 Arthur  | {Arthur: boxes 3->4, sw 3->2} {Jack: decoys 1->0} hit 14 piercing hit 11 piercing <Jack DROPS TO 0> ** Jack disintegrates his Cloak of Protection and stands at 20 ** <Jack back up at 20> CRIT 19 piercing ** Arthur hits a Digi-Jack ** miss [Arthur -> Jack: 13 piercing]  || Arthur 99  Jack 7
R5 Jack    | hit 6 fire hit 5 fire hit 11 fire hit 8 fire hit 9 fire ** a cannon puts Jack's shield back: 12 ** hit 19 force hit 1 fire  || Arthur 40  Jack 19
R6 Arthur  | {Arthur: sw 2->1} {Jack: decoys 1->0} ** Arthur hits a Digi-Jack ** miss [Arthur -> Jack: 17 piercing] <Jack DROPS TO 0> ** Jack disintegrates his Ring of Protection and stands at 20 ** <Jack back up at 20> hit 15 piercing hit 8 piercing <Jack DROPS TO 0> ** Jack disintegrates his Bracers of Defense and stands at 20 ** <Jack back up at 20> hit 14 piercing  || Arthur 67  Jack 20
R6 Jack    | miss miss hit 13 fire hit 3 fire miss ** a cannon puts Jack's shield back: 16 ** hit 18 force hit 6 fire  || Arthur 27  Jack 36
R7 Arthur  | {Arthur: sw 1->0} {Jack: shield_up False->True} hit 12 piercing ** Jack's Shield ** miss [Arthur -> Jack: 12 piercing] hit 9 piercing <Jack DROPS TO 0> ** Jack disintegrates his wrist laser and stands at 20 ** <Jack back up at 20> hit 14 piercing  || Arthur 48  Jack 20
R7 Jack    | hit 17 fire ** a cannon puts Jack's shield back: 17 ** hit 12 force CRIT 8 fire hit 9 fire  || Arthur 2  Jack 37
R8 Arthur  | {Arthur: deadeye False->True} {Jack: decoys 2->0} ** Arthur hits a Digi-Jack ** miss [Arthur -> Jack: 19 piercing] hit 14 piercing ** Arthur hits a Digi-Jack ** miss <Jack DROPS TO 0> <Jack OUT> CRIT 26 piercing  || Arthur 2  Jack 0
```

The totals at the end of each line are hit points plus temporary hit points, and Jack walks in with 143 and a shield of 12. A drop to 0 is logged just before the attack that caused it. `** Arthur hits a Digi-Jack ** miss` is one shot that would have hit Jack and popped a hologram instead (`decoys`); one hologram comes back at the start of each of Jack's turns. A bracketed `[Arthur -> Jack: N piercing]` straight after a miss is Peerless Aim: Arthur's first miss each turn hits anyway, so a bullet that pops a Digi-Jack goes on through it. `** Jack's luck **` is a Lucky point spent to give the next shot disadvantage, which only cancels Dead Eye's advantage. `** Jack's Shield **` and `** Boon of Fate **` each turn the next shot into a miss. In Jack's turns the order is his action (the cloak, then Scorching Ray at five or six rays a cast, then in round 7 a single Fire Bolt), then the cannons (one turned Protector to restore his shield, the other a Force Ballista), then one small shot of fire from each Digi-Jack standing. `boxes` are Dead Eye, `surges` Action Surge, `snake` the Snake Oil that refills three boxes, `sw` Second Wind. The cloak holds through all six hits in round 2: he makes every concentration save. In round 5 the `CRIT` is a natural 20 with no Dead Eye behind it.

</details>

---

## The Bar

**Arthur**

He was drawing the big swordsman's hand. It was a good hand to draw, all knuckle and scar, wrapped round a cup it could have crushed. He had most of it down when the door banged open on a man who was already talking.

"...and THAT, kiddo, is what happens when you..."

The man stopped. He looked at the lamp, and the bottles, and the row of backs.

"This isn't my volcano."

He was a tall feller in a good coat over a waistcoat over a yellow shirt, with a watch chain and a little machine strapped to one wrist. Arthur looked at the face for a while before he worked out what was wrong with it. It was a handsome face, the kind they put on a tonic bottle. There was a small clasp at the hairline and another under the chin. It was a face worn over a face.

"Okay," the man said. "Okay. Regrouping." He pointed down the bar, one stool at a time. "Bandit. Bandit. Big bandit. Priest bandit. Child bandit. Evil child bandit, love that. Space suit bandit. ROBOT bandit." He stopped on the machine, delighted. "Look at you. You're like a loader that ate four other loaders."

The red eyes stayed where they were.

The old man had set a paper cup on the bar. Steam came off it.

"Didn't order that. I'll take the most expensive thing you have, two of them, and then I'd like to buy the building."

"It's paid for," the old man said.

"By who?" The feller leaned in. "No, I'm asking. Give me a name. I'll buy *them*."

The old man went back to his glass. The feller picked up the cup, the way a man does when his hands want something to do, and drank, and for the first time since the door opened he said nothing at all.

"That's from the machine on the programmers' floor," he said. Nobody had asked him. "That machine's gone. I had it fired out of an airlock." He looked into the cup. He looked like a man who has found his own boyhood name carved in a strange fencepost. Then it was gone from him, and he drank the rest. "It's garbage. It was always garbage."

By the door, the slate already said what it said.

> **TONIGHT:**
>
> MORGAN v JACK

The feller took the chalk off its string and wrote HANDSOME in front of JACK, twice the size, and underlined it. "Brand guidelines," he said. "Which one's Morgan?"

Arthur lifted two fingers off the bar.

He got looked over. The hat, the coat, the Schofield. He coughed into his fist while it was going on, which he had not meant to.

"Is that a revolver? That has a little hammer on it. Somebody's museum is missing that." The mask smiled. It smiled a shade after the man behind it did. "Did they send me the tutorial? I'm not complaining. So you're a bandit."

"Yep," Arthur said.

That stopped him a second time.

"No. See, this is where you tell me about freedom, and living off the land, and how I'm the real monster."

"Robbed trains. Banks. A stagecoach or two." Arthur turned his glass. "Killed a good many folk, and some of 'em hadn't done nothing but owe money. Outlaw was the word we used. Bandit'll do."

"Huh. Well, I'm the hero, so this is going to work out great for one of us."

"I'm sure you are," Arthur said. "I rode twenty years with a feller who was."

"Oh, are we doing confessions? I have a great one." And he told it, leaning on the bar, to all of them. A man had come at him once with a spoon. So he had taken the spoon away and used it, on the man's eyes, with the man's children standing there. He told how the man had gone about the room afterward bumping into his own furniture, and what noise the children had made, and he did the noise. He laughed until he had to hold on to the counter.

Nobody else laughed. The boy in green had put his milk down. The priest had shut his book, without marking the page. The big gray feller with the red on him turned his head and looked, once, the way a man looks at something lying in the road.

"Tough room," Jack said, wiping under the eyes of the mask. "He was a bandit. Did I leave that out? It's funnier when you know he was a bandit."

Arthur had ridden with a man who talked like that, and with another who laughed like that. It had taken the two of them to do what this one feller did alone.

Jack had moved down to the end of the bar. He did not lower his voice. Arthur did not think he could.

"Big guy. What do you run, per job? Double it. All I need is, when the antique over there heads for that door, you're standing in it."

It was some time before the machine answered.

"I know your voice," it said. "I worked for it for seventy years." The red eyes went to the slate and came back. "I have a record at this location. It is one and four. Nothing on it was bought. Nothing on his will be."

"That's a no? That sounded like a no with extra steps." Jack clapped it on the plating, and took his hand back and looked at it. "Fine. I'll do it myself, like everything." He finished the paper cup and made for the door. "I'm going to go set up. You people take your time."

The door shut. The old man reached up with the broom handle, and the gray glass over the bottles woke.

It was a street. Arthur knew the kind: a cattle town at noon, false fronts and a water trough, and the mud of the week's rain drying to ruts. It was not Valentine, but whoever had built it had heard of Valentine. The feller in the mask was already in the middle of it, unfolding two yellow machines on three legs apiece.

"He goes early," the old painter said.

"So did your friend there."

"Sakai went early to lie down in the water. This one goes early to build a wall." The painter looked at it a while longer. "He fights the way a great lord fights. With other people."

"He chose the guy who coughs," Spike said. He had not looked up from his cigarette.

"It was chalked before he come in."

"He'd have chosen."

"I know it." Arthur shut the journal on the swordsman's hand and put it in the satchel. He drank what was in the glass, and settled his hat, and went.

---

## The Street

**Arthur**

The door let him out of the front of a dry-goods store, into noon.

There were three of the feller. Two stood out in front, a few yards apart, and the third stood behind them between the yellow machines. All three had the grin. All three were talking, the same words, with the two in front a hair behind the one at the back. The two in front stood on top of the mud as if it were a floor. The one at the back was in it to the ankle, and he had a skin of blue light on him like a soap bubble.

"Welcome," they said, "to the first day of the rest of your very short"

Arthur had sat through one feller's speeches for twenty years. He did not have the wind for another.

The world went slow. The mud went the color of old paper and the sky the color of tin. He painted the one at the back, one red mark and then six.

The first went through the blue. It burst the way a bubble does, and the bullet kept on into him. For the second, one of the front ones stepped sideways into the line of the gun. It came apart in blue sparks. The bullet did not seem to notice. Behind it the real one grunted and took a step back. The other front one walked into the third, and that bullet he lost. The fourth went wide, with the world slowed, which a shot of his did not do. The fifth clipped him. The sixth went in square.

His hands went on by themselves, as they had since he was fourteen. Four more. One square. One turned off a pane of light that stood up out of nothing. One wide again. One in the chest.

The world came back, with the noise in it.

The feller was still on his feet. The copies were gone and the blue was gone, and there was blood on the yellow shirt in six places. He was looking at Arthur as a man looks at a dog that has gone on the rug.

"I was *talking*," he said.

**Jack**

Down fifty-five percent before the opening bell.

Jack checked the readout again, because the first time had been wrong. It had not been wrong. Shield, zero. Digi-Jacks, zero. And the luck was gone. He had always had it and he had never once thought of it as a thing that ran out. Six times in three seconds the universe had done him a favor, which was the universe's job, and six bullets had gone into him anyway. From a *revolver*.

Nobody shot during the speech. That was the arrangement he had with people. They stood there and hated him through it, and then the turrets shot them. It had worked on a board of directors and most of a planet.

He thumbed the stud on his wrist and went away.

It was a good cloak. He had taken the patent off a man who no longer needed it. One turret swung its dish to the spot where he wasn't and gave him his shield back. The other put a bolt in the cowboy's ribs. A new Digi-Jack drew itself in the street, grinning, and took a little off the old man's coat with its laser.

"Okay," Jack said, walking backward. "Here is what happens now. You stand there, looking for me, and you get tired. You look tired already. You look like a before picture. And then I"

The cowboy shot him.

The first two took the shield and some more besides. The Digi-Jack walked into the third, as designed, and the third went through the Digi-Jack, which was not as designed. Four. Five. The hard-light pane caught the sixth. The seventh went by his ear, by a margin he would not be discussing with anybody. Eight.

Two percent.

He was invisible. He checked. He held his own hand up in front of the mask and saw the street through it. He had paid for invisible.

He looked down. There were his footprints, handmade, size eleven, going backward through the mud in a line a child could have followed. Also, he had not at any point stopped talking.

"Okay," Jack said. "That one's on me."

He put his wrist out and held the stud down. It opened the cloak, and he did not care. Six beams. Six for six. The cowboy's coat went up along one arm. The turret gave him his shield again, fatter this time. The other turret hit, and the Digi-Jack hit.

Now *that* was a quarter.

**Arthur**

He beat the fire out of his sleeve with his hat.

The slow had gone out of him. The color had come back into the street, and with it the cough. He rode it out bent over, with the Schofield hanging. Then he found the snake oil in the satchel by feel and drank half the bottle. It lit the fire behind his eyes again, low and steady. He banked it. He would want it later.

Another of the light ones had drawn itself in front. It stepped across him when he raised the gun. He was beginning to understand the feller, and he shot it. Behind it the blue flared and the real one jerked. The second shot broke what was left of the blue and laid him flat on his back in the mud.

Arthur let the gun down an inch.

There was a white light at the feller's hip. A flat box on his belt went to ash, all at once, like paper in a stove. Then he sat up.

"That was a storage deck!" He got his feet under him. "Do you know what was in that? There was a rocket launcher in that. There were *two*. There was a sandwich."

Arthur shot him again, and it went in. The fourth went wide.

Then the wrist came up, and it was six again, and all six found him. The yellow machine's bolt took him under the heart like a mule's hind foot. The light one's little beam was hardly anything, and it found him too. That was twelve of the big ones the feller had sent, and not one had missed. Arthur had been shot at by Pinkertons, and by O'Driscolls, and by the United States Army. None of them had ever done that.

He got the health cure out and drank it standing. It was a good bottle.

The light one stepped across. He shot through it. The blue burst, and the next one put the feller down.

White light again, inside the waistcoat this time. The feller got up slower. He looked at the street, and the machines, and Arthur, like a man who has come into a room and forgotten what for.

"Where was I?"

"You was telling me you're the hero."

"Right. Thank you."

Arthur shot him. The last one of the four rang off a pane of light.

That was twice he had killed the man. Both times the man had paid something and got up. Arthur had known fellers who settled their debts that way. He wondered how much this one had on him.

**Spike**

Spike had seen the type. Every syndicate kept one upstairs, a guy who had never stood in a room he didn't own.

In the gray glass the wrist came up again. Five this time. Four of them hit, and Arthur sat down in the mud. One went past his hat. It was the first all day that hadn't found him. The turret found him anyway.

"Somebody tell me the old man's got more of those bottles," Spike said.

Nobody told him.

"It is spending in order." The machine had not been asked. "Lowest value first. Storage. Then the unit in the vest. It is correct."

"From him that's a compliment," Spike said.

"It is an observation. I spent mine in order."

Nobody had anything to say to that.

Arthur drank something and got up. He fired four. Two went into the blue, and through it. The third put the mask on its back for the third time. This time it was the coat. It went white from the collar down and came off him like ash off a log, and the guy got up in a waistcoat and shirtsleeves.

"That was BESPOKE," said the tin speaker.

One of the copies walked in front of the fourth. Arthur had quit waiting on them. It went through.

"How many times does he get to do that?" Guts said.

"It has three things left on it that are lit," the machine said. "The ring. The cuffs. The weapon. It will rise three more times. The seventh time it will not."

The painter turned his head. "You make predictions now."

"I have confirmed one."

Five more out of the wrist, and all five hit. The turret's bolt lifted Arthur off his feet. When the picture steadied he was on one knee with his hat in the mud and smoke coming off his back. He was not getting up quickly. He had about a fifth of himself left, by Spike's count, and Spike had some practice at that count.

"Three more times," Spike said. "He hasn't got three more times in him."

"No," said the boy in green. He did not say which of them he meant.

Spike had worked for men upstairs. He had been the guy they kept in front. He knew what Arthur was shooting at down there, and he knew how far back it stood.

"Come on, cowboy," he said.

**Jack**

He was in his shirtsleeves. In mud. On *television*.

The cowboy drank out of another little bottle and stood up.

"What is that?" Jack said. "What's in the bottle? I'll buy the company."

A Digi-Jack stepped across, as designed. The cowboy shot through it without so much as looking at it. That was the shield. The next one put Jack on his back.

The ring went. He felt it go: a white heat round his finger, and then nothing round his finger. He got up.

The third hit him. The fourth put him down again, and it was the cuffs, both at once. He got up.

Twice in four shots.

"That ring was a gift!" he said. "From me!"

He held the stud down. Five. The first went over the saloon. The second went over the saloon. Two hit. The fifth took a post out of the hitching rail.

His hand was not shaking. The laser was out of true. Whoever had calibrated it was going out of an airlock, and Jack would be at the window. He looked at the cell. It was red. That had been the last of the big ones.

But the turret put his shield back, and the other turret hit, and the Digi-Jack hit. And look at that. The cowboy was on his hands and knees, coughing red into the street. Heroes won. It was right there in the word.

The cowboy put something in his mouth and chewed it, and stood up.

"Stop DOING that!"

One into the shield. The pane caught the second. Then the second came through the pane, which hard light did not permit, under warranty. The third went in. The fourth put him down.

It was the laser. He lay in the mud and watched it go white on his arm. He got up and looked at his wrist. It was a wrist.

He took stock. No deck, no coat, no ring, no cuffs. Nothing on him was lit. He had a waistcoat and a watch and a face.

He also had a pistol in the back of his belt. It was a Hyperion, the incendiary, the model he sold to people he didn't like. He shot the cowboy with it. The turret gave him a shield and the other turret hit. There were two Digi-Jacks standing now, and they both hit.

The cowboy went down on both knees and one hand and stayed there. His hat was gone. He was bleeding from the mouth, and Jack had not hit him in the mouth.

"Stay down," Jack said.

He had meant it as an order. He heard how it came out.

"I'm the hero," he said, and the two in front said it with him. "That's why you're down there and I'm up here. It's how you can tell."

**Arthur**

There was a bottle in the satchel yet that might have set him right. He did not have the time it would take to drink it.

There were three of the feller again. Two stood in front, on top of the mud. One stood at the back, in it. They were all saying the same thing.

He knew where the feller at the back stood. He had been one of the ones in front for twenty years. There had been a deal of them. Davey, and Jenny. Sean. Lenny. Hosea. One after another they had stepped across for a man, and come apart, and behind them the man had gone on talking.

The fire was still banked behind his eyes. He let it up.

The world went slow, for the last time that day. He did not paint the two in front.

The left one stepped across, and he shot through it. The blue burst behind it. The second went into the man. The right one stepped across and took the third, and was gone, and that bullet he lost.

Then there was one of him. He had no blue on him, and no light on him anywhere. He stood in mud to the shins, in a waistcoat, with the grin on. His mouth was moving, slowly, the way everything was. Arthur could read it. *I'm the goddamn hero.*

He put the fourth where the last red mark was.

The feller went over backward, full length. Arthur kept the gun on him and waited for something on him to burn white.

There was nothing left on him to burn.

"Sure you are," Arthur said. "You all are."

The yellow machines went on turning their dishes for a while, looking for him, and then they stopped. In the front of the dry-goods store there was a line of lamplight. He found his hat. It took him two tries to stand.

---

## After

**Jack**

"...which is why you NEVER..."

He was on a stool. There was a paper cup in front of him, full, with steam coming off it.

Jack touched the clasps first. Hairline. Chin. Both shut. Then he went over the rest of himself, like a man coming out of a crowd. Coat. Ring. Cuffs. The laser on his wrist, with a green cell. The deck on his belt. He pressed two fingers to the waistcoat and felt the unit ticking over. All six. There was not a hole in the shirt.

The slate said *MORGAN.* After it, smaller: *(seven times).* Somebody had left HANDSOME up, with the line under it.

"Seven? Six of those don't count. That is what the stuff is *for*. That's like counting the airbag." He turned on the stool. "Old guy. What does it take to make that say the other name? Everybody has a number."

"It's paid for," the old man said.

"Who keeps..." He stopped, because it was the same glass. The old man was polishing the same glass.

So he told them. He told the whole bar what they were, which was bandits, and what the place was, which was a bandit bar. He told them what was going to be parked on top of it by the end of the fiscal year, which was a moon base. He had cleared rooms with less.

Nobody turned round. He looked for the fear in the room, the way he would have patted his pockets for his wallet. In his experience, when it was missing, you fixed that with money or with a spoon. He had tried the money. He looked down the bar, at the sword the size of a door, and the priest, and the big gray one who had looked at him once. He found he did not want that one to look at him twice.

"Your record at this location is zero and one," the robot said.

"Thank you, toaster."

"I am informed it is a different sentence when you say it yourself."

"I didn't lose. I was robbed. By a bandit. That is the *definition*."

The red eyes stayed on him a little longer than he liked. "Noted," it said.

Jack drank the coffee. It was still garbage. He sat holding the empty cup.

"Is there more of this?"

There was. He did not ask who was paying. He had decided it was him.

**Arthur**

The door had put him back the way it did, with the burns gone and the hole out of his sleeve. It had left him the cough. It always did.

He had his whiskey. He was watching it, mostly, when a sheet of paper came sliding down the bar and stopped against his hand.

"I have seen you with the small book," the old painter said.

"That's only scratchings."

"There is a bird on that wall, and seventeen syllables of rice. There is room beside the rice." He turned his brush about and held it out, handle first.

"I'd only spoil it, mister." The paper was so fine Arthur was half afraid to breathe on it. He dug in the satchel and came up with the pencil stub. The painter took it from him and looked at the point, and tried it on his thumbnail.

"A brush with no water in it."

"Pencil."

"What it puts down, can it be taken back?"

"Some. I don't."

"Good." He gave it back.

Arthur drew the street. He did the false fronts in a few lines, and the trough, and the two machines on their legs. He drew the two in front with hardly any weight on the pencil, and put no ground under them. The one at the back he leaned on. He gave that one the mud to his ankles and a shadow, and a line of tracks going backward. He put the grin on all three. It was the same grin. It was the only thing about the man that was.

"The two in front you have drawn with almost nothing," the painter said.

"They was only light."

"And this one you have pressed into the paper."

"He was the only one of 'em in the mud."

"Nobody taught you that."

"Nobody taught me nothing. I just put down what was there."

"That is all of it. I have been thirty years trying to tell people so." The painter looked at the three of them. "It wants a line of writing. The bird does not. This does."

Arthur thought about it. Then he wrote underneath, in the hand he used for the journal.

*Handsome Jack. He is the one at the back.*

The old man pinned it up beside the rice.

It had not been there a minute when the feller came down the bar with his paper cup.

"Is that me? That's me. You got the jaw, I'll give you that. Who are the two guys in front?"

"Them's you too."

Jack read the line. For a second or so he didn't say anything.

"That's called management, cowboy."

"I know what it's called. I was one of the fellers in front. Twenty years."

"Yeah? How'd that work out for you?"

He had meant it to cut, and it did. Arthur coughed, and waited it out.

"About how you'd think."

"A thousand. I want it off the wall."

"It ain't for sale."

"Everything is for sale."

"Not in here. Ain't you noticed?" Arthur picked up his glass. "I reckon that's what's eating you."

"Nothing is eating me. I'm *great*."

He stood in front of it a while longer all the same. Arthur could not have said which of the three he was looking at. Then he went back to his stool.

Down at the end, the red eyes had gone to the new paper, and they stayed there. The big feller had stood out in front for somebody too. Seventy years, by his own telling. Arthur touched his hat to him. After a moment the machine inclined its head, about as far as a locomotive would.

---

*From the journal of Arthur Morgan, the page with a swordsman's hand on it:*

> Killed a man seven times today before it took. He wears a mask of his own face, and keeps two more of himself made out of light to stand in front. He talks like Dutch and he laughs like Micah. He says he is the hero, and I believe he believes it.
>
> The old Japanese gentleman give me a sheet of his paper and they hung what I drew on the wall, by a bird and a poem. I never had nothing of mine on a wall before, bar the posters, and I did not draw those.
>
> He asked how it worked out for me, all them years standing in front. I been thinking on it. I reckon it worked out that I knew where to aim.
