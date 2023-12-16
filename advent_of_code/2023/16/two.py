from pathlib import Path
from collections import defaultdict
import sys

result = 0

previous = set()
sys.setrecursionlimit(10000)


def go(location, direction):
    x, y = location
    dx, dy = direction
    if x < 0 or y < 0 or x >= width or y >= width:
        previous.add(((x - dx), (y - dy)))
        return
    if location in d and direction in d[location]:
        return
    d[location].append(direction)
    c = lines[x][y]
    if c == "." or (c == "-" and dx == 0) or (c == "|" and dy == 0):
        go((x + dx, y + dy), direction)
    else:
        match c:
            case "/":
                go((x - dy, y - dx), (-dy, -dx))
            case "\\":
                go((x + dy, y + dx), (dy, dx))
            case _:
                go((x + dy, y + dx), (dy, dx))
                go((x - dy, y - dx), (-dy, -dx))


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    width = len(lines[0])
    assert width == len(lines)
    directions = (
        [((0, i), (1, 0)) for i in range(width)]
        + [((width - 1, i), (-1, 0)) for i in range(width)]
        + [((i, 0), (0, 1)) for i in range(width)]
        + [((i, width - 1), (0, -1)) for i in range(width)]
    )
    for direction in directions:
        if direction[0] not in previous:
            d = defaultdict(list)
            go(*direction)
            result = max(len(d), result)


assert result == 8335
print(result)
