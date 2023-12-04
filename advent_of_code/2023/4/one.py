from pathlib import Path
from collections import defaultdict
import re

ORDER_REGEX = r"Card\s+(\d+)"


result = 0


def parse_input(line):
    order = int(re.findall(ORDER_REGEX, line)[0])
    line = line.split(": ")[1].split(" | ")
    wining = re.split("\s+", line[0].strip())
    having = re.split("\s+", line[1].strip())
    count = 0
    for i in wining:
        if i in having:
            count += 1
    if count:
        return 2 ** (count - 1)
    else:
        return 0


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    for line in lines:
        game = parse_input(line)
        result += game

assert result == 18653
print(result)
