from pathlib import Path

result = 0

with open(Path(__file__).parent / "input.txt", encoding="utf-8") as f:
    lines = f.read().split("\n")
    a, b = map(list, zip(*[list(map(int, line.split("   "))) for line in lines]))
    a.sort()
    b.sort()
    result = sum(abs(a[i] - b[i]) for i in range(len(a)))


assert result == 2113135
print(result)
