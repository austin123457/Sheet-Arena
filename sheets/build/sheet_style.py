from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, ListFlowable, ListItem, PageBreak
from reportlab.platypus.flowables import HRFlowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
FD = "/usr/share/fonts/truetype/dejavu/"
FONTS = [("DVS","DejaVuSansCondensed.ttf"),("DVS-B","DejaVuSansCondensed-Bold.ttf"),("DVS-I","DejaVuSansCondensed-Oblique.ttf"),("DVS-BI","DejaVuSansCondensed-BoldOblique.ttf"),("DVSerif-B","DejaVuSerif-Bold.ttf")]
if not os.path.isdir(FD):      # no DejaVu (Windows): Calibri and Georgia under the same names
    FD = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts") + os.sep
    FONTS = [("DVS","calibri.ttf"),("DVS-B","calibrib.ttf"),("DVS-I","calibrii.ttf"),("DVS-BI","calibriz.ttf"),("DVSerif-B","georgiab.ttf")]
for n, f in FONTS:
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
