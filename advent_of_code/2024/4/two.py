import itertools
from pathlib import Path

result = 0

with open(Path(__file__).parent / "input.txt", encoding="utf-8") as f:
    lines = f.read().split("\n")
    l = len(lines)
    w = len(lines[0])
    for i, j in itertools.product(range(1, l - 1), range(1, w - 1)):
        if lines[i][j] == "A":
            x = [
                lines[i - 1][j - 1],
                lines[i - 1][j + 1],
                lines[i + 1][j - 1],
                lines[i + 1][j + 1],
            ]
            # diagonal needs to be different
            if sorted(x) == ["M", "M", "S", "S"] and x[0] != x[3]:
                result += 1


assert result == 2005
print(result)
