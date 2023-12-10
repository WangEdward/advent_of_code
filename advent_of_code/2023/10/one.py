from pathlib import Path
from collections import defaultdict

result = 0

pipes = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    "S": [],
}


def get_s(x, y):
    if grid[(x - 1, y)] in ["|", "7", "F"]:
        pipes["S"].append((-1, 0))
    if grid[(x + 1, y)] in ["|", "L", "J"]:
        pipes["S"].append((1, 0))
    if grid[(x, y - 1)] in ["-", "L", "F"]:
        pipes["S"].append((0, -1))
    if grid[(x, y + 1)] in ["-", "7", "J"]:
        pipes["S"].append((0, 1))


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    grid = defaultdict(list)
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            grid[(x, y)] = c
            if c == "S":
                start = (x, y)

    get_s(*start)

    cur = start
    last = None
    while True:
        result += 1
        pipe = pipes[grid[cur]]
        for i in range(2):
            tmp = (cur[0] + pipe[i][0], cur[1] + pipe[i][1])
            if last != tmp:
                last = cur
                cur = tmp
                break
        if cur == start:
            break
    result //= 2


assert result == 7145
print(result)
