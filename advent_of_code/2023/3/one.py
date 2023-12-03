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
    for y in range(start_y - 1, end_y + 1):
        for _x in range(x - 1, x + 2):
            if (_x, y) in d:
                return True
    return False


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    parse_map(lines)
    for x, line in enumerate(lines):
        line += "."
        tmp_num = ""
        for y, char in enumerate(line):
            if char.isdigit():
                tmp_num += char
            else:
                if tmp_num:
                    if check_range(start_y=y - len(tmp_num), end_y=y, x=x):
                        result += int(tmp_num)
                    tmp_num = ""
    print(result)
