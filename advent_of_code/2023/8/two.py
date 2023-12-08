from pathlib import Path
import re
import math

REGEX = r"\w{3}"

routes = {}
result = []


def parse_line(line):
    source, left, right = re.findall(REGEX, line)
    routes[source] = (left, right)


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    instructions = lines.pop(0)
    lines.pop(0)
    for line in lines:
        parse_line(line)
    current = list(filter(lambda x: x.endswith("A"), routes.keys()))

    for x in current:
        result.append(0)
        instruction_pointer = 0
        while not x.endswith("Z"):
            x = (
                routes[x][0]
                if instructions[instruction_pointer] == "L"
                else routes[x][1]
            )
            instruction_pointer += 1
            result[-1] += 1
            instruction_pointer %= len(instructions)
    result = math.lcm(*result)

assert result == 21083806112641
print(result)
