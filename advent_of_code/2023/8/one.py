from pathlib import Path
import re

REGEX = r"\w{3}"

routes = {}
result = 0


def parse_line(line):
    source, left, right = re.findall(REGEX, line)
    routes[source] = (left, right)


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    instructions = lines.pop(0)
    lines.pop(0)
    for line in lines:
        parse_line(line)
    current = "AAA"
    instruction_pointer = 0
    while current != "ZZZ":
        if instructions[instruction_pointer] == "L":
            current = routes[current][0]
        else:
            current = routes[current][1]
        instruction_pointer += 1
        result += 1
        instruction_pointer %= len(instructions)

assert result == 21389
print(result)
