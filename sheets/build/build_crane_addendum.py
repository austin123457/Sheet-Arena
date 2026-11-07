from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.platypus.flowables import HRFlowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DVS", FD + "DejaVuSansCondensed.ttf"))
pdfmetrics.registerFont(TTFont("DVS-B", FD + "DejaVuSansCondensed-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVS-I", FD + "DejaVuSansCondensed-Oblique.ttf"))
pdfmetrics.registerFont(TTFont("DVS-BI", FD + "DejaVuSansCondensed-BoldOblique.ttf"))
pdfmetrics.registerFontFamily("DVS", normal="DVS", bold="DVS-B", italic="DVS-I", boldItalic="DVS-BI")
pdfmetrics.registerFont(TTFont("DVSerif-B", FD + "DejaVuSerif-Bold.ttf"))

INK = colors.HexColor("#1b1a1a"); ACC = colors.HexColor("#b35a1f"); PARCH = colors.HexColor("#f4f0e8")
GRID = colors.HexColor("#c9c2b4"); MUTED = colors.HexColor("#67645f"); STEEL = colors.HexColor("#474c54")

body = ParagraphStyle("body", fontName="DVS", fontSize=9.6, leading=13.2, textColor=INK, spaceAfter=6)
small = ParagraphStyle("small", parent=body, fontSize=8.6, leading=11.6, textColor=MUTED)
title = ParagraphStyle("title", fontName="DVSerif-B", fontSize=20, leading=24, textColor=INK, spaceAfter=2)
h2 = ParagraphStyle("h2", fontName="DVSerif-B", fontSize=12, leading=15, textColor=ACC, spaceBefore=10, spaceAfter=3)
cell = ParagraphStyle("cell", parent=body, fontSize=8.6, leading=11, spaceAfter=0)
cellb = ParagraphStyle("cellb", parent=cell, fontName="DVS-B")
cellhead = ParagraphStyle("cellhead", parent=cell, fontName="DVS-B", textColor=colors.white)


def P(t, s=body):
    return Paragraph(t, s)


doc = SimpleDocTemplate("../pdf/Kyle_Crane_Beast_Mode_Addendum.pdf", pagesize=letter,
                        leftMargin=0.7 * inch, rightMargin=0.7 * inch, topMargin=0.7 * inch, bottomMargin=0.7 * inch,
                        title="Kyle Crane — Beast Mode addendum", author="Claude")
W = letter[0] - 1.4 * inch
story = [P("Kyle Crane — Beast Mode addendum", title),
         P("Adds the healing the original sheet left out, keyed to the game's own skill descriptions. Everything else on "
           "the sheet stands.", small),
         HRFlowable(width="100%", thickness=1.2, color=ACC, spaceBefore=4, spaceAfter=8)]

story.append(P("What the game does", h2))
story.append(P("Activating Beast Mode restores a small chunk of health, and the Beast Unleashed skill restores health on every "
               "hit while the mode is active. Beast Conquered makes the activation a roar that stuns nearby enemies. The meter "
               "that charges Beast Mode fills as Crane fights and takes damage, so in play the activation heal is a comeback "
               "tool, not an opener."))

story.append(P("Added to the sheet", h2))
rows = [
    ("Beast Mode heal", "Once per Beast Mode, he regains 44 hit points (four times his Barbarian level, about a fifth of his "
                        "maximum). It fires when he enters Beast Mode if he is already below half his hit points; otherwise it "
                        "is banked and fires the first time he drops below half (113) while the mode is active. No action."),
    ("Beast Unleashed", "While in Beast Mode, each claw or bite hit restores hit points equal to his proficiency bonus (6). "
                        "Priced off the Path of the Beast bite, which heals a proficiency bonus once a turn under half health; "
                        "this is that effect on every hit, at any health, because that is what the skill does."),
    ("Beast Conquered", "When he enters Beast Mode, each enemy of his choice within 30 feet makes a DC 17 Wisdom save or is "
                        "Frightened of him until the end of his next turn (the roar buys seconds, not a lost turn). Creatures "
                        "immune to Frightened shrug it off; a Barbarian's Mindless Rage ends it the moment they rage."),
]
data = [[P("Feature", cellhead), P("Rule", cellhead)]] + [[P(a, cellb), P(b, cell)] for a, b in rows]
t = Table(data, colWidths=[1.4 * inch, W - 1.4 * inch])
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), STEEL), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                       ("GRID", (0, 0), (-1, -1), 0.4, GRID), ("BACKGROUND", (0, 2), (-1, 2), PARCH),
                       ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                       ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5)]))
story.append(t)

story.append(P("Why these numbers", h2))
story.append(P("The sheet already gives Beast Mode a ten-minute duration and four uses, which is far more uptime than the game's "
               "meter allows, so the heals are kept modest to pay for it: one 44-point surge per activation and about 18 a turn "
               "from three claws. A new activation needs the previous Beast Mode to have ended, so the surge cannot be chained by "
               "re-raging mid-fight."))

story.append(P("What it did in the arena", h2))
story.append(P("Against the Berserker Armor it turned a seven-round loss into a nine-round one: Beast Unleashed put back about "
               "18 a turn and the surge fired once at 111 hit points, against roughly 45 a turn coming in. Over three thousand "
               "silent reruns Guts still won 99.8% of them. The claws, Reckless Attack and Infectious Fury are the right tools "
               "for a slugfest; the build's real feats are the ones a flat arena takes away: a 40-foot climb speed, Stealth +15, "
               "and Sneak Attack from somewhere he cannot be reached."))

doc.build(story)
print("ok")
