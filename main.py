#!/usr/bin/env python3
"""Write one small good thing from today to /output/entry.txt."""

import os

LINE = "This morning the bus driver waited while an old man shuffled across the road, then tapped the horn twice \u2014 not a warning, just a hello \u2014 and the whole bus smiled."

def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(LINE))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
