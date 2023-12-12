from pathlib import Path
from functools import cache
import re

result = 0


def solve(line):
    status, pattern = line.split()
    pattern = tuple(map(int, pattern.split(",")))
    status = re.sub(r"\.+", ".", status)
    status = status + f"?{status}" * 4
    pattern *= 5
    return calc((status, pattern))


@cache
def calc(row):
    line, pattern = row
    if len(pattern) == 0:
        return line.count("#") == 0
    if line == "":
        return 0
    if line[0] == ".":
        return calc((line[1:], pattern))
    elif line[0] == "#":
        if len(line) < pattern[0]:
            return 0
        if len(line) > pattern[0] and line[pattern[0]] == "#":
            return 0
        if line[: pattern[0]].count(".") != 0:
            return 0
        return calc((line[pattern[0] + 1 :], pattern[1:]))
    else:
        return calc((f"#{line[1:]}", pattern)) + calc((line[1:], pattern))


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    for line in lines:
        result += solve(line)


assert result == 6720660274964
print(result)
