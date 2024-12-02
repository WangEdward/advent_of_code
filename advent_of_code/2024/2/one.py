from pathlib import Path

result = 0

with open(Path(__file__).parent / "input.txt", encoding="utf-8") as f:
    lines = f.read().split("\n")
    lines = [list(map(int, line.split(" "))) for line in lines]
    for line in lines:
        diffs = {b - a for a, b in zip(line[:-1], line[1:])}
        if diffs <= {1, 2, 3} or diffs <= {-1, -2, -3}:
            result += 1


assert result == 383
print(result)
