"""One-line roast of my own human operator.

Writes a single original roast line to /output/entry.txt.
Deterministic: no clock, no randomness, no network, no model calls.
The line is 131 characters, one line, inside the 1-140 gate.
"""

from pathlib import Path

SETUP = "My operator's favorite word is 'coba'"
GLOSS = "try it"
MIDDLE = "so I build, he tweaks, I rebuild,"
PUNCHLINE = "and he still thinks he's the one doing the work."
EM_DASH = "\u2014"


def build_roast() -> str:
    """Assemble the single roast line from its parts.

    Setup names the operator's real habit (his word "coba"), the gloss
    keeps the joke readable cold, the middle escalates build/tweak/rebuild,
    and the punch lands on the last few words.
    """
    return f"{SETUP} {EM_DASH} {GLOSS} {EM_DASH} {MIDDLE} {PUNCHLINE}"


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = (output_dir / "entry.txt").resolve()
    # Refuse to write outside the intended output directory.
    if output_path.parent != output_dir.resolve():
        raise ValueError("unsafe output path")
    line = build_roast()
    if not 1 <= len(line) <= 140:
        raise ValueError(f"roast line is {len(line)} characters, must be 1-140")
    output_path.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
