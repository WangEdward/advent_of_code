from pathlib import Path
from collections import defaultdict
import re

ORDER_REGEX = r"Card\s+(\d+)"


result = 0
d = defaultdict(lambda: 1)


def parse_input(line):
    order = int(re.findall(ORDER_REGEX, line)[0])
    line = line.split(": ")[1].split(" | ")
    wining = re.split(r"\s+", line[0].strip())
    having = re.split(r"\s+", line[1].strip())
    count = sum(i in having for i in wining)
    current_round = d[order - 1]
    for i in range(order, order + count):
        d[i] += current_round
    return current_round


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    for line in lines:
        game = parse_input(line)
        result += game

assert result == 5921508
print(result)
