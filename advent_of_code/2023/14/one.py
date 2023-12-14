from pathlib import Path

result = 0


def solve(lines):
    lines = list(zip(*lines))
    width = len(lines[0])
    count = 0
    for line in lines:
        score = width
        for index, c in enumerate(line):
            if c == "#":
                score = width - index - 1
            elif c == "O":
                count += score
                score -= 1
    return count


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    result = solve(lines)


assert result == 109424
print(result)
