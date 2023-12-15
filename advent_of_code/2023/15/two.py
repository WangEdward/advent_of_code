from pathlib import Path
from collections import defaultdict

result = 0


def hash(s, current=0):
    if s == "":
        return current
    c = s[0]
    current += ord(c)
    current *= 17
    current %= 256
    return hash(s[1:], current)


d = defaultdict(dict)


def solve(line):
    if line[-1] == "-":
        s = line[:-1]
        h = hash(s)
        d[h].pop(s, None)
    else:
        s = line[:-2]
        h = hash(s)
        d[h][s] = int(line[-1])


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split(",")
    for line in lines:
        solve(line)
    for index_box, box in d.items():
        for index_slot, lens in enumerate(box.values()):
            result += (index_box + 1) * (index_slot + 1) * lens


assert result == 265462
print(result)
