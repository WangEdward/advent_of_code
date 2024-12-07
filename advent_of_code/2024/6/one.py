from pathlib import Path
from itertools import cycle


result = 0
rocks = set()
locations = set()
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dtable = {"^": 0, ">": 1, "v": 2, "<": 3}
cp = None


def store(lns):
    for x, line in enumerate(lns):
        for y, c in enumerate(line):
            if c == "#":
                rocks.add((x, y))
            elif c != ".":
                locations.add((x, y))
                global cp, directions
                cp = (x, y)
                directions = cycle(directions[dtable[c] :] + directions[: dtable[c]])


with open(Path(__file__).parent / "input.txt", encoding="utf-8") as f:
    lines = f.read().split("\n")
    width = len(lines[0])
    length = len(lines)
    store(lines)
    cd = next(directions)
    while True:
        np = (cp[0] + cd[0], cp[1] + cd[1])
        if np in rocks:
            cd = next(directions)
            continue
        if np[0] < 0 or np[0] >= length or np[1] < 0 or np[1] >= width:
            break
        cp = np
        locations.add(cp)
    result = len(locations)


assert result == 5305
print(result)
