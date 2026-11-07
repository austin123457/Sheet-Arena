"""Might Guy, the canon merge (command-line name guy): Caleb's chassis, Night Guy at 60d12+15,
advantage on Evening Elephant, and Daytime Tiger at 30d12+7 when two or more melee enemies crowd him.
Sheet: Might_Guy_Canon_5e_Build.pdf."""
from ..engine import roll
from .guy_caleb import GuyCaleb


class GuyCanon(GuyCaleb):
    name = "GuyC"
    night_dice = 60
    g8_adv = True

    def turn(self, fight):
        enemies = fight.enemies(self)
        if not enemies: return
        cluster = [e for e in enemies if e.melee]
        # a crowd: seven gates open, 3+ Focus, two or more melee enemies -> Daytime Tiger instead of the Attack action
        if self.gate == 7 and self.g8 is None and self.focus >= 3 and len(cluster) >= 2 and self.hp >= 70:
            self.hp -= (14 if self.gate >= 6 else self.gate)
            if self.hp <= 0: self.out = True; return
            self.focus -= 3; self.hp -= roll(4, 10)
            if self.hp <= 0: self.out = True; return
            for e in cluster:
                dmg = roll(30, 12) + 7
                if e.save("Dex", 16):
                    if e.evasion: continue
                    dmg //= 2
                else: e.prone = True
                e.take(dmg, "force", "Daytime Tiger")
            return
        return super().turn(fight)
