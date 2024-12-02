from pathlib import Path

result = 0

with open(Path(__file__).parent / "input.txt", encoding="utf-8") as f:
    lines = f.read().split("\n")
    a, b = map(list, zip(*[list(map(int, line.split("   "))) for line in lines]))
    result = sum(i * b.count(i) for i in a)


assert result == 19097157
print(result)
