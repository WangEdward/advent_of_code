from pathlib import Path
from itertools import cycle


result = 0
rocks = set()
dlist = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dtable = {"^": 0, ">": 1, "v": 2, "<": 3}
sp = None
sc = ""


def store(lines):
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            if c == "#":
                rocks.add((x, y))
            elif c != ".":
                global sp, sc
                sp = (x, y)
                sc = c


def go(new_rock):
    cp = sp
    directions = cycle(dlist[dtable[sc] :] + dlist[: dtable[sc]])
    cd = next(directions)
    locations = set()
    while (cp, cd) not in locations:
        locations.add((cp, cd))
        np = (cp[0] + cd[0], cp[1] + cd[1])
        if np in rocks or np == new_rock:
            cd = next(directions)
            continue
        if np[0] < 0 or np[0] >= length or np[1] < 0 or np[1] >= width:
            break
        cp = np
    else:
        return False
    return locations


with open(Path(__file__).parent / "input.txt", encoding="utf-8") as f:
    lines = f.read().split("\n")
    width = len(lines[0])
    length = len(lines)
    store(lines)
    route = set(i[0] for i in go(None))
    route.remove(sp)
    for x, y in route:
        if not go((x, y)):
            result += 1


assert result == 2143
print(result)
