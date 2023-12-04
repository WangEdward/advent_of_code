import itertools
from pathlib import Path
from collections import defaultdict


result = 0
d = defaultdict(bool)


def parse_map(lines):
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char != "." and not char.isdigit():
                d[(x, y)] = True


def check_range(start_y, end_y, x):
    return any(
        (_x, y) in d
        for y, _x in itertools.product(
            range(start_y - 1, end_y + 1), range(x - 1, x + 2)
        )
    )


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    parse_map(lines)
    for x, line in enumerate(lines):
        line += "."
        tmp_num = ""
        for y, char in enumerate(line):
            if char.isdigit():
                tmp_num += char
            elif tmp_num:
                if check_range(start_y=y - len(tmp_num), end_y=y, x=x):
                    result += int(tmp_num)
                tmp_num = ""

assert result == 525181
print(result)
