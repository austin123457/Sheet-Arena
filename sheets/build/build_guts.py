from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                KeepTogether, ListFlowable, ListItem, PageBreak)
from reportlab.platypus.flowables import HRFlowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ---------- fonts ----------
FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DVS", FD + "DejaVuSansCondensed.ttf"))
pdfmetrics.registerFont(TTFont("DVS-B", FD + "DejaVuSansCondensed-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVS-I", FD + "DejaVuSansCondensed-Oblique.ttf"))
pdfmetrics.registerFont(TTFont("DVS-BI", FD + "DejaVuSansCondensed-BoldOblique.ttf"))
pdfmetrics.registerFontFamily("DVS", normal="DVS", bold="DVS-B", italic="DVS-I", boldItalic="DVS-BI")
pdfmetrics.registerFont(TTFont("DVSerif", FD + "DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("DVSerif-B", FD + "DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVSerif-I", FD + "DejaVuSerif-Italic.ttf"))
pdfmetrics.registerFont(TTFont("DVSerif-BI", FD + "DejaVuSerif-BoldItalic.ttf"))
pdfmetrics.registerFontFamily("DVSerif", normal="DVSerif", bold="DVSerif-B", italic="DVSerif-I", boldItalic="DVSerif-BI")

# ---------- palette (iron and dried blood) ----------
INK = colors.HexColor("#1b1a1a")
BLOOD = colors.HexColor("#6e1e1e")
STEEL = colors.HexColor("#3f4248")
PARCH = colors.HexColor("#f1efea")
GRID = colors.HexColor("#c4c1ba")
MUTED = colors.HexColor("#67645f")

# ---------- styles ----------
body = ParagraphStyle("body", fontName="DVS", fontSize=9.6, leading=13.2, textColor=INK, spaceAfter=5)
small = ParagraphStyle("small", parent=body, fontSize=8.6, leading=11.6)
cell = ParagraphStyle("cell", parent=body, fontSize=8.2, leading=10.2, spaceAfter=0)
cellb = ParagraphStyle("cellb", parent=cell, fontName="DVS-B")
cellhead = ParagraphStyle("cellhead", parent=cell, fontName="DVS-B", textColor=colors.white)
title = ParagraphStyle("title", fontName="DVSerif-B", fontSize=26, leading=30, textColor=INK, spaceAfter=2)
subtitle = ParagraphStyle("subtitle", fontName="DVS", fontSize=10.5, leading=14, textColor=STEEL, spaceAfter=2)
h2 = ParagraphStyle("h2", fontName="DVSerif-B", fontSize=12.5, leading=16, textColor=BLOOD, spaceBefore=11, spaceAfter=3)
stat = ParagraphStyle("stat", parent=body, fontSize=9.3, leading=12.6, spaceAfter=3)
statname = ParagraphStyle("statname", fontName="DVSerif-B", fontSize=13, leading=16, textColor=INK, spaceAfter=1)
snapname = ParagraphStyle("snapname", fontName="DVSerif-B", fontSize=10.8, leading=13.5, textColor=INK, spaceAfter=1)
stattag = ParagraphStyle("stattag", parent=small, fontName="DVS-I", textColor=MUTED, spaceAfter=5)
abil_head = ParagraphStyle("abil_head", parent=cell, fontName="DVS-B", alignment=TA_CENTER, textColor=BLOOD)
abil_val = ParagraphStyle("abil_val", parent=cell, fontSize=10, leading=12, alignment=TA_CENTER)
bullet_style = ParagraphStyle("bul", parent=stat, spaceAfter=1.5)
snapline = ParagraphStyle("snapline", parent=stat, fontSize=8.9, leading=12, spaceAfter=2)


def P(text, style=body):
    return Paragraph(text, style)


def rule():
    return HRFlowable(width="100%", thickness=0.6, color=GRID, spaceBefore=0, spaceAfter=4)


def bullets(items, style=bullet_style):
    return ListFlowable(
        [ListItem(Paragraph(t, style), leftIndent=10, value="•") for t in items],
        bulletType="bullet", start="•", bulletFontName="DVS", bulletFontSize=8,
        leftIndent=12, bulletOffsetY=-1,
    )


def abil_table(vals, width):
    t = Table(
        [[P(a, abil_head) for a in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]],
         [P(v, abil_val) for v in vals]],
        colWidths=[width / 6.0] * 6,
    )
    t.setStyle(TableStyle([
        ("LINEABOVE", (0, 0), (-1, 0), 0.6, GRID),
        ("LINEBELOW", (0, 1), (-1, 1), 0.6, GRID),
        ("LINEBELOW", (0, 0), (-1, 0), 0.3, GRID),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("DVS", 7.8)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 0.42 * inch,
                      "Guts  ·  D&D 5th Edition build (2024 rules; alternates and 2014 notes on the last page)")
    canvas.drawRightString(letter[0] - doc.rightMargin, 0.42 * inch, f"page {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(
    "../pdf/Guts_5e_Build.pdf", pagesize=letter,
    leftMargin=0.6 * inch, rightMargin=0.6 * inch, topMargin=0.6 * inch, bottomMargin=0.7 * inch,
    title="Guts — D&D 5e Build", author="Claude", subject="Character build",
)
W = letter[0] - doc.leftMargin - doc.rightMargin
story = []

# ---------- title ----------
story.append(P("Guts", title))
story.append(P("Human · Barbarian (Path of the Berserker) 12 / Fighter (Champion) 8 · Soldier background · the Black Swordsman", subtitle))
story.append(HRFlowable(width="100%", thickness=1.4, color=BLOOD, spaceBefore=4, spaceAfter=8))

story.append(P("Built on the 2024 rules, like the Goblin Slayer sheet. \u201cFeats\u201d here are the things he pulls off on the "
               "page; every snapshot ends by running its big one against the numbers."))
story.append(P("<b>Design calls.</b> Barbarian is the chassis because the defining fact about Guts is that he does not go down: "
               "Rage halves every blow, Reckless Attack is how he has fought since he was six, and Relentless Rage is "
               "\u201cI can't die yet.\u201d Fighter 8 is Gambino's training and the Hawks: Action Surge is the burst that cuts a "
               "horse and rider in half, Improved Critical is why his swings keep landing like that, Second Wind is him standing "
               "back up. The Beast of Darkness is the Berserker subclass; the Berserker Armor is an item that turns the dial past "
               "where the subclass stops. Strength goes to 20 and stays there. The superhuman part is a 4d6 slab of iron, the "
               "armor, and a 236-hit-point body with resistance to everything that hits it."))

# ---------- headline block: the Black Swordsman ----------
story.append(P("Snapshot: the Black Swordsman, level 14 (Barbarian 6 / Fighter 8)", h2))
story.append(rule())

block = [
    P("Guts, the Black Swordsman", statname),
    P("Medium Humanoid (Human) · Berserk volumes 1–3, two years after the Eclipse, the Guts most readers meet first · "
      "black armor and cloak, the Dragonslayer on his back, Rickert's iron arm, a repeating crossbow, a bag of knives and bombs",
      stattag),
    P("<b>AC</b> 17 (black half plate) · <b>HP</b> 164 (8d10 + 6d12) · <b>Speed</b> 40 ft · <b>Initiative</b> +2 with "
      "advantage · <b>Proficiency</b> +5", stat),
    abil_table(["20 (+5)", "14 (+2)", "16 (+3)", "8 (−1)", "12 (+1)", "8 (−1)"], W - 24),
    Spacer(1, 4),
    P("<b>Saves</b> Str +10, Con +8 (others by ability) · <b>Skills</b> Athletics +10 (advantage), Intimidation +4 (+10, "
      "Strength-based, while raging), Perception +6, Survival +6, Acrobatics +7, Animal Handling +6, Nature +4 · "
      "<b>Tools</b> dice · <b>Languages</b> Common, and nothing else", stat),
    P("<b>Feats</b> Great Weapon Fighting, Blind Fighting, Savage Attacker, Tough, Great Weapon Master, Slasher, Sentinel, "
      "Crossbow Expert · <b>Weapon Masteries</b> the Dragonslayer (Cleave), greatsword (Graze), dagger (Nick), light crossbow (Slow)",
      stat),
    P("<b>Lingering injuries</b> (DMG): right eye gone, so disadvantage on Perception checks that rely on sight and on ranged "
      "attacks; left forearm gone, replaced by the prosthetic. <b>Brand of Sacrifice:</b> see \u201cWhat he carries.\u201d", stat),
    Spacer(1, 2),
    P("<b>Attacks</b> (two per Attack action; Action Surge 1/short rest; numbers assume he is raging, because he is)", stat),
    bullets([
        "<b>The Dragonslayer (+1).</b> +11 to hit, 4d6+13 slashing (Str, Great Weapon Master's +5, Rage's +2, the blood on the "
        "blade); 1s and 2s on the dice count as 3; Savage Attacker rerolls the dice once a turn; Frenzy adds 2d6 to the first "
        "hit of the turn; a crit on 19–20, and after any crit or kill, Hew gives him a bonus-action swing. Cleave puts the "
        "same swing into a second creature next to the first. On a miss, Graze still does 5.",
        "<b>Reckless Attack.</b> Advantage on every Strength attack this turn; everything has advantage against him until his "
        "next. He has never once not used it.",
        "<b>Repeating crossbow</b> (bolted to the arm). +7, 1d8+2 piercing, range 80/320, no Loading, no disadvantage in melee: "
        "two bolts a round, four with Action Surge.",
        "<b>Arm cannon.</b> +7, 4d10 piercing and fire, range 20/60, one shot; reloading is an action. Fired into a face from "
        "a foot away, usually.",
        "<b>Iron hand.</b> +10, 1d6+7 bludgeoning (it counts as a mace). <b>Throwing knives.</b> +10, 1d4+7, range 20/60. "
        "<b>Bombs.</b> 3d6 fire in a 5-ft radius, Dex save DC 12 for half.",
        "<b>Sentinel.</b> A reaction swing at anything beside him that hits someone else, and nothing he hits with it moves.",
    ]),
    Spacer(1, 4),
    P("<b>Resources.</b> Rage ×4 (+2 damage, resistance to bludgeoning, piercing and slashing, advantage on Strength checks "
      "and saves), Mindless Rage (immune to Charmed and Frightened while raging), Danger Sense (advantage on Dex saves), "
      "Action Surge, Second Wind ×3 (1d10+8; Tactical Mind, Tactical Shift), Remarkable Athlete (half-speed move after a "
      "crit), Blindsight 10 ft, Heroic Inspiration every long rest.", stat),
    P("<b>How he fights.</b> Rage as a bonus action, Reckless Attack, walk into it. The first hit of the turn is the one with "
      "Frenzy on it, so it goes at the biggest thing in reach. Crits and kills chain into Hew; Cleave eats the thing standing "
      "next to the kill. The crossbow is for things that fly and things he cannot reach; the cannon is for the moment a "
      "monster's face is close enough to smell. He does not retreat, does not dodge, does not parry: Rage halves what lands "
      "and 164 hit points absorb the rest. When he stops raging he sits down, bleeds, and gets back up on Second Wind.", stat),
]
# one row per flowable so the box can split across the page break
statbox = Table([[f] for f in block], colWidths=[W])
statbox.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), PARCH),
    ("BOX", (0, 0), (-1, -1), 1.0, BLOOD),
    ("LEFTPADDING", (0, 0), (-1, -1), 11), ("RIGHTPADDING", (0, 0), (-1, -1), 11),
    ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ("TOPPADDING", (0, 0), (-1, 0), 9), ("BOTTOMPADDING", (0, -1), (-1, -1), 9),
]))
story.append(statbox)

# ---------- build table ----------
build_head = [P("Build, level by level", h2), rule(),
              P("Point buy 15 / 13 / 15 / 8 / 12 / 8, Soldier background +2 Str, +1 Con: starting array Str 17, Dex 13, "
                "Con 16, Int 8, Wis 12, Cha 8. Fighter first for Str/Con saves and because Gambino taught him to hold a sword "
                "before anything taught him to rage. Six General feats, two Origin feats and a Fighting Style: nine in all.", small)]
rows = [
    ("1", "Fighter 1", "Great Weapon Fighting, Second Wind ×2, masteries (greatsword Graze, longsword Sap, dagger Nick). "
                       "<b>Savage Attacker</b> (Soldier), <b>Tough</b> (Human). Athletics, Intimidation, Perception, Survival, Acrobatics.",
     "Gambino's camp, age 6–9: a sword bigger than he is."),
    ("2", "Fighter 2", "Action Surge, Tactical Mind.", "A boy on the battlefield at nine."),
    ("3", "Fighter 3", "Champion: Improved Critical (19–20), Remarkable Athlete.", "Kills Gambino at eleven; alone on the roads."),
    ("4", "Fighter 4", "<b>Great Weapon Master</b> (+1 Str → 18). 4th mastery: greataxe (Cleave). Second Wind ×3.", "Bazuso, age 15."),
    ("5", "Fighter 5", "Extra Attack, Tactical Shift.", "Corkus's ambush; loses to Griffith; joins the Hawks."),
    ("6", "Barbarian 1", "Rage ×2 (+2 damage), Unarmored Defense.", "Captain of the Raiders."),
    ("7", "Barbarian 2", "Reckless Attack, Danger Sense.", "Count Julius."),
    ("8", "Barbarian 3", "Berserker: Frenzy. Rage ×3. Primal Knowledge (Nature; Strength-based Intimidation while raging).",
     "The Hundred-Man Slayer."),
    ("9", "Barbarian 4", "<b>Slasher</b> (+1 Str → 19).", "Zodd. Doldrey: Boscogn."),
    ("10", "Fighter 6", "<b>Sentinel</b> (+1 Str → 20).", "The duel with Griffith; a year alone."),
    ("11", "Barbarian 5", "Fast Movement (40 ft).", "Wyald; breaking Griffith out."),
    ("12", "Barbarian 6", "Mindless Rage. Rage ×4.", "The Eclipse."),
    ("13", "Fighter 7", "Champion: second Fighting Style, Blind Fighting (blindsight 10 ft).",
     "Godo's forge, the Dragonslayer, Rickert's arm; two years of nights."),
    ("14", "Fighter 8", "<b>Crossbow Expert</b> (+1 Dex → 14).", "The Black Swordsman: the Snake Baron, the Count."),
    ("15", "Barbarian 7", "Feral Instinct, Instinctive Pounce.", "Lost Children: Rosine."),
    ("16", "Barbarian 8", "<b>Durable</b> (+1 Con → 17; bonus-action Hit Die, advantage on death saves).", "The Tower of Conviction: Mozgus."),
    ("17", "Barbarian 9", "Brutal Strike (+1d10, shove 15 ft or hamstring). Rage damage +3.", "The Hill of Swords: Zodd again; Griffith reborn."),
    ("18", "Barbarian 10", "Berserker: Retaliation.", "Flora's tower; the Berserker Armor; Grunbeld."),
    ("19", "Barbarian 11", "Relentless Rage.", "Vritannis: Ganishka's war."),
    ("20", "Barbarian 12", "<b>Resilient (Wisdom)</b> (+1 Wis → 13; Wis saves +7). Rage ×5.", "The Sea God; Elfhelm."),
]
data = [[P("Lvl", cellhead), P("Class", cellhead), P("What you get", cellhead), P("Where in the story", cellhead)]]
for lvl, cls, txt, where in rows:
    data.append([P(lvl, cellb), P(cls, cell), P(txt, cell), P(where, cell)])
bt = Table(data, colWidths=[0.4 * inch, 0.9 * inch, 3.55 * inch, W - 4.85 * inch], repeatRows=1)
bt_style = [
    ("BACKGROUND", (0, 0), (-1, 0), STEEL),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("GRID", (0, 0), (-1, -1), 0.4, GRID),
    ("TOPPADDING", (0, 0), (-1, -1), 2.4), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.4),
    ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
]
for i in range(1, len(data)):
    if i % 2 == 0:
        bt_style.append(("BACKGROUND", (0, i), (-1, i), PARCH))
bt.setStyle(TableStyle(bt_style))
story.extend(build_head)
story.append(bt)
story.append(Spacer(1, 6))
story.append(P("<b>At level 20:</b> Str 20, Dex 14, Con 17, Int 8, Wis 13, Cha 8 · 236 HP · AC 18 in the Berserker Armor · "
               "two swings at +13 for 4d6+16, Frenzy 3d6, Brutal Strike 1d10, Retaliation, Hew and Cleave on top · Rage ×5 with "
               "Relentless Rage · nine feats. Wisdom save +7: he holds against what comes at him from outside (Slan in "
               "Qliphoth, the Eclipse, every night of the Brand); what is already inside him is the armor's own saving throw.", stat))

# ---------- snapshots ----------
story.append(PageBreak())
story.append(P("Snapshots by arc", h2))
story.append(rule())
story.append(P("Story order (the manga opens with the Black Swordsman and flashes back to all of this). Pacing: a level or so "
               "a year through childhood, a level a campaign with the Hawks, then a level per major fight once the Brand is on "
               "him. The last line of each block takes the arc's famous feat and runs it against the sheet.", small))


def snap_full(name, where, levelline, vals, lines, checked):
    content = [P(name, snapname), P(where + "  ·  " + levelline, stattag),
               abil_table(vals, W - 22), Spacer(1, 4)]
    for ln in lines:
        content.append(P(ln, snapline))
    content.append(P("<b>The feat, checked.</b> " + checked, snapline))
    t = Table([[content]], colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PARCH),
        ("BOX", (0, 0), (-1, -1), 0.9, BLOOD),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return KeepTogether([t, Spacer(1, 8)])


def snap(name, where, levelline, lines, checked):
    content = [P(name, snapname), P(where + "  ·  " + levelline, stattag)]
    for ln in lines:
        content.append(P(ln, snapline))
    content.append(P("<b>The feat, checked.</b> " + checked, snapline))
    t = Table([[content]], colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PARCH),
        ("LINEBEFORE", (0, 0), (0, -1), 2.5, BLOOD),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return KeepTogether([t, Spacer(1, 7)])


story.append(snap(
    "Gambino's camp",
    "Golden Age, volumes 3–4 · ages 6 to 11",
    "Levels 1–3 · Fighter 1–3",
    ["Str 17 (+3), Dex 13 (+1), Con 16 (+3), Int 8, Wis 12 (+1), Cha 8 · <b>AC</b> 14 (a hand-me-down chain shirt) · "
     "<b>HP</b> 15, then 26, then 37 · greatsword +5, 2d6+3 · Second Wind ×2 (1d10+1) · Action Surge from level 2 · "
     "crits on 19–20 from level 3",
     "<b>Feats:</b> Great Weapon Fighting, Savage Attacker, Tough."],
    "A six-year-old swinging a sword he can barely lift, a nine-year-old on a battlefield, an eleven-year-old who kills the "
    "man who raised him when that man comes at him with a blade. Second Wind and Action Surge are the only reason a child "
    "with 15 hit points survives the first two; a 19–20 crit on a drunk, crippled mercenary captain is the third."))

story.append(snap(
    "Bazuso",
    "Golden Age, volume 4 · age 15",
    "Level 4 · Fighter 4",
    ["Str 18 (+4) · <b>AC</b> 16 (scavenged half plate) · <b>HP</b> 48 · greatsword +6, 2d6+6 (Great Weapon Master's +2), "
     "crits on 19–20, Hew after a crit or a kill · Action Surge · Second Wind ×3 (1d10+4)",
     "<b>Feats:</b> + <b>Great Weapon Master</b>."],
    "Bazuso the Grey Knight is a Knight (AC 18, 52 HP, two swings at +5 for 2d6+3). Guts needs four ordinary hits and lands "
    "one in two; Bazuso needs five of his and lands one in two. Run it out and a level-4 Guts loses this fight slightly more "
    "often than he wins it. He wins it with two crits (10% a swing, dice rerolled by Savage Attacker, 4d6+6 each) and the "
    "Action Surge that puts them in the same round, which is exactly how the Hawks read it from the ridge: a lucky brat with "
    "a sword too big for him. The next fight he picks, he loses."))

story.append(snap(
    "The Band of the Hawk",
    "Golden Age, volumes 4–6 · ages 15 to 17",
    "Levels 5–7 · Fighter 5, Barbarian 1–2",
    ["<b>HP</b> 59 → 83 · two attacks at +7 (PB +3 from level 5) · Rage ×2 (+2, resistance) from level 6 · Reckless Attack "
     "and Danger Sense from level 7 · Second Wind ×3 (1d10+5)",
     "<b>Feats:</b> unchanged."],
    "Corkus's ambush is a handful of Bandits (11 HP each) in the dark; Extra Attack makes it a cleanup. Griffith beats him "
    "because a level-5 swordsman with +7 to hit does not touch a duelist with Riposte behind an AC of 20; it is the one "
    "fight on this sheet he was supposed to lose. Count Julius: Dex +1 and no Stealth proficiency gets him into a sleeping "
    "castle, one Reckless swing kills a Noble (9 HP), and he is seen by the son on the way out, which is what a +1 Stealth "
    "buys you."))

story.append(snap_full(
    "The Hundred-Man Slayer",
    "Golden Age, volume 6 · age 17 or 18, captain of the Raiders",
    "Level 8 · Fighter 5 / Barbarian 3",
    ["18 (+4)", "13 (+1)", "16 (+3)", "8 (−1)", "12 (+1)", "8 (−1)"],
    ["<b>AC</b> 16 (half plate) · <b>HP</b> 95 (5d10 + 3d12) · <b>Speed</b> 30 ft · <b>Initiative</b> +1 with advantage · "
     "<b>Proficiency</b> +3 · <b>Saves</b> Str +7, Con +6",
     "<b>Skills</b> Athletics +7 (advantage), Intimidation +2 (+7 Strength-based while raging), Perception +4, Survival +4, "
     "Acrobatics +4, Animal Handling +4, Nature +2 · <b>Masteries</b> greatsword (Graze), greataxe (Cleave), longsword (Sap), dagger (Nick)",
     "<b>Greatsword</b> (a two-hander too big for a man his size, even then): two attacks at +7, 2d6+9 slashing raging (Str, "
     "Great Weapon Master's +3, Rage's +2), 1s and 2s count as 3, Savage Attacker's reroll, Frenzy's 2d6 on the first hit, "
     "crit on 19–20, Hew after any crit or kill, Graze for 4 on a miss. Reckless Attack every turn.",
     "<b>Resources</b> Rage ×3 (+2, resistance to weapons), Danger Sense, Action Surge, Second Wind ×3 (1d10+5), Tactical Shift.",
     "<b>Feats</b> Great Weapon Fighting, Savage Attacker, Tough, Great Weapon Master."],
    "A hundred Tudor foot soldiers, a few at a time up a slope, each a Guard or Soldier with 11 to 16 hit points. 2d6+9 "
    "kills one per hit; two swings a round plus Hew's bonus swing after each kill is three or four dead a round, so a hundred "
    "is 25 to 30 rounds of continuous fighting, three Rages back to back. Incoming: each man gets about one swing before he "
    "dies, hits AC 16 half the time for 4 or 5, halved by Rage. That is roughly 110 damage across the fight against 95 hit "
    "points and three Second Winds (about 30 more). He wins with single-digit hit points, a broken sword and a body full of "
    "holes, and has to be carried off, which is the panel."))

story.append(snap(
    "Zodd, and Doldrey",
    "Golden Age, volumes 5 and 7 · age 18",
    "Level 9 · Fighter 5 / Barbarian 4",
    ["Str 19 (+4) · <b>HP</b> 107 · attacks as at level 8 · Slasher: a hit takes 10 ft of speed, a crit gives the target "
     "disadvantage on its attacks",
     "<b>Feats:</b> + <b>Slasher</b>."],
    "Zodd is an Apostle: call it CR 18, AC 19, 250 HP, two claws at +12 for 3d8+7. Guts hits AC 19 on an 11 with advantage "
    "for 2d6+9, so 20-odd a round when both land: a hundred rounds to kill Zodd, and two of Zodd's rounds to kill Guts even "
    "with resistance. He wounds him and lives; Griffith's Beherit is why the encounter ends. Doldrey is the other end of the "
    "scale: Boscogn is a Knight (AC 18, 52 HP) on a warhorse (19 HP), and Guts has Zodd's thrown greatsword in his hands, an "
    "oversized 4d6 blade with Cleave. A Reckless crit (19–20) is 8d6+9, 37 on average; Cleave puts the same swing into the "
    "horse and kills it; Hew's bonus attack after the kill is 4d6+9 more into the rider. One turn, sixty damage to a "
    "52-hit-point general and a dead horse under him, which is the two halves."))

story.append(snap(
    "The duel, and the year alone",
    "Golden Age, volume 8 · ages 18 to 19",
    "Level 10 · Fighter 6 / Barbarian 4",
    ["Str 20 (+5) · <b>HP</b> 118 · attacks +9, 2d6+11 raging · Sentinel: a reaction swing at anyone beside him who hits "
     "someone else, and nothing he hits with it moves",
     "<b>Feats:</b> + <b>Sentinel</b>."],
    "Griffith's sabre is a Tiny resilient object (DMG): AC 19, 2d4 hit points. Any hit from a 2d6+11 swing shatters it, and "
    "Griffith, a Battle Master with a rapier, was never going to parry a Reckless swing at +9 with advantage while fighting "
    "to keep a friend instead of to win. The year in the mountains is where the Str 20 comes from: Sentinel is the version of "
    "him that will not let anyone get past him again."))

story.append(snap(
    "Wyald, and the rescue",
    "Golden Age, volumes 9–12 · age 19 or 20",
    "Level 11 · Fighter 6 / Barbarian 5",
    ["<b>HP</b> 130 · <b>Speed</b> 40 ft · attacks as at level 10",
     "<b>Feats:</b> unchanged."],
    "Wyald's ape form: Huge, AC 16, 180 HP, grapples everything it touches. Fast Movement is how Guts keeps getting out of "
    "the hands; 2d6+11 a swing finds the throat; and then Wyald stops playing. Honest reading of the numbers: he loses that "
    "fight, and Zodd is what ends it. The Tower of Rebirth is cleanup against Guards."))

story.append(snap_full(
    "The Eclipse",
    "Golden Age, volumes 12–13 · age 20",
    "Level 12 · Fighter 6 / Barbarian 6",
    ["20 (+5)", "13 (+1)", "16 (+3)", "8 (−1)", "12 (+1)", "8 (−1)"],
    ["<b>AC</b> 16 · <b>HP</b> 142 (6d10 + 6d12) · <b>Speed</b> 40 ft · <b>Initiative</b> +1 with advantage · "
     "<b>Proficiency</b> +4 · <b>Saves</b> Str +9, Con +7",
     "<b>Greatsword</b> two attacks at +9, 2d6+11 slashing raging, Frenzy 2d6, crit 19–20, Hew, Graze 5. <b>After it "
     "breaks:</b> the stump is a shortsword, +9, 1d6+11, and still two swings a round with Hew behind them.",
     "<b>Resources</b> Rage ×4, <b>Mindless Rage</b> (immune to Charmed and Frightened while raging), Reckless Attack, "
     "Danger Sense, Action Surge, Second Wind ×3 (1d10+6).",
     "<b>Feats</b> Great Weapon Fighting, Savage Attacker, Tough, Great Weapon Master, Slasher, Sentinel."],
    "Every mortal in that dome is Frightened the moment the sky opens, which in 5e terms means nobody but the Barbarian who "
    "raged first can act, and that is the whole Eclipse on one line: Mindless Rage. Lesser apostles run 80 to 120 hit "
    "points and he kills several with a broken blade at 1d6+11 a hit, Hew chaining the kills, Rage halving the teeth. The "
    "apostle that takes his arm is a grapple he escapes by cutting himself free; Femto's servant takes the eye; those are "
    "the DMG's lingering injuries, rolled in the worst session of his life. He does not win. The Skull Knight is the DM "
    "ending the encounter, and 142 hit points, four Rages and three Second Winds are why there was still something to carry out."))

story.append(snap(
    "Godo's forge",
    "Between the Golden Age and volume 1 · two years",
    "Level 13 · Fighter 7 / Barbarian 6",
    ["<b>HP</b> 153 · the Dragonslayer (4d6, Cleave, Str 20 to swing it), Rickert's arm (mace, cannon, crossbow mount) · "
     "Champion's second style: <b>Blind Fighting</b>, blindsight 10 ft",
     "<b>Feats:</b> unchanged."],
    "Two years of the Brand: every night something comes, and he fights it in the dark with one eye. Blind Fighting is what "
    "that looks like after seven hundred nights. The Dragonslayer needs Str 20 to swing without disadvantage, which he "
    "reached at level 10; the first time he lifts it, it is already his."))

story.append(snap(
    "The Black Swordsman",
    "Volumes 1–3 · age 22 or 23",
    "Level 14 · Fighter 8 / Barbarian 6",
    ["The full stat block on page 1. <b>AC</b> 17 · <b>HP</b> 164 · two swings at +11 for 4d6+13 raging, Frenzy 2d6, crossbow "
     "+7 for 1d8+2 twice a round, cannon +7 for 4d10",
     "<b>Feats:</b> + <b>Crossbow Expert</b>."],
    "Stat the Count's apostle form as a Huge aberration: AC 17, around 200 HP, Multiattack. Guts opens with Rage and Reckless "
    "Attack: two swings at +11 with advantage, 4d6+13 each (29 on average, more with Savage Attacker's reroll), Frenzy's 2d6 "
    "on the first, Hew after any crit, then an Action Surge round that doubles it and still leaves the cannon for the face "
    "(4d10). That is 120 to 150 damage in round one and the Count on the floor in three. The Count hits AC 17 easily; Rage "
    "halves it, so 164 hit points buys the three rounds. The Beherit ends the fight because the Count chooses it, not because "
    "Guts needed it to. The Snake Baron (CR 9, 130 HP) is the warm-up and goes the same way with less to spare."))

story.append(snap(
    "Lost Children, and the Tower of Conviction",
    "Volumes 14–21 · age 23",
    "Levels 15–16 · Fighter 8 / Barbarian 7–8",
    ["<b>HP</b> 176 → 188 · Con 17 from level 16 · Feral Instinct (advantage on initiative) and Instinctive Pounce (half a "
     "move for free when he rages) · Durable: a Hit Die as a bonus action, advantage on death saves",
     "<b>Feats:</b> + <b>Durable</b>."],
    "Rosine flies, AC 16, 110 HP: Reckless Attack does nothing for a target out of reach, so two bolts a round at +7 for "
    "1d8+2 bring her low and the sword finishes it, and he bleeds nearly to death doing it, which Durable's bonus-action "
    "Hit Die is for. Mozgus is a pseudo-apostle: AC 18, 160 HP, immune to slashing and piercing while his skin is set, the "
    "immunity gone the turn he opens his wings. Guts eats the fire and the hammer until that turn (188 HP, resistance), then "
    "one Reckless window: +11 with advantage, 4d6+13, Frenzy 2d6, Savage Attacker's reroll, a 19–20 crit doubling the dice "
    "and Hew after it, 60 to 90 in the window. Two windows and Mozgus is in two pieces."))

story.append(snap(
    "The Hill of Swords",
    "Volume 22 · age 23",
    "Level 17 · Fighter 8 / Barbarian 9",
    ["<b>HP</b> 200 · <b>Proficiency</b> +6 · the Dragonslayer now +2: +13 to hit, 4d6+16 raging (Rage +3), Frenzy 3d6 · "
     "Brutal Strike: give up advantage on one swing for +1d10 and a 15-ft shove, or a hamstring",
     "<b>Feats:</b> unchanged."],
    "Zodd at full strength, both of them better than last time. +13 for 4d6+16 is 32 a swing; Brutal Strike's shove is the "
    "knockdown and the horn. Zodd still has 250 hit points and claws that hit AC 17 on a 5; fifty rounds of this is a draw "
    "for a reason, and Griffith stepping between them is what stops it."))

story.append(snap_full(
    "The Berserker Armor",
    "Volumes 26–28: Flora's tower, Grunbeld; then Qliphoth and Slan · age 24",
    "Level 18 · Fighter 8 / Barbarian 10",
    ["20 (+5)", "14 (+2)", "17 (+3)", "8 (−1)", "12 (+1)", "8 (−1)"],
    ["<b>AC</b> 18 (the Berserker Armor) · <b>HP</b> 212 (8d10 + 10d12) · <b>Speed</b> 50 ft in the armor · <b>Initiative</b> +2 with "
     "advantage · <b>Proficiency</b> +6 · <b>Saves</b> Str +11, Con +9; Wis +1, and that is the problem",
     "<b>The Dragonslayer (+2)</b> two attacks at +13, 4d6+16 slashing raging, Frenzy 3d6 on the first hit, Brutal Strike "
     "+1d10 with a 15-ft shove, crit 19–20, Hew, Cleave, Graze 5. <b>Retaliation:</b> a reaction swing at anything within 5 ft "
     "that damages him. Crossbow +8 for 1d8+2, cannon +8 for 4d10, knives +11 for 1d4+7.",
     "<b>In the armor, raging</b> (see \u201cWhat he carries\u201d): resistance to all damage but psychic, immune to Frightened and "
     "Stunned, does not fall unconscious at 0 hit points, cannot stop, cannot tell friend from foe without Schierke.",
     "<b>Resources</b> Rage ×4 (+3), Mindless Rage, Reckless Attack, Danger Sense, Feral Instinct, Instinctive Pounce, "
     "Action Surge, Second Wind ×3 (1d10+8), Durable.",
     "<b>Feats</b> Great Weapon Fighting, Blind Fighting, Savage Attacker, Tough, Great Weapon Master, Slasher, Sentinel, "
     "Crossbow Expert, Durable."],
    "Grunbeld's dragon form: use an adult red dragon's numbers, AC 19 and 256 HP. Guts in the armor: Reckless swings at +13 "
    "for 4d6+16, Frenzy 3d6, Brutal Strike's 1d10 and the shove, Hew on crits, and Retaliation hands him a free swing every "
    "time the dragon touches him. Call it five swings a round at 32 with advantage: 130 a round and the dragon on its back in "
    "two. The bite and claws hit AC 18 all day; the armor halves them and will not let him drop. Schierke pulling him out is "
    "the only thing that ends it, which is also the manga. Slan, afterward: the Dragonslayer has drunk enough apostle blood to "
    "cut what lives on the astral side, and a God Hand bleeds when he stabs her because she wanted to find out what it felt like."))

story.append(snap(
    "Vritannis",
    "Volumes 32–34 · age 24",
    "Level 19 · Fighter 8 / Barbarian 11",
    ["<b>HP</b> 224 · Relentless Rage: at 0 hit points while raging, a DC 10 Con save (then 15, then 20) and he is back at 22",
     "<b>Feats:</b> unchanged."],
    "Ganishka's war: demon soldiers by the dozen (CR 2 or 3 each, 30-odd HP; Cleave and Hew eat two a swing), the tiger-things, "
    "and the elephants. The arc's feat is simply that he goes down and gets up, three times. On a +9 Con save he passes DC 10 "
    "and DC 15 without trying and DC 20 half the time; the sheet gives him two of those three for free."))

story.append(snap_full(
    "The Sea God, and Elfhelm",
    "Volumes 37–41 and on · age 24 or 25",
    "Level 20 · Fighter 8 / Barbarian 12",
    ["20 (+5)", "14 (+2)", "17 (+3)", "8 (−1)", "13 (+1)", "8 (−1)"],
    ["<b>AC</b> 18 · <b>HP</b> 236 (8d10 + 12d12) · <b>Speed</b> 50 ft in the armor · <b>Initiative</b> +2 with advantage · "
     "<b>Proficiency</b> +6 · <b>Saves</b> Str +11, Con +9, Wis +7",
     "<b>The Dragonslayer (+2)</b> two attacks at +13, 4d6+16 raging, Frenzy 3d6, Brutal Strike +1d10, crit 19–20, Hew, "
     "Cleave, Graze 5; Retaliation. <b>Iron hand</b> +11, 1d6+8 bludgeoning.",
     "<b>Resources</b> Rage ×5 (+3), Relentless Rage (back up at 24), Mindless Rage, Reckless Attack, Danger Sense, Feral "
     "Instinct, Action Surge, Second Wind ×3, Durable, the armor.",
     "<b>Feats</b> all nine."],
    "The Sea God is a Gargantuan body the party is inside; there is no AC to beat. The feat is the heart: a Huge object of a "
    "creature, maybe 150 hit points, resistant to slashing, hacked apart at 4d6+16 a swing while the armor keeps the acid and "
    "the crushing at half and Relentless Rage stands him back up at 24 every time the body takes him to zero (DC 10, 15, 20 on "
    "a +9 save). He does it, the armor takes two more levels of exhaustion and one more small thing, and he is carried out. "
    "Elfhelm is the long rest the sheet has never been allowed to take, and it is also where the story stops letting him have it."))

# ---------- what he carries ----------
story.append(P("What he carries", h2))
story.append(rule())
story.append(bullets([
    "<b>The Dragonslayer.</b> \u201cToo big to be called a sword.\u201d An oversized greatsword: 4d6 slashing, Heavy, Two-Handed, "
    "mastery Cleave. A Medium creature needs Strength 20 to swing it without disadvantage; anyone weaker swings it at "
    "disadvantage, or not at all. Soaked in apostle blood from the Snake Baron on, it counts as magical; call it +1 by the "
    "Count and +2 by the Millennium Falcon arc, and from Qliphoth on it hits astral things (incorporeal, ethereal, the God "
    "Hand) as if they were meat. The bonus is the blood, not the steel.",
    "<b>Rickert's arm.</b> An iron hand that counts as a mace for punching (1d6 bludgeoning) and restores two-handed grips. "
    "Inside it, a cannon: +Dex to hit, 4d10 piercing and fire, range 20/60, one shot, an action to reload; against a crowd, "
    "a 10-foot cone with a DC 15 Dex save for half instead. Bolted on top, a repeating crossbow: a light crossbow without "
    "the Loading property, which is what lets Extra Attack and Action Surge turn it into a hose.",
    "<b>Knives and bombs.</b> Daggers (Nick) for throwing; bombs as the DMG writes them, 3d6 fire in a 5-ft radius.",
    "<b>The black armor.</b> Half plate, stealth disadvantage and all. He has never once tried to be quiet.",
    "<b>The Berserker Armor</b> (legendary, cursed). AC 16 + Dex (max 2); unlike other heavy-looking armor, you can Rage in it. "
    "While you rage in it: resistance to all damage except psychic; immunity to the Frightened and Stunned conditions; your "
    "Speed increases by 10 feet (the limiters come off); the armor sets your broken bones with its own spikes, so no injury can stop you acting; at 0 hit points you do not fall "
    "unconscious but keep acting while making death saves; your Rage cannot be ended early and does not end while an enemy "
    "stands. The cost: at the start of each of your turns, Wisdom save DC 15 or you attack the nearest creature, friend or "
    "not (a caster bonded to you, Schierke, can give up her action to let you pass); when the Rage finally ends, you gain two "
    "levels of exhaustion and the armor keeps something small (the color in your sight, taste, feeling in a hand, a streak of "
    "hair, years off the end). Every time the Beast of Darkness wins the Wisdom save, it is a little more the one wearing you.",
    "<b>The Brand of Sacrifice.</b> You feel creatures of the Interstice (fiends, undead, apostles, the God Hand) within "
    "120 feet, know their direction, and cannot be surprised by them; it bleeds when they are close. Every night you spend "
    "outside consecrated ground or elf magic, something comes: the DM runs an encounter at night, and a night you fought "
    "through is not a long rest. The Brand marks you as prey, and everything evil within a mile knows which way to walk.",
    "<b>Lingering injuries</b> (DMG). Right eye: disadvantage on Perception checks that rely on sight and on ranged attack "
    "rolls. Left forearm: no second grip without the prosthetic, which restores it and is also a mace and a cannon. Blind "
    "Fighting at Fighter 7 is two years of fighting specters in the dark with one eye.",
]))

# ---------- alternates ----------
story.append(KeepTogether([
    P("Alternates, and 2014 rules", h2),
    rule(),
    P("<b>Other feats that are him:</b> Tavern Brawler (he bites, headbutts and punches apostles), Crusher (the iron fist; it "
      "was the level-20 pick in the first draft, before Resilient), Grappler (prying jaws open, holding a Count still), Charger "
      "(the way he opens most fights), Athlete, Mage Slayer. <b>Not him:</b> anything that makes him careful (Defensive "
      "Duelist, Defense), anything that makes him lucky (Lucky). <b>On Resilient (Wisdom):</b> the first draft left it out so "
      "the Beast could win that save; the honest reading is that Guts resists what comes at him from outside (Slan, the Eclipse, "
      "the Brand) and only loses to what is already inside him, which the armor models with its own Wisdom save."),
    P("<b>Champion vs Battle Master vs Samurai.</b> Champion is the raw version and the one above: crits on 19–20 feed Hew, "
      "and his legend is made of swings that landed like that. Battle Master puts the duelist on the sheet instead: Riposte "
      "and Parry for the Griffith fights, Sweeping Attack for the hundred men, Menacing Attack for the glare. Samurai "
      "(Xanathar's) is the other famous Guts build, Fighter 15 / Barbarian 5: Reckless Attack feeds Rapid Strike for four "
      "swings a round and Fighting Spirit is the Beast, but you lose Relentless Rage and Retaliation. Pure Barbarian 20 "
      "(Berserker) is the honest third answer: Strength 24, Constitution 24, 300-odd hit points, and nothing of Gambino's "
      "training, no Action Surge, no crits, no crossbow."),
    P("<b>2014 rules.</b> Variant Human (Great Weapon Master at level 1), same split, same order. The 2014 Berserker's Frenzy "
      "gives a bonus-action attack every turn and a level of exhaustion when the rage ends: that exhaustion <i>is</i> the "
      "Berserker Armor's toll, so on 2014 rules drop the armor's exhaustion clause and let the subclass pay it. Great Weapon "
      "Master's −5/+10 replaces the +PB; with Reckless Attack's advantage he should be taking it on every swing."),
]))

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print("ok")
