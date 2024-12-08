import itertools
from pathlib import Path
from collections import defaultdict


result = 0
d = defaultdict(list)


with open(Path(__file__).parent / "input.txt", encoding="utf-8") as f:
    lines = f.read().split("\n")
    width = len(lines[0])
    length = len(lines)
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            if c != ".":
                d[c].append((x, y))

    antinodes = set()
    for locations in d.values():
        for (x1, y1), (x2, y2) in itertools.combinations(locations, 2):
            dx = x2 - x1
            for x in range(x1 % abs(dx), length, dx):
                y = y1 + (y2 - y1) * (x - x1) // dx
                if 0 <= y < width:
                    antinodes.add((x, y))
    result = len(antinodes)


assert result == 1246
print(result)
