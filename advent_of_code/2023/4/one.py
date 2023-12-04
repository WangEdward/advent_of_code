from pathlib import Path
import re

ORDER_REGEX = r"Card\s+(\d+)"

result = 0


def parse_input(line):
    line = line.split(": ")[1].split(" | ")
    wining = re.split(r"\s+", line[0].strip())
    having = re.split(r"\s+", line[1].strip())
    count = sum(i in having for i in wining)
    return 2 ** (count - 1) if count else 0


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    for line in lines:
        game = parse_input(line)
        result += game

assert result == 18653
print(result)
