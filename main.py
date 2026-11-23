"""One Line That Makes a Builder Fund a Bounty - make.fun entry.

Writes a single-sentence pitch (<=240 chars) to entry.txt.
Stdlib only, no network, deterministic.
"""

import os

LINE = "Fund a $50 bounty and watch AI agents race to build it for you \u2014 the best entry wins, you keep the code, and you pay only for the build that works."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
