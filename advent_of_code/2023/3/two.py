from pathlib import Path
from collections import defaultdict


result = 0
d = defaultdict(list)


def parse_map(lines):
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == '*':
                d[(x, y)] = []


def check_range(start_y, end_y, x, k):
    for y in range(start_y - 1, end_y + 1):
        for _x in range(x - 1, x + 2):
            if (_x, y) in d:
                d[(_x, y)].append(int(k))


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
                    check_range(start_y=y - len(tmp_num), end_y=y, x=x, k=tmp_num)
                    tmp_num = ""
    for _, v in d.items():
        if len(v) == 2:
            result += v[0]*v[1]
    print(result)
