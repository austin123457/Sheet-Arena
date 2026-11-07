from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, ListFlowable, ListItem, PageBreak
from reportlab.platypus.flowables import HRFlowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
FD = "/usr/share/fonts/truetype/dejavu/"
for n, f in [("DVS","DejaVuSansCondensed.ttf"),("DVS-B","DejaVuSansCondensed-Bold.ttf"),("DVS-I","DejaVuSansCondensed-Oblique.ttf"),("DVS-BI","DejaVuSansCondensed-BoldOblique.ttf"),("DVSerif-B","DejaVuSerif-Bold.ttf")]:
    pdfmetrics.registerFont(TTFont(n, FD + f))
pdfmetrics.registerFontFamily("DVS", normal="DVS", bold="DVS-B", italic="DVS-I", boldItalic="DVS-BI")
INK = colors.HexColor("#1b1b1b"); GREEN = colors.HexColor("#1f6b2f"); STEEL = colors.HexColor("#3f4a3f"); PARCH = colors.HexColor("#f1f4ec"); GRID = colors.HexColor("#c3c9bd"); MUTED = colors.HexColor("#67645f")
body = ParagraphStyle("b", fontName="DVS", fontSize=9.5, leading=13, textColor=INK, spaceAfter=5)
small = ParagraphStyle("s", parent=body, fontSize=8.6, leading=11.6)
cell = ParagraphStyle("c", parent=body, fontSize=8.2, leading=10.3, spaceAfter=0)
cellb = ParagraphStyle("cb", parent=cell, fontName="DVS-B"); cellhead = ParagraphStyle("ch", parent=cell, fontName="DVS-B", textColor=colors.white)
title = ParagraphStyle("t", fontName="DVSerif-B", fontSize=26, leading=30, textColor=INK, spaceAfter=2)
subtitle = ParagraphStyle("st", fontName="DVS", fontSize=10.5, leading=14, textColor=STEEL, spaceAfter=2)
h2 = ParagraphStyle("h2", fontName="DVSerif-B", fontSize=12.5, leading=16, textColor=GREEN, spaceBefore=11, spaceAfter=3)
stat = ParagraphStyle("stat", parent=body, fontSize=9.2, leading=12.4, spaceAfter=3)
statname = ParagraphStyle("sn", fontName="DVSerif-B", fontSize=13, leading=16, textColor=INK, spaceAfter=1)
snapname = ParagraphStyle("snn", fontName="DVSerif-B", fontSize=10.8, leading=13.5, textColor=INK, spaceAfter=1)
stattag = ParagraphStyle("tag", parent=small, fontName="DVS-I", textColor=MUTED, spaceAfter=5)
abil_head = ParagraphStyle("ah", parent=cell, fontName="DVS-B", alignment=TA_CENTER, textColor=GREEN)
abil_val = ParagraphStyle("av", parent=cell, fontSize=10, leading=12, alignment=TA_CENTER)
snapline = ParagraphStyle("sl", parent=stat, fontSize=8.9, leading=12, spaceAfter=2)
hb_name = ParagraphStyle("hn", fontName="DVS-B", fontSize=9.6, leading=12.6, textColor=GREEN, spaceBefore=5, spaceAfter=1)
hb_tag = ParagraphStyle("ht", parent=small, fontName="DVS-I", textColor=MUTED, spaceAfter=2)
P = lambda t, s=body: Paragraph(t, s)
rule = lambda: HRFlowable(width="100%", thickness=0.6, color=GRID, spaceBefore=0, spaceAfter=4)
def bullets(items):
    return ListFlowable([ListItem(Paragraph(t, stat), leftIndent=10, value="•") for t in items], bulletType="bullet", start="•", bulletFontName="DVS", bulletFontSize=8, leftIndent=12, bulletOffsetY=-1)
def abil_table(vals, width):
    t = Table([[P(a, abil_head) for a in ["STR","DEX","CON","INT","WIS","CHA"]],[P(v, abil_val) for v in vals]], colWidths=[width/6.0]*6)
    t.setStyle(TableStyle([("LINEABOVE",(0,0),(-1,0),0.6,GRID),("LINEBELOW",(0,1),(-1,1),0.6,GRID),("LINEBELOW",(0,0),(-1,0),0.3,GRID),("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
    return t
def grid(data, widths):
    t = Table(data, colWidths=widths, repeatRows=1)
    st = [("BACKGROUND",(0,0),(-1,0),STEEL),("VALIGN",(0,0),(-1,-1),"TOP"),("GRID",(0,0),(-1,-1),0.4,GRID),("TOPPADDING",(0,0),(-1,-1),2.6),("BOTTOMPADDING",(0,0),(-1,-1),2.6),("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5)]
    for i in range(1, len(data)):
        if i % 2 == 0: st.append(("BACKGROUND",(0,i),(-1,i),PARCH))
    t.setStyle(TableStyle(st)); return t
def on_page(c, doc):
    c.saveState(); c.setFont("DVS", 7.8); c.setFillColor(MUTED)
    c.drawString(doc.leftMargin, 0.42*inch, "Might Guy  ·  D&D 5th Edition build (2024 rules; the Eight Gates and his techniques are homebrew)")
    c.drawRightString(letter[0]-doc.rightMargin, 0.42*inch, f"page {doc.page}"); c.restoreState()
doc = SimpleDocTemplate("../pdf/Might_Guy_5e_Build.pdf", pagesize=letter, leftMargin=0.6*inch, rightMargin=0.6*inch, topMargin=0.6*inch, bottomMargin=0.7*inch, title="Might Guy — D&D 5e Build", author="Claude")
W = letter[0] - 1.2*inch
S = []
S.append(P("Might Guy", title))
S.append(P("Human · Monk (Warrior of the Open Hand) 20 · Soldier background · the Eight Gates as a feature, the techniques as cards", subtitle))
S.append(HRFlowable(width="100%", thickness=1.4, color=GREEN, spaceBefore=4, spaceAfter=8))
S.append(P("Built on the 2024 rules like the others. He is the only one of the set who is almost entirely a Player's Handbook class: Monk 20 already runs on walls and water, deflects anything, resists everything but force for a minute and hits five times a turn. What the book does not have is a man who can trade his body for the power to kill a god, so that is where the homebrew is: the Eight Gates, with a benefit and a bill at every gate, and the techniques each gate unlocks."))
S.append(P("<b>Design calls.</b> Dexterity and Wisdom are the stats, and Body and Mind at level 20 puts Dexterity at 25, which is the fastest thing on any of these sheets. No ninjutsu, no genjutsu: Intelligence 8 is the Academy entrance exam he failed. The Gates are numbered, cumulative, and cost hit points every turn they stay open from the fourth up; the Eighth kills him in ten rounds, no save, no exception, exactly as it did his father. His feats scale with the gates: Morning Peacock at six beat a Kisame clone, Daytime Tiger at seven beat the real one, and the Eighth nearly killed Madara with the Ten-Tails inside him."))
S.append(P("Snapshot: the Fourth War, level 20 (Monk 20), gates closed", h2)); S.append(rule())
block = [P("Might Guy", statname),
 P("Medium Humanoid (Human), age 31 · the green jumpsuit, the orange leg warmers, the flak jacket, the bowl cut · the lines in italics are what changes when the Gates open", stattag),
 P("<b>AC</b> 21 (Unarmored Defense) · <b>HP</b> 203 (20d8, Tough) · <b>Speed</b> 60 ft, and walls and water count as ground · <b>Initiative</b> +7 · <b>Proficiency</b> +6 · <b>Focus Points</b> 20 (back to 4 at every initiative roll)", stat),
 abil_table(["12 (+1)","25 (+7)","16 (+3)","8 (−1)","18 (+4)","8 (−1)"], W-24), Spacer(1,4),
 P("<b>Saves</b> all six, Disciplined Survivor: Str +7, Dex +13, Con +9, Int +5, Wis +10, Cha +5; one Focus Point rerolls a failed save · <b>Skills</b> Athletics +13 (expertise, Skill Expert), Acrobatics +13, Perception +10, Insight +10, Intimidation +5, Survival +10 · <b>Save DC</b> 18", stat),
 P("<b>Defenses.</b> Deflect Attacks: a reaction takes 1d10+27 off any attack that hits him, and if that empties it he can spend a Focus Point to throw it back (Dex save DC 18, 2d12+7). Evasion. Superior Defense: 3 Focus for resistance to everything but force for a minute. Self-Restoration ends charm, fear and poison on his own turn. <b>Watch the feet:</b> he fights Sharingan users by looking at their feet, so anything that needs him to meet an eye (Tsukuyomi, eye-contact genjutsu) simply does not reach him.", stat),
 P("<b>Attacks.</b> Unarmed strike +13, 1d12+7 bludgeoning, magical. Two per Attack action; Flurry of Blows (1 Focus, bonus action) adds three, each able to Topple (Dex DC 18 or prone), Push (15 ft) or Addle (no reactions). Stunning Strike once a turn (1 Focus): Con DC 18 or Stunned until his next turn; on a success its speed is halved and his next hit has advantage. Quivering Palm (4 Focus): touch, then at any point in the next minute, Con DC 18 or 10d12 force. Soshuga, his nunchaku: a quarterstaff, +13, 1d12+7 with Topple.", stat),
 P("<b>Feats</b> Savage Attacker, Tough, Charger, Grappler, Athlete, Speedy, Boon of Speed · <b>Other</b> Wholeness of Body (4 a day, 2d12+4), Acrobatic Movement, Fleet Step, Step of the Wind, Patient Defense, Perfect Focus, Summoning (Ningame, once a day).", stat),
 P("<i><b>Gates open.</b> Sixth Gate: +2 to hit, +2 AC, seven strikes a turn with Flurry, every strike +2d12 force, Morning Peacock, and 2d10 off his own hit points every turn. Seventh: +4 to hit, +3d12 force, attacks against him have disadvantage, Daytime Tiger, 3d10 a turn. Eighth: +5 to hit, +6d12 force, immune to Stunned, Paralyzed, Frightened, Charmed and Grappled, nothing can take him below 1 HP, Evening Elephant and Night Guy, and he dies at the end of his tenth turn or the turn after Night Guy, whichever comes first.</i>", stat),
 P("<b>How he fights.</b> Dynamic Entry (Charger) into Flurry, Topple on the first hit that lands and Stunning Strike on the second. Deflect the one hit a round that matters. Against anyone who is actually dangerous he opens to the Sixth on the first turn and the Seventh on the second, and takes the bill. The Eighth is not a tactic. It is the day he decided to die.", stat)]
box = Table([[f] for f in block], colWidths=[W]); box.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),PARCH),("BOX",(0,0),(-1,-1),1.0,GREEN),("LEFTPADDING",(0,0),(-1,-1),11),("RIGHTPADDING",(0,0),(-1,-1),11),("TOPPADDING",(0,0),(-1,-1),1),("BOTTOMPADDING",(0,0),(-1,-1),1),("TOPPADDING",(0,0),(-1,0),9),("BOTTOMPADDING",(0,-1),(-1,-1),9)])); S.append(box)
S.append(P("The Eight Gates", h2)); S.append(rule())
S.append(P("Homebrew feature. He can open gates on his turn without an action, up to three per turn, in order; a gate stays open until he closes it (no action) or the fight ends. Benefits are cumulative. The bill is paid at the start of each of his turns while the gate is open and cannot be reduced by anything, and the exhaustion lands when the gates close. Save DC 18.", small))
gates = [("1 · Opening", "Speed +10 ft; advantage on Strength and Dexterity checks; Front Lotus.", "After the fight: 1 level of exhaustion."),
 ("2 · Healing", "Regains 20 HP when it opens; while open he ignores the effects of exhaustion.", "None."),
 ("3 · Life", "Unarmed strikes +1d12 force; Reverse Lotus.", "After the fight: 2 levels of exhaustion total."),
 ("4 · Pain", "One extra unarmed strike per Attack action; speed +20 ft total.", "1d10 a turn while open."),
 ("5 · Limit", "+2 to attack rolls; +2 AC.", "1d10 a turn; 3 levels of exhaustion after."),
 ("6 · View", "Unarmed strikes +2d12 force total; Morning Peacock.", "2d10 a turn; after the fight he cannot move for 1d4 hours."),
 ("7 · Wonder", "+4 to attack rolls total; attacks against him have disadvantage; +3d12 force; Daytime Tiger.", "3d10 a turn, 4d10 more each Daytime Tiger; 5 levels of exhaustion after; a limb is lamed until a long rest."),
 ("8 · Death", "+5 to attack rolls; +6d12 force; immune to Stunned, Paralyzed, Frightened, Charmed and Grappled; speed 300 ft; damage cannot reduce him below 1 HP; Evening Elephant and Night Guy.", "He dies at the end of his tenth turn, or at the end of the turn after Night Guy. No save. Only a power on the level of the Six Paths can stop it.")]
S.append(grid([[P("Gate", cellhead), P("What opens", cellhead), P("What it costs", cellhead)]] + [[P(a, cellb), P(b, cell), P(c, cell)] for a, b, c in gates], [0.95*inch, 3.45*inch, W-4.4*inch]))
S.append(P("Techniques", h2)); S.append(rule())
techs = [("Dynamic Entry", "no gate · Charger, reflavoured", "After moving 10 ft in a straight line, his first kick deals +1d8 or shoves 10 ft. He shouts the name."),
 ("Leaf Hurricane · Severe Leaf Hurricane", "no gate · Flurry of Blows with Topple; the Severe version costs 1 Focus", "The spinning kicks are Flurry with Topple on every hit. Severe: instead of the Flurry, every creature within 5 ft makes a Dex save DC 18 or takes 2d12+7 and falls prone."),
 ("Front Lotus", "First Gate · 1 Focus, needs a hit with Grappler's Punch and Grab", "He carries the grappled creature 20 ft into the air and drives it into the ground: 4d12+7 bludgeoning, the target lands prone, and he takes 1d10 himself."),
 ("Reverse Lotus", "Third Gate · 1 Focus", "A kick into the air, a flurry while it falls, and a strike that meets it at the ground: three unarmed strikes against one creature, the last with advantage, and if the last hits, +6d12 and prone. He takes 2d10."),
 ("Morning Peacock", "Sixth Gate · action, replacing the Attack action · 2d10 to himself", "Six unarmed strikes against one creature so fast the air ignites: each deals +2d6 fire on top of everything else. The target cannot take reactions until his turn ends. Flurry of Blows still works on the same turn."),
 ("Daytime Tiger", "Seventh Gate · action · 4d10 to himself", "A single punch that compresses the air into a tiger and sends it at one creature within 60 ft. Con save DC 18: 20d10 force, pushed 60 ft and knocked prone on a failure, half damage on a success. It is air, not chakra, so nothing that eats chakra (Samehada) can eat it."),
 ("Evening Elephant", "Eighth Gate · action", "Five blows of air pressure, each a step faster and heavier than the last, against one creature within 60 ft: five unarmed strikes at +18 with advantage, dealing 4d12, 8d12, 12d12, 16d12 and 20d12 force. Reactions can halve a blow; nothing can negate one."),
 ("Night Guy", "Eighth Gate · action · once, ever", "The kick that bends space. One creature within 120 ft makes a Con save DC 25, taking 30d12 force on a failure or half on a success; no reaction, feature or spell can reduce or negate it, and the target is hurled 300 ft. His leg is destroyed, he drops to 1 HP, and he dies at the end of his next turn."),
 ("Summoning: Ningame", "once a day · action", "Ningame the tortoise: Huge beast, AC 20, 120 HP, bite +9 for 2d10+5, swim 40 ft; he can carry Guy and give him total cover inside the shell, and he complains the whole time."),
 ("Springtime of Youth", "bonus action · once a short rest", "A speech. Allies within 30 ft who can hear him gain 10 temporary hit points and advantage on their next saving throw against being Frightened. Enemies may make a DC 10 Wisdom save to avoid being annoyed.")]
for name, tag, text in techs:
    S.append(KeepTogether([P(name, hb_name), P(tag, hb_tag), P(text, small)]))
S.append(P("Build, level by level", h2)); S.append(rule())
S.append(P("Point buy 12 / 15 / 14 / 8 / 14 / 8, Soldier +2 Dex +1 Con: Str 12, Dex 17, Con 15, Int 8, Wis 14, Cha 8. Five General feats, two Origin, an Epic Boon. Body and Mind at 20 adds +4 Dexterity and Wisdom.", small))
rows = [("1","Monk 1","Martial Arts, Unarmored Defense. Savage Attacker (Soldier), Tough (Human).","Might Duy's son. Fails the Academy entrance exam."),
 ("2","Monk 2","Monk's Focus (Flurry, Patient Defense, Step of the Wind), Unarmored Movement, Uncanny Metabolism.","Admitted on a second try. Duy starts him on the Gates."),
 ("3","Monk 3","Open Hand Technique, Deflect Attacks. First and Second Gates.","Age 7: the Seven Swordsmen. Duy opens the Eighth and dies in front of him."),
 ("4","Monk 4","Charger (+1 Dex → 18): Dynamic Entry. Slow Fall. Third Gate.","The rivalry with Kakashi begins."),
 ("5","Monk 5","Extra Attack, Stunning Strike.","Chunin exams. Loses to Kakashi; keeps the score anyway."),
 ("6","Monk 6","Empowered Strikes, Wholeness of Body.","Jonin at 20."),
 ("7","Monk 7","Evasion. Fourth Gate.","Team Guy: Lee, Neji, Tenten."),
 ("8","Monk 8","Grappler (+1 Dex → 19): Front Lotus. Fifth Gate.","Teaches Lee the Lotus, and swears he will never let him die for it."),
 ("9","Monk 9","Acrobatic Movement.","Part I, the Chunin exams: stops Gaara from killing Lee."),
 ("10","Monk 10","Heightened Focus (Flurry is three strikes), Self-Restoration.","Part I: Dynamic Entry on Kisame; saves Kakashi from Itachi by watching his feet."),
 ("11","Monk 11","Fleet Step.","Part II, Kazekage Rescue: Sixth Gate, Morning Peacock, Kisame's clone."),
 ("12","Monk 12","Athlete (+1 Dex → 20).","Kakashi and Guy, 50–49."),
 ("13","Monk 13","Deflect Energy.","Island Turtle: Seventh Gate, Daytime Tiger, the real Kisame."),
 ("14","Monk 14","Disciplined Survivor.","The Fourth War begins."),
 ("15","Monk 15","Perfect Focus.","The Ten-Tails."),
 ("16","Monk 16","Speedy (+1 Con → 16).","Kakashi, Obito, the fight for the Ten-Tails jinchuriki."),
 ("17","Monk 17","Quivering Palm. Martial Arts die d12.","Madara, resurrected, alone against the Allied Forces."),
 ("18","Monk 18","Superior Defense.","Eighth Gate."),
 ("19","Monk 19","Boon of Speed (+1 Dex → 21).","Evening Elephant. Night Guy."),
 ("20","Monk 20","Body and Mind (Dex 25, Wis 18).","Naruto brings him back. One leg, a wheelchair, and Lee's boy to teach.")]
S.append(grid([[P("Lvl", cellhead), P("Class", cellhead), P("What you get", cellhead), P("Where in the story", cellhead)]] + [[P(a, cellb), P(b, cell), P(c, cell), P(d_, cell)] for a, b, c, d_ in rows], [0.4*inch, 0.75*inch, 3.5*inch, W-4.65*inch]))
S.append(PageBreak()); S.append(P("Snapshots by arc, with the feat checked", h2)); S.append(rule())
def snap(name, where, lvl, lines, checked):
    content = [P(name, snapname), P(where + "  ·  " + lvl, stattag)] + [P(l, snapline) for l in lines] + [P("<b>The feat, checked.</b> " + checked, snapline)]
    t = Table([[content]], colWidths=[W]); t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),PARCH),("LINEBEFORE",(0,0),(0,-1),2.5,GREEN),("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)]))
    return KeepTogether([t, Spacer(1,7)])
S.append(snap("Duy's son", "Part II flashbacks (the story of Might Duy) · ages 7 to 11", "Levels 1–4 · Monk 1–4", ["Str 12, Dex 17, Con 15, Int 8, Wis 14, Cha 8 · <b>AC</b> 15 · <b>HP</b> 10 → 42 · unarmed +5, 1d6+3 · Flurry · Deflect Attacks · the first three Gates"], "A boy who fails the entrance exam because he cannot mould chakra, and whose father, the Eternal Genin, opens the Eighth Gate against the Seven Swordsmen so his son's team can live. Guy learns the Gates from a man who used them once. The sheet gives him three of them by level 3 and the rule that the Eighth is a death, because he watched it be one."))
S.append(snap("The rival", "Part I; Kakashi Gaiden · ages 11 to 20", "Levels 5–8 · Monk 5–8", ["<b>HP</b> 54 → 86 · Extra Attack, Stunning Strike · Charger (Dynamic Entry), Grappler (Front Lotus) · Fourth and Fifth Gates"], "He loses to Kakashi at the exams and starts counting. By jonin at twenty he has a Lotus that puts a man through the floor (4d12+7 off a Grappler hit) and five Gates, and a promise to Lee that the sheet keeps: the Lotus costs the user 1d10 every time."))
S.append(snap("Part I: Kisame, Itachi, Gaara", "Naruto, the Chunin exams and the Search for Tsunade · age 26", "Levels 9–10 · Monk 9–10", ["<b>AC</b> 20 · <b>HP</b> 110 · three-strike Flurry · Acrobatic Movement · Self-Restoration"], "Dynamic Entry puts Kisame (CR 22) across a hallway: a Charger hit for 1d12+5+1d8, and Kisame goes 10 ft because that is what the feat does. Then Itachi, with Kakashi down behind him: 'Watch the feet' means no Sharingan genjutsu reaches him, and Itachi, who has read the same sheet, leaves rather than find out what the rest of the kit does. Stopping Gaara's sand is Stunning Strike on a Con save of +4."))
S.append(snap("Part II: the Kisame clone", "Naruto Shippuden, the Kazekage Rescue · age 29", "Level 11 · Monk 11", ["<b>AC</b> 20 · <b>HP</b> 118 · Fleet Step · <b>Sixth Gate:</b> seven strikes a turn, +2d12 force on each, Morning Peacock, 2d10 a turn"], "A 30% Kisame, call it CR 12 with 110 hit points. Morning Peacock is six strikes at +12 with 2d6 fire on each, with Flurry on top: seven swings around 27 each, five or six landing, is 150 and the clone is ash in one turn. The bill is 2d10 and a day he cannot move."))
S.append(snap("Island Turtle: Daytime Tiger", "Naruto Shippuden, the Island Turtle · age 30", "Level 13 · Monk 13", ["<b>AC</b> 21 · <b>HP</b> 136 · Deflect Energy · <b>Seventh Gate:</b> +4 to hit, attacks against him have disadvantage, +3d12 force, Daytime Tiger"], "The real Kisame, CR 22, 300 hit points, and Samehada eats chakra. Daytime Tiger is air: a Con save at +10 against DC 18 passes on an 8, so about 65% of the time he takes 55 and 35% of the time he takes 110 and goes 60 feet. In the manga it landed clean, which is the 35%, and then the seven Gates' bill: 3d10 a turn, 4d10 for the Tiger, and Guy cannot stand afterward. Kisame survives it, barely, and takes his own life rather than be questioned. The sheet lets him survive it. The story did not let him keep what he survived with."))
S.append(snap("The Eighth Gate: Madara", "Naruto Shippuden, the Fourth War · age 31", "Levels 18–20 · Monk 18–20", ["<b>AC</b> 21 (25 at the Seventh) · <b>HP</b> 203 · Superior Defense · Dex 25 at 20 · <b>Eighth Gate:</b> +5 to hit, +6d12 force, untouchable, ten turns to live"], "Madara with the Ten-Tails in him is a CR 30 with 900 hit points, regeneration, and Truth-Seeking Orbs that erase anything they touch. Evening Elephant's five blows at +18 with advantage against AC 22 land four or five times for 60d12 of force, about 390: Madara's orbs cannot eat air, his chest caves, and he says out loud that this is the strongest taijutsu he has ever met. Night Guy is 30d12 with no reaction allowed: 195 on average into a Con save at +12 against DC 25, which Madara fails 60% of the time, and he fails it. That is 585 damage from one man who has never cast a spell, against a thing that was beating the Five Kage and the nine tailed beasts at once. Madara regenerates. Guy does not: 1 HP, the leg gone, the tenth turn coming. Naruto with the Six Paths in him is the one exception the Gate card names."))
S.append(P("Alternates", h2)); S.append(rule())
S.append(P("<b>Warrior of the Elements</b> is the wrong school and <b>Warrior of Shadow</b> the wrong man; Open Hand is correct. <b>Fighter 2 for Action Surge</b> (Monk 18 / Fighter 2) is the common power build; it costs Superior Defense, which is more him than a second action. <b>Barbarian 1</b> for Rage is tempting as a Gate and is not: the Gates are not anger. For a 2014 table, Way of the Open Hand is the same subclass, Deflect Missiles only covers ranged attacks, and the Gates and techniques carry over unchanged."))
doc.build(S, onFirstPage=on_page, onLaterPages=on_page); print("ok")
