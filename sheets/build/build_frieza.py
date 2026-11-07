exec(open('sheet_style.py', encoding='utf-8').read())
GREEN = colors.HexColor("#4b2a6b")
h2 = ParagraphStyle("h2", fontName="DVSerif-B", fontSize=12.5, leading=16, textColor=GREEN, spaceBefore=11, spaceAfter=3)
hb_name = ParagraphStyle("hn", fontName="DVS-B", fontSize=9.6, leading=12.6, textColor=GREEN, spaceBefore=5, spaceAfter=1)
abil_head = ParagraphStyle("ah", parent=cell, fontName="DVS-B", alignment=TA_CENTER, textColor=GREEN)
def on_page(c, doc):
    c.saveState(); c.setFont("DVS", 7.8); c.setFillColor(MUTED)
    c.drawString(doc.leftMargin, 0.42*inch, "Frieza  ·  cosmic division, D&D 5th Edition frame (2024 rules) with exponents; not run in the arena")
    c.drawRightString(letter[0]-doc.rightMargin, 0.42*inch, f"page {doc.page}"); c.restoreState()
doc = SimpleDocTemplate("../pdf/Frieza_Cosmic.pdf", pagesize=letter, leftMargin=0.6*inch, rightMargin=0.6*inch, topMargin=0.6*inch, bottomMargin=0.7*inch, title="Frieza — D&D 5e, Cosmic Division", author="Claude")
W = letter[0] - 1.2*inch; S = []
E = lambda n: f"<sup>E{n}</sup>"
sec = lambda t: P(t, ParagraphStyle("sec", parent=stat, fontName="DVSerif-B", fontSize=10.5, textColor=GREEN, spaceBefore=4, spaceAfter=2))
def statblock(rows):
    box = Table([[f] for f in rows], colWidths=[W]); box.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),PARCH),("BOX",(0,0),(-1,-1),1.0,GREEN),("LEFTPADDING",(0,0),(-1,-1),11),("RIGHTPADDING",(0,0),(-1,-1),11),("TOPPADDING",(0,0),(-1,-1),1),("BOTTOMPADDING",(0,0),(-1,-1),1),("TOPPADDING",(0,0),(-1,0),9),("BOTTOMPADDING",(0,-1),(-1,-1),9)]))
    return box

S.append(P("Frieza", title))
S.append(P("Cosmic division · the emperor of the universe, every form from Planet Vegeta to Black Frieza · written in exponents · never run in the arena, because nothing on any sheet here is within two exponents of him", subtitle))
S.append(HRFlowable(width="100%", thickness=1.4, color=GREEN, spaceBefore=4, spaceAfter=8))
S.append(P("Built from the whole story as written: Toriyama's <i>Dragon Ball</i> manga (chapters 247–332), <i>Dragon Ball Minus</i>, the Toriyama-written films <i>Resurrection 'F'</i> (2015) and <i>Dragon Ball Super: Broly</i> (2018), and Toyotarō's <i>Dragon Ball Super</i> manga from Toriyama's outlines, through Black Frieza in chapter 87. Where the Super anime differs, the manga is primary. Power levels are the manga's and the Daizenshuu's; the 1990 Bardock special, Cooler, and the card-game numbers aren't canon and aren't here."))

S.append(P("Exponents: how a sheet like this works", h2)); S.append(rule())
S.append(P("Every creature has an <b>exponent</b>, its tier. Its Strength, Dexterity, Constitution, HP and damage are written in its own units, so two creatures of the same exponent play ordinary 5e against each other: Frieza and Super Saiyan Goku read like any two level-20 fighters. The mind isn't tiered (Intelligence, Wisdom and Charisma are just themselves). Across exponents, <b>damage converts: ×100 per exponent up, ÷100 per exponent down</b>, dice and all, so an E4 d10 is a d10×100 to an E3 body (call it a d1,000), and an E3 hit on an E4 body is a hundredth of itself, rounded down. The <b>d20 doesn't scale</b>, because it measures odds, not size: one exponent apart, the higher creature has advantage on attacks and saves against the lower, and the lower has disadvantage; two or more apart, the higher one always hits and always saves, and the lower one can't touch it. A technique can carry its own exponent (Night Guy is an E2 attack from an E1 body).", body))
S.append(grid([[P("Exponent", cellhead), P("Scale", cellhead), P("On these sheets", cellhead)]] + [[P(a, cellb), P(b, cell), P(c, cell)] for a, b, c in [
 ("E1", "city, mountain", "the ladder: Guy, the Slayer, Kratos, V; Edo Madara"),
 ("E2", "the moon", "Raditz-saga Piccolo (power level 408), Ten-Tails Madara"),
 ("E3", "a planet", "Frieza's first, second and third forms (530,000 to a few million)"),
 ("E4", "a big planet, shot through the core", "final-form Frieza at 50% and 100% (60 and 120 million), Super Saiyan Goku (150 million)"),
 ("E7", "gods (by the feats)", "Golden Frieza, level with Super Saiyan Blue Goku"),
 ("E11", "past the gods (by the feats)", "Black Frieza: one strike each for Ultra Instinct Goku and Ultra Ego Vegeta")]], [0.8*inch, 2.0*inch, W-2.8*inch]))
S.append(P("<b>How the exponents were set.</b> Where there are power levels, they set it: Raditz-saga Piccolo's 408 is the bottom of E2, and every ×100 of power level is one exponent, rounded down. That puts first-form Frieza at E3 and final form at E4, exactly the ×226 the numbers say between them, and it agrees with the feats: moon to planet is about ×1,800 in energy, and Piccolo to first-form Frieza is ×1,300 in power level. Super gives no power levels, so there the rule is the on-page relation: a fighter who can't touch another is two exponents under it. <b>Where I land</b> is on those feats, the same rule Madara's sheet uses (feats over statements and scaling chains): Golden Frieza about E7, Black Frieza about E11. <b>The statement reading</b> is the upper bound: the Elder Kai's line that Goku and Beerus clashing would shatter the universe (Super anime, episode 12) is a statement, not a feat, but taken at its word, universe-scale is about eighteen exponents past a planet, which would put Golden Frieza near E22 and Black Frieza near E26.", small))

S.append(P("Black Frieza (headline)", h2)); S.append(rule())
S.append(statblock([P("Frieza, Black", statname),
 P("Super manga chapter 87 · the form ten years in a time chamber on a conquered planet made · black and violet, the same small body (about 158 cm in final form) · “I'm the strongest in the universe now.”", stattag),
 P("<b>Exponent</b> 11 · <b>AC</b> 22 · <b>HP</b> 330" + E(11) + " · <b>Speed</b> 50 ft, fly 150 ft · <b>Initiative</b> +10 with advantage · proficiency +9 · <b>Legendary Resistance</b> 3 (not against another cosmic sheet) · <b>Legendary Actions</b> 3", stat),
 abil_table(["30 (+10)" + E(11), "30 (+10)" + E(11), "30 (+10)" + E(11), "20 (+5)", "14 (+2)", "22 (+6)"], W-24), Spacer(1,4),
 P("<b>Saves</b> Str +19, Dex +19, Con +19, Wis +11 · <b>Senses</b> he senses power the way every Dragon Ball fighter after the Namek arc does · <b>Languages</b> every tongue of the empire", stat),
 sec("Traits"),
 P("<b>Vacuum-Born.</b> He breathes nothing and survives space, and he lived through Namek exploding around him in pieces. <b>Forms.</b> He can show any earlier form (each is its own block, below) and goes Black as a Bonus Action. <b>The Emperor's Pride.</b> He toys with what he's sure he outclasses: he doesn't use The Strike until something has hurt him or until he's decided it's over, which is how Goku got a Spirit Bomb into him, and a Kamehameha into Golden Frieza. <b>Hard to Keep Dead.</b> He's come back from Hell twice (Sorbet's Dragon Ball wish; the Fortuneteller's 24 hours, then Whis's staff); that's story, not a combat trait.", stat),
 sec("Actions"),
 P("<b>Multiattack.</b> Three Death Beams (finger beams): +19, range 300 ft, 3d10+10" + E(11) + " piercing. <b>The Strike.</b> One blow, +19, 10d10+10" + E(11) + " bludgeoning: the hit that put down Ultra Instinct Goku and Ultra Ego Vegeta in chapter 87. <b>Telekinesis.</b> A creature he can see makes a Str save (DC 27) or he holds it, throws it 300 ft, or makes it explode from the inside (Krillin, chapter 317); two exponents down, there's no save. <b>Death Saucer</b> (Recharge 5–6): a homing disc, +19, 6d10" + E(11) + " slashing, a critical hit on 18–20 (one cut Frieza himself apart on Namek). <b>Death Ball</b> (once a fight): a planet killer; anything standing on the planet has until the end of its fifth turn to leave it (Namek, chapter 320).", stat),
 sec("Legendary Actions"),
 P("<b>Death Beam</b> (costs 1). <b>Afterimage</b> (costs 1): he moves 150 ft without provoking. <b>Telekinetic Shove</b> (costs 2): Str DC 27 or knocked 100 ft and Prone.", stat)]))

S.append(PageBreak())
S.append(P("Every form, on one table", h2)); S.append(rule())
S.append(P("Same-exponent numbers are ordinary 5e, so the forms inside an exponent read like a level-12 and a level-20 version of the same fighter; the jump between exponents is what the power levels do.", small))
forms = [("First form", "E3", "530,000 (his own words)", "22 / 24 / 22", "17", "180" + E(3), "+15, 2d10+6" + E(3), "Planet Vegeta; Namek until chapter 296"),
 ("Second form", "E3", "over 1,000,000 (ch. 296)", "26 / 24 / 24", "17", "210" + E(3), "+17, 2d10+8" + E(3), "the horns grow, Nail falls"),
 ("Third form", "E3", "no official number (ch. 302)", "28 / 24 / 26", "18", "240" + E(3), "+18, 3d10+9" + E(3), "Piccolo, fused with Nail, loses"),
 ("Final, 50%", "E4", "60,000,000 (Daizenshuu 7)", "22 / 28 / 22", "19", "200" + E(4), "+15, 2d10+6" + E(4), "Goku's Kaiō-ken ×20, the Spirit Bomb"),
 ("Final, 100%", "E4", "120,000,000 (Daizenshuu 7)", "28 / 30 / 26", "20", "300" + E(4), "+18, 2d10+9" + E(4), "Super Saiyan Goku (150 million) beats him"),
 ("Mecha Frieza", "E4", "no number", "28 / 28 / 28", "21", "300" + E(4), "+18, 2d10+9" + E(4), "Future Trunks cuts him in half (ch. 331)"),
 ("Golden", "E7", "no number", "28 / 28 / 26", "21", "300" + E(7), "+18, 3d10+9" + E(7), "even with Super Saiyan Blue Goku until the form burns him out"),
 ("Black", "E11", "no number", "30 / 30 / 30", "22", "330" + E(11), "+19, 3d10+10" + E(11), "one strike each for UI Goku and UE Vegeta")]
S.append(grid([[P(h, cellhead) for h in ("Form", "Exp.", "Power level", "Str / Dex / Con", "AC", "HP", "Death Beam", "Measured against")]] + [[P(a, cellb)] + [P(x, cell) for x in rest] for a, *rest in forms], [0.85*inch, 0.4*inch, 1.3*inch, 0.85*inch, 0.35*inch, 0.65*inch, 0.9*inch, W-5.3*inch]))

S.append(P("The conversion, in real numbers", h2)); S.append(rule())
S.append(bullets([
 "<b>Raditz-saga Piccolo's Special Beam Cannon</b> (12d10" + E(2) + ", about 66) on <b>first-form</b> Frieza (E3): 66 ÷ 100 = 0.66 of a point, which is nothing, and Piccolo rolls with disadvantage just to hit him. The beam that went through Raditz doesn't scratch the form that blew up Planet Vegeta.",
 "<b>Night Guy</b> (20d12" + E(2) + ", about 130), the biggest blow on the ladder, on <b>first-form</b> Frieza: a technique's exponent counts for the d20 too, so Guy lands it with disadvantage, and 130 ÷ 100 = 1.3, so 1 of his 180" + E(3) + ". On final form (E4): 0.013, nothing; and two exponents up, Guy can't land it at all.",
 "<b>Final-form Frieza's Death Beam</b> (2d10+9" + E(4) + ", about 20) on Raditz-saga Piccolo (E2): 20 × 100² = 200,000 in Piccolo's terms against his 270" + E(2) + ". On a ladder fighter (E1): 20 × 100³ = 20,000,000 against Kratos's 293.",
 "<b>Black Frieza's Strike</b> (10d10+10" + E(11) + ", about 65) on <b>final-form</b> Frieza (E4): 65 × 100⁷ = 6.5 quadrillion of final form's hit points. On anything in this arena (E1): 6.5 × 10²¹. That's the \"stupid huge math\", and it only happens when the exponents differ.",
 "<b>Against himself:</b> Golden Frieza (E7) and Black Frieza (E11) are four exponents apart, so his younger, golden self can't touch him either. The one thing the exponent math agrees with the manga on most cleanly is that Frieza's worst enemy keeps being last year's Frieza."]))

S.append(P("The story, with the feats checked", h2)); S.append(rule())
def snap(name, where, checked):
    content = [P(name, snapname), P(where, stattag), P("<b>The feat, checked.</b> " + checked, snapline)]
    t = Table([[content]], colWidths=[W]); t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),PARCH),("LINEBEFORE",(0,0),(0,-1),2.5,GREEN),("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)]))
    return KeepTogether([t, Spacer(1,7)])
S.append(snap("Planet Vegeta", "Dragon Ball Minus; Dragon Ball Super: Broly · first form, E3", "Afraid of a Super Saiyan uprising, he destroys the Saiyans' world with one Death Ball, through Bardock's last blast, about a month after Bardock and Gine send Kakarot away. A planet, from the form he calls holding back: E3, the bottom of the planet tier. (That Beerus ordered it is mainly the Super anime's version.)"))
S.append(snap("Namek", "chapters 247–328 · E3, then E4", "Every form, in order: 530,000 in the first; \"over a million\" in the second (chapter 296); the third (302); the final form (304). He shoots Vegeta through the chest (307–308), kills Dende, makes Krillin explode with telekinesis (317), takes the Spirit Bomb and gets up, and shoots Namek's core with five minutes on the clock (320). Super Saiyan Goku (150 million) beats his 100% (120 million): the same exponent, a bigger number, an ordinary fight, which is what the sheet says it should be. His own Death Saucer cuts him apart (326), Goku gives him energy, and he attacks anyway (327)."))
S.append(snap("Mecha Frieza and King Cold", "chapters 330–332 · E4", "Rebuilt with cybernetics, he lands on Earth with his father, and a boy with a sword cuts him in half before he finishes a sentence (331); Trunks kills King Cold next. Future Trunks as a Super Saiyan is at least Frieza's exponent; on this sheet it's an E4 fight he loses to a better sword. His cells go into Cell."))
S.append(snap("Resurrection 'F'", "the 2015 film, written by Toriyama · Golden, E7", "Sorbet and Tagoma wish him back; four months of the first training of his life give him Golden Frieza, who out-muscles Super Saiyan Blue Goku until the form burns his stamina away. He blows up the Earth with one blast (Whis shields a few and rewinds three minutes) and dies to a Kamehameha. A planet again, from a form three exponents past his Namek self by its fights: what he destroys on the page lags far behind who he's trading blows with, which is the whole feats-versus-statements argument in one film."))
S.append(snap("The Tournament of Power", "Super manga chapters 31–42 · Golden", "Revived for twenty-four hours to fight for Universe 7, he hides behind Jiren, has Goku pin him, and rams the three of them out of the ring so Android 17 wins (42); Whis restores him with his staff as Beerus's gift, and he promises to stay evil. In the Broly film (2018) he recruits Broly, kills Paragus to set him off, and gets beaten flat; Gogeta saves him."))
S.append(snap("Black Frieza", "Super manga chapter 87 · E11", "On Cereal he kills Gas and Elec, then puts Ultra Instinct Goku and Ultra Ego Vegeta on the ground with one strike each, says he trained ten years in a time chamber, and leaves: he came for someone else. Two of the strongest fighters in the story can't touch him, which by the exponent rule is two exponents and more; the sheet puts him at E11, four past Golden. The serial has been on hiatus since chapter 103, and he hasn't been back."))

S.append(KeepTogether([P("Why he isn't in the arena", h2), rule(), P("The highest exponent on any other sheet is E2. Black Frieza is nine exponents past that, which is past the point where anything rolls: he always hits, always saves, can't be touched, and converts every point of damage by 10¹⁸. Final-form Frieza at E4 would still be two exponents above Piccolo and Madara. The cosmic division needs company at E3 and E4 before it needs a fight: the Ginyu Force (about 120,000: E3), Namek-arc Goku, Cell, Buu. (Saiyan-saga Vegeta, at 18,000, is still E2: a raid boss, and a natural rival for Piccolo.) Frieza is the yardstick for that division, not a contestant in this one.")]))
doc.build(S, onFirstPage=on_page, onLaterPages=on_page); print("ok")
