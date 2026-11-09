# The Ledger

*Alexander Anderson vs Kratos.* Straight after [Full House](intermission-full-house.md): the chalkboard fills, the bar empties, and a priest and a god are left with a conversation before their bout.

The fight is real: the most dramatic of 400 runs of `python battle.py 1v1 anderson kratos`, picked by `fight_log.py anderson kratos 400`. Kratos wins about 92% of the time: fire to keep Anderson from regrowing, then the clause on Anderson's own sheet, the heart. This one is close. Hold Monster takes Kratos's first three turns, and Anderson crits a held god four times. Kratos breaks out with 91 HP left, and Out of Hades has to bring him back at 1 before he gets Anderson down and burning. The sim stops when Kratos wins the Strength contest. What he does with his hand after that is the story's.

<details>
<summary>The round-by-round log</summary>

```
winner: Kratos in 7 rounds
R1 Anderson | {Anderson: hold_used False->True} {Kratos: paralyzed False->True}  || Anderson 284  Kratos 293
R2 Anderson | {Anderson: haste False->True}  || Anderson 284  Kratos 293
R3 Anderson | CRIT 80 radiant CRIT 26 radiant CRIT 18 radiant CRIT 17 radiant  || Anderson 284  Kratos 152
R4 Anderson | hit 25 radiant hit 13 radiant hit 15 radiant hit 8 radiant  || Anderson 284  Kratos 91
R4 Kratos  | {Anderson: prone False->True} {Kratos: raging False->True} [Kratos -> Anderson: 3 fire] [Kratos -> Anderson: 12 fire] [Kratos -> Anderson: 9 radiant] hit 22 slashing [Kratos -> Anderson: 7 fire] [Kratos -> Anderson: 5 radiant] CRIT 26 slashing [Kratos -> Anderson: 2 fire] [Kratos -> Anderson: 8 radiant] hit 26 slashing [Kratos -> Anderson: 7 fire] [Kratos -> Anderson: 1 radiant] hit 22 slashing [Kratos -> Anderson: 2 fire] [Kratos -> Anderson: 5 radiant] hit 25 slashing [Kratos -> Anderson: 5 fire] [Kratos -> Anderson: 9 radiant] hit 24 slashing  || Anderson 64  Kratos 100
R5 Anderson | hit 38 radiant hit 13 radiant hit 11 radiant hit 13 radiant  || Anderson 94  Kratos 25
R5 Kratos  | miss [Kratos -> Anderson: 3 fire] [Kratos -> Anderson: 6 radiant] hit 20 slashing [Kratos -> Anderson: 4 fire] [Kratos -> Anderson: 10 radiant] hit 19 slashing  || Anderson 3  Kratos 61
R6 Anderson | {Kratos: hades True->False} hit 24 radiant hit 8 radiant hit 12 radiant <Kratos DROPS TO 0> <Kratos back up at 1> hit 17 radiant  || Anderson 33  Kratos 1
R6 Kratos  | {Anderson: times_down 0->1, down False->True} <Anderson DROPS TO 0> <Anderson DOWN> hit 23 slashing hit 18 slashing miss  || Anderson 0  Kratos 42
R7 Anderson |   || Anderson 0  Kratos 42
R7 Kratos  | ** Kratos tears out Anderson's heart **  || Anderson 0  Kratos 77
```

Held creatures take critical hits from anything next to them, which is round 3. Kratos's HP jumps are Valor and Second Wind. Anderson regrows 30 at the start of each turn, unless 20 fire or radiant landed on him since his last one, and Kratos is using the Blades of Chaos because Anderson grows back. Round 7 is the heart clause: a grapple and a Strength contest in one Attack action.

</details>

---

## The Chalkboard

The chalk squeaked. Nobody in the bar breathed.

When the old man stepped back, the slate read:

> **TONIGHT:**
>
> SPIKE & SMASHER v ARTHUR & GUTS
>
> LINK v JIN *(again)*
>
> ANDERSON v KRATOS

He set the chalk down in the tray and went back behind the counter, picked up a glass, and started polishing it.

For a moment nobody said anything.

Then Spike started to laugh.

"Oh, *come on*," he said, waving his cigarette at the board. "Him?"

At the end of the bar, Adam Smasher's red eyes turned slowly toward Spike and stayed there. His fingers stopped tapping.

"Partner," Spike said to him, and raised his glass.

"Do not call me that," said Smasher.

Arthur was staring at the board with his jaw set. "Me and the big fella," he said, and looked sideways at Guts. "Against *him*." He jerked his head at Spike. "Damn it all."

"Hey, it's not personal," Spike said. "Pretty sure it's the chalk."

"I know it ain't personal," Arthur said. "That's what makes it worse." He drained his whiskey, stood, and put a hand on Spike's shoulder on the way past, briefly, hard. "Try not to die again. I'm getting tired of it."

"No promises."

Guts was already up, shouldering the sword. He looked at Smasher, a long flat one-eyed look, and something unspoken passed between them that had to do with iron and the things it does to men. Then he followed Arthur out the door.

Smasher rose from his reinforced stool, ducked under the lintel, and went after them without a word. The doorframe groaned.

Spike stubbed out his cigarette, finished his drink, and looked at the bartender.

"Put it on my tab?"

The old man didn't look up.

"It's paid for."

"Course it is." Spike went out whistling something slow.

At the far end of the bar, Jin had been looking at the board for a long time. He turned to Link.

"Again," he said.

Link nodded.

"I have been thinking about the blue light," Jin said. He finished his sake and set the cup down carefully. "For a long time. I believe there may be a way."

Link considered him.

"Maybe," he said.

Jin smiled, the first smile Kratos had seen on him. He stood and bowed to the room, and Link finished his milk. The two of them went out together, the samurai and the boy in green, already talking. That is, Jin was talking and Link was nodding.

The door swung shut behind them.

And then there were two.

---

## The Conversation

**Kratos**

The bar was very quiet without the others.

The priest sat three stools down, turning his glass slowly on the counter. He didn't look at the board. He didn't look at Kratos. He seemed to be looking at something a long way off.

Kratos drank his mead.

"You're not in a hurry," the priest said eventually.

"No."

"Neither am I." The priest smiled faintly. "Odd, isn't it? There was a time I'd have been out that door with a bayonet in each hand before the chalk stopped squeaking." He turned the glass again. "Perhaps I'm getting old."

"Perhaps you are tired," said Kratos.

The priest looked at him then, sideways, over the top of his round glasses.

"Aye," he said. "Perhaps."

They drank.

"I should tell you," the priest said, "since we're going to try to kill each other in a bit, that I'm a Catholic priest. Iscariot. We're the Vatican's Thirteenth Section. We hunt monsters. Vampires, ghouls, heretics." He waved a hand. "That sort of thing."

"I gathered."

"And you're a pagan god."

"I was."

"Was." The priest sat back. "What changed?"

Kratos was quiet for a long time.

"I had a son," he said.

The priest's face did something soft.

"Ah," he said. "Aye. That'll do it."

**Anderson**

He hadn't meant to ask more. He had meant to finish his drink and go out to the sand and do the Lord's work, the way he always had.

But the god had a son, and Alexander Anderson had spent half his life feeding orphans, and he could not help himself.

"Tell me about him."

The god looked at him for a long moment with those ash-pale eyes. Anderson thought he wouldn't answer.

"He is clever," said the god. "Too clever. He talks too much. He is kinder than I was at his age. Kinder than I am now." He turned the cup in his big scarred hands. "He has gone to find his own path. Among the giants."

"You're proud of him."

"Yes."

"Does he know that?"

The god was silent. Then: "I believe so. I did not say it enough."

"No father ever does." Anderson finished his drink, and the bartender filled it without being asked. "And the ash? On your skin." He'd noticed it the moment the god walked in: white, ground into the skin, old. "That's not paint."

The god's jaw tightened.

"No," he said.

Anderson waited.

"There was a god," said Kratos slowly. "Ares. The god of war, in my land, before I took the name. I served him. He made me his weapon. I burned villages for him, and cities." He set the cup down. "One night he sent me to a temple. I killed everyone inside. In the dark, in the rage, I did not see who they were."

Anderson felt the cold go down his spine before the god even said it.

"My wife," Kratos said. "And my daughter. Calliope. Ares had brought them there. So that I would kill them, and have nothing left but him."

The bar was silent.

"The village oracle cursed me. She bound their ashes to my skin, so all men would know what I had done." Kratos looked down at his arms. "It has never washed off."

Anderson closed his eyes.

He had heard a great many confessions in his life, from murderers and thieves, adulterers and liars. He had heard men confess things that made his stomach turn and his hands itch for his bayonets. He had never heard one like that.

"Lord have mercy," he said quietly.

"No god has ever had mercy on me," said Kratos. "I do not expect yours to start."

---

**Anderson**

"That's where you're wrong," Anderson said.

Kratos looked at him.

"I'm not saying it to be clever," Anderson said. "I'm not saying it because it's my job, though it is. I'm saying it because it's *true*." He turned on his stool to face the god fully. "That's the whole thing, you see. That's the entire point of the faith I follow. It's not that we're good. It's that we're *not*, every one of us, and we're forgiven anyway."

"Forgiven," said Kratos, as if the word tasted strange.

"Aye. For all of it."

"For killing my family."

"For *all* of it," Anderson said. "Your wife. Your daughter. The villages. The cities. Whatever else you've done that you haven't told me." He leaned forward. "I'll wager it's quite a list."

Kratos's face did not change, but something in his shoulders did.

"You keep a ledger," Anderson said quietly. "Don't you? I can see it on you. Every life you took, every one you failed, all of it written down. And you think if you can just do enough good on the other side, if you can balance it, maybe someday you'll be allowed to put the book down."

Kratos did not answer.

"Forgiveness isn't balancing the ledger," Anderson said. "It's tearing it up. It's God taking the book out of your hands and putting it on the fire and saying, *that's enough, son. That's enough.*"

"Then it is worthless," Kratos said. His voice was very low. "If it cannot be earned."

"No," said Anderson. "It's priceless. That's a different thing."

---

**Kratos**

He sat with that for a while.

The priest sat with him and didn't push. Kratos was grateful for that, though he would not have said so.

"You speak of forgiveness," he said finally, "with blood on your blades."

The priest didn't flinch. Kratos would give him that.

"Aye," Anderson said. "I do."

"You hunt men. You call them heretics and put bayonets in them. You serve a god who sends you to kill." Kratos turned his head to look at him squarely. "I served a god who sent me to kill. I know what that god makes of a man."

The priest was silent for a long moment.

"Aye," he said finally. "You're right."

Kratos had not expected that.

"I'm a weapon," the priest said. "The Lord's bayonet. I made my peace with that a long time ago. I do terrible things for a good God, because the world is full of worse things than me, and somebody has to stand between them and the children." He looked at his own big scarred hands. "I don't pretend it makes me a good man. It doesn't. I'm a sinner, same as you. Maybe worse, in my way."

"Then how can you speak of forgiveness?"

"Because I *need* it," said Anderson simply. "More than most. If it's not for me, it's not for anybody." He smiled, a little crookedly. "And if it's for me, God help us, then it's surely for you."

Kratos looked at him for a long time.

"Your god did not trick you into killing your children," he said.

"No," Anderson agreed quietly. "He didn't. Mine wouldn't." His jaw set. "And if I ever met the one who did that to you, I'd put every blade I own through him and say a prayer over what was left."

"I did," said Kratos. "I killed him."

"Good," said Anderson, with great feeling.

They sat.

"Did it help?" the priest asked. "Killing him?"

Kratos thought of Ares on the sand, the Blade of the Gods in his chest, the long fall afterward. He thought of the cliff, and the sea, and the ash still on his skin the next morning.

"No."

"Aye," said Anderson. "It never does."

---

**Anderson**

"May I ask you something?" Anderson said. "Something hard."

Kratos looked at him.

"Your son. When he learned what you were. What you'd done." Anderson chose the words carefully. "Did he forgive you?"

Kratos did not move.

Anderson watched the god's face and saw something there that he'd seen before, in confessionals, in the faces of hardened men at the end of their lives. It was the look of a man who has been handed something he doesn't know how to hold.

"Yes," said Kratos at last. His voice had gone very rough. "He did."

"And did you let him?"

Kratos said nothing for a long time.

"I do not know how," he said.

There it was. Anderson felt it go into him like a nail into wood.

"No," he said gently. "Nobody does, at first. It's the hardest thing there is, harder than any fight. To be forgiven, and to *let yourself be*." He laid one hand flat on the bar between them. "You've already had it, you see. Not from God, maybe, not that you'd let yourself see. From your boy. That's the same thing, near enough."

"It is not the same," Kratos said, "as being worthy of it."

"*Nobody* is worthy of it," Anderson said. "That's what I keep telling you. That's the whole *point*."

Kratos looked at him. The priest looked back.

Then the god did something Anderson did not expect: he let out a long breath, almost a laugh, the ghost of one.

"You are a stubborn man," Kratos said.

"So I've been told." Anderson grinned. "By better than you."

Kratos finished his mead and set the cup down.

"I do not accept your god," he said. "I have met too many gods."

"I know," said Anderson. "That's all right. He's patient."

"But I will think," said Kratos slowly, "about the ledger."

Anderson smiled. It was the smile he saved for the orphans.

"That's all I ask," he said.

Then the two of them stood, as if by agreement, and went out to the sand.

---

## The Bout

**Anderson**

He did not hate this one. That was new. He had always fought with hate before, hate for the monster in front of him, joy in its destruction. This time he went out onto the sand with something closer to sorrow.

But duty was duty.

He lifted a page from his book and spoke the words, and the Lord's authority went out from him like a hand around the god's throat. *Hold.*

The god froze in mid-step, axe raised, and could not move.

Anderson came in with his bayonets, praying out loud the whole way. It was a habit. He could never stop himself.

"*Forgive me, Spartan*," he said, and drove both blades into the god's chest. "*Forgive me.*"

He struck four times while the god stood frozen. Each blow was a perfect one, finding the soft places between muscle and bone. The god's blood ran gold and red down his ash-white skin.

"*Our Father, who art in Heaven*," Anderson said, between the blows. "*Hallowed be Thy name.*"

**Kratos**

He could not move.

He had been held before, by the chains of the Titans and the will of the Fates, and by Zeus's lightning. He had never been held by *words*.

The priest's bayonets went into him again and again, and with every blow the priest prayed. *Forgive us our trespasses. As we forgive those who trespass against us.*

He was praying *for* him, Kratos realized. Even now, putting steel through his ribs, the man was praying for him.

Kratos found that this hurt more than the blades.

He broke free.

The Blades of Chaos came off his back in a roar of fire. Six blows, every one burning, and the gold of Legacy in the rage. The priest went backward across the sand, his coat on fire, his flesh blackening where the chains struck. Kratos did not stop. He hit him with the blades, the shield and the fire, everything he had.

The priest got up anyway, burning, and *grinning*.

"*There* you are!" Anderson roared. "*There's* the god of war!"

He came back in with the bayonets, and Kratos felt them go deep.

**Anderson**

They traded blows like two men in a church bell.

He put the god down once. He felt him fall, felt his heart stop under the blades. *God rest you*, Anderson thought, *it's over*.

The god got up.

Anderson stared at him. He'd felt the heart stop. He knew he had.

"*How?*" he breathed.

"I have climbed out of Hades," the god said. His voice was a rasp, and he could barely stand. "Four times."

He came in with the chains.

Anderson felt the fire go into him, all the way into the marrow, into the place where the Lord's regenerating grace lived. He fell, burning. The fire did not stop. It held him down, flesh crisping as fast as it regrew. He tried to rise and could not.

He lay on the sand and looked up at the sky, and felt a big ash-white hand close on his collar and lift him.

**Kratos**

The priest was burning in his grip. The fire kept the flesh from knitting.

Kratos knew what he had to do. He had read it in the priest's eyes in the bar, in the way he'd talked about the things that could kill him. He'd read it in the way he'd looked away, just slightly, when Kratos looked at his chest.

*The heart.*

He drove his hand into the priest's chest.

The priest gasped. Kratos felt the ribs part, the heat, and then the thing itself, beating hard against his palm. It was the source of every regrown limb, the reason this man could not die. Kratos's fingers closed around it.

One pull, and it was done. The trial would be over. That was what he was, wasn't it? He had pulled the hearts out of gods. Hades' soul, with his own claws. Helios's head, with his bare hands. Zeus, beaten to death with his fists. *One more line in the ledger.*

The priest was looking at him. He wasn't fighting it. He couldn't fight it. Even now, with Kratos's hand around his heart, he was looking up at Kratos with something in his face that was not fear.

"Go on, then," Anderson said quietly. "I forgive you."

Kratos went very still.

He stood there for a long time, with the priest's heart beating against his palm, and thought about the ledger. He thought about every name in it. He thought of a temple and a village, and Calliope.

He thought of Atreus, at the top of the mountain, saying it didn't matter what he'd been. What mattered was what he chose to be now.

*That's enough, son. That's enough.*

Kratos opened his hand.

He drew it back out of the priest's chest, slowly and carefully, and laid the man down on the sand. The fire was going out. The ribs were already beginning to knit.

Then he sat down in the sand beside him, very heavily, like a man who has set down something he has been carrying for a very long time.

---

## After

The bar was empty when they came back. Neither of them had won, quite. The chalk on the board had changed. Under ANDERSON v KRATOS, in the bartender's careful hand, it now said: *KRATOS.* And next to it, smaller, as if added later: *(mostly).*

They sat at the counter, side by side. The old man set down a whiskey and a mead.

Anderson's coat was in rags. There was a fresh scar on his chest, pink and raw, in the shape of a large hand. He kept touching it.

Kratos didn't speak for a long time.

"I did not do it," he said at last.

"No," said Anderson. "You didn't."

"I have done it before. To gods. Without thinking."

"I know."

"Why did I not do it?"

Anderson looked at him over his round glasses.

"I think you know," he said. "I think you knew it before we ever left the bar. You just needed somebody to tell you that you were allowed."

Kratos looked down at his hand, the one that had held the heart. The ash was still there, as it always was. He turned it over and looked at the palm.

"I could not take it," he said. "Your forgiveness. Your god's."

"No," Anderson agreed. "Not yet. That's all right."

"So I gave it away instead."

Anderson laughed. It was the big laugh, the one that shook the bottles, and he slapped the counter hard enough to make the glasses jump.

"*Aye*," he said. "*You did.* And d'you know what? That's how it starts. Nobody learns to take it first. You learn to give it." He raised his glass. "Then one day you turn round and find somebody's been giving it to you the whole time."

Kratos looked at the glass for a long moment.

Then he raised his mead.

"To the ledger," he said.

"To the fire," said Anderson.

They drank.

Somewhere out on the sand, a cowboy and a giant swordsman were fighting a borg and a bounty hunter. Somewhere else a samurai was trying something new against a wall of blue light. The night was long, and the bar would be full again before morning.

But for now it was just the two of them: the god who had killed gods, and the priest who had told him he was forgiven anyway, drinking quietly while the old man polished glasses.

The ash on Kratos's skin did not wash off.

But for the first time in a very long time, he did not look at it.
