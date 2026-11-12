# The Smallest Cut

*Miyamoto Musashi vs FLLFFL.* A lime-green man drawn in five lines comes in carrying a sword with a jet engine in the back of it. He forged it, he hates it, and he is looking for somebody who can break it. The slate gives him a man of fifty with two plain swords, and when the television comes on it sounds like a pallet of steel stock coming off a truck. It comes after [Expendable Assets](arthur-vs-jack.md).

The fight is real: the one with the most steel on steel in 12,000 runs of `python battle.py 1v1 musashi alfa`, picked by `fight_log.py musashi alfa 12000 Musashi reactions`, which scores a duel by its rounds and by every parry, dodge and cut made on the other man's turn. Musashi is the favorite: 80.6% of 2,000 through `battle.py`. The usual fight is two rounds of everything both of them have. In a separate count of 20,000, Musashi won 16,187, and of those 12,736 ended in the second round, 3,321 in the third, 93 in the fourth, and one in the fifth. This is a fight like that one. Alfa wins initiative and goes first in every round. His first cut of the fight would land, so Musashi's long sword cuts into it first (Holding Down the Pillow), and that cut is the One Cut, with five superiority dice in it. Alfa's Uncanny Dodge halves it to 35 and his own cut never arrives. Then six more of his do, with the flame behind each, and Musashi is at 89 of 204 before he has had a turn. After that the two of them trade for four rounds and spend everything: all four Second Winds each, all three Action Surges between them. Musashi makes five Pillow cuts, one in each round. Four land and stop the blow they were aimed at. The fourth of the five Alfa parries, on his own turn, in the middle of his own attack. Musashi's short sword parries four of Alfa's cuts and takes 13, 8, 6 and 9 off the steel. It takes nothing off the fire, which comes through every time. Alfa parries two of Musashi's cuts and Peerless Aim lands both of them anyway. Four times Musashi puts a Trip into a cut, and four times Alfa keeps his feet. In round 5 Musashi has 19 hit points and Alfa's third cut would land with a Sneak Attack on it, which is 17 at the very least. The Pillow cut gets there first. Then the Riposte, and Alfa has 9. Musashi's next cut is a katana with a Trip die on it, 1d8+7 and 1d8. Both dice come up 1. Nine is the least that cut can do.

<details>
<summary>The round-by-round log</summary>

```
winner: Musashi in 5 rounds
R1 Alfa    | {Musashi: dice 6->1, one_cut True->False} {Alfa: surges 1->0, dice 5->3} ** Musashi: One Cut on Alfa ** ** Alfa: Uncanny Dodge ** hit 35 slashing (Musashi) miss ** Musashi parries 13 ** [Alfa -> Musashi: 4 fire] hit 5 slashing miss ** Alfa: Precision Attack ** [Alfa -> Musashi: 13 slashing] [Alfa -> Musashi: 6 fire] [Alfa -> Musashi: 8 fire] hit 11 slashing miss ** Alfa: Precision Attack ** [Alfa -> Musashi: 15 slashing] [Alfa -> Musashi: 8 fire] [Alfa -> Musashi: 5 fire] hit 16 slashing [Alfa -> Musashi: 10 fire] hit 14 slashing  || Musashi 89  Alfa 182
R1 Musashi | {Musashi: sw 4->3, surges 2->1} miss [Musashi -> Alfa: 11 slashing] hit 16 slashing miss hit 11 slashing miss hit 8 slashing hit 12 slashing hit 8 slashing hit 10 slashing  || Musashi 116  Alfa 106
R2 Alfa    | {Alfa: sw 4->3} hit 9 slashing (Musashi) miss ** Musashi parries 8 ** [Alfa -> Musashi: 10 fire] hit 8 slashing [Alfa -> Musashi: 3 fire] hit 24 slashing  || Musashi 71  Alfa 120
R2 Musashi | {Musashi: sw 3->2, surges 1->0} {Alfa: parry False->True} ** Alfa parries ** miss [Musashi -> Alfa: 8 slashing] hit 18 slashing miss hit 10 slashing miss CRIT 15 slashing miss miss hit 13 slashing  || Musashi 94  Alfa 56
R3 Alfa    | {Alfa: sw 3->2} hit 8 slashing (Musashi) miss ** Musashi parries 6 ** [Alfa -> Musashi: 7 fire] hit 12 slashing [Alfa -> Musashi: 12 fire] hit 14 slashing  || Musashi 49  Alfa 68
R3 Musashi | {Musashi: sw 2->1} {Alfa: parry False->True} hit 17 slashing ** Alfa parries ** miss [Musashi -> Alfa: 12 slashing] hit 8 slashing miss hit 12 slashing  || Musashi 75  Alfa 19
R4 Alfa    | {Alfa: sw 2->1, parry False->True} ** Alfa parries ** miss (Musashi) ** Musashi parries 9 ** [Alfa -> Musashi: 8 fire] hit 6 slashing [Alfa -> Musashi: 3 fire] hit 28 slashing [Alfa -> Musashi: 4 fire] hit 11 slashing  || Musashi 15  Alfa 40
R4 Musashi | {Musashi: sw 1->0} hit 15 slashing miss [Musashi -> Alfa: 11 slashing] miss miss miss  || Musashi 40  Alfa 14
R5 Alfa    | {Alfa: sw 1->0, dice 3->2} miss miss ** Alfa: Precision Attack ** [Alfa -> Musashi: 16 slashing] [Alfa -> Musashi: 5 fire] hit 12 slashing (Musashi) miss then: hit 15 slashing (Musashi)  || Musashi 19  Alfa 9
R5 Musashi | <Alfa DROPS TO 0> <Alfa OUT> hit 9 slashing  || Musashi 19  Alfa 0
```

An attack tagged `(Musashi)` inside one of Alfa's turns is the Pillow cut. It is logged just before the attack it was aimed at: when it hits, Alfa's attack after it reads `miss`, because it never arrived. In round 4 it is the Pillow cut that reads `miss`, after `** Alfa parries **`, and Alfa's attack goes on and hits. The flame is logged as its own line, `[Alfa -> Musashi: N fire]`, just before the hit it rode in on, and `** Musashi parries N **` comes before the hit it was taken off: in round 1 a cut for 18 is logged as `hit 5`, with 4 fire that the parry couldn't touch. A `miss` followed by `** Alfa: Precision Attack **` is a near miss that a superiority die turned into a hit, and its steel and its fire are in the brackets after it. A `miss` followed by `[Musashi -> Alfa: N slashing]` is Peerless Aim, which makes one of Musashi's misses a turn a hit. Twice the miss it rescues is one Alfa had just parried. After `then:` is the Riposte the short sword had been holding since Alfa's first cut of round 5 missed, landing once Alfa's turn was over. `sw` is Second Wind: the totals after `||` already have it in them, so Musashi's 116 at the end of his first turn is 89 and a breath worth 27. Alfa had spent his one Reaction on the Dodge, so nine cuts came at him with no Parry and no Riposte to answer them. `dice 6->1` is the One Cut. The critical hit in round 2 puts Alfa at disadvantage for the whole of round 3 (Slasher), and from round 3 the first cut he makes at Musashi each turn has it anyway (Rhythm). That costs him his Sneak Attack on the cuts it touches. A drop to 0 is logged just before the attack that caused it.

</details>

---

## The Bar

**Alfa**

He looked at the steel first. He had been a smith before he was anything else, and he had come a long way looking for a hammer.

There was a good deal of steel in the room. A slab of iron leaned on the counter beside a man with one eye, and it was as long as the man. Somebody had forged it by hand, in a bad temper, and had known his trade. A boy in green wore a sword on his back that nobody had forged at all. Alfa could not have said how he knew that. There was a revolver, old and well kept. There was a suit of green plate with the helmet on, and near its hand a crack in the edge of the counter. At the far end sat a thing built of gray steel from the feet up, with red eyes. He looked at that one longest. His own right arm was gray from the shoulder down, and he knew what it had cost.

In the middle of the row there were two men of his own trade. One wore old laced armor. The other was about fifty, in a robe that had been slept in, with a long sword and a short one through his sash. They were plain working swords. The long one had been sharpened so many times that the edge had moved back into the blade.

Nobody reached for anything. They looked at him the way people do in a new place. At the near end a man in a hat had a small book open, and a pencil, and was looking from Alfa to the page as if one of them had cheated him.

"Five lines and a circle," the man said. "That's all there is of him. And I'll be damned if it ain't a likeness."

"Is it me," said a thin man with a cigarette, "or is that guy drawn?"

"He can hear you, Spike."

Alfa sat down. He laid the sword across his knees and kept his hand on the grip. He did not put it on the counter. He had not put it anywhere in a long time.

The old man behind the bar set down a cup of barley tea. Beside it he put a folded rag and a small tin of oil. It was the light kind, for a bearing that turns fast and runs hot.

"It's paid for."

Alfa looked at the tin. Nobody had asked him what he wanted. Nobody had asked him in years.

"Is that a rocket?" The voice came from two stools down, from a man who was wearing a handsome face over his own. "On a sword? No, I love it. Somebody taped a lighter to a letter opener. Ten thousand. I want it over a fireplace."

The green head turned. That was all it did. It had not turned for the slab of iron, or for the thing with the red eyes.

"I'd leave that be, mister," said the man in the hat. "He don't look easy to rile, and I believe you just found the one way."

"It isn't for sale," Alfa said.

"Everything is for"

"Not in here," said the man in the hat, and the thin man, and a priest with a book, all three together. The handsome face went back to its paper cup.

The swordsman of fifty had come down the bar while that was going on. He stood and looked at the sword the way a carpenter looks at another man's joint.

"You made that."

"Yes."

"And you put the fire in the back of it."

"Yes."

"What is the steel?"

"I've never told anyone."

"Good. Then nobody can make a second one." He bent a little closer. He did not touch it. "He insulted it and you turned your head. You did not turn for anything else in this room."

"It has never lost," Alfa said. It was a long speech for him and he took it slowly. "I have. Seven times, with that in my hand. The sword didn't lose any of them. Whatever it touches comes apart. I made it when I was young, and I wanted a thing that couldn't lose. That's what I got."

"And now?"

"I want it broken. I've been looking for someone who can do it." He looked down the bar, at the slab of iron.

The man with one eye had looked up. "I'd take a swing at it," he said. "I never met a thing that didn't break."

The old man had come round the counter. He wiped the slate with his sleeve and took up the chalk.

> **TONIGHT:**
>
> MUSASHI v FLLFFL

"Fluh," said the thin man. "Fliffle?"

"Alfa."

"That is not what that says."

"It's what it says."

The thin man tilted his head one way, and then the other. "Oh," he said. "Huh. Okay."

Alfa read the first name, and then he looked at the man standing beside him, and at the two plain swords.

"With respect," he said, "I was looking for a hammer."

"I know. He has sent you a carpenter." The swordsman did not seem offended. "I cannot break that. I doubt the big one can, though he would enjoy the attempt. But a man who hates his own sword has generally not been told the truth about it. People are afraid of a sword like that. They lose to you, and they go home and say it was the sword." He straightened up. "I would like to see what it does. Afterward we can talk about what ought to be done to it."

"I don't kill."

"Nobody does, here. That one shot me thirteen times." He nodded at the red eyes. "It is a restful place to lose in."

He went to the door. He had been three days late for the machine, they told Alfa afterward. He was not late now. Coming late works on an angry man, and he had looked at Alfa and had not found one.

He opened the door. There was no sand beyond it. There was a white floor and a white sky, with nothing on either of them. Far off there was a single line where the one met the other.

Alfa knew it. He had fought on it all his life. It was ground with nothing drawn on it but the line a man stands on.

The swordsman stood in the doorway a long moment.

"Paper," he said. He said it like a man who has been given something, and he went out.

Alfa drank the tea. He put the tin of oil inside his gi, and the rag with it, and followed.

---

## The Page

**Musashi**

He had seen that white once before, lying on his back under it. He had not been able to stand on it then.

There was no sun to put behind him and no tide to wait for. He did not mind. He had been thirty years putting ink on paper, and nobody had ever let him walk out onto the sheet.

The green man came through the door, and the door went away. At sixty feet he was a few strokes of a full brush: a head, a back, the limbs. One arm had been done in a different ink. Whoever made him had known when to stop, which is the hardest thing there is to know.

Musashi did not walk this time. Walking had bought him the first cut from the machine. It would buy nothing here. He drew both swords and stood, and waited to be shown.

A blue flame came on at the back of the green man's sword. It made a sound like silk tearing, and it did not stop tearing.

Then the man was in front of him. He had crossed the sixty feet in the time it takes to see a thing happen. Musashi had not been second to move since he was thirteen years old.

The cut was good, and it was going to land. He knew that the way a man knows in the dark that the next stair is not there. So he did what he had done all his life. He did not stop the blow. He cut the man while the blow was still being made, while the whole of the man's mind was in it. The old name for it is about a pillow: you do not let his head come up off it. He had one cut with everything in it, and he had not meant to spend it in the first breath. But it was the cut that was in his hand. He put it into the green man at the collar, going down.

The man was not there for all of it. He turned inside the cut the way a door turns on its pin. He took half of it, and the other half cut white air. His own blow went nowhere.

*Half.* The machine had stood still and taken the whole.

Then the flame lit six times. The short sword was where it should be for the first of them. It met the edge and knocked the weight out of it. It did nothing about the fire, which came round the steel like water round a post and laid itself along his arm. The next cut was a hand's width wide of him. Then the flame barked, once, short, and the blade jumped sideways in the air and was on its line. He had never seen a cut corrected after it was thrown. Another came in clean. Another was wide, and corrected the same way. Another. Then the man was six paces off, and the jet threw him back in for the last one as straight as a snapped chalk line.

Musashi's robe was burning in six places. He had less than half of himself left, and he had not yet made a cut that was his own idea.

But he had seen one thing. Each time, the flame came a little before the edge.

He breathed. There is a breath that puts a man together again for a while, and he knew how to take it four times. Then he went in with both swords and cut nine times without stopping. The green man had spent all of his attention on that turn inside the big cut. He had none left over to answer with. One of the nine went wide, and the wrist turned it over and brought it back to the line. Seven got home. With the short sword Musashi put his weight in low, to take the man's feet out from under him. The feet were not there.

They stood apart. Each of them had about half of himself. It had taken as long as it takes to say so.

**Guts**

The old man reached up with the broom handle, and the gray glass came on white. Guts thought it was broken. Then he saw two marks on the white, a green one and a brown one, and a blue spark.

Then the noise came out of the box.

He had lived a winter at a smith's once, up a mountain. The old man there kept his bar stock in a rack by the forge door, and one night the rack let go. Guts had come up out of his blankets with the sword already in his hand. This was that noise. It was not one sword on another. He knew that sound well enough, a clank and a grunt and a clank. This was every bar in the rack hitting the stone floor and every other bar, and the first ones still ringing when the last came down.

"Jesus," Spike said. "Somebody just dropped a pallet of steel stock off a truck."

"Language," said the priest. He did not look away from the glass.

It stopped. The ringing went on a little by itself and then that stopped too. The two marks stood apart. Smoke was coming off the brown one.

"Seven," Jin said. "And one of Musashi's, inside the first."

"Inside it?"

"The first cut in that was not the green man's. Musashi cut into it."

It began again. This time it was the brown one moving, with both swords, and there was less ringing in it. Guts knew what that meant. The green one was not catching them.

Then the green one, three times. Guts was watching for it now, and he saw it. The blue spark lit. The green one came in. The long sword was already there, and it was not in the way of the cut. It was in the man. The cut stopped being a cut.

"He did it again."

"He does not stop the blow," Kratos said. "He arrives before it."

Guts had never stopped a blow in his life, except by being harder than it was. He had a sword you could shelter a child behind. Neither of those two had ever been harder than anything. He leaned in on his elbows. It was a long time since anybody had shown him something about a sword.

"Neither is augmented," the machine said.

"One of them's got a chrome arm, partner."

"Grip and rotation. It is a replacement for an arm." The red eyes had not left the glass. "It is not what is doing that. I have checked. Do not call me that."

The noise came again, and it was the whole rack this time.

**Alfa**

Fourteen seconds. His first fight had taken that long from the start to the end, and most of them since had gone the same way. Seven cuts and it was over. He had made the seven. The man was standing in a burning robe, and breathing, and Alfa was open from the collar to the ribs. It would have gone on to the hip if he had been a quarter of a second slower in the turn.

He had gone in again with three. The first had not arrived. It had not arrived the first time either. The long sword was in him, there, somewhere between the thought and the wrist, and the cut came apart in his hand. The second got as far as the short sword and lost half its weight on it. The fire went on without it. He did not look to see where the fire went. He never looked. The third went home under the short sword, clean, and it was the best he had.

Now the old man was coming with nine again, and this time Alfa's hand was free to answer.

He took the first on the flat and turned it. It was a clean parry and that cut should have gone past his shoulder. The old man's wrist rolled over, and the same cut came back round onto its line without ever having stopped. Alfa had been parrying for thirty years. Nothing he turned had ever come back.

He kept the guard up. It turned four more. Four got through anyway. One of those went in deep, under the arm that was still his own, and after it the sword was heavier than he had built it. The short sword came in low again with all the weight behind it. He let the jet lift him over it and came down standing.

He had a quarter of himself left.

He breathed, and went in, and every cut he threw now had to go out through that wound. There was something else as well. The old man had stopped moving on any count that Alfa could find. He was a half beat off it, to one side or the other, and it was never the same side. The first cut did not arrive. The long sword was in him first. That was three times. The second lost its weight on the short sword and sent its fire on. The third went home.

He understood it then, and he understood it as a smith. The flame came before the edge. It had to. He had built it so, the ignition and then the thrust. For thirty years the space between the two had been too small to matter to anybody. This man had read it in the first exchange. Alfa had made a sword that told the other man when.

The old man breathed and came with five. One went home. Alfa turned the next, and the wrist rolled, and it came back round. Two more got in. The low one came for his feet a third time, and he stood through it.

He had less than a tenth of himself now, and two breaths.

The fire could not be made to come later. He had built it too well. But a thing that always tells the truth can tell one lie, and the first one is always believed.

**Musashi**

The flame lit, and he cut into it.

Nothing was there. The flame had come on and the man had not come behind it. The long sword went into the place where the blow should have been, and the green man's sword was waiting for it in that place. It knocked the long sword aside with a note like a temple bell.

In sixty fights and more, nobody had done that to that cut. Most of them had never known that it was made.

Then the real cut came in behind the lie. The short sword got to it and took what it could. The fire came through. Two more followed, and the first of the two was the worst he had taken that day, up under the short sword, where the third one always went. Then the last, and its fire.

He had about as much of himself left as there is ink in a brush that has painted the whole branch.

He found that he was pleased. He had spent fifty years finding out how far the sword goes. Here was a man who had come to the same place by another road, with a fire in the back of his blade, and who had just told him a lie with it that he had believed.

He took the last of the four breaths and went in with five. The green man's guard was still up from the lie. One cut got home, low, with his weight in it, and the green man's feet stayed where they were. One was turned, and the wrist brought it back. The last three found the green man's sword, and nothing else, one after another, and each of them rang.

The green man breathed. It was his last one too. Musashi could hear that in it.

The first of the three came, and Musashi was not where it was. It was the first clean miss the man had made all day. The short sword took note of it. The second was wide by a hand, and the flame barked and brought it home, and the fire with it.

Now one good cut would do it. He had no breath left to take. The cut was coming, the third, the one that went home every time. And the flame lit.

He could not know. He had believed it four times and been right three. There is a thing he told his students about such a moment, and he had never been certain it was true. *When you cannot tell, do not answer the question. Cut the man who is asking it.*

He cut. The long sword got there first. The blow had been a true one, and it came apart.

The green man's turn was over. The short sword paid what it had been owing since the miss.

Then it was his own turn to begin, and he had nothing to begin with. He had no breath. He had nothing of what makes a cut more than a cut. That had all gone in the first second, and the man had stepped out from under half of it. He had a long sword and a tired arm.

He made a plain cut, low, at the ankle. It was the one the green man had stood through or stepped over four times. It was the smallest cut he had made since he was a boy. He would have corrected a student for it.

It arrived.

**Alfa**

It was a small cut. He looked down at it with some interest.

He had taken twenty-three that day and stood up out of every one. There was the one that began it, which had a name, he was sure, and which he had only half got out of. He had always thought that when the cut came it would be one like that. This one was hardly deep enough to need a bandage. It was only that there was nothing left behind it to hold him up.

His feet were not under him. They had been under him four times.

He sat down on the white, and then he lay back on it. The sword was in his hand. The flame at the back of it burned a moment longer and then went out by itself.

He had been killed before, in other men's tellings. There was a train once. None of those had felt like this. This felt like being put down by someone who meant him to get up.

The white was very clean. There was one line on it, a long way off.

Somewhere close by he could smell barley tea.

---

## After

**Alfa**

He was on a stool. The cup was in front of him, full, with the steam going up. He was closed from the collar to the ribs, and under the arm. The sword lay across his knees with the gray hand on it.

The old swordsman was on the next stool with a cup of hot water. There was not a burn on the robe. It was no cleaner.

Alfa knew what this was. He had done it himself a good many times. When he beat a man he went and sat with him afterward, in the chair by the bed, until the man woke up. He had never been the one in the bed.

The slate said *MUSASHI.* After it, smaller: *(a moment sooner).*

"One and one, old man," the thin one said, and lifted his glass. The swordsman nodded to it.

"I usually do this part," Alfa said.

"Which part?"

"The chair."

The swordsman considered that. "How is the other side of it?"

"Restful."

"I said so." He turned his cup a little. "I could not break it."

"No."

"I struck it a dozen times with a good sword. There is no mark on it. There were several on mine, before the door mended them, which I think is a pity. So I will tell you what I saw. That much I can do." He held up four fingers. "Four times I caught your edge on the short sword. I was entitled to. In that moment I was the better of us, and I had stopped you: your arm, and your line, and what you intended. And four times the fire came round and burned me anyway. I had not beaten the fire. It had nothing to do with me, or with you. It burns the man who has just won."

Alfa said nothing for a moment.

"That's it," he said. "That's the thing I hate." He had not said it aloud before, to anybody.

"Yes. Now the rest. Five times I cut before you did. Four of those I could do because the flame told me when. So the part of that sword you are ashamed of is the part that lost you the fight. The steel did not fail. The hand did not fail. And the fourth time, you took the worst thing about your sword and made it tell me a lie, and you parried a cut that nobody has parried. The sword did not do that." He drank. "I have fought swords. There was a man at Funashima with a very famous one. It was so long that they called it the Drying Pole, and everyone knew its name. In the boat on the way over I cut a wooden one out of an oar. It was a hand longer than his."

"And?"

"He is buried on that island. I never asked what became of the sword. The oar I left in the boat." He set the cup down. "You are looking for a hammer. I think you are looking for an oar."

"Without it I'm a tired old man with good footwork."

"I am a tired old man with good footwork. It has done for sixty." He glanced down the bar. "And lost to one. I do not say it is everything."

"Twelve thousand," said the handsome face, from two stools down.

"Not in here," said four voices. One of them was the swordsman's.

At the far end the red eyes had been on them for some time. "The last strike," the machine said. "State what was in it."

"Nothing," the swordsman said. "That is why it arrived."

The red eyes went to Alfa's arm.

"The limb. State whether you would reverse it."

"Tomorrow," Alfa said.

The machine did not answer at once. "Noted," it said.

"I'd still take a swing at that thing," said the man with one eye.

"After the tea."

Alfa took the tin out of his gi, and the rag. He turned the sword over on his knees and opened the housing at the back of the blade, and began on the bearing. He had done it every night for thirty years. It took him no thought at all.

"You keep it well," the swordsman said, "for a man who wants it broken."

"It isn't the sword's fault."

He heard it after he had said it.

"No," the swordsman said. "It never is. A man should not have a favorite weapon. I have told people so for years. You have one and you hate it, and that is the same as loving it. Either way it is the only thing you can see." He nodded past Alfa, at the man in the laced armor. "Sakai there carries smoke and darts and a short blade at his back, and he was taught to be ashamed of all of it. You carry one thing, and you are ashamed of that. The two of you should talk."

The man in the armor inclined his head. "There is time," he said. Beyond him, set along the bar in front of nobody, there was a cup of sake that no one had touched.

The old man had put down an inkstone, and a brush, and one sheet of paper. The swordsman said, "Ah," and wet the stone.

He did not take long. There was a ring for the head. There was one stroke for the back, and two for the legs, and two for the arms. The right arm he did with the brush nearly dry, so that it came out gray.

"Morgan did it in five lines and a circle," he said. "I cannot do it in fewer. I have tried, just now, in my head."

It was a likeness. The figure stood the way Alfa stood. It had nothing in its hand. The gray arm ended in a hand that was open.

"You haven't finished it," Alfa said.

"It is the only one of you that is finished." He blew on the ink. "The other one is on your knees."

The old man pinned it to the wall beside the slate. There were three papers there already: a bird on a dead branch, a few lines of writing, and a street in pencil.

Alfa looked at it for as long as the tea took to cool. Then he closed the housing and wiped the blade down, and laid the sword on the counter, between the oil and the cup.

He took his hand off it.

The gray hand did not know what to do with itself. He gave it the cup.
