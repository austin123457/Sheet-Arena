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

INK = colors.HexColor("#1a1a1c")
CRIM = colors.HexColor("#8b1a1a")
STEEL = colors.HexColor("#3b3b40")
PARCH = colors.HexColor("#f3f0ea")
GRID = colors.HexColor("#c6c2ba")
MUTED = colors.HexColor("#67645f")

body = ParagraphStyle("body", fontName="DVS", fontSize=9.5, leading=13, textColor=INK, spaceAfter=5)
small = ParagraphStyle("small", parent=body, fontSize=8.6, leading=11.6)
cell = ParagraphStyle("cell", parent=body, fontSize=8.2, leading=10.3, spaceAfter=0)
cellb = ParagraphStyle("cellb", parent=cell, fontName="DVS-B")
cellhead = ParagraphStyle("cellhead", parent=cell, fontName="DVS-B", textColor=colors.white)
title = ParagraphStyle("title", fontName="DVSerif-B", fontSize=26, leading=30, textColor=INK, spaceAfter=2)
subtitle = ParagraphStyle("subtitle", fontName="DVS", fontSize=10.5, leading=14, textColor=STEEL, spaceAfter=2)
h2 = ParagraphStyle("h2", fontName="DVSerif-B", fontSize=12.5, leading=16, textColor=CRIM, spaceBefore=11, spaceAfter=3)
stat = ParagraphStyle("stat", parent=body, fontSize=9.2, leading=12.4, spaceAfter=3)
statname = ParagraphStyle("statname", fontName="DVSerif-B", fontSize=13, leading=16, textColor=INK, spaceAfter=1)
snapname = ParagraphStyle("snapname", fontName="DVSerif-B", fontSize=10.8, leading=13.5, textColor=INK, spaceAfter=1)
stattag = ParagraphStyle("stattag", parent=small, fontName="DVS-I", textColor=MUTED, spaceAfter=5)
abil_head = ParagraphStyle("abil_head", parent=cell, fontName="DVS-B", alignment=TA_CENTER, textColor=CRIM)
abil_val = ParagraphStyle("abil_val", parent=cell, fontSize=10, leading=12, alignment=TA_CENTER)
bullet_style = ParagraphStyle("bul", parent=stat, spaceAfter=1.5)
snapline = ParagraphStyle("snapline", parent=stat, fontSize=8.9, leading=12, spaceAfter=2)
hb_name = ParagraphStyle("hb_name", fontName="DVS-B", fontSize=9.6, leading=12.6, textColor=CRIM, spaceBefore=5, spaceAfter=1)
hb_tag = ParagraphStyle("hb_tag", parent=small, fontName="DVS-I", textColor=MUTED, spaceAfter=2)


def P(t, s=body):
    return Paragraph(t, s)


def rule():
    return HRFlowable(width="100%", thickness=0.6, color=GRID, spaceBefore=0, spaceAfter=4)


def bullets(items, style=bullet_style):
    return ListFlowable([ListItem(Paragraph(t, style), leftIndent=10, value="•") for t in items],
                        bulletType="bullet", start="•", bulletFontName="DVS", bulletFontSize=8,
                        leftIndent=12, bulletOffsetY=-1)


def abil_table(vals, width):
    t = Table([[P(a, abil_head) for a in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]],
               [P(v, abil_val) for v in vals]], colWidths=[width / 6.0] * 6)
    t.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, 0), 0.6, GRID), ("LINEBELOW", (0, 1), (-1, 1), 0.6, GRID),
                           ("LINEBELOW", (0, 0), (-1, 0), 0.3, GRID),
                           ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    return t


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("DVS", 7.8)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 0.42 * inch,
                      "Itachi Uchiha  ·  D&D 5th Edition build (2024 rules; homebrew jutsu marked)")
    canvas.drawRightString(letter[0] - doc.rightMargin, 0.42 * inch, f"page {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate("../pdf/Itachi_Uchiha_5e_Build.pdf", pagesize=letter,
                        leftMargin=0.6 * inch, rightMargin=0.6 * inch, topMargin=0.6 * inch, bottomMargin=0.7 * inch,
                        title="Itachi Uchiha — D&D 5e Build", author="Claude", subject="Character build")
W = letter[0] - doc.leftMargin - doc.rightMargin
story = []

story.append(P("Itachi Uchiha", title))
story.append(P("Human (Uchiha) · Wizard (Illusionist) 17 / Rogue (Assassin) 3 · Criminal background · the Sharingan as a bloodline, "
               "the Mangekyo as four spells the book does not have", subtitle))
story.append(HRFlowable(width="100%", thickness=1.4, color=CRIM, spaceBefore=4, spaceAfter=8))
story.append(P("Built on the 2024 rules like the others. \u201cFeats\u201d are the things he does on the page, and every snapshot ends by "
               "checking its big one against the numbers. Where the Player's Handbook has no spell for what he does, the jutsu "
               "is written as one, with a slot level and a cost, in \u201cJutsu the book does not have.\u201d"))
story.append(P("<b>Design calls.</b> He is a mind, not a body: Intelligence is the stat, the Sharingan is the bloodline, and "
               "genjutsu is Illusion and Enchantment cast without a word or a gesture because the target looked at him. Rogue 3 is "
               "ANBU: Expertise, Sneak Attack with a kunai, and Assassinate for the one night that defines him. The chakra problem "
               "the series keeps mentioning is the spell-slot table: Amaterasu, Tsukuyomi, Izanami and Susanoo are his 6th, 7th, "
               "8th and 9th-level spells, one slot each, which is why he can use each once and then he is finished. The illness "
               "takes twenty hit points and makes the third Mangekyo spell of a day the one that kills him. The Edo Tensei body is "
               "the only version of him that was ever at full strength, so the peak snapshot is a dead man."))

# ---------- headline block ----------
story.append(P("Snapshot: Part II and the Edo Tensei body, level 20 (Wizard 17 / Rogue 3)", h2))
story.append(rule())

block = [
    P("Itachi Uchiha", statname),
    P("Medium Humanoid (Human, Uchiha), age 21 · the Akatsuki cloak, the slashed Leaf headband, the Suzaku ring, kunai and shuriken, "
      "a crow on the shoulder · the lines in italics are the Edo Tensei body raised in the Fourth War", stattag),
    P("<b>AC</b> 17 (Mage Armor), 19 against anything he can see (Sharingan) · <b>HP</b> 85 (17d6 + 3d8), <b>65</b> while the "
      "illness has him · <b>Speed</b> 30 ft · <b>Initiative</b> +10 with advantage · <b>Proficiency</b> +6", stat),
    abil_table(["8 (−1)", "18 (+4)", "10 (+0) · 8 ill", "20 (+5)", "12 (+1)", "10 (+0)"], W - 24),
    Spacer(1, 4),
    P("<b>Saves</b> Int +11, Wis +7; advantage on saves against illusions and Enchantment (Sharingan); advantage on "
      "concentration (War Caster) · <b>Skills</b> Stealth +16, Perception +13 (passive 23, advantage with the Sharingan), "
      "Investigation +17, Arcana +11, Acrobatics +10, Sleight of Hand +10, Insight +7, Deception +6 · <b>Tools</b> thieves' tools, "
      "disguise kit, poisoner's kit · <b>Spell save DC</b> 19 · <b>Spell attack</b> +11", stat),
    P("<b>Sharingan.</b> Sees chakra (Detect Magic at will, 60 ft), advantage on Perception and Insight, sees through illusions "
      "of 3rd level or lower, +2 AC against attackers it can see, copies any 1st to 5th-level wizard spell it watches cast, and "
      "casts single-target Illusion and Enchantment spells with no verbal or somatic component on a creature that can see his "
      "eyes. <b>Mangekyo Sharingan.</b> Unlocks Amaterasu, Tsukuyomi, Izanami and Susanoo; every casting costs a level of "
      "exhaustion and a point of eye strain (he is at 7 of 10: disadvantage on sight-based Perception; at 10 he is blind).", stat),
    P("<b>Feats</b> Alert, Keen Mind, Elemental Adept (Fire), War Caster, +2 Dexterity · <b>Weapon Masteries</b> dagger (Nick), dart (Vex)", stat),
    Spacer(1, 2),
    P("<b>Attacks</b>", stat),
    bullets([
        "<b>Kunai</b> (dagger): +10, 1d4+4 piercing, thrown 20/60. <b>Shuriken</b> (darts): +10, 1d4+4, 20/60; a hit gives advantage "
        "on the next throw (Vex). Two attacks a turn is not his thing; one kunai from the blind side with <b>Sneak Attack +2d6</b> is "
        "(advantage, or an ally beside the target; in the first round, advantage on anything that hasn't acted and +3 damage).",
        "<b>Fire Bolt</b>: +11, 4d10 fire, 120 ft; 1s on the dice count as 2 and fire resistance is ignored (Elemental Adept). "
        "<b>Mind Sliver</b>: DC 19 Int save, 4d6 psychic and −1d4 on the target's next save: a flicker of genjutsu.",
    ]),
    Spacer(1, 2),
    P("<b>Spell slots</b> 4 / 3 / 3 / 3 / 2 / 1 / 1 / 1 / 1 · Arcane Recovery brings back nine levels of slots once a day on a "
      "short rest · <b>Cantrips</b> Fire Bolt, Mind Sliver, Minor Illusion (free, with sound and image), Mage Hand, Prestidigitation · "
      "<b>Rituals from the book</b> Find Familiar (the crow), Detect Magic, Alarm", stat),
    P("<b>Prepared (22), with the jutsu each one is.</b> 1st: Mage Armor, Shield (Substitution: the log), Disguise Self "
      "(Transformation), Silent Image (a genjutsu). 2nd: Misty Step (Body Flicker), Mirror Image (clones), Phantasmal Force "
      "(Ephemeral, the finger genjutsu), Hold Person (Shackling Stakes), Scorching Ray (Phoenix Sage Fire). 3rd: Fireball (Great "
      "Fireball), Counterspell (reversing a genjutsu), Dispel Magic (Release), Hypnotic Pattern (a genjutsu on a room), Tidal Wave "
      "(Water Dragon Bullet). 4th: Phantasmal Killer (a genjutsu that kills), Shadow Clone. 5th: Dominate Person (a genjutsu that "
      "commands), Mislead (Crow Clone). 6th: Amaterasu. 7th: Tsukuyomi. 8th: Izanami. 9th: Susanoo.", stat),
    P("<b>Features.</b> Illusionist: Improved Illusions (no verbal component, +60 ft range), Phantasmal Creatures (Summon Beast and "
      "Summon Fey as flocks of crows, one free casting of each a day), Illusory Self (reaction: the attack hits an Itachi that "
      "scatters into crows; once per short rest, or a 2nd-level slot), Illusory Transformation. Rogue: Cunning Action, Steady Aim, "
      "Expertise, Assassinate, Assassin's Tools. Wizard: Ritual Adept, Memorize Spell, Scholar (Investigation).", stat),
    P("<b>The illness</b> (Part II). Con 8, so 65 HP and −1 on Con saves. He starts each day with a level of exhaustion unless he "
      "takes the medicine. At the end of any fight in which he cast two or more Mangekyo spells, DC 15 Con save or he drops to 0 "
      "and begins dying.", stat),
    P("<i><b>Edo Tensei.</b> Undead. 85 HP, Con 10, no illness, no medicine. Immune to poison and exhaustion, so the Mangekyo costs "
      "nothing but eye strain. Regains 10 HP at the start of each of his turns; at 0 HP the body reforms in 1d4 rounds unless "
      "sealed. Obeys the summoner until freed; he freed himself with Shisui's eye.</i>", stat),
    P("<b>How he fights.</b> Genjutsu first: eye contact and a Phantasmal Force or Hold Person without a word, and the target never "
      "knows which Itachi is real (Mirror Image, Mislead, a Shadow Clone). A kunai from the blind side for Sneak Attack while the "
      "clone takes the hit. Fireball for a group, Counterspell for the other caster. The Mangekyo is the last resort: Tsukuyomi "
      "for the one who must be stopped, Amaterasu for the one who cannot be reached, Susanoo when what is coming would kill him. "
      "Three Mangekyo spells in one fight is the whole top of his slot table, and with the illness, the fourth round is the one he "
      "coughs blood in.", stat),
]
statbox = Table([[f] for f in block], colWidths=[W])
statbox.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), PARCH), ("BOX", (0, 0), (-1, -1), 1.0, CRIM),
                             ("LEFTPADDING", (0, 0), (-1, -1), 11), ("RIGHTPADDING", (0, 0), (-1, -1), 11),
                             ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                             ("TOPPADDING", (0, 0), (-1, 0), 9), ("BOTTOMPADDING", (0, -1), (-1, -1), 9)]))
story.append(statbox)

# ---------- homebrew ----------
story.append(P("Jutsu the book does not have", h2))
story.append(rule())
story.append(P("Each is written as a 5e spell or feature. Save DC and spell attack are his (19 and +11 at level 20). Where the "
               "series shows a cost, the cost is on the card.", small))

hb = [
    ("Sharingan", "bloodline feature, gained at level 3 (age 8); no action to keep active",
     "While active: you see chakra (as Detect Magic, 60 ft, at will); advantage on Wisdom (Perception) and (Insight) checks; you "
     "automatically see through illusions of 3rd level or lower and have advantage on saving throws against Illusion and "
     "Enchantment spells; attacks made by a creature you can see have a −2 penalty against you (you read the move before it is "
     "made); when you see a creature cast a wizard spell of 1st to 5th level, you may copy it into your spellbook over your next "
     "short rest at no cost; and when you cast an Illusion or Enchantment spell that targets one creature, you can cast it with "
     "no verbal or somatic component if the target can see your eyes."),
    ("Mangekyo Sharingan", "bloodline feature, gained at level 14 (age 13, when Shisui died)",
     "Amaterasu, Tsukuyomi, Izanami and Susanoo are added to your spellbook as you reach their levels. Each casting of one of "
     "them costs you a level of exhaustion (eyes bleed) and a point of eye strain. At 5 strain, disadvantage on Perception checks "
     "that rely on sight; at 10, you are blind except for the chakra sense (Blindsight 30 ft). Strain never heals. Taking another "
     "Uchiha's eyes resets it (he never did)."),
    ("Amaterasu", "6th-level Evocation · 1 action · one creature or object you can see within 120 ft · no components (the right eye) · until burned out",
     "Black fire takes the target. Dexterity save; on a failure it is ignited, on a success the flames land in its space instead "
     "and burn there. An ignited creature takes 6d10 fire damage at once and 4d10 fire at the start of each of its turns. The "
     "flames ignore resistance to fire and treat immunity as resistance; water does nothing; they end only when the target is "
     "destroyed, when the burning part is cut away (an action and 4d10 slashing damage to itself, if the DM allows the anatomy), "
     "or by Dispel Magic cast at 6th level or higher. An ignited object burns through in 1d4 rounds whatever it is made of."),
    ("Tsukuyomi", "7th-level Illusion · 1 action · one creature within 60 ft that can see your eyes · no components (the left eye) · instantaneous",
     "The target lives through 72 hours of your design in an instant. Wisdom save. On a failure it takes 10d10 psychic damage, "
     "falls Unconscious for 1 hour or until Greater Restoration or Heal, and gains 3 levels of exhaustion that fade one per long "
     "rest. On a success, half damage and nothing else. A creature with a Sharingan makes the save with advantage and, if it "
     "succeeds, breaks the illusion entirely and knows it did."),
    ("Izanami", "8th-level Illusion · 1 action · one creature within 30 ft · no components · permanent",
     "No saving throw and no eye contact needed: this is a loop of sensation, not sight. The target relives the same minute of "
     "its life again and again, Incapacitated and unaware of the world, until it genuinely accepts the truth the loop shows it "
     "about itself. Nothing else ends it, not even Wish; the DM decides when acceptance has happened, and may let the target "
     "attempt a DC 30 Wisdom (Insight) check once per day of story time. The eye you cast it from goes dark permanently."),
    ("Susanoo", "9th-level Conjuration · 1 action · self · concentration, up to 10 minutes",
     "A Huge warrior of chakra forms around you. While it lasts: you gain 150 temporary hit points; your AC can't be lower than "
     "21; you have resistance to all damage; you can't be moved or grappled against your will. Its arms carry two things. "
     "<b>Yata Mirror:</b> three times per casting, as a reaction when you are hit by an attack or targeted by a spell or effect, "
     "the Mirror takes on the nature that repels it and the attack, spell or effect fails against you entirely. <b>Sword of "
     "Totsuka:</b> as an action, a melee spell attack with reach 15 ft, +11, 6d8 force; a creature hit must succeed on a Wisdom "
     "save or be sealed into the sword's gourd, where it dreams drunk forever (as Imprisonment, with no ongoing save); Legendary "
     "Resistance applies. <b>Yasaka Magatama:</b> as an action, a ranged spell attack, 120 ft, 8d8 force. The cost: at the end of "
     "each of your turns after the first you lose 5 hit points that nothing prevents, and when the spell ends you gain 2 levels "
     "of exhaustion on top of the Mangekyo's one."),
    ("Shadow Clone Technique", "4th-level Conjuration · 1 bonus action · self · 1 minute",
     "A duplicate of you appears within 5 ft. It has your AC, saves, skills and attack bonuses, 10 hit points, and acts on your "
     "turn as you direct: it can move, make weapon attacks, cast your cantrips, or take the Dodge or Help action, but cannot cast "
     "leveled spells. When it drops to 0 or you dismiss it, it is gone in smoke and you know what it knew. At 5th level: an "
     "<b>Exploding Shadow Clone</b>, which when it ends detonates for 8d6 fire in a 20-ft radius, Dexterity save for half."),
    ("Crow Clone", "this is Mislead (5th) as written",
     "You turn invisible and leave an Itachi behind that talks and walks and dissolves into crows when struck. Illusory Self is "
     "the cheap version for one attack."),
    ("Shisui's eye", "item: a crow that carries it, one use",
     "Programmed Illusion wrapped around a Kotoamatsukari: when the crow sees Itachi's Mangekyo, the creature that is hosting the "
     "crow is affected as by Dominate Monster with no save and no awareness of it, for one command. He wrote it to protect "
     "Konoha from Sasuke and used it on himself to break Kabuto's control. The eye needs a decade to charge again."),
]
for name, tag, text in hb:
    story.append(KeepTogether([P(name, hb_name), P(tag, hb_tag), P(text, small)]))

# ---------- build table ----------
story.append(P("Build, level by level", h2))
story.append(rule())
story.append(P("Point buy 8 / 15 / 10 / 15 / 12 / 10, Criminal background +2 Int, +1 Dex: starting array Str 8, Dex 16, Con 10, "
               "Int 17, Wis 12, Cha 10. Wizard first for Intelligence and Wisdom saves: nobody genjutsus him. Four General feats, "
               "two Origin feats; the Human's Versatile feat is Skilled (Arcana, Deception, Acrobatics). The ages are the "
               "series' own, and the level curve is what a prodigy's looks like: most of it before thirteen.", small))
rows = [
    ("1", "Wizard 1", "Fire Bolt, Minor Illusion, Mage Hand; Mage Armor, Disguise Self, Silent Image, Find Familiar; Ritual Adept, Arcane Recovery. <b>Alert</b> (Criminal), <b>Skilled</b> (Human). Perception, Insight, Investigation, Sleight of Hand, Stealth.",
     "Age 4: sees the end of the war. Age 7: top of the Academy class after one year."),
    ("2", "Wizard 2", "Scholar: Investigation expertise.", "Graduates at 7."),
    ("3", "Wizard 3", "Illusionist: Improved Illusions, Illusion Savant. <b>The Sharingan awakens.</b>", "Age 8."),
    ("4", "Wizard 4", "<b>Keen Mind</b> (+1 Int → 18): Study as a bonus action.", "Age 8–9: shurikenjutsu nobody can follow."),
    ("5", "Wizard 5", "3rd-level: Fireball (Great Fireball), Counterspell. Memorize Spell.", "Age 10: Chunin."),
    ("6", "Rogue 1", "Expertise (Stealth, Perception), Sneak Attack 1d6, masteries (dagger Nick, dart Vex).", "Age 10–11."),
    ("7", "Rogue 2", "Cunning Action.", "Age 11: ANBU."),
    ("8", "Rogue 3", "Assassin: Assassinate, Assassin's Tools. Steady Aim. Sneak Attack 2d6.", "ANBU missions."),
    ("9", "Wizard 6", "Phantasmal Creatures: flocks of crows.", "Age 12."),
    ("10", "Wizard 7", "4th-level: Phantasmal Killer, Shadow Clone.", "The clone that explodes."),
    ("11", "Wizard 8", "<b>Elemental Adept: Fire</b> (+1 Int → 19).", "Age 12–13."),
    ("12", "Wizard 9", "5th-level: Dominate Person, Mislead (Crow Clone).", "Age 13: ANBU captain."),
    ("13", "Wizard 10", "Illusory Self: the crow-clone dodge.", "Shisui."),
    ("14", "Wizard 11", "6th-level. <b>Mangekyo Sharingan:</b> Amaterasu.", "Age 13: Shisui dies and leaves him an eye."),
    ("15", "Wizard 12", "<b>War Caster</b> (+1 Int → 20).", "Age 13."),
    ("16", "Wizard 13", "7th-level: Tsukuyomi.", "Age 13: the night of the massacre."),
    ("17", "Wizard 14", "Illusory Transformation.", "Ages 13–17: Akatsuki. Orochimaru, Kisame, Deidara."),
    ("18", "Wizard 15", "8th-level: Izanami.", "Ages 17–18: Part I. Kakashi, Jiraiya, Sasuke."),
    ("19", "Wizard 16", "<b>+2 Dexterity</b> (18).", "Ages 18–21: the illness."),
    ("20", "Wizard 17", "9th-level: Susanoo.", "Age 21: Sasuke. Then the Edo Tensei body."),
]
data = [[P("Lvl", cellhead), P("Class", cellhead), P("What you get", cellhead), P("Where in the story", cellhead)]]
for lvl, cls, txt, where in rows:
    data.append([P(lvl, cellb), P(cls, cell), P(txt, cell), P(where, cell)])
bt = Table(data, colWidths=[0.4 * inch, 0.85 * inch, 3.7 * inch, W - 4.95 * inch], repeatRows=1)
bt_style = [("BACKGROUND", (0, 0), (-1, 0), STEEL), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("GRID", (0, 0), (-1, -1), 0.4, GRID),
            ("TOPPADDING", (0, 0), (-1, -1), 2.4), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.4),
            ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5)]
for i in range(1, len(data)):
    if i % 2 == 0:
        bt_style.append(("BACKGROUND", (0, i), (-1, i), PARCH))
bt.setStyle(TableStyle(bt_style))
story.extend([bt, Spacer(1, 6)])
story.append(P("<b>At level 20:</b> Str 8, Dex 18, Con 10 (8 ill), Int 20, Wis 12, Cha 10 · 85 HP (65) · AC 17, 19 against what he "
               "can see · DC 19, +11 · one slot each of 6th through 9th: Amaterasu, Tsukuyomi, Izanami, Susanoo, once a day apiece · "
               "six feats, two of them the bloodline.", stat))

# ---------- snapshots ----------
story.append(PageBreak())
story.append(P("Snapshots by arc", h2))
story.append(rule())
story.append(P("Story order. The last line of each block takes the arc's famous feat and runs it against the sheet. Enemies are "
               "statted by feel: Kakashi in Part I as CR 15 with a Wisdom save of +8, Orochimaru and Jiraiya as CR 22 with +9 and "
               "+11 and Legendary Resistance, Part II Sasuke as CR 17 with +6, Nagato as CR 24, Sage-Mode Kabuto as CR 23.", small))


def snap_full(name, where, levelline, vals, lines, checked):
    content = [P(name, snapname), P(where + "  ·  " + levelline, stattag), abil_table(vals, W - 22), Spacer(1, 4)]
    for ln in lines:
        content.append(P(ln, snapline))
    content.append(P("<b>The feat, checked.</b> " + checked, snapline))
    t = Table([[content]], colWidths=[W])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), PARCH), ("BOX", (0, 0), (-1, -1), 0.9, CRIM),
                           ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                           ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    return KeepTogether([t, Spacer(1, 8)])


def snap(name, where, levelline, lines, checked):
    content = [P(name, snapname), P(where + "  ·  " + levelline, stattag)]
    for ln in lines:
        content.append(P(ln, snapline))
    content.append(P("<b>The feat, checked.</b> " + checked, snapline))
    t = Table([[content]], colWidths=[W])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), PARCH), ("LINEBEFORE", (0, 0), (0, -1), 2.5, CRIM),
                           ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                           ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]))
    return KeepTogether([t, Spacer(1, 7)])


story.append(snap(
    "The child who saw the war",
    "Itachi Shinden; flashbacks in Part II · ages 4 to 7",
    "Levels 1–2 · Wizard 1–2",
    ["Str 8, Dex 16 (+3), Con 10, Int 17 (+3), Wis 12 (+1), Cha 10 · Proficiency +2 · <b>AC</b> 16 (Mage Armor) · <b>HP</b> 6, "
     "then 10 · shuriken +5, 1d4+3 · Fire Bolt +5, 1d10 · DC 13 · slots 2, then 3 · Silent Image, Disguise Self, a raven familiar",
     "<b>Feats:</b> Alert, Skilled."],
    "A four-year-old who watched a battlefield and decided on pacifism, and a seven-year-old who finished the Academy in a year at "
    "the top of the class. The famous shurikenjutsu is Dex 16 and a +5 throw at level 2, which no adult in the room can match, and "
    "the ricochet that hits the target behind the rock is a trick shot the DM allows on a Sleight of Hand check at +5. The "
    "genjutsu nobody taught him yet is Minor Illusion and Silent Image."))

story.append(snap(
    "Sharingan",
    "Itachi Shinden · age 8",
    "Level 3 · Wizard 3 (Illusionist)",
    ["<b>AC</b> 18 against anything he can see · <b>HP</b> 14 · illusions with no verbal component · sees chakra, copies what he watches",
     "<b>Feats:</b> unchanged."],
    "The eyes open at eight. On the sheet that is the bloodline feature and the Illusionist's silent casting arriving on the same "
    "level, which is right: from here on, a genjutsu is a look. The copying clause is why his spellbook fills faster than a "
    "wizard's should."))

story.append(snap(
    "Chunin at ten, ANBU at eleven",
    "Itachi Shinden; Sasuke's memories · ages 10 to 12",
    "Levels 5–8 · Wizard 5, Rogue 1–3",
    ["Int 18 (+4) · Proficiency +3 · <b>HP</b> 22 → 37 · DC 15 · Fireball 8d6 at level 5 · kunai +6, Sneak Attack 2d6 from "
     "level 8, Assassinate · Expertise in Stealth and Perception · Cunning Action",
     "<b>Feats:</b> + <b>Keen Mind</b>."],
    "The Great Fireball is the Uchiha coming-of-age jutsu and he had it years early: Fireball at level 5. The Rogue levels are "
    "the ANBU child: Stealth +9 at ten years old, a kunai with Sneak Attack from the dark, Assassinate's advantage on anyone who "
    "has not moved yet. A level-8 character on missions a jonin would be sent on is a CR 8 eleven-year-old, which is what the "
    "village thought it had."))

story.append(snap(
    "Shisui, and the Mangekyo",
    "Part II flashbacks; Itachi Shinden · age 13",
    "Levels 12–14 · Wizard 9–11",
    ["Int 19 (+4) · Proficiency +4 · <b>HP</b> 53 → 61 · DC 16 · Dominate Person, Mislead, Illusory Self · at level 14, the "
     "Mangekyo: <b>Amaterasu</b> (6th)",
     "<b>Feats:</b> + <b>Elemental Adept (Fire)</b>."],
    "ANBU captain at thirteen is Dominate Person and the Crow Clone at level 12. Then Shisui gives him an eye and goes into the "
    "river, and the Mangekyo awakens: the sheet gives it as a feature at level 14 with Amaterasu already in the book. Shisui's "
    "other eye goes into a crow with a Programmed Illusion in it, for a day fifteen years off. The feat of this arc is not a "
    "fight. It is the grief, and the sheet has no number for it."))

story.append(snap_full(
    "The night of the massacre",
    "Part II, the truth told by Obito and then by Itachi; Itachi Shinden · age 13",
    "Level 16 · Wizard 13 / Rogue 3",
    ["8 (−1)", "16 (+3)", "10 (+0)", "20 (+5)", "12 (+1)", "10 (+0)"],
    ["<b>AC</b> 16, 18 against what he can see · <b>HP</b> 69 · <b>Initiative</b> +8 with advantage · <b>Proficiency</b> +5 · "
     "<b>Saves</b> Int +10, Wis +6 · <b>DC</b> 18 · <b>Spell attack</b> +10 · Stealth +13, Perception +11",
     "<b>Slots</b> 4 / 3 / 3 / 3 / 2 / 1 / 1 · Fireball 8d6, Hypnotic Pattern, Hold Person, Counterspell, Phantasmal Killer, "
     "Shadow Clone, Dominate Person, Mislead, Amaterasu, <b>Tsukuyomi</b> (7th)",
     "<b>Kunai</b> +8, 1d4+3, Sneak Attack 2d6, Assassinate (+3 in the first round, advantage on anyone who hasn't acted) · "
     "Illusory Self · Cunning Action",
     "<b>Feats</b> Alert, Skilled, Keen Mind, Elemental Adept (Fire), War Caster."],
    "The whole clan in one night, with Obito working the other end of the compound. Most of the Uchiha are non-combatants; the "
    "Police Force are Veterans (CR 3) and a few of the elders are CR 8 to 10. Assassinate and Sneak Attack from the dark for the "
    "ones on patrol, Fireball for a street, Hypnotic Pattern for a courtyard, Hold Person for whoever meets his eyes. Fugaku and "
    "Mikoto do not roll; they sit down. Tsukuyomi is kept for the one person who had to live: a Wisdom save at +1 against DC 18 "
    "fails on anything under 17, and Sasuke gets the 72 hours and the three levels of exhaustion. A level-16 wizard clears a "
    "village in a night. It is the only feat on these four sheets that is worse for being possible."))

story.append(snap(
    "Akatsuki",
    "Part II flashbacks; Itachi Shinden, Akatsuki Hiden · ages 13 to 17",
    "Level 17 · Wizard 14 / Rogue 3",
    ["Proficiency +6 · <b>HP</b> 73 · <b>DC</b> 19 · <b>Spell attack</b> +11 · Illusory Transformation · the Suzaku ring (Project "
     "Image, once a day: how Akatsuki meets)",
     "<b>Feats:</b> unchanged."],
    "Orochimaru tries to take his body and has to look at him to do it. Eye-contact genjutsu with no components, DC 19, against a "
    "Wisdom save of +9: fails on a 9 or less. He had not spent a Legendary Resistance because he never saw a spell. One Sneak "
    "Attack kunai takes the hand, and Orochimaru leaves the organisation. Deidara (Wisdom +3) is recruited by a Phantasmal Force "
    "of his own death; that save fails on anything under 16. Kisame is the partner who does the fighting the sheet cannot."))

story.append(snap_full(
    "Part I: the Leaf, Kakashi, Jiraiya, Sasuke",
    "Naruto, the Search for Tsunade arc · age 17 or 18",
    "Level 18 · Wizard 15 / Rogue 3",
    ["8 (−1)", "16 (+3)", "10 (+0)", "20 (+5)", "12 (+1)", "10 (+0)"],
    ["<b>AC</b> 16, 18 against what he can see · <b>HP</b> 77 · <b>Initiative</b> +9 with advantage · <b>Proficiency</b> +6 · "
     "<b>Saves</b> Int +11, Wis +7 · <b>DC</b> 19 · <b>Spell attack</b> +11 · Stealth +15, Perception +13, Investigation +17",
     "<b>Slots</b> 4 / 3 / 3 / 3 / 2 / 1 / 1 / 1 · Tidal Wave 4d8 (Water Dragon), Exploding Shadow Clone 8d6, Counterspell, "
     "Hold Person, Fireball, Mislead, Amaterasu, Tsukuyomi, <b>Izanami</b> (8th, learned, never used while alive)",
     "<b>Kunai</b> +9, 1d4+3, Sneak Attack 2d6 · Fire Bolt +11, 3d10 · Shield · Illusory Self",
     "<b>Feats</b> Alert, Skilled, Keen Mind, Elemental Adept (Fire), War Caster."],
    "Three jonin in a hallway. Kurenai's genjutsu is Counterspelled and turned back on her with Hold Person (her Wisdom save +6 "
    "against DC 19 fails on 12 or less). Asuma eats a kunai. Kakashi, Sharingan and all, makes the Tsukuyomi save with advantage "
    "against DC 19 at +8: he needs an 11 on the better of two dice, about 75% to pass, and he failed, which is why he spent a week "
    "in bed with three levels of exhaustion. The Water Dragon is Tidal Wave, the clone that blows up in Kakashi's face is the "
    "5th-level Shadow Clone at 8d6. Jiraiya (CR 22, Wisdom +11, Legendary Resistance) is the fight the sheet agrees not to take: "
    "Amaterasu burns a hole in the Toad Mouth because an object gets no save, and they leave. Sasuke in the hotel is CR 5 with a "
    "Wisdom save of +1: the Chidori is caught on the Sharingan's −2 and a Shield, the wrist breaks because a thirteen-year-old's "
    "wrist does, and Tsukuyomi fails on anything under 18."))

story.append(snap(
    "Part II: the hunt for the Nine-Tails, and Sasuke",
    "Naruto Shippuden, the Kazekage Rescue through the Itachi Pursuit arcs · age 21, dying",
    "Level 20 · Wizard 17 / Rogue 3, the illness",
    ["The headline block, with the illness lines in force: Con 8, 65 HP, a level of exhaustion each morning without the medicine, "
     "and the DC 15 Con save at the end of any fight with two Mangekyo spells in it",
     "<b>Feats:</b> + <b>+2 Dexterity</b> (18), and the 9th-level slot: <b>Susanoo</b>."],
    "The Itachi that fights Team Kakashi in the Kazekage Rescue is a borrowed body with a third of his chakra (Pain's technique, "
    "not his): run him as a Shadow Clone with the cantrips and the 1st- and 2nd-level slots. The Itachi that meets Naruto on the "
    "road is Mislead with the crow, leaving Shisui's eye behind. Then the Uchiha hideout. Tsukuyomi first, and Sasuke's Sharingan "
    "gives him advantage on a +6 save against DC 19: about 64% to break it, and he does, which shocks Itachi and the sheet alike. "
    "Amaterasu: Sasuke's Dex save is +9, passes on a 10 or better, and he passes by shedding the snake. Kirin is 12d10 lightning, "
    "66 on average, into Susanoo's resistance: 33 of the 150 temporary hit points. Orochimaru's hydra comes out and meets the "
    "Sword of Totsuka: a Wisdom save at +9 with no Legendary Resistance left, sealed. Then the cost: three Mangekyo spells, 15 "
    "hit points lost to Susanoo's upkeep, and a DC 15 Con save at −1, which fails on 15 or less. He was going to lose that roll, "
    "and he had already decided to. Two fingers to the forehead."))

story.append(snap_full(
    "Edo Tensei: Nagato, Kabuto, Izanami",
    "Naruto Shippuden, the Fourth Shinobi World War · dead, and at full strength for the first time",
    "Level 20 · Wizard 17 / Rogue 3, undead",
    ["8 (−1)", "18 (+4)", "10 (+0)", "20 (+5)", "12 (+1)", "10 (+0)"],
    ["<b>AC</b> 17, 19 against what he can see · <b>HP</b> 85, regains 10 at the start of each turn, reforms in 1d4 rounds unless "
     "sealed · <b>Initiative</b> +10 with advantage · <b>Proficiency</b> +6 · <b>DC</b> 19 · <b>Spell attack</b> +11 · immune to "
     "poison and exhaustion: the Mangekyo costs nothing but eye strain",
     "<b>Slots</b> 4 / 3 / 3 / 3 / 2 / 1 / 1 / 1 / 1 · all four Mangekyo spells · Susanoo with the Sword of Totsuka, the Yata "
     "Mirror and Yasaka Magatama · kunai +10, Sneak Attack 2d6 · Fire Bolt 4d10 · Shisui's eye, one use",
     "<b>Feats</b> Alert, Skilled, Keen Mind, Elemental Adept (Fire), War Caster, +2 Dexterity."],
    "Kabuto's control is the summoner's hold on an undead; the crow's Kotoamatsukari is a Dominate Monster with no save aimed at "
    "himself, with one command: protect Konoha. Nagato (CR 24, Legendary Resistance) spends his resistances on Naruto and B and "
    "then the Totsuka lands: Wisdom save at +12 against DC 19, a 30% fail that comes up, and he is sealed, which is the "
    "manga. Yasaka Magatama at 8d8 force is what he adds to the Rasenshuriken and the Tailed Beast Ball against Chibaku Tensei. "
    "Then Kabuto in Sage Mode closes his eyes, and every genjutsu on the sheet that needs eye contact is useless, which is the "
    "entire point of the fight. Izanami needs no eyes and no save; he and Sasuke walk Kabuto into the loop, and the left eye goes "
    "dark for it. Kabuto gets out exactly the way the card says, by accepting what he was, and the first thing he does with his "
    "freedom is save Sasuke's life. Then Itachi ends the Edo Tensei with Kabuto's own hands, and goes."))

# ---------- what he carries ----------
story.append(P("What he carries", h2))
story.append(rule())
story.append(bullets([
    "<b>Kunai</b> (daggers, Nick) and <b>shuriken</b> (darts, Vex), more than he will ever throw. <b>Explosive tags:</b> as the DMG's "
    "bombs, 3d6 fire in a 10-ft radius, Dex save DC 15 for half, four of them. Wire.",
    "<b>The Akatsuki cloak</b> is a cloak; Mage Armor is the guard. <b>The Suzaku ring:</b> Project Image once a day, which is how "
    "the organisation holds its meetings. <b>The slashed headband:</b> a Leaf headband with a line through it, and it is his.",
    "<b>The crow</b> (Find Familiar, a raven), and in another crow, <b>Shisui's eye</b> (see the jutsu card).",
    "<b>The medicine</b> (Part II): a dose a day holds the illness off: no exhaustion that morning. It does nothing for the Con save "
    "at the end of a fight with two Mangekyo spells in it. He ran out of days before he ran out of doses.",
    "<b>ANBU gear</b> (ages 11 to 13): the Weasel mask and a tanto (shortsword, Vex). He put them down and never picked them up again.",
]))

story.append(KeepTogether([
    P("Alternates, and 2014 rules", h2),
    rule(),
    P("<b>Shadow Monk 3 instead of Assassin 3</b> gets you Unarmored Defense at the same AC, Deflect Attacks for the kunai he bats "
      "aside, and Darkness and Pass Without Trace as ninja tools, at the price of Sneak Attack and Assassinate. <b>Pure Wizard 20</b> "
      "adds Spell Mastery and two Signature Spells (Counterspell and Hypnotic Pattern at will is the Uchiha prodigy) and loses the "
      "one night the Assassin levels are there for. A <b>Sorcerer</b> build with Subtle Spell is the other honest reading of the "
      "finger genjutsu; it makes him a Charisma character, and he is not one."),
    P("<b>2014 rules.</b> Variant Human (Alert at level 1), same split. Take the <b>School of Enchantment</b> instead of Illusion: "
      "Hypnotic Gaze is the Sharingan genjutsu word for word, Instinctive Charm is the finger-point that makes an attacker hit "
      "someone else, and Alter Memories is why nobody remembers being caught. You lose Illusory Self, so the crow-clone dodge "
      "goes back to being Mirror Image and Mislead, which is fine."),
]))

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print("ok")
