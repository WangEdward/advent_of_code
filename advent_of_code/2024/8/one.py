import itertools
from pathlib import Path
from collections import defaultdict


result = 0
d = defaultdict(list)


def store(lns):
    for x, line in enumerate(lns):
        for y, c in enumerate(line):
            if c != ".":
                d[c].append((x, y))


with open(Path(__file__).parent / "input.txt", encoding="utf-8") as f:
    lines = f.read().split("\n")
    width = len(lines[0])
    length = len(lines)
    store(lines)
    antinodes = set()
    for locations in d.values():
        for (x1, y1), (x2, y2) in itertools.combinations(locations, 2):
            if 0 <= x1 * 2 - x2 < length and 0 <= y1 * 2 - y2 < width:
                antinodes.add((x1 * 2 - x2, y1 * 2 - y2))
            if 0 <= x2 * 2 - x1 < length and 0 <= y2 * 2 - y1 < width:
                antinodes.add((x2 * 2 - x1, y2 * 2 - y1))
    result = len(antinodes)


assert result == 390
print(result)
