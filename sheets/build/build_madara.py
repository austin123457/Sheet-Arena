exec(open('sheet_style.py', encoding='utf-8').read())
GREEN = colors.HexColor("#5a1630")
h2 = ParagraphStyle("h2", fontName="DVSerif-B", fontSize=12.5, leading=16, textColor=GREEN, spaceBefore=11, spaceAfter=3)
hb_name = ParagraphStyle("hn", fontName="DVS-B", fontSize=9.6, leading=12.6, textColor=GREEN, spaceBefore=5, spaceAfter=1)
abil_head = ParagraphStyle("ah", parent=cell, fontName="DVS-B", alignment=TA_CENTER, textColor=GREEN)
def on_page(c, doc):
    c.saveState(); c.setFont("DVS", 7.8); c.setFillColor(MUTED)
    c.drawString(doc.leftMargin, 0.42*inch, "Madara Uchiha  ·  raid boss for D&D 5th Edition (2024 rules; a homebrew CR 30 monster in two phases)")
    c.drawRightString(letter[0]-doc.rightMargin, 0.42*inch, f"page {doc.page}"); c.restoreState()
doc = SimpleDocTemplate("../pdf/Madara_Uchiha_Raid.pdf", pagesize=letter, leftMargin=0.6*inch, rightMargin=0.6*inch, topMargin=0.6*inch, bottomMargin=0.7*inch, title="Madara Uchiha — D&D 5e Raid Boss", author="Claude")
W = letter[0] - 1.2*inch; S = []

def statblock(rows):
    box = Table([[f] for f in rows], colWidths=[W]); box.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),PARCH),("BOX",(0,0),(-1,-1),1.0,GREEN),("LEFTPADDING",(0,0),(-1,-1),11),("RIGHTPADDING",(0,0),(-1,-1),11),("TOPPADDING",(0,0),(-1,-1),1),("BOTTOMPADDING",(0,0),(-1,-1),1),("TOPPADDING",(0,0),(-1,0),9),("BOTTOMPADDING",(0,-1),(-1,-1),9)]))
    return box
sec = lambda t: P(t, ParagraphStyle("sec", parent=stat, fontName="DVSerif-B", fontSize=10.5, textColor=GREEN, spaceBefore=4, spaceAfter=2))

S.append(P("Madara Uchiha", title))
S.append(P("Raid boss · Human (Uchiha), the Edo Tensei and then the Ten-Tails jinchūriki · CR 30, two phases · the man who founded Konoha, fought Hashirama for a lifetime, beat the Five Kage alone, and put the whole world to sleep under the moon", subtitle))
S.append(HRFlowable(width="100%", thickness=1.4, color=GREEN, spaceBefore=4, spaceAfter=8))
S.append(P("Built from the manga, chapter by chapter (the anime only where it agrees). This is not a character sheet like the others in the set: it's a monster, sized for a party, the first entry in the <b>raid tier</b>. The ladder is human peak to god-killer; the raid tier is everything above it up to the moon. Ten-Tails Madara fought on even terms with Six Paths Naruto and Sasuke, and <i>The Last</i> has that Naruto face-tank a beam that splits the moon, which puts this Madara at the top of the tier. The other raid bosses this sheet is sized against are the moon-level fighters of Dragon Ball's Raditz saga: Roshi blew up the moon, and Yamcha by then is stronger than Roshi was."))
S.append(P("<b>Design calls.</b> Two phases, because the story has two Madaras. <b>Phase 1</b> is the Edo Tensei body Kabuto raised for the Fourth War: reanimated, regrowing from anything, unkillable by damage, and ended only by a seal. <b>Phase 2</b> is Madara revived and made the Ten-Tails jinchūriki: immune to ninjutsu, so only taijutsu, senjutsu and Six Paths chakra touch him, which in 5e is a damage threshold and immunity to spells. His win condition isn't damage at all. It's the Infinite Tsukuyomi, and the only shelter the manga shows is a Rinnegan user's Susanoo over his friends."))

S.append(P("Phase 1: the Edo Tensei (Fourth War, chapters 560–591)", h2)); S.append(rule())
S.append(statblock([P("Madara Uchiha, Reanimated", statname),
 P("Medium Humanoid (Human, Uchiha), reanimated by Edo Tensei in his prime with Hashirama's cells and both Rinnegan · 179 cm, the red armor, the gunbai and the kama on its chain", stattag),
 P("<b>AC</b> 22, 25 in Perfect Susanoo · <b>HP</b> 700 · <b>Speed</b> 40 ft · <b>Initiative</b> +7 with advantage · <b>CR</b> 30 (proficiency +9) · <b>Legendary Resistance</b> 3 a day", stat),
 abil_table(["20 (+5)","20 (+5)","22 (+6)","20 (+5)","20 (+5)","22 (+6)"], W-24), Spacer(1,4),
 P("<b>Saves</b> Dex +14, Con +15, Int +14, Wis +14; advantage against illusions and charm (Sharingan) · <b>Senses</b> the Sharingan and Rinnegan: he sees chakra, reads every feint, and tells a clone from the real one · <b>Languages</b> the speech of the Land of Fire", stat),
 sec("Traits"),
 P("<b>Reanimated Body.</b> He regains 50 HP at the start of each of his turns and doesn't tire. At 0 HP, or if a genjutsu or anything else would take him out of the fight, the body is pinned instead, and Phase 2 begins. Only a <b>seal</b> ends Phase 1 for good: Itachi's Sword of Totsuka (a hit, then a DC 19 Wisdom save, Legendary Resistance applies), the Dead Demon Consuming Seal, or a sealing team. <b>Perfect Susanoo.</b> Below half HP the full warrior stands up around him: AC 25 and the sword below.", stat),
 sec("Actions"),
 P("<b>Multiattack.</b> Three gunbai and kama strikes: +16, 3d10+9 bludgeoning or slashing. <b>Tengai Shinsei</b> (once): a meteor falls, and on his next turn a second falls onto the first; each deals 18d10 bludgeoning to every enemy, Dex DC 24 for half. <b>Great Fire Annihilation</b> (Recharge 5–6): a sea of fire, 14d10 to every enemy, Dex DC 24 for half. <b>Advent of a World of Flowering Trees</b> (once): pollen that gets through a Susanoo; every enemy makes a DC 24 Con save or falls asleep until it's hurt. <b>Susanoo's Sword</b> (Perfect Susanoo only): one cut through up to four enemies in a line, 12d10 force, Dex DC 24 for half.", stat),
 sec("Legendary Actions (3 a round, at the end of another creature's turn)"),
 P("<b>Gunbai.</b> One strike. <b>Wood Dragon</b> (costs 2): Str DC 24 or held (Disadvantage on its attacks until the end of its next turn), and the dragon drains 4d10 from it into him. <b>Uchiha Return</b> (Reaction, not a legendary action): the gunbai turns a ranged spell or chakra attack back on its caster.", stat)]))

S.append(PageBreak())
S.append(P("Phase 2: the Ten-Tails jinchūriki (chapters 663–677)", h2)); S.append(rule())
S.append(statblock([P("Madara Uchiha, Sage of the Six Paths", statname),
 P("Revived by Rinne Tensei and made the Ten-Tails' host · white hair, the Rinne Sharingan opening on his forehead, ten black orbs behind him, a shakujō of Truth-Seeking Ball in his hand", stattag),
 P("<b>AC</b> 24 · <b>HP</b> 900 (at the start of the phase, healed of everything) · <b>Speed</b> 40 ft, fly 80 ft · Legendary Resistance carries over", stat),
 sec("Traits"),
 P("<b>Six Paths Senjutsu.</b> Spells and quickhacks don't take: he succeeds on every save against a spell and isn't affected by its effects. Only taijutsu, senjutsu and Six Paths chakra hurt him, so any single source of damage under <b>100</b> does nothing (the Seventh Gate punch did nothing, and Daytime Tiger only pushed him back; Night Guy took the left half of his body). Nothing kills him outright. <b>Hashirama's Cells.</b> He regains 30 HP at the start of each of his turns, and a lost limb grows back.", stat),
 sec("Actions"),
 P("<b>Multiattack.</b> Three <b>Truth-Seeking Ball</b> strikes: +18, 4d10+9 force; they nullify what they touch, so they ignore resistance and immunity alike (Nayru's Love included). <b>Chibaku Tensei</b> (Recharge 5–6): satellites dropped like meteors, 18d10 bludgeoning to every enemy, Dex DC 25 for half, and held on a failure. <b>Infinite Tsukuyomi</b> (the start of his fourth turn in Phase 2): the Rinne Sharingan reflects off the moon, and every creature it shines on falls into the dream and out of the fight, with no save. A Rinnegan user is immune, and a creature with a Susanoo up can shelter itself and two others under it, as Sasuke did for Team 7.", stat),
 sec("Legendary Actions (3 a round)"),
 P("<b>Limbo: Border Jail.</b> One of his invisible shadows strikes: +18 with Advantage, 3d10+9 bludgeoning. Only a Rinnegan sees the shadows; Six Paths senjutsu can touch them.", stat)]))

S.append(P("What stops him, and what's on the ladder that can", h2)); S.append(rule())
S.append(bullets([
 "<b>A seal, in Phase 1.</b> Itachi's Totsuka is canon's answer to an Edo body (it sealed Nagato), and Itachi is on the ladder. The catch is the same one the Five Kage hit: Madara has three Legendary Resistances and a +14 Wisdom save, and the sword needs a Susanoo first.",
 "<b>Night Guy.</b> The one ladder move that tore this Madara apart in canon (chapter 672). On Guy's sheet it's 60d12+15, which clears the threshold by a mile; it isn't enough to finish 900 HP that regrow.",
 "<b>Shelter from the moon.</b> Itachi's Susanoo, up when the moon rises, keeps him and two others out of the dream.",
 "<b>Six Paths power</b>, which nobody on the ladder has: that's what cut him in half and sealed his shadows. The raid tier is where it lives."]))

S.append(P("His life, with the feats checked", h2)); S.append(rule())
def snap(name, where, lines, checked):
    content = [P(name, snapname), P(where, stattag)] + [P(l, snapline) for l in lines] + [P("<b>The feat, checked.</b> " + checked, snapline)]
    t = Table([[content]], colWidths=[W]); t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),PARCH),("LINEBEFORE",(0,0),(0,-1),2.5,GREEN),("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)]))
    return KeepTogether([t, Spacer(1,7)])
S.append(snap("The clan wars", "chapters 622–625 · as a ladder character he'd be level 15 to 20", ["The Sharingan when he ends the friendship at the river; the first Mangekyō anyone knew of; Izuna's eyes and the Eternal Mangekyō"], "He fights Hashirama for a lifetime and once for twenty-four hours straight. With the Eternal Mangekyō he still loses, and stops Hashirama from killing himself for the truce. He names the village. This is a ladder-tier Madara: a level 20 Uchiha with a Susanoo, strong enough to bully a young Ōnoki and Mū into line, nowhere near a moon."))
S.append(snap("The Valley of the End", "chapters 399, 621, 626", ["Kurama under his Sharingan, wrapped in Susanoo"], "He loses. Hashirama's thousand hands break the Susanoo-clad Kurama, Madara 'wins' against a wood clone, and the real Hashirama runs him through. He lives only because of an Izanagi he'd set in advance, which costs him his right eye, and a bite of Hashirama's flesh grafted into the wound. Decades later the Rinnegan opens and he lives on the Demonic Statue. He saves Obito, arranges Rin's death, and dies telling the boy to be Madara."))
S.append(snap("Edo Tensei: the Fourth Division and the Five Kage", "chapters 559–591 · Phase 1", ["The Phase 1 stat block"], "Two meteors: Gaara and Ōnoki stop the first, and he drops the second on it and wipes out most of the Fourth Division (the blast destroys his own body too, which grows back). Then the Five Kage. They crack the ribcage, lighten A through Susanoo, erase all twenty-five wood clones with Dust Release, and pin him for sealing once; he answers with the Perfect Susanoo, one swing through a mountain range, and leaves Tsunade cut in half and the rest critical. That's Phase 1 doing what it's built to do: a party that hurts him a lot and can't finish him without a seal."))
S.append(snap("The jinchūriki", "chapters 656–677 · Phase 2", ["The Phase 2 stat block"], "Revived, he breaks Hashirama's Gate of the Great God, absorbs his senjutsu and fights blind in Sage Mode; then the statue's chains take all nine beasts and he seals the Ten-Tails into himself. Guy's Seventh Gate punch does nothing. Evening Elephant knocks him into a crater and he enjoys it. Night Guy takes the left side of his upper body, and he calls Guy the strongest taijutsu fighter he has faced. Naruto and Sasuke with the Sage's power solve Limbo, seal a shadow, cut him in half, and he still reaches the moon. The Infinite Tsukuyomi takes everyone but the dead and Team 7 under Sasuke's Susanoo."))
S.append(snap("The end", "chapters 678–691", ["Black Zetsu's knife"], "He doesn't lose the raid; he loses the plot. Black Zetsu stabs him for Kaguya's sake, Kaguya is reborn out of his body, and when she's sealed he's thrown out of it, the beasts gone and his life with them. He dies talking with Hashirama, admitting the other man's dream outlived his own, mid-sentence."))

S.append(P("In the arena", h2)); S.append(rule())
S.append(P("Against the whole ladder at once, all sixteen, he wins every time. The party's damage burns Phase 1 down in a round or two, too fast for Itachi to raise a Susanoo and swing the Totsuka, and nothing on the ladder can put 900 regrowing hit points behind a 100-point threshold on the ground before the moon rises on the fourth turn. Slower parties stall in Phase 1 (Link's immunity against an unkillable body is a forty-round draw), and Itachi's seal lands about one raid in a hundred. That's the honest answer to the question he was built for: he's the one who finally wins solo, and the ladder isn't the tier that beats him."))
S.append(KeepTogether([P("A DM's dial", h2), rule(), P("For a table instead of an arena: run the Infinite Tsukuyomi as a visible clock (a moon on the battlemap that rises a step each round) and let the players see the shelter rule coming. Drop the Phase 2 threshold to 50 for a level 20 party that has its own big hits, and give the Totsuka (or any sealing item) a way to bypass Legendary Resistance on a critical hit. Don't drop the seal from Phase 1: it's the one canon door, and finding it is the raid.")]))
doc.build(S, onFirstPage=on_page, onLaterPages=on_page); print("ok")
