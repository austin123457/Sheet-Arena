exec(open('sheet_style.py', encoding='utf-8').read())
GREEN = colors.HexColor("#7a1f3d")
h2 = ParagraphStyle("h2", fontName="DVSerif-B", fontSize=12.5, leading=16, textColor=GREEN, spaceBefore=11, spaceAfter=3)
hb_name = ParagraphStyle("hn", fontName="DVS-B", fontSize=9.6, leading=12.6, textColor=GREEN, spaceBefore=5, spaceAfter=1)
abil_head = ParagraphStyle("ah", parent=cell, fontName="DVS-B", alignment=TA_CENTER, textColor=GREEN)
def on_page(c, doc):
    c.saveState(); c.setFont("DVS", 7.8); c.setFillColor(MUTED)
    c.drawString(doc.leftMargin, 0.42*inch, "V  ·  D&D 5th Edition build (2024 rules; his chrome, the quickhacks and the Relic are homebrew)")
    c.drawRightString(letter[0]-doc.rightMargin, 0.42*inch, f"page {doc.page}"); c.restoreState()
doc = SimpleDocTemplate("../pdf/V_5e_Build.pdf", pagesize=letter, leftMargin=0.6*inch, rightMargin=0.6*inch, topMargin=0.6*inch, bottomMargin=0.7*inch, title="V — D&D 5e Build", author="Claude")
W = letter[0] - 1.2*inch; S = []

def hb(name, tag, text):
    return KeepTogether([P(name, hb_name), P(tag, hb_tag), P(text, small)])

S.append(P("V", title))
S.append(P("Human · Rogue (Arcane Trickster) 9 / Fighter (Battle Master) 11 · Nomad of the Bakker clan · the merc who did every job in Night City, with a dead rockerboy in his head and a Nomad waiting at the edge of the Badlands", subtitle))
S.append(HRFlowable(width="100%", thickness=1.4, color=GREEN, spaceBefore=4, spaceAfter=8))
S.append(P("Built on the 2024 rules, canon-first, from <i>Cyberpunk 2077</i> (update 2.x) and <i>Phantom Liberty</i>. This is the completionist's V: Vincent, the Nomad lifepath, every gig, side job and DLC mission done, level 60 and Street Cred 50, Panam romanced, and the secret ending: <b>Don't Fear the Reaper</b>, Arasaka Tower stormed with nobody but Johnny, Adam Smasher dead, Mikoshi, and V back in his own body. What the game does next is Path of Glory and the Crystal Palace. What this V does next is a headcanon, and the sheet says so where it matters: he turns the job down and leaves Night City with Panam and the Aldecaldos."))
S.append(P("<b>Design calls.</b> At level 60 V has 81 attribute points, enough for three trees at 20 and not four. This one maxes <b>Reflexes</b> (the blades and the Sandevistan), <b>Technical Ability</b> (crafting, the chrome, Edgerunner) and <b>Intelligence</b> (the deck), with <b>Cool 15</b> for the stealth and the crits and <b>Body 6</b>, the minimum and then some. In 5e that is Dexterity 20 and Intelligence 20 with nothing to spare. Rogue comes first because the Nomad prologue is a smuggling run, and the Arcane Trickster is the netrunner: an Intelligence caster whose invisible hand is a remote breach. Fighter (Battle Master) is the Solo Night City made of him after Konpeki. Technical Ability is the Crafter feat from his Nomad background and the chrome on page 2, all of it homebrew, written the way Caleb's Adam Smasher writes his. The game gives V one Operating System slot, so he runs a Sandevistan <i>or</i> a cyberdeck; on this sheet he picks before each job, and a ripperdoc swaps them in an hour."))

S.append(P("Snapshot: Don't Fear the Reaper, level 20 (Rogue 9 / Fighter 11)", h2)); S.append(rule())
block = [P("V", statname),
 P("Medium Humanoid (Human), twenty-seven, 2077 · Bakker by birth, Aldecaldo by choice · Johnny's aviators in the jacket, the Malorian on the hip, Mantis Blades under the forearms, a Kiroshi stare · “I'm not dyin' for nothin'.”", stattag),
 P("<b>AC</b> 18 (Chitin subdermal plating), 20 in Sandevistan · <b>HP</b> 194 (Tough) · <b>Speed</b> 30 ft, double jump · <b>Initiative</b> +11 (Alert) · <b>Proficiency</b> +6 · <b>Superiority dice</b> 5d10, DC 19 · <b>RAM</b> 20 (with the deck)", stat),
 abil_table(["8 (−1)","20 (+5)","14 (+2)","20 (+5)","10 (+0)","8 (−1)"], W-24), Spacer(1,4),
 P("<b>Saves</b> Dex +11, Int +11; Indomitable rerolls a failure at +11 once a day · <b>Skills</b> Stealth +17, Investigation +17, Acrobatics +17, Perception +12 (expertise), Sleight of Hand +11, Survival +6, Insight +6, Intimidation +5 · Reliable Talent · <b>Tools</b> tinker's, smith's and alchemist's supplies (Crafter), thieves' tools, vehicles (land) · <b>Languages</b> Common (English), Spanish, Japanese", stat),
 P("<b>Defenses.</b> Uncanny Dodge halves a hit; Evasion; Riposte with a superiority die when a melee attack misses. <b>Second Heart:</b> the first time he drops to 0 HP, he's back at full instead. <b>Reflex Tuner:</b> the first time he falls below 50 HP, time slows for him until the end of his next turn (attacks against him at Disadvantage). In Sandevistan, attacks against him have Disadvantage too.", stat),
 P("<b>Attacks.</b> <b>Mantis Blades</b> (+3, Light, Finesse, Nick): +14, 1d10+8 slashing, three per Attack action and a fourth from Nick; Sneak Attack +5d6 once a turn; <b>Vulnerability Analytics</b> makes his first hit each turn a critical. <b>Scalpel</b> (+3 electric katana): +14, 1d10+8 lightning, three per Attack action, his choice against anything that shorts out. <b>Malorian Arms 3516</b> (+3 pistol): +14, 2d8+8 piercing, 60/180 ft, Sharpshooter. Action Surge once a short rest, Second Wind four times (1d10+11).", stat),
 P("<b>Feats</b> Crafter (Nomad), Alert (Human), Sharpshooter, Tough, +2 Dex, +2 Int ×2 · <b>Rogue 9</b> Expertise ×4, Sneak Attack 5d6, Cunning Action, Steady Aim, Cunning Strike, Uncanny Dodge, Evasion, Reliable Talent; Arcane Trickster: Mage Hand Legerdemain, Magical Ambush · <b>Fighter 11</b> Two-Weapon Fighting, Second Wind, Action Surge, Tactical Mind, Tactical Shift, Indomitable, Tactical Master, three attacks; Battle Master: Precision Attack, Riposte, Trip, Feinting, Evasive Footwork, Disarming, Menacing; Know Your Enemy", stat),
 P("<b>How he fights.</b> He chooses the chrome before he walks in. With the Sandevistan: switch it on, let Ticking Time Bomb stun the ring around him, and take eight blade swings in the time it takes anyone else to blink, a Jailbreak leap after every crit or kill. With the deck: Optical Camo first, then a queue out of hiding (Synapse Burnout, Short Circuit), Blackwall Gateway when there's a crowd, and the blades when the RAM runs dry. Against Smasher it's the Sandevistan and the Scalpel, because twenty volts' worth of anything turns the borg's reactions off.", stat)]
box = Table([[f] for f in block], colWidths=[W]); box.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),PARCH),("BOX",(0,0),(-1,-1),1.0,GREEN),("LEFTPADDING",(0,0),(-1,-1),11),("RIGHTPADDING",(0,0),(-1,-1),11),("TOPPADDING",(0,0),(-1,-1),1),("BOTTOMPADDING",(0,0),(-1,-1),1),("TOPPADDING",(0,0),(-1,0),9),("BOTTOMPADDING",(0,-1),(-1,-1),9)])); S.append(box)

S.append(PageBreak())
S.append(P("The chrome", h2)); S.append(rule())
S.append(P("Every item below is homebrew, built on the 2024 magic-item rules and written from the game's own numbers. In 2.x the armor is in the cyberware, not the jacket, so his AC is his skin. He runs well over his cyberware capacity: <b>Edgerunner</b> (Technical Ability 20) lets him, at the cost of a little health he can spare.", small))
S.append(P("Operating System: one slot, chosen before the fight", hb_name))
S.append(hb("Militech “Apogee” Sandevistan", "Legendary · OS slot · in the game: 85% time slow, 6 seconds, a 25-second cooldown, +20% crit chance and crit damage, kills extend it",
 "Bonus Action. For 3 rounds the world runs at a crawl: on each of his turns he takes one extra action (any action), he has +2 AC and Advantage on Dexterity saves, attack rolls against him have Disadvantage, and his weapon attacks score a critical hit on an 18–20. Each creature he kills while it runs adds a round. It comes back three rounds after it ends, or on a short rest. <b>Ticking Time Bomb</b> (Technical Ability 20): switching it on fires an EMP: each enemy within 10 ft makes a DC 19 Constitution save or is Stunned until the start of his next turn. A Sandevistan user who sees him switch on can answer with his own (Smasher's Counter-Sandevistan)."))
S.append(hb("Militech Canto Mk.6", "Legendary cyberdeck · OS slot · from Somewhat Damaged (Phantom Liberty) · the only deck that runs Blackwall Gateway",
 "With the deck installed, his Arcane Trickster spellcasting is quickhacking: he doesn't use spell slots, he spends <b>RAM</b> (20, regaining 4 at the start of each of his turns). As an action he uploads a queue of up to two quickhacks to creatures he can see within 60 ft, and the last one costs half (<b>Queue Mastery</b>); as a Bonus Action he uploads one costing 2 RAM or less. Save DC 19. <b>Magical Ambush</b>: a quickhack uploaded while he's hidden or invisible gives the target Disadvantage on the save. A creature with ICE can hack back (Smasher's does)."))
S.append(P("Arms, nervous system, skeleton, skin", hb_name))
S.append(hb("Mantis Blades (Tier 5++)", "Legendary · arms · +3 · the blades from the trailers, and the reason the Relic's Jailbreak exists",
 "Martial melee weapons, Light and Finesse, 1d10 slashing, mastery Nick; with Two-Weapon Fighting he makes four attacks per Attack action. <b>Jailbreak</b> (Relic): a critical hit or a kill charges a leap: as a Bonus Action he jumps up to 30 ft at a creature and makes one Mantis Blade attack that's a critical hit if it hits. <b>Spatial Mapping</b> (Relic): a leap that hits leaves the target's Speed at 0 until the end of its next turn."))
S.append(hb("Second Heart", "Legendary · circulatory · in the game: back to 100% health at 0, every 240 seconds", "The first time he drops to 0 HP and isn't killed outright, he's at his hit point maximum instead. Recharges on a long rest."))
S.append(hb("Reflex Tuner and Kerenzikov", "Epic · nervous system", "<b>Reflex Tuner:</b> the first time each day he falls below 50 HP, time slows for him until the end of his next turn: attack rolls against him have Disadvantage. <b>Kerenzikov:</b> when he Dashes or Disengages, his next attack before the end of the turn has Advantage, and the Jinchu-Maru scores a critical hit with it on a 19–20."))
S.append(hb("Chitin, Optical Camo, Kiroshi optics, reinforced tendons", "Epic and legendary · skin, integumentary, eyes, legs",
 "<b>Chitin</b> (Phantom Liberty subdermal armor): AC 13 + Dex. <b>Optical Camo</b>: Bonus Action, once a short rest: he's Invisible until he hits with a weapon; <b>Emergency Cloaking</b> (Relic) means switching it on in a fight makes enemies lose track of him. <b>Kiroshi optics</b>: scanning is his Know Your Enemy, and <b>Vulnerability Analytics</b> (Relic) shows weak points: his first weapon hit each turn is a critical hit. <b>Reinforced tendons</b>: a double jump, and no damage from falls of 20 ft or less."))
S.append(hb("The Relic", "Artifact · his skull · not a power, a clock",
 "The biochip Konpeki put in his head. Johnny Silverhand's engram is overwriting him, and the damage stays even after the chip comes out: Alt and the doctors give him about six months. In play it's a story clock, not a mechanic. The Relic tree from Dogtown is on this sheet (Jailbreak, Spatial Mapping, Emergency Cloaking, Vulnerability Analytics, Machine Learning); Johnny is not. He talks, he's right more often than V would like, and on the roof at Embers he's the one who says let's go in alone."))

S.append(P("Quickhacks (with the Canto installed)", h2)); S.append(rule())
qrows = [("Short Circuit","2","Con","6d10 lightning, half on a save; +2d10 against a full-body cyborg or a machine. Twenty lightning from one source shorts Smasher out."),
 ("Overheat","3","Con","3d10 fire, and 2d10 at the end of each of its next two turns; half and no burn on a save."),
 ("Synapse Burnout","5","Int","8d10 psychic, +2d10 if the target is below half its HP; half on a save."),
 ("Contagion","3","Con","3d8 poison and Poisoned, then the same to one more enemy within 30 ft; half and no condition on a save."),
 ("Reboot Optics","3","Con","Disadvantage on its attacks until the end of its next turn."),
 ("Weapon Glitch","2","—","No save: its next attack roll has Disadvantage."),
 ("Blackwall Gateway","8","Con","Canto only. 8d10 necrotic to the target and up to two more within 60 ft; half on a save. Robots and turrets shut down."),
 ("Cripple Movement, Sonic Shock","2","—","Speed 0 / Deafened and no calls for help, until the end of its next turn."),
 ("Cyberpsychosis","8","Wis","As Dominate Person, and it attacks its own side. Not on a boss."),
 ("Memory Wipe, Suicide, System Collapse","4–10","—","Drop out of the fight, kill itself, black out. None of them work on a boss.")]
S.append(grid([[P("Quickhack", cellhead), P("RAM", cellhead), P("Save", cellhead), P("Effect (DC 19)", cellhead)]] + [[P(a, cellb), P(b, cell), P(c, cell), P(d_, cell)] for a, b, c, d_ in qrows], [1.55*inch, 0.45*inch, 0.45*inch, W-2.45*inch]))
S.append(P("Bosses are what the game says they are: the instant kills don't land on them. Everyone in the arena counts as one.", small))

S.append(P("What he carries", h2)); S.append(rule())
S.append(bullets([
 "<b>Malorian Arms 3516</b>, Johnny's hand cannon, taken off Grayson in <i>Chippin' In</i>. <b>Overwatch</b>, the silenced sniper rifle, for saving Saul in <i>Riders on the Storm</i>. <b>Amnesty</b>, Cassidy's revolver, from the bottle game in <i>We Gotta Live Together</i>.",
 "<b>Scalpel</b> (<i>Big in Japan</i>), <b>Satori</b> (the Konpeki helipad), <b>Jinchu-Maru</b> (Oda, <i>Play It Safe</i>), <b>Byakko</b> (all of Wakako's gigs). <b>La Chingona Dorada</b>, Jackie's pistols, from the ofrenda in <i>Heroes</i>. <b>Skippy</b>, who talks. <b>Kongou</b> from Yorinobu's nightstand.",
 "From Dogtown: <b>Rasetsu</b>, <b>Hawk</b>, <b>Kyubi X-MOD2</b>, <b>Rosco</b> off Dodger, and the Canto Mk.6's spec from Cynosure. Divided We Stand, Prejudice, Problem Solver, Death and Taxes, Mox and the rest of the iconic wall in the apartment.",
 "Panam's Basilisk at his back, the car he drove out of the Badlands, and Delamain on call."]))

S.append(P("Build, level by level", h2)); S.append(rule())
S.append(P("Point buy 8 / 15 / 14 / 15 / 10 / 8, Nomad +2 Dex, +1 Int: Str 8, Dex 17, Con 14, Int 16, Wis 10, Cha 8. Rogue first for Dexterity and Intelligence saves. Two Origin feats (Crafter from the background, Alert from the Human), five ASIs.", small))
rows = [("1","Rogue 1","Expertise (Stealth, Acrobatics), Sneak Attack 1d6, masteries; Crafter, Alert","Yucca. The Bakker clan casts him out; a stolen car, a border run, and Jackie Welles"),
 ("2","Rogue 2","Cunning Action","Six months of jobs with Jackie: Night City from the bottom"),
 ("3","Rogue 3","Arcane Trickster: Mage Hand Legerdemain, a first deck; Steady Aim","Viktor Vektor's chair: Kiroshis and a Paraline. The Rescue"),
 ("4","Rogue 4","+2 Int (18)","The Pickup: Dex, Maelstrom, the Flathead"),
 ("5","Rogue 5","Cunning Strike, Uncanny Dodge, Sneak Attack 3d6","The Heist: Konpeki Plaza, Saburo dead, Jackie dead, a bullet from Dex. The Relic"),
 ("6","Fighter 1","Two-Weapon Fighting, Second Wind, masteries","Playing for Time: he wakes up in a landfill with Johnny Silverhand in his head"),
 ("7","Fighter 2","Action Surge, Tactical Mind","Automatic Love and The Space in Between: Evelyn, Judy, Fingers"),
 ("8","Fighter 3","Battle Master: Precision, Riposte, Trip","Mantis Blades from Vik; Takemura; Never Fade Away"),
 ("9","Fighter 4","+2 Dex (19)","Ghost Town, Lightning Breaks: Panam, Saul, the Aldecaldos. Riders on the Storm"),
 ("10","Fighter 5","Extra Attack, Tactical Shift","Chippin' In: Grayson, the Malorian, Johnny's Porsche, Rogue"),
 ("11","Fighter 6","Sharpshooter (Dex 20)","Queen of the Highway: the Basilisk, and Panam"),
 ("12","Fighter 7","Know Your Enemy; Feinting, Evasive Footwork","Tapeworm: Johnny's past and V's future in the same head"),
 ("13","Fighter 8","+2 Int (20)","Phantom Liberty: Dogtown, Songbird, the President's plane"),
 ("14","Fighter 9","Indomitable, Tactical Master","Firestarter: Hansen, the Black Sapphire, the Relic tree"),
 ("15","Fighter 10","Combat Superiority d10; Disarming, Menacing","Somewhat Damaged: Cynosure, the Cerberus, the Canto"),
 ("16","Fighter 11","Three attacks","The Killing Moon: Reed. Songbird gets her answer, and The Tower is off the table"),
 ("17","Rogue 6","Expertise (Investigation, Perception)","Psycho Squad, the gigs, Delamain's fragments, Beat on the Brat: Street Cred 50"),
 ("18","Rogue 7","Evasion, Reliable Talent","The Apogee from a ripperdoc; Johnny at 70% and rising"),
 ("19","Rogue 8","Tough","Nocturne Op55N1: the roof at Embers, and five minutes of saying nothing"),
 ("20","Rogue 9","Magical Ambush, Sneak Attack 5d6","Don't Fear the Reaper: Arasaka Tower alone, Smasher, Mikoshi, Alt. He goes back to his body")]
S.append(grid([[P("Lvl", cellhead), P("Class", cellhead), P("What you get", cellhead), P("Where in the story", cellhead)]] + [[P(a, cellb), P(b, cell), P(c, cell), P(d_, cell)] for a, b, c, d_ in rows], [0.4*inch, 0.8*inch, 2.75*inch, W-3.95*inch]))

S.append(PageBreak()); S.append(P("Snapshots by arc, with the feat checked", h2)); S.append(rule())
def snap(name, where, lvl, lines, checked):
    content = [P(name, snapname), P(where + "  ·  " + lvl, stattag)] + [P(l, snapline) for l in lines] + [P("<b>The feat, checked.</b> " + checked, snapline)]
    t = Table([[content]], colWidths=[W]); t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),PARCH),("LINEBEFORE",(0,0),(0,-1),2.5,GREEN),("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)]))
    return KeepTogether([t, Spacer(1,7)])
S.append(snap("The Nomad", "the prologue: Yucca to Night City", "Levels 1–2 · Rogue 1–2", ["Dex 17, Int 16 · <b>AC</b> 14 (leather) · <b>HP</b> 10 → 17 · a pistol and a crowbar · Sneak Attack 1d6 · Crafter: he keeps the car running"], "A Bakker who won't stay a Bakker is an Expertise in Stealth and a Cunning Action: the border crossing is a Stealth check at +7 against a border patrol's passive Perception of 12, and he makes it with a car full of iguana."))
S.append(snap("Konpeki Plaza", "The Heist", "Level 5 · Rogue 5", ["<b>HP</b> 38 · Uncanny Dodge · Sneak Attack 3d6 · the Flathead and Jackie on the job"], "Arasaka's tower hotel is a CR 9 facility with CR 5 guards and Saburo's own security. The Rogue gets in (Stealth +9 with Expertise) and gets out with Jackie dying in the cab. What he can't survive is Dex's bullet to the head at point-blank: the sheet agrees, and so does the game. The Relic is why there's a level 6."))
S.append(snap("The Aldecaldos", "Ghost Town to Queen of the Highway", "Levels 9–11 · Fighter 4–6", ["Dex 19 → 20 · <b>HP</b> 70 → 86 · Extra Attack, Action Surge · the Malorian and Overwatch"], "Riders on the Storm is a Wraith camp: CR 2 raiders by the dozen and Saul in a cage. Two Mantis Blade attacks with Sneak Attack and an Action Surge empty a room a turn, and the sheet's job is to keep him on his feet while Panam yells at him over the radio. The Basilisk scene is a Persuasion check he doesn't need to make."))
S.append(snap("Dogtown", "Phantom Liberty: Songbird, Reed, the Cynosure", "Levels 13–16 · Fighter 8–11", ["Int 20 · <b>HP</b> 102 → 126 · Indomitable · d10 dice · the Relic tree · the Canto Mk.6"], "The Cerberus in Cynosure is a CR 18 construct that hunts by sound. Blackwall Gateway and Short Circuit from Optical Camo (Magical Ambush: Disadvantage on its saves) is the netrunner's answer, and the Canto is the deck that came out of that room. He sides with Songbird; Reed falls at the Killing Moon; the FIA's cure, and the life without chrome it costs, never comes up."))
S.append(snap("Don't Fear the Reaper", "Act 3, the secret ending", "Level 20 · Rogue 9 / Fighter 11", ["The headline block: AC 18, 194 HP, Second Heart, the Apogee, the Scalpel"], "No Panam, no Rogue, no Hanako: one merc and a ghost through the lobby, the netrunner floor, the mainframe and the Smasher arena, with no save game to reload. In the arena on Caleb's sheet, V with the Sandevistan beats Adam Smasher a little under half the time (about 42–47% over 300 fights). That's the honest number for a fight the game lets you retry, and the sheet doesn't pretend otherwise: it's a coin flip with a dead man's gun on the table, and canon is the flip that came up."))

S.append(P("After Mikoshi: the road out", h2)); S.append(rule())
S.append(P("Alt offers him the Blackwall and he says no. He wakes up in his own body with six months on the clock, a nation of fixers who know his name, and Mr. Blue Eyes on the line with a job at the Crystal Palace. <b>Headcanon from here, not the game:</b> he doesn't take it. He drives out to the Aldecaldo camp at the edge of the Badlands, and Panam is there, and the clan that took in a Bakker castoff takes him in again. Whatever's left of the six months he spends on the road. The game's Star ending is where the Aldecaldos leave Night City with him; this sheet just gets him there the hard way."))
S.append(KeepTogether([P("A DM's dial", h2), rule(), P("Two knobs. The Sandevistan's Disadvantage on attacks against him is the biggest number on the sheet: take it out and he's a strong Solo who trades blows instead of slipping them. Vulnerability Analytics' free critical once a turn is the other: make it once a round on a recharge if the table finds it too much. Leave Second Heart alone. It's the most V thing he owns: Konpeki proved he dies, and every act after it proved he doesn't stay that way.")]))
doc.build(S, onFirstPage=on_page, onLaterPages=on_page); print("ok")
