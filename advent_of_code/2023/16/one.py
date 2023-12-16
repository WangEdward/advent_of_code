from pathlib import Path
from collections import defaultdict
import sys

result = 0

d = defaultdict(list)
sys.setrecursionlimit(10000)


def solve(location, direction):
    x, y = location
    if x < 0 or y < 0 or x >= width or y >= width:
        return
    if location in d and direction in d[location]:
        return
    d[location].append(direction)
    dx, dy = direction
    c = lines[x][y]
    if c == "." or (c == "-" and dx == 0) or (c == "|" and dy == 0):
        solve((x + dx, y + dy), direction)
    else:
        match c:
            case "/":
                solve((x - dy, y - dx), (-dy, -dx))
            case "\\":
                solve((x + dy, y + dx), (dy, dx))
            case _:
                solve((x + dy, y + dx), (dy, dx))
                solve((x - dy, y - dx), (-dy, -dx))


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    width = len(lines[0])
    assert width == len(lines)
    solve((0, 0), (0, 1))
    result = len(d)


assert result == 8098
print(result)
