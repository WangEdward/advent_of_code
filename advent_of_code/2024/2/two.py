from pathlib import Path

result = 0

with open(Path(__file__).parent / "input.txt", encoding="utf-8") as f:
    lines = f.read().split("\n")
    lines = [list(map(int, line.split(" "))) for line in lines]
    for line in lines:
        for i in range(len(line)):
            tmp = line.copy()
            tmp.pop(i)
            diffs = {b - a for a, b in zip(tmp[:-1], tmp[1:])}
            if diffs <= {1, 2, 3} or diffs <= {-1, -2, -3}:
                result += 1
                break


assert result == 436
print(result)
