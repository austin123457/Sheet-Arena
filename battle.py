#!/usr/bin/env python3
"""battle.py — run fights between the sheets.

  python battle.py 1v1 slayer link -n 400          one matchup, win rates
  python battle.py team slayer+guy smasher+jin     teams, '+' joins a side
  python battle.py ffa slayer link guy smasher     free-for-all
  python battle.py matrix -n 200                   every 1v1, win% grid
  python battle.py solo link -n 100                one fighter vs everyone else at once
  python battle.py list                            the roster

Dice come from the OS (secrets); nothing is seeded. Fights cap at 40 rounds (a draw)."""
import argparse
from sim.engine import ROUND_CAP
from sim.roster import make, NAMES, Fight, Counter

ROSTER = ["slayer", "link", "anderson", "guy", "smasher", "beast", "jin", "guts", "itachi", "crane", "arthur", "spike", "gs", "talion"]

def run(teams, n):
    wins = Counter(); rounds = 0; draws = 0
    for _ in range(n):
        f = Fight([[make(x) for x in t] for t in teams]); res, r = f.run(); rounds += r
        if r >= ROUND_CAP: draws += 1
        else: wins[res] += 1
    return wins, draws, rounds / n

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["1v1", "team", "ffa", "matrix", "solo", "list"])
    ap.add_argument("fighters", nargs="*")
    ap.add_argument("-n", type=int, default=300, help="fights per matchup")
    a = ap.parse_args()
    if a.mode == "list":
        for k in ROSTER: print(f"{k:10s} -> {NAMES[k]}")
        return
    if a.mode == "1v1":
        A, B = a.fighters[:2]; w, dr, r = run([[A], [B]], a.n)
        print(f"{A} {100*w[0]/a.n:.1f}%  {B} {100*w[1]/a.n:.1f}%  draws {100*dr/a.n:.0f}%  avg {r:.1f} rounds")
    elif a.mode == "team":
        teams = [t.split("+") for t in a.fighters]; w, dr, r = run(teams, a.n)
        for i, t in enumerate(teams): print(f"{'+'.join(t):24s} {100*w[i]/a.n:.1f}%")
        print(f"draws {100*dr/a.n:.0f}%  avg {r:.1f} rounds")
    elif a.mode == "ffa":
        names = a.fighters or ROSTER; w, dr, r = run([[x] for x in names], a.n)
        for i, x in sorted(enumerate(names), key=lambda kv: -w[kv[0]]): print(f"{x:10s} {100*w[i]/a.n:.0f}%")
        print(f"draws {100*dr/a.n:.0f}%  avg {r:.1f} rounds")
    elif a.mode == "solo":
        A = a.fighters[0]; others = [x for x in ROSTER if x != A]; w, dr, r = run([[A], others], a.n)
        print(f"{A} alone vs {len(others)}: {100*w[0]/a.n:.1f}%  avg {r:.1f} rounds")
    elif a.mode == "matrix":
        names = a.fighters or ROSTER
        print("row beats column (%)"); print(" " * 10 + " ".join(f"{x[:6]:>6s}" for x in names))
        for A in names:
            row = []
            for B in names:
                if A == B: row.append("     -"); continue
                w, dr, r = run([[A], [B]], a.n); row.append(f"{100*w[0]/a.n:6.0f}")
            print(f"{A:10s}" + " ".join(row))

if __name__ == "__main__":
    main()
