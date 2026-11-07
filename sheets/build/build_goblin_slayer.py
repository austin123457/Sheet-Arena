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

# ---------- palette ----------
INK = colors.HexColor("#1e1c1a")
RUST = colors.HexColor("#8a3b1e")
STEEL = colors.HexColor("#474c54")
PARCH = colors.HexColor("#f4f0e8")
GRID = colors.HexColor("#c9c2b4")
MUTED = colors.HexColor("#6b6660")

# ---------- styles ----------
body = ParagraphStyle("body", fontName="DVS", fontSize=9.6, leading=13.2, textColor=INK, spaceAfter=5)
small = ParagraphStyle("small", parent=body, fontSize=8.6, leading=11.6)
cell = ParagraphStyle("cell", parent=body, fontSize=8.6, leading=11, spaceAfter=0)
cellb = ParagraphStyle("cellb", parent=cell, fontName="DVS-B")
cellhead = ParagraphStyle("cellhead", parent=cell, fontName="DVS-B", textColor=colors.white)
title = ParagraphStyle("title", fontName="DVSerif-B", fontSize=26, leading=30, textColor=INK, spaceAfter=2)
subtitle = ParagraphStyle("subtitle", fontName="DVS", fontSize=10.5, leading=14, textColor=STEEL, spaceAfter=2)
h2 = ParagraphStyle("h2", fontName="DVSerif-B", fontSize=12.5, leading=16, textColor=RUST, spaceBefore=11, spaceAfter=3)
stat = ParagraphStyle("stat", parent=body, fontSize=9.3, leading=12.6, spaceAfter=3)
statname = ParagraphStyle("statname", fontName="DVSerif-B", fontSize=13, leading=16, textColor=INK, spaceAfter=1)
snapname = ParagraphStyle("snapname", fontName="DVSerif-B", fontSize=10.8, leading=13.5, textColor=INK, spaceAfter=1)
stattag = ParagraphStyle("stattag", parent=small, fontName="DVS-I", textColor=MUTED, spaceAfter=5)
abil_head = ParagraphStyle("abil_head", parent=cell, fontName="DVS-B", alignment=TA_CENTER, textColor=RUST)
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


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("DVS", 7.8)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 0.42 * inch,
                      "Goblin Slayer  ·  D&D 5th Edition build (2024 rules; 2014 conversion on the last page)")
    canvas.drawRightString(letter[0] - doc.rightMargin, 0.42 * inch, f"page {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(
    "../pdf/Goblin_Slayer_5e_Build.pdf", pagesize=letter,
    leftMargin=0.6 * inch, rightMargin=0.6 * inch, topMargin=0.6 * inch, bottomMargin=0.7 * inch,
    title="Goblin Slayer — D&D 5e Build", author="Claude", subject="Character build",
)
W = letter[0] - doc.leftMargin - doc.rightMargin
story = []

# ---------- title ----------
story.append(P("Goblin Slayer", title))
story.append(P("Human · Fighter (Battle Master) 16 / Rogue (Scout) 4 · Farmer background · no magic, ever", subtitle))
story.append(HRFlowable(width="100%", thickness=1.4, color=RUST, spaceBefore=4, spaceAfter=8))

story.append(P("Built on the 2024 rules, which hand out the most feat slots: two Origin feats at level 1, a Fighting "
               "Style feat, and a +1 on every General feat. \u201cFeats\u201d in the arc section means the things he pulls off in "
               "the story: each snapshot ends with what the arc shows, and the table after them runs the big ones against the "
               "numbers. A 2014 conversion is on the last page."))
story.append(P("<b>Design calls.</b> Fighter for the sword-and-shield grind; the Rogue dip is the five years under the Rhea "
               "burglar (expertise, ambush damage, Cunning Action). Raw stats stay modest on purpose, because he wins by "
               "preparation rather than by being superhuman, and his gear is cheap and replaceable, so AC stays mediocre and "
               "he gets hit a lot and survives it. This split ties pure Fighter 20 for total feats (10)."))

# ---------- snapshot stat block (level 10) ----------
story.append(P("Snapshot: series start, level 10 (Fighter 7 / Rogue 3, Silver rank)", h2))
story.append(rule())

abil = Table(
    [[P(a, abil_head) for a in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]],
     [P(v, abil_val) for v in ["18 (+4)", "13 (+1)", "15 (+2)", "10 (+0)", "12 (+1)", "8 (−1)"]]],
    colWidths=[(W - 24) / 6.0] * 6,
)
abil.setStyle(TableStyle([
    ("LINEABOVE", (0, 0), (-1, 0), 0.6, GRID),
    ("LINEBELOW", (0, 1), (-1, 1), 0.6, GRID),
    ("LINEBELOW", (0, 0), (-1, 0), 0.3, GRID),
    ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
]))

block = [
    P("Goblin Slayer", statname),
    P("Medium Humanoid (Human), Silver-rank adventurer · cheap-looking leather, a full steel helm, a small round shield, "
      "a sword of a strange length", stattag),
    P("<b>AC</b> 16 (chain shirt under grimy leather, shield) · <b>HP</b> 101 (7d10 + 3d8) · <b>Speed</b> 30 ft · "
      "<b>Initiative</b> +5 · <b>Proficiency</b> +4", stat),
    abil,
    Spacer(1, 4),
    P("<b>Saves</b> Str +8, Con +6 (others by ability)", stat),
    P("<b>Skills</b> Perception +9 (passive 19), Survival +9, Stealth +9, Nature +8, Athletics +8, Animal Handling +5, "
      "Investigation +4", stat),
    P("<b>Tools</b> thieves' tools, carpenter's tools, leatherworker's tools · <b>Languages</b> Common, Goblin, Halfling", stat),
    P("<b>Feats</b> Alert, Tough, Dueling, Tavern Brawler, Shield Master · <b>Weapon Masteries</b> shortsword (Vex), "
      "dagger (Nick), handaxe (Vex), club (Slow)", stat),
    Spacer(1, 2),
    P("<b>Attacks</b> (two per Attack action; Action Surge 1/short rest)", stat),
    bullets([
        "<b>Sword \u201cof a strange length\u201d (shortsword).</b> +8 to hit, 1d6+6 piercing; a hit gives advantage on his "
        "next attack (Vex).",
        "<b>Thrown dagger.</b> +8, range 20/60 ft, 1d4+4 piercing.",
        "<b>Whatever a dead goblin dropped.</b> Proficient with all of it; a club, handaxe or spear in one hand is 1d6+6 with Dueling.",
        "<b>Shield rim (Shield Master).</b> Once a turn after a melee hit: Str save DC 16 or the target is knocked prone or shoved 5 ft.",
        "<b>Headbutt, or a torch, a rock, a goblin (Tavern Brawler).</b> +8, 1d4+4 bludgeoning, reroll 1s; an unarmed hit "
        "shoves the target 5 ft once a turn.",
        "<b>Sneak Attack.</b> +2d6 once a turn with the sword or a dagger when he has advantage or an ally is beside the target.",
    ]),
    Spacer(1, 4),
    P("<b>Resources.</b> 5 superiority dice (d8, save DC 16): Ambush, Trip Attack, Precision Attack, Disarming Attack, "
      "Tactical Assessment. Second Wind ×3 (1d10+7; Tactical Mind adds 1d10 to a failed check, Tactical Shift gives a free "
      "half-move). Know Your Enemy (bonus action: immunities, resistances, vulnerabilities). Cunning Action, Steady Aim, "
      "Skirmisher. Heroic Inspiration every long rest.", stat),
    P("<b>Kit</b>, all cheap on purpose because it gets thrown away once it is covered in goblin: full helm (cosmetic), "
      "4–6 daggers, torches, oil flasks, caltrops, rope and grapnel, mirror on a stick, wire for snares, healer's kit, "
      "antitoxin, two potions of healing (the \u201cstamina potion\u201d), vials of basic poison until the Poisoner feat lets him "
      "brew his own, flour pouch (the dust explosion is a DM ruling; alchemist's fire is the closest stand-in).", stat),
    P("<b>How he fights.</b> Scout the nest first (Survival, Search, Know Your Enemy). Open from stealth: Ambush die on "
      "initiative, Sneak Attack on the first stab. Trip or Disarm the dangerous one, Precision Attack when the eye-shot has "
      "to land, shield bash to put a goblin down and finish it. Shaman dies first. Never fight them in the open if the "
      "corridor is right there.", stat),
]
statbox = Table([[block]], colWidths=[W])
statbox.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), PARCH),
    ("BOX", (0, 0), (-1, -1), 1.0, RUST),
    ("LEFTPADDING", (0, 0), (-1, -1), 11), ("RIGHTPADDING", (0, 0), (-1, -1), 11),
    ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
]))
story.append(statbox)

# ---------- build table ----------
build_head = [P("Build, level by level", h2), rule(),
              P("Point buy 15 / 13 / 14 / 10 / 12 / 8, Farmer background +2 Str, +1 Con: starting array "
                "Str 17, Dex 13, Con 15, Int 10, Wis 12, Cha 8. Fighter first for Str/Con saves and all armor.", small)]

rows = [
    ("1", "Fighter 1", "Dueling (Fighting Style feat), Second Wind ×2, 3 weapon masteries. <b>Tough</b> (Farmer), <b>Alert</b> (Human). "
                       "Skills: Perception, Survival, Stealth, Animal Handling, Nature."),
    ("2", "Fighter 2", "Action Surge, Tactical Mind."),
    ("3", "Fighter 3", "Battle Master: Ambush, Trip Attack, Precision Attack (4 d8). Student of War: Athletics, leatherworker's tools."),
    ("4", "Fighter 4", "<b>Tavern Brawler</b>: headbutt 1d4+Str with a 5-ft push, improvised weapons, reroll 1s. 4th mastery. Second Wind ×3."),
    ("5", "Fighter 5", "Extra Attack, Tactical Shift."),
    ("6", "Fighter 6", "<b>Shield Master</b> (+1 Str → 18)."),
    ("7", "Rogue 1", "Expertise (Perception, Stealth), Sneak Attack 1d6, Thieves' Cant; Investigation, thieves' tools."),
    ("8", "Rogue 2", "Cunning Action."),
    ("9", "Rogue 3", "Scout: Survivalist (expertise in Nature and Survival), Skirmisher. Steady Aim. Sneak Attack 2d6."),
    ("10", "Fighter 7", "Know Your Enemy. Maneuvers: Disarming Attack, Tactical Assessment (5 dice)."),
    ("11", "Fighter 8", "<b>Poisoner</b> (+1 Dex → 14): poisoner's kit, bonus-action application, brew PB doses."),
    ("12", "Fighter 9", "Indomitable. Tactical Master (any mastery weapon can Push, Sap or Slow instead)."),
    ("13", "Fighter 10", "Improved Combat Superiority (d10). Maneuvers: Pushing Attack, Goading Attack. Second Wind ×4. 5th mastery: spear (Sap)."),
    ("14", "Fighter 11", "Two Extra Attacks (three attacks)."),
    ("15", "Fighter 12", "<b>Thrown Weapon Fighting</b> (style feat): draw a dagger as part of the throw, +2 damage when thrown."),
    ("16", "Fighter 13", "Indomitable ×2, Studied Attacks."),
    ("17", "Fighter 14", "<b>Resilient (Wisdom)</b> (+1 Wis → 13, Wis saves)."),
    ("18", "Fighter 15", "Relentless. Maneuvers: Parry, Riposte (9 known, 6 dice)."),
    ("19", "Fighter 16", "<b>Durable</b> (+1 Con → 16; bonus-action Hit Die, advantage on death saves). 6th mastery: scimitar (Nick)."),
    ("20", "Rogue 4", "<b>Observant</b> (+1 Wis → 14; Search as a bonus action)."),
]
data = [[P("Lvl", cellhead), P("Class", cellhead), P("What you get", cellhead)]]
for lvl, cls, txt in rows:
    data.append([P(lvl, cellb), P(cls, cell), P(txt, cell)])
bt = Table(data, colWidths=[0.42 * inch, 0.95 * inch, W - 1.37 * inch], repeatRows=1)
bt_style = [
    ("BACKGROUND", (0, 0), (-1, 0), STEEL),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("GRID", (0, 0), (-1, -1), 0.4, GRID),
    ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
    ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
]
for i in range(1, len(data)):
    if i % 2 == 0:
        bt_style.append(("BACKGROUND", (0, i), (-1, i), PARCH))
bt.setStyle(TableStyle(bt_style))
story.append(KeepTogether(build_head + [bt]))
story.append(Spacer(1, 6))
story.append(P("<b>At level 20:</b> Str 18, Dex 14, Con 16, Int 10, Wis 14, Cha 8 · 220 HP · AC 17 · three attacks at +10 for "
               "1d6+6, thrown daggers at +10 for 1d4+6 · Sneak Attack 2d6 · 6d10 superiority dice, 9 maneuvers, save DC 18 · "
               "brewed poison on the blade (DC 14, +2d8 poison and Poisoned) · ten feats.", stat))

# ---------- snapshots by arc ----------
story.append(PageBreak())
story.append(P("Snapshots by arc", h2))
story.append(rule())
story.append(P("Story order, which is the novel and main-manga order: the Goblin Lord comes before Water Town there, and the "
               "anime swapped them. Pacing is about two levels a year through Year One and the lost years, then a level per "
               "novel once the party forms. He is Silver the whole way; Silver in this build is tier 3, which is why a nest is "
               "never a threat to him and a Champion with the helmet off nearly is."))


def snap(name, where, levelline, lines, shows):
    content = [P(name, snapname), P(where + "  ·  " + levelline, stattag)]
    for ln in lines:
        content.append(P(ln, snapline))
    content.append(P("<b>What the arc shows.</b> " + shows, snapline))
    t = Table([[content]], colWidths=[W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PARCH),
        ("LINEBEFORE", (0, 0), (0, -1), 2.5, RUST),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return KeepTogether([t, Spacer(1, 7)])


story.append(snap(
    "Year One, day one",
    "Year One (novel and manga), opening chapters · Porcelain rank, age 15",
    "Level 1 · Fighter 1",
    ["Str 17 (+3), Dex 13 (+1), Con 15 (+2), Int 10, Wis 12 (+1), Cha 8 (−1) · Proficiency +2 · <b>AC</b> 14 (leather, "
     "shield; the chain shirt comes later) · <b>HP</b> 14 · <b>Initiative</b> +3",
     "Shortsword +5, 1d6+5 · thrown dagger +5, 1d4+3 · Second Wind ×2 (1d10+1) · masteries: shortsword (Vex), dagger "
     "(Nick), club (Slow) · Perception +3 (passive 13), Survival +3, Stealth +3, Nature +2, Animal Handling +3",
     "<b>Feats:</b> Tough, Alert, Dueling."],
    "Fresh out of the Rhea's training: already alert, already tough, already sword-and-shield, and still one bad nest "
    "from dead. Fourteen hit points is the early chapters, where every hunt costs him blood and he learns the hard way "
    "what he did not prepare for."))

story.append(snap(
    "Year One, end of the first year",
    "Year One (novel and manga)",
    "Level 5 · Fighter 5",
    ["Same array · Proficiency +3 · <b>AC</b> 16 (chain shirt under the leather now) · <b>HP</b> 54 · <b>Initiative</b> +4",
     "Two attacks at +6, 1d6+5 · headbutt or improvised weapon 1d4+3 with a 5-ft push · Action Surge · Second Wind ×3 "
     "(1d10+5), Tactical Mind, Tactical Shift · Battle Master: 4d8 (DC 14): Ambush, Trip Attack, Precision Attack · "
     "Student of War: Athletics +6, leatherworker's tools · 4th mastery: handaxe (Vex) · Perception +4 (passive 14), "
     "Survival +4, Stealth +4",
     "<b>Feats:</b> Tough, Alert, Dueling, <b>Tavern Brawler</b>."],
    "The kid with a sword becomes Goblin Slayer: Extra Attack, the first maneuvers (ambush from the dark, trip, aim for "
    "the eye), and the Rhea's rule that anything in reach is a weapon. He is still learning what a nest is, which is "
    "why Expertise has not arrived yet."))

story.append(snap(
    "The lost years",
    "Offscreen, ages 16–20; flashbacks and side stories only",
    "Levels 6–9 · Fighter 6, then Rogue 1–3",
    ["<b>Shield Master</b> at 6 (Str 18). Rogue 1–3 at 7–9: Expertise (Perception, Stealth), Sneak Attack 2d6, Cunning "
     "Action, Steady Aim, Scout (expertise in Nature and Survival, Skirmisher), thieves' tools."],
    "Five years of solo nests turn the Rhea's lessons into doctrine: scout, count, poison, ambush, never fight fair. "
    "The Rogue levels are not new training; they are the old training finally being used on purpose."))

story.append(snap(
    "Series start, through the Goblin Lord",
    "Light novel 1 · anime season 1, episodes 1–5 and 10–12 · main manga from volume 1 · Silver rank, age 20",
    "Level 10 · Fighter 7 / Rogue 3",
    ["The full stat block on page 1. <b>AC</b> 16 · <b>HP</b> 101 · <b>Initiative</b> +5 · two attacks at +8, 1d6+6 · "
     "shield bash DC 16 · Sneak Attack 2d6 · 5d8 (DC 16), 5 maneuvers · Know Your Enemy · passive Perception 19",
     "<b>Feats:</b> Tough, Alert, Dueling, Tavern Brawler, Shield Master."],
    "Episode 1 is the whole kit in one nest: Ambush from the dark, a thrown dagger before the lookout can scream, the "
    "shaman opened with the shield rim, torches and Sneak Attack doing the rest. Know Your Enemy and Tactical Assessment "
    "are the farm defense, reading the horde and setting the ground. The Goblin Lord duel is 101 hit points and Second "
    "Wind keeping him upright long enough to finish it."))

story.append(snap(
    "Water Town, the Goblin Champion",
    "Light novel 2 · anime season 1, episodes 6–9 · main manga after the Goblin Lord",
    "Level 11 · Fighter 8 / Rogue 3",
    ["Str 18 (+4), Dex 14 (+2), Con 15 (+2), Int 10, Wis 12 (+1), Cha 8 (−1) · Proficiency +4 · <b>AC</b> 17 · "
     "<b>HP</b> 111 · <b>Initiative</b> +6",
     "Two attacks at +8, 1d6+6 · Sneak Attack 2d6 · 5d8 (DC 16), 5 maneuvers · poisoned blade: bonus action to apply, "
     "DC 14 Con save or 2d8 poison and Poisoned; he brews four doses at a time · Stealth +10, Perception +9 (passive 19)",
     "<b>Feats:</b> + <b>Poisoner</b>."],
    "This is the arc the hit-point pool exists for. A Goblin Champion (stat it as a CR 5–6 brute with Multiattack) takes "
    "him apart once the helmet comes off, and 111 HP is why \u201cbeaten within an inch of death\u201d still means alive. He is "
    "back in the sewers days later with the same AC, because he will not buy better armor."))

story.append(snap(
    "Harvest festival and the Dark Elf's ritual",
    "Light novel 3 · anime season 2, first half · main manga",
    "Level 12 · Fighter 9 / Rogue 3",
    ["Same array · Proficiency +4 · <b>AC</b> 17 · <b>HP</b> 121 · Indomitable ×1 · Tactical Master (any mastery weapon "
     "can Push, Sap or Slow on demand)",
     "<b>Feats:</b> unchanged."],
    "The wizard-boy episodes are Tactical Mind taught out loud: think before you swing, count before you enter. The "
    "fortress is the party's magic doing the killing while he controls the ground; Tactical Master is him turning a "
    "goblin's own club into a shove toward the pit."))

story.append(snap(
    "The elf forest and the wedding",
    "Light novel 4 · anime season 2, second half · main manga",
    "Level 13 · Fighter 10 / Rogue 3",
    ["Same array · Proficiency +5 · <b>AC</b> 17 · <b>HP</b> 131 · <b>Initiative</b> +7 · two attacks at +9, 1d6+6 · "
     "shield bash DC 17 · 5d10 (DC 17), 7 maneuvers: + Pushing Attack, Goading Attack · Second Wind ×4 · 5th mastery: "
     "spear (Sap) · Perception +11 (passive 21), Survival +11, Stealth +12, Nature +10",
     "<b>Feats:</b> unchanged."],
    "Pushing and Goading are the \u201cthey come to me\u201d tools: keep goblins off the elves, off Priestess, off the wedding. "
    "Passive Perception 21 is why the party's scout is the human in a tin helmet and not the elf."))

story.append(snap(
    "Goblin's Crown",
    "Light novel 5 · the 2020 film · main manga",
    "Level 14 · Fighter 11 / Rogue 3",
    ["Same array · Proficiency +5 · <b>AC</b> 17 · <b>HP</b> 141 · three attacks at +9, 1d6+6 · Sneak Attack 2d6 · "
     "5d10 (DC 17), 7 maneuvers",
     "<b>Feats:</b> unchanged."],
    "The snow fortress and the Goblin Paladin: the first goblins with armor, training and a plan of their own, and the "
    "first time he fights like a machine, three attacks a round with a Trip or Goading die on each turn. The Noble "
    "Fencer is episode 1's Priestess in a mirror, and the rescue goes the same way."))

story.append(snap(
    "The later volumes",
    "Light novel 6 onward · where the main manga is heading",
    "Levels 15–17 · Fighter 12–14 / Rogue 3",
    ["At 17: Str 18, Dex 14, Con 15, Int 10, Wis 13, Cha 8 · Proficiency +6 · <b>AC</b> 17 · <b>HP</b> 171 · "
     "<b>Initiative</b> +8 · three attacks at +10, 1d6+6 · thrown dagger +10, 1d4+6, drawn as part of the throw · "
     "5d10 (DC 18), 7 maneuvers · Indomitable ×2 · Studied Attacks · Wis save +7",
     "<b>Feats:</b> + <b>Thrown Weapon Fighting</b> (15), <b>Resilient: Wisdom</b> (17)."],
    "The veteran years, with rookies to teach and Priestess climbing the ranks. Thrown Weapon Fighting formalizes the "
    "dagger throws he has been making since Year One; Studied Attacks is miss once, never twice; Resilient (Wisdom) is a "
    "mind that nothing in a nest can get into anymore."))

story.append(snap(
    "Endgame",
    "A last stand, if the story gives him one",
    "Level 20 · Fighter 16 / Rogue 4",
    ["Str 18, Dex 14, Con 16, Int 10, Wis 14, Cha 8 · Proficiency +6 · <b>AC</b> 17 · <b>HP</b> 220 · three attacks at "
     "+10, 1d6+6 · 6d10 (DC 18), 9 maneuvers: + Parry, Riposte · Relentless · Durable (bonus-action Hit Die, advantage on "
     "death saves) · Observant (Search as a bonus action)",
     "<b>Feats:</b> all ten."],
    "Nothing new in how he fights, only more of it: a die back every fight, a parry for the hit that would have landed, "
    "and a body that refuses to go down. The goblins never get stronger. He simply never stops."))

# ---------- story feats checked ----------
story.append(P("Story feats, checked against the numbers", h2))
story.append(rule())
sf = [
    ("Episode 1: a nest of a dozen goblins and a shaman, solo, with a terrified cleric in tow (level 10)",
     "Goblins are CR 1/4 and most die to one hit of 1d6+6; the shaman (a goblin boss casting as a 2nd-level caster) dies to "
     "the shield-rim bash and a stab. The only danger in that nest is being ambushed in the dark, which Alert, the Ambush die "
     "and passive Perception 19 take off the table. On paper it is a level-10 character clearing a CR 1 encounter, which is "
     "the point: he is wildly overqualified and never once acts like it."),
    ("Episode 4: the ogre in the ruins, killed with a Gate scroll (level 10)",
     "Stat it as an Oni (CR 7, 110 HP), not a 5e ogre. The scroll does the killing; his part is knowing where to open it and "
     "when (Tactical Assessment, Know Your Enemy). Without the scroll a level-10 Fighter/Rogue loses that fight in three "
     "rounds, which is why he bought it."),
    ("Water Town: beaten within an inch of death by the Goblin Champion (level 11)",
     "A CR 5\u20136 brute: an ogre-sized goblin with Multiattack, two hits at +7 for 2d8+5, landing on AC 17 on a 10. Six hits "
     "put 111 HP into single digits, and that is the beating. It takes six because he will not buy better armor, and he is "
     "back in the sewers days later because 111 HP heals."),
    ("The Goblin Lord, one on one in the dark (level 10)",
     "A hobgoblin warlord in goblin skin: CR 6, 97 HP, AC 20. Two attacks at +8 for 1d6+6 plus Sneak Attack 2d6 average about "
     "20 a round against AC 20, so four rounds, with Priestess's Protection doing the pinning and Second Wind covering the "
     "hits he takes doing it."),
    ("The farm: a hundred goblins against the town's adventurers (level 10)",
     "A hundred CR 1/4 goblins is a deadly encounter for four level-10 characters and a slaughter when it is thirty "
     "adventurers behind trenches and traps. His feat there is the plan and the speech (Tactical Assessment, and the one "
     "Charisma check of his life), not the body count."),
    ("Goblin\u2019s Crown: the Goblin Paladin and the snow fortress (level 14)",
     "A hobgoblin warlord in plate (CR 6) with a few champions and a horde. Three attacks at +9 for 1d6+6 is two or three "
     "rounds for the paladin. The fortress is the hard part, and he solves it the way he solves everything: it is not a fight, "
     "it is a nest."),
]
sfd = [[P("The feat", cellhead), P("Checked against the sheet", cellhead)]]
for a, b in sf:
    sfd.append([P(a, cellb), P(b, cell)])
sft = Table(sfd, colWidths=[2.3 * inch, W - 2.3 * inch], repeatRows=1)
sft_style = [
    ("BACKGROUND", (0, 0), (-1, 0), STEEL),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("GRID", (0, 0), (-1, -1), 0.4, GRID),
    ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
    ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
]
for i in range(1, len(sfd)):
    if i % 2 == 0:
        sft_style.append(("BACKGROUND", (0, i), (-1, i), PARCH))
sft.setStyle(TableStyle(sft_style))
story.append(sft)

# ---------- feats ----------
story.append(P("The feat accounting", h2))
story.append(rule())
story.append(P("<b>In the build (10).</b> Alert, Tough, Dueling, Tavern Brawler, Shield Master, Poisoner, Thrown Weapon "
               "Fighting, Resilient (Wisdom), Durable, Observant."))
story.append(P("<b>Alternates worth a slot</b> (swap one in anywhere from level 11 on): Piercer (a damage reroll on his thrusts; "
               "its +1 Str would leave him at 19, so pair it with Grappler or Athlete to reach 20); Grappler (neck-snaps, "
               "goblins as shields); Sentinel (keeping goblins off Priestess); Mage Slayer (the shaman-first doctrine); "
               "Inspiring Leader on Wisdom (the farm-defense speech); Keen Mind (bonus-action Study for goblin lore); Athlete "
               "(cave crawling); Skill Expert (Medicine); Healer (Origin; he field-dresses wounds). Dungeon Delver is "
               "2014-only and is the single most on-brand feat in the game: take it if your DM allows 2014 feats."))
story.append(P("<b>Not him.</b> Lucky (he would be insulted), Great Weapon Master and Sharpshooter (no big weapons, no bows), "
               "Blind Fighting and Skulker's blindsight (he cannot see in the dark; the torch is half his tactics), Savage "
               "Attacker, Charger, and anything with a spell in it."))

# ---------- trademark table ----------
story.append(P("What the series shows, and what is on the sheet", h2))
story.append(rule())
tm = [
    ("Sharpened shield rim", "Shield Master bash, or Tavern Brawler improvised weapon: 1d4+4 slashing."),
    ("Dagger to the eye", "Thrown dagger with Precision Attack; Sneak Attack from stealth; Thrown Weapon Fighting from level 15."),
    ("Poisoned blade", "Bought basic poison early, then the Poisoner feat."),
    ("Helmet headbutt", "Tavern Brawler unarmed strike with push."),
    ("Knows the nest before he enters", "Expertise in Survival and Nature, Observant, Tactical Assessment, Know Your Enemy."),
    ("Never caught off guard", "Alert, the Ambush maneuver, passive Perception 19 and up."),
    ("Fire, oil, flour, flooding", "Oil plus torch is rules-as-written; the flour bomb and the flooded cave are DM rulings."),
    ("The Gate scroll", "5e scrolls need a caster. Treat it as a DM-issued one-shot item, or swap Scout for Thief if you want "
                        "Use Magic Device at Rogue 13."),
    ("Survives beatings that should kill him", "Tough, Durable, Second Wind ×4, Indomitable, 220 HP behind a 17 AC."),
    ("Counts out loud", "Roleplay. He will start at one."),
]
tdata = [[P("Trademark", cellhead), P("Mechanic", cellhead)]]
for a, b in tm:
    tdata.append([P(a, cellb), P(b, cell)])
tt = Table(tdata, colWidths=[2.1 * inch, W - 2.1 * inch], repeatRows=1)
tt_style = [
    ("BACKGROUND", (0, 0), (-1, 0), STEEL),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("GRID", (0, 0), (-1, -1), 0.4, GRID),
    ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
    ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
]
for i in range(1, len(tdata)):
    if i % 2 == 0:
        tt_style.append(("BACKGROUND", (0, i), (-1, i), PARCH))
tt.setStyle(TableStyle(tt_style))
story.append(tt)

# ---------- 2014 ----------
story.append(KeepTogether([
    P("2014 rules instead", h2),
    rule(),
    P("Variant Human (+1 Str, +1 Wis, Perception, feat: Alert), Outlander or Folk Hero background, same class split. "
      "Feat order: Tavern Brawler (+1 Str, Fighter 4), Tough (Fighter 6), Shield Master (Fighter 8), Poisoner (Fighter 12), "
      "Resilient: Wisdom (Fighter 14), Dungeon Delver (Fighter 16), Durable (Rogue 4). Most 2014 feats carry no +1, so take "
      "one straight +2 Str if you want to reach 18."),
    P("Thrown Weapon Fighting via Fighting Initiate and the Quick Toss maneuver (both Tasha's) are worth a slot if allowed. "
      "For the literal text \u201cFavored Enemy: goblinoids,\u201d trade Rogue 4 for Ranger 1 (Natural Explorer: Underdark for "
      "caves; learn Goblin), at the cost of one feat."),
    P("<b>Pure Fighter 20</b> also lands on ten feats (Epic Boon of Fortitude at 19) and adds a fourth attack and a second "
      "Action Surge, but you lose Expertise and Sneak Attack; take Skill Expert twice (Survival, Perception) in place of "
      "Durable and Observant."),
]))

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print("ok")
