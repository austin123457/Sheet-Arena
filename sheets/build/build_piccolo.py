exec(open('sheet_style.py', encoding='utf-8').read())
GREEN = colors.HexColor("#2f5d1e")
h2 = ParagraphStyle("h2", fontName="DVSerif-B", fontSize=12.5, leading=16, textColor=GREEN, spaceBefore=11, spaceAfter=3)
hb_name = ParagraphStyle("hn", fontName="DVS-B", fontSize=9.6, leading=12.6, textColor=GREEN, spaceBefore=5, spaceAfter=1)
abil_head = ParagraphStyle("ah", parent=cell, fontName="DVS-B", alignment=TA_CENTER, textColor=GREEN)
def on_page(c, doc):
    c.saveState(); c.setFont("DVS", 7.8); c.setFillColor(MUTED)
    c.drawString(doc.leftMargin, 0.42*inch, "Piccolo, Raditz saga  ·  raid boss for D&D 5th Edition (2024 rules; a homebrew CR 30 monster)")
    c.drawRightString(letter[0]-doc.rightMargin, 0.42*inch, f"page {doc.page}"); c.restoreState()
doc = SimpleDocTemplate("../pdf/Piccolo_Raditz_Saga_Raid.pdf", pagesize=letter, leftMargin=0.6*inch, rightMargin=0.6*inch, topMargin=0.6*inch, bottomMargin=0.7*inch, title="Piccolo (Raditz saga) — D&D 5e Raid Boss", author="Claude")
W = letter[0] - 1.2*inch; S = []
sec = lambda t: P(t, ParagraphStyle("sec", parent=stat, fontName="DVSerif-B", fontSize=10.5, textColor=GREEN, spaceBefore=4, spaceAfter=2))
def statblock(rows):
    box = Table([[f] for f in rows], colWidths=[W]); box.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),PARCH),("BOX",(0,0),(-1,-1),1.0,GREEN),("LEFTPADDING",(0,0),(-1,-1),11),("RIGHTPADDING",(0,0),(-1,-1),11),("TOPPADDING",(0,0),(-1,-1),1),("BOTTOMPADDING",(0,0),(-1,-1),1),("TOPPADDING",(0,0),(-1,0),9),("BOTTOMPADDING",(0,-1),(-1,-1),9)]))
    return box

S.append(P("Piccolo", title))
S.append(P("Raid boss · the Raditz saga (the opening of the manga's Saiyan arc, chapters 195–208) · CR 30 · Demon King Piccolo's last son, eight years old, Kami's other half, and the one who made the Special Beam Cannon", subtitle))
S.append(HRFlowable(width="100%", thickness=1.4, color=GREEN, spaceBefore=4, spaceAfter=8))
S.append(P("Built from the manga, with Kanzenshuu's chapter guides and the Daizenshuu where they add a number. \"Raditz saga\" is Funimation's name for the opening episodes; in the manga it's the start of the Saiyan arc, and this sheet runs from Raditz landing (chapter 195) to the night Piccolo destroys the moon (chapter 208). He's in the <b>raid tier</b> because of that night: a moon-buster, on the page, months after Raditz, at the same strength. The scouter readings are the manga's: <b>322</b> when Raditz finds him, <b>408</b> with the weighted turban and mantle off, and <b>1,330</b> for the charged Makankōsappō. Raditz's 1,500 comes from the Daizenshuu, not the page."))
S.append(P("<b>Design calls.</b> A monster, like Madara, not a character: CR 30 with the tier's Legendary Resistance and Legendary Actions, scores past 5e's caps where his feats put them (the system is the frame, not the ceiling: a moon-buster's Strength is 40, not 22), and raid toughness (anything below the raid tier needs 100 damage in one hit to matter: Raditz no-sold Piccolo's shockwave at a fraction of his power, and the ladder is a long way under that). The Special Beam Cannon is the whole sheet: the one attack in the arena that goes through resistance, immunity and thresholds at once, because it went through a Saiyan who outclassed him and the man holding him. The price is what the manga shows: it takes time to charge, and it only landed when Goku held Raditz still."))

S.append(P("Piccolo, the Demon King's son", h2)); S.append(rule())
S.append(statblock([P("Piccolo (Piccolo Jr.)", statname),
 P("Medium Humanoid (Namekian, though nobody, Piccolo included, knows that yet) · 226 cm · the turban and the weighted mantle, the purple gi with the kanji for 'demon' on it · eight years old", stattag),
 P("<b>AC</b> 18, 21 once the weighted turban and mantle are off · <b>HP</b> 1230 (60d10 + 900) · <b>Speed</b> 40 ft, fly 80 ft · <b>Initiative</b> +10 · <b>CR</b> 30 (proficiency +9) · <b>Legendary Resistance</b> 3 a day", stat),
 abil_table(["40 (+15)","30 (+10)","40 (+15)","16 (+3)","20 (+5)","12 (+1)"], W-24), Spacer(1,4),
 P("<b>Saves</b> Str +24, Dex +19, Con +24, Wis +14 · <b>Senses</b> he feels power at a distance (chapter 195), and his hearing is sharp · <b>Languages</b> Common, Namekian (he doesn't know it yet)", stat),
 sec("Traits"),
 P("<b>Raid Toughness.</b> A single hit of less than 100 damage from anything below the raid tier does nothing. <b>Weighted Clothes.</b> His first Bonus Action in a fight takes off the turban and mantle (AC 21). <b>Regeneration.</b> He regains 50 HP at the start of each of his turns. <b>Regrowth</b> (3 a day, Bonus Action): he regains 200 HP and regrows a lost limb. At the Budokai he tore off his own arm mid-fight and grew it back on the spot (chapter 189); the arm Raditz blew off came back without a fuss in chapter 205. <b>Kami's Other Half.</b> If he dies, Kami dies, and the Dragon Balls with him. <b>Flight</b>, <b>Zanzōken</b>, and the techniques he showed at the 23rd Budokai and won't use here: the giant form, antenna lightning, the stretching arms.", stat),
 sec("Actions"),
 P("<b>Multiattack.</b> A barrage of five ki blasts, +24, range 300 ft, 10d10+15 force (the barrages of hand blasts he threw at Goku, chapter 183). <b>Mouth Blast</b> (Recharge 5–6): a beam through up to three creatures, 30d10 force, Dex DC 32 for half (the shot that went through Goku's shoulder at the Budokai). <b>Makankōsappō</b> (the Special Beam Cannon): an action to charge, two fingers to his forehead, holding it with concentration (a hit means a Con save, DC 10 or half the damage, up to 30); on his next turn an action fires it: +24, 60d10 piercing, a critical hit on 19–20, and it ignores resistance, immunity and damage thresholds. <b>The Moon</b> (once): an action destroys it. Anything that needs it, a Saiyan's Great Ape or the Infinite Tsukuyomi, is done.", stat),
 sec("Legendary Actions (3 a round)"),
 P("<b>Eye Beam.</b> +24, 6d10 fire (the beams that cancelled Kuririn's blasts in chapter 172).", stat)]))

S.append(PageBreak()); S.append(P("The feats, checked", h2)); S.append(rule())
def snap(name, where, checked):
    content = [P(name, snapname), P(where, stattag), P("<b>The feat, checked.</b> " + checked, snapline)]
    t = Table([[content]], colWidths=[W]); t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),PARCH),("LINEBEFORE",(0,0),(0,-1),2.5,GREEN),("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)]))
    return KeepTogether([t, Spacer(1,7)])
S.append(snap("Born of the Demon King", "chapter 161, then the 23rd Tenkaichi Budokai, chapters 162–194 · three years old", "Demon King Piccolo spits out one last egg as Goku goes through him. Three years later 'Ma Junior' takes Kami's own Mafūba, reverses it and swallows the bottle with Kami inside. In the final against Goku he destroys distant mountains with a blast, goes giant, tears off and regrows an arm his own homing blast hit, turns all of Papaya Island into a wasteland with one shockwave, and puts a mouth blast through Goku's shoulder. He loses on a ring-out, to a headbutt. That's the top of the ladder already; the moon is still five years away."))
S.append(snap("Raditz", "chapters 195–204 · eight years old", "Raditz walks through his shockwave at 322 and calls him no match. Allied with Goku, weights off, he reads 408; Raditz blows his left arm off with one blast of two. He charges the Makankōsappō while Goku stalls (1,020, 1,030, then 1,330), and the first shot misses: Raditz is too fast, and only his shoulder gets clipped. The second goes through Raditz and through Goku, who's holding him in a full nelson, because the Dragon Balls can bring Goku back. In the arena the same thing is true: against a raid boss nobody holds still, the beam breaks before it fires."))
S.append(snap("The moon", "chapters 205–208", "He regrows the arm in front of Kame-Sennin, Kuririn and Bulma, takes the unconscious Gohan, throws him at a mountain (which Gohan destroys), and leaves him alone in the wild. One night the full moon comes up and Gohan becomes a Great Ape; Piccolo remembers what Raditz said and destroys the moon, then pulls off the tail and makes the boy a sword and a gi with the kanji for 'demon' on it. That's the feat that puts him in this tier."))

S.append(P("In the arena", h2)); S.append(rule())
S.append(bullets([
 "<b>Against the ladder</b> he wins every one-on-one, Link included: the beam goes through Nayru's Love. Against all sixteen at once the ladder wins about half the time (Night Guy, the BFG, a lucky Crucible), and the rest are draws: in a crowd he never gets the quiet turn the beam needs, so Link outlasts him.",
 "<b>Against Madara</b>, raid against raid with both at their strongest (the Ten-Tails jinchūriki from the first turn: his revival was Black Zetsu's doing, not his own), Piccolo wins about one fight in four over 2,000. He blows up the moon on his first action every time, which kills the Infinite Tsukuyomi before it can rise. What beats him the other three times is Madara being a step above him: Dex 40 and Con 44 to his 30 and 40, Limbo's shadows that he can't touch, and a Truth-Seeking Ball that eats one blast a round. When the beam gets a quiet turn, it decides the fight."]))
S.append(KeepTogether([P("A DM's dial", h2), rule(), P("The Makankōsappō is the knob. At a table, let him charge it as a reaction-free bonus action over two turns instead of an action, and it becomes the threat it was against Raditz. And let the moon matter: a party that knows Piccolo can take it off the sky has an answer to anything that needs it.")]))
doc.build(S, onFirstPage=on_page, onLaterPages=on_page); print("ok")
