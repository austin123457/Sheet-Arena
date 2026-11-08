# Dead or Alive

*Spike Spiegel and Arthur Morgan vs Adam Smasher.* A sequel to [Two Men Who Should Be Dead](spike-vs-arthur.md).

The fight is real: the most dramatic of 600 runs of `python battle.py team spike+arthur smasher`, picked by `fight_log.py spike+arthur smasher 600 Spike`. The pair wins about two times in three. This is one of the hard ones: Smasher's Sandevistan and Action Surge put nine rounds into Spike in a single turn, Nine Lives buys him one more, and a crit in round 3 ends him. Arthur fights the last five rounds alone, through the Armor Regeneration Matrix and all four of Smasher's Second Winds, and finishes it at 5 HP (26 after his own last Second Wind) with a Dead Eye crit for exactly what Smasher had left.

<details>
<summary>The round-by-round log</summary>

```
winner: Spike + Arthur in 8 rounds
R1 Arthur  | {Arthur: deadeye False->True, boxes 6->1, surges 2->1} hit 6 piercing >Smasher hit 7 piercing >Smasher hit 8 piercing >Smasher CRIT 13 piercing >Smasher CRIT 11 piercing >Smasher hit 10 piercing >Smasher hit 6 piercing >Smasher hit 7 piercing >Smasher hit 8 piercing >Smasher miss >Smasher  || Spike 183  Arthur 223  Smasher 145
R1 Smasher | {Spike: luck 6->2, prone False->True} {Smasher: surges 2->1, sandy 0->3} [Missiles -> Arthur: 6 fire] [Missiles -> Arthur: 6 bludgeoning] hit 0 piercing >Spike hit 18 piercing >Spike hit 15 piercing >Spike hit 16 piercing >Spike hit 15 piercing >Spike  || Spike 119  Arthur 211  Smasher 145
R1 Spike   | hit 1 piercing >Smasher hit 3 piercing >Smasher miss >Smasher hit 3 bludgeoning >Smasher hit 2 bludgeoning >Smasher  || Spike 119  Arthur 211  Smasher 136
R2 Arthur  | {Arthur: surges 1->0} hit 7 piercing >Smasher miss >Smasher miss >Smasher hit 7 piercing >Smasher hit 5 piercing >Smasher hit 5 piercing >Smasher CRIT 12 piercing >Smasher hit 5 piercing >Smasher  || Spike 119  Arthur 211  Smasher 87
R2 Smasher | {Spike: luck 2->0, nine True->False, prone False->True} {Smasher: sw 4->3, surges 1->0, sandy 3->2} hit 0 piercing >Spike hit 15 piercing >Spike hit 15 piercing >Spike hit 15 piercing >Spike hit 17 piercing >Spike hit 12 piercing >Spike hit 14 piercing >Spike hit 21 piercing >Spike <Spike DROPS TO 0> <Spike back up at 1> hit 20 piercing >Spike  || Spike 1  Arthur 211  Smasher 111
R2 Spike   | {Spike: wob 4->3} hit 7 piercing >Smasher miss >Smasher CRIT 10 bludgeoning >Smasher hit 0 bludgeoning >Smasher hit 5 bludgeoning >Smasher  || Spike 12  Arthur 211  Smasher 89
R3 Arthur  | {Arthur: boxes 1->0} hit 7 piercing >Smasher miss >Smasher hit 8 piercing >Smasher hit 8 piercing >Smasher  || Spike 12  Arthur 211  Smasher 61
R3 Smasher | {Spike: prone False->True} {Smasher: sw 3->2, sandy 2->1} [Missiles -> Arthur: 6 fire] [Missiles -> Arthur: 7 bludgeoning] <Spike DROPS TO 0> <Spike OUT> CRIT 20 piercing >Spike  || Spike 0  Arthur 198  Smasher 91
R4 Arthur  | {Arthur: deadeye True->False, boxes 0->4, snake 2->1} hit 14 piercing >Smasher miss >Smasher CRIT 15 piercing >Smasher hit 8 piercing >Smasher  || Spike 0  Arthur 198  Smasher 46
R4 Smasher | {Smasher: sw 2->1, sandy 1->0} hit 11 piercing >Arthur hit 17 piercing >Arthur miss >Arthur hit 12 piercing >Arthur  || Spike 0  Arthur 136  Smasher 73
R5 Arthur  | {Arthur: deadeye False->True} {Smasher: matrix True->False} hit 8 piercing >Smasher hit 10 piercing >Smasher hit 7 piercing >Smasher CRIT 9 piercing >Smasher hit 4 piercing >Smasher  || Spike 0  Arthur 136  Smasher 75
R5 Smasher | {Smasher: sw 1->0} hit 16 piercing >Arthur hit 16 piercing >Arthur hit 14 piercing >Arthur hit 15 piercing >Arthur  || Spike 0  Arthur 75  Smasher 100
R6 Arthur  | {Arthur: sw 4->3} miss >Smasher CRIT 9 piercing >Smasher CRIT 14 piercing >Smasher CRIT 15 piercing >Smasher  || Spike 0  Arthur 100  Smasher 51
R6 Smasher | hit 13 piercing >Arthur hit 21 piercing >Arthur hit 13 piercing >Arthur hit 10 piercing >Arthur  || Spike 0  Arthur 43  Smasher 51
R7 Arthur  | {Arthur: boxes 4->3, sw 3->2} hit 10 piercing >Smasher hit 8 piercing >Smasher hit 2 piercing >Smasher hit 9 piercing >Smasher  || Spike 0  Arthur 66  Smasher 22
R7 Smasher | hit 13 piercing >Arthur hit 18 piercing >Arthur hit 13 piercing >Arthur hit 17 piercing >Arthur  || Spike 0  Arthur 5  Smasher 22
R8 Arthur  | {Arthur: sw 2->1} <Smasher DROPS TO 0> <Smasher OUT> CRIT 22 piercing >Smasher  || Spike 0  Arthur 26  Smasher 0
```

HP includes temporary HP (the Matrix's 40). Smasher's plating takes 6 off every weapon hit, which is why Spike's fists do 1 to 3; his Stunning Strike doesn't work on a full-body conversion. `sandy` is Smasher's Sandevistan (three rounds), `matrix` the Armor Regeneration Matrix.

</details>

---

## The Bar at the End of Everywhere

**Spike**

The bar didn't have a name. It didn't have a door either, as far as Spike could tell. He'd been lying in the sand with his eyes closed, and then he was on a stool with his elbows on the counter, and a bartender with a face like an old shoe was setting down a glass of something amber in front of him.

Spike looked at the glass. He looked at the bartender.

"I didn't order this."

"It's paid for," the bartender said, and went back to polishing a glass that didn't need it.

Spike drank it anyway. It was good. That was suspicious too, but he was too tired to be suspicious about two things at once.

The stool next to him creaked. Somebody big sat down heavily, and the somebody coughed: deep, wet, rattling.

Spike didn't turn his head. "Last time I saw you, you were lying in the sand."

"Last time I saw you," Arthur Morgan said, "so were you."

The bartender put a glass in front of him too. Arthur looked at it for a long moment, then drank it in one swallow and set it down very carefully, like a man who'd learned what happens when you set them down any other way.

"You know where we are?" Arthur asked.

"Nope."

"You know why?"

Spike pointed at the television above the bar with his chin.

It was an old set, heavy and boxy, and the picture rolled a little. A pair of hosts in cowboy hats stood in front of a cheap Western backdrop, a blonde in a fringed vest and a man with a ridiculous mustache. Spike would have known that set anywhere. He'd watched a thousand episodes of *Big Shot* with his feet up on the Bebop's couch while Jet complained about the lack of beef in the bell peppers and beef.

"*—and boy howdy, have we got a big one for you today, cowboys!*" The blonde winked at the camera. "*The biggest bounty in the history of this show!*"

The picture cut to a mugshot. It wasn't a face, exactly. It was more like a skull made of armor plate, with a crown of red optics and a jaw like a car crusher. Below it, in big yellow letters:

**ADAM SMASHER**

**WANTED: DEAD OR ALIVE**

Then a number came up underneath, with so many zeros on it that Spike stopped counting.

Arthur leaned forward. "Is that... dollars?"

"Woolongs."

"How much is that in dollars?"

Spike thought about it. He thought about the Bebop's empty fridge and the bell peppers with no beef. He thought about every bounty they'd ever chased: the ones that got away, the ones that blew up, and the ones where the reward went to repairing whatever got wrecked catching them.

"All of them," Spike said. "That's all the dollars."

The bartender cleared his throat and nodded toward the back of the room. There was a wanted poster on the wall there, yellow and curling at the edges, the kind Arthur used to tear off fence posts in a dozen towns. It had the same armored skull on it, drawn in charcoal, and underneath, in careful old-fashioned type:

*Adam Smasher. Head of Security, Arasaka Corporation. Wanted for the murder of more people than this poster has room for. REWARD:* followed by the same number, in dollars this time.

"I'll be damned," Arthur said softly.

He sat back on his stool and was quiet for a long time. Spike could almost see him doing the math: not how much it was, but what it could buy, and who it could buy it for.

"I got a friend," Arthur said eventually. "John. He's got a wife and a boy. They deserve better than what I've given 'em." He coughed and wiped his mouth with the back of his hand. "A ranch, maybe. Somewhere quiet."

Spike thought about Jet, alone on the Bebop and pretending he wasn't waiting for anyone. He thought about Faye, and Ed, and the dog.

"Yeah," Spike said. "I know some people too."

He set his glass down and stood up.

"So," Arthur said. "We do this?"

"We do this," Spike said. "Partner."

Arthur actually laughed at that, a short rough bark that turned into a cough halfway through.

"Partner," he said. "Lord help us both."

---

## The Fight

**Smasher**

TARGETS ACQUIRED: 2.

TARGET 1: organic. Male, approx. 30 years. Chrome detected: one ocular implant. Minimal. *Meat.*

TARGET 2: organic. Male, approx. 36 years. Chrome detected: none. Pulmonary scan shows advanced tuberculosis. Life expectancy: under six months. *Meat, rotting.*

THREAT ASSESSMENT: LOW.

Smasher had been fighting for seventy years. He had killed Johnny Silverhand in the tower, survived the bomb that brought it down, and pulled apart more edgerunners than he could be bothered to count. He had stopped thinking of them as people long ago. They were problems, and problems got solved.

Two men stood in front of him: a skinny one in a blue suit and a big one in a heavy coat. Neither of them looked afraid.

That was new. He'd have to fix it.

**Arthur**

The world went slow again.

It was easier this time. Maybe because there was only one target, and it was big as a barn. Arthur painted it all over: the joints, the plating seams, the glowing red eyes. Every place a bullet might go.

Then he fired.

Ten shots. Most of them flattened against the chrome like hailstones hitting a tin roof, and Arthur felt his heart sink. But some found seams: the two in the left knee joint went *in*, and something sparked and smoked. The thing staggered half a step.

*It can bleed*, he thought. *Or whatever it does instead of bleeding.*

Then it moved, faster than anything that big had any right to move. It went blurred and shimmering, and Arthur's eyes slid off it like water off oilcloth. Missiles screamed out of its shoulders, and the ground around Arthur went up in fire and rock. He threw himself flat, coughing, his coat smoking.

When he looked up, the thing was firing at Spike.

**Spike**

Five shots, faster than he could see.

He caught the first on his forearm, turned it, felt it skip off. The other four went in. The fourth knocked him flat on his back, and a giant foot came down an inch from his head.

*Okay. Okay, that's a problem.*

He rolled up and went in, because he didn't know how to do anything else. He fired the Jericho twice, point-blank into the chest plate, and the bullets *pinged* off like he was shooting a battleship. Then a palm strike into the joint of the arm, a knee into the side, an elbow to the jaw. Every one jarred his bones all the way to the shoulder and did almost nothing.

It was like punching a tank, a tank that was looking down at him.

"You're a lot of chrome," Spike said.

The tank said nothing. Its red eyes clicked, refocused, and locked on him.

**Arthur**

He kept shooting.

He didn't know what else to do. Eight shots: six went in somewhere. He watched plate crack and hydraulic fluid spray from a joint like blood from a cut artery. The thing was hurt. It had to be hurt.

Then it *blurred* again, faster than before.

He'd never heard a gun fire that fast. It wasn't shots so much as one long roar, like ripping canvas, and all of it pointed at Spike.

The skinny man went down, came up, and went down again, the bullets throwing him across the sand like a rag doll. He lay there and didn't move. Arthur's heart stopped.

Then Spike got up. Of course he did.

Arthur could see from forty feet away that there was nothing left in him. He was swaying like a scarecrow in a high wind, red from collar to belt. He got up anyway, wiped the blood off his chin, and *smiled*.

"*Spike!*" Arthur shouted. "*Get back!*"

Spike went in instead.

**Spike**

*One more.*

He breathed and felt it steady him, a little. Enough.

He went in low and fast, a punch to the knee joint where the cowboy's bullets had already cracked it. Something gave with a crunch. He spun inside the arm, drove an elbow into the cracked plate, and felt it *crack further*.

Then he put everything he had into a strike to the chest, dead center, the one that stops hearts.

Nothing happened. There was no heart to stop.

*Huh*, Spike thought, a little sadly. *That figures.*

He stepped back. The red eyes were looking down at him with absolutely nothing in them.

**Smasher**

TARGET 1: CRITICAL.

He had been right about the first one. Meat, and fast meat, but meat doesn't change what it is by moving quickly.

He raised the rifle. The skinny one didn't try to dodge this time. He just stood there, swaying, and looked up at Smasher with something in his face that Smasher's threat-assessment software couldn't parse.

It wasn't fear. It looked almost like *relief*.

Smasher fired once.

TARGET 1: NEUTRALIZED.

**Arthur**

Spike went down and didn't get up.

Arthur watched him fall. He watched the blue suit go still in the sand, and he heard himself make a sound he didn't recognize.

He'd watched a lot of men die. He'd watched Hosea die, and Lenny, and Sean in the street in Rhodes with half his head gone. He'd thought he was done feeling it.

He wasn't.

"*Alright*," Arthur said. He stood up, and his voice was very quiet. "*Alright, you son of a bitch.*"

He reached into his satchel and found the snake oil, and drank half the bottle in one swallow. It burned all the way down and lit a fire behind his eyes. The world went slow again.

He painted the machine all over and fired.

**Smasher**

TARGET 2: PERSISTENT.

The old one kept shooting, and the old one kept *hitting*. Somewhere in seventy years of combat data, Smasher's systems flagged a pattern: Morgan Blackhand, on the roof of Arasaka Tower, fifty-four years ago. That was the only other man who had ever hit him like this.

A shot went into the cracked knee joint. A shot went into the cracked chest plate. One more went in under the jaw, and his optics flickered. A warning ran red across his vision.

STRUCTURAL INTEGRITY: 18%. DEPLOYING ARMOR REGENERATION MATRIX.

His plating flowed and reknit, sealing the cracks. The old man stared at him across the sand.

Smasher fired back. Four shots, and every one of them hit.

**Arthur**

He was lying on his back in the sand again.

He could feel the bullets inside him, four of them, maybe more. He coughed, and what came up wasn't just the sickness this time.

*Get up, Arthur.*

He got up. He didn't know how. He just did, the way he always had.

He breathed in deep, all the way down to the bottom of his ruined lungs, and felt something steady in him. It wasn't strength. It was just stubbornness.

He fired three shots, and every one of them was perfect: the knee, the chest, the jaw, in the seams where the new plate hadn't quite set. The machine *staggered*.

It fired back, and Arthur went down again.

He got up again.

He fired four more shots and watched one of the red eyes go dark.

The machine fired back four more, and this time, when Arthur went down, he knew he wasn't getting up again. He had nothing left. He lay on his back and stared at the sky, and he could feel his heart slowing.

*So this is how it goes.*

Then he thought about John. He thought about Abigail and Jack and the ranch. He thought about the skinny man in the blue suit, lying in the sand twenty feet away. He'd gone in when Arthur told him to get back, *one more*, and smiled while he did it.

Arthur Morgan sat up.

He took one more breath, the last good one in him, and brought the Schofield up.

The world went slow for the last time.

He could see it all: the machine's single red eye, the crack in the chest plate the skinny man had opened with his bare hands. Through the crack he could see a faint red glow, the core that kept the thing alive.

He painted one mark, dead center.

*This one's for you, partner.*

He fired.

**Smasher**

TARGET 2: PERSIS—

CORE BREACH.

CORE BR—

SYSTEM FAI—

**Arthur**

The machine fell like a tree, slowly at first and then all at once, and hit the sand hard enough to shake it.

Arthur sat in the sand with the Schofield in his hand and smoke curling from the barrel. He didn't move for a long time.

Then he got up, walked over to Spike, and knelt down beside him.

The skinny man's eyes were closed. He looked peaceful, more peaceful than Arthur had ever seen him. He looked like a man who'd finally been allowed to stop.

Arthur reached into Spike's jacket and found the crumpled, blood-soaked pack of cigarettes. There was one left, mostly dry. He lit it, and took one drag, and then set it gently between Spike's lips.

"There," he said. "We're even."

---

The bartender was waiting for him when he got back to the bar. He didn't say anything. He set a heavy leather satchel on the counter, and a pen, and a sheet of paper.

Arthur looked at the satchel. It was more money than he'd ever seen and more than he would ever need. He didn't have long enough left to need it.

He picked up the pen and wrote two names in careful, cramped handwriting.

*John Marston. For Abigail and Jack, wherever they end up. Somewhere quiet.*

He thought for a while about the second one. Then he wrote:

*Jet Black. The Bebop. From Spike.*

He pushed the paper across the counter and picked up the glass the bartender had poured him. He drank it slowly this time.

Somewhere outside, the sun was coming up.
