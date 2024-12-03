import re
from pathlib import Path

result = 0

with open(Path(__file__).parent / "input.txt", encoding="utf-8") as f:
    lines = f.read()
    exp = r"mul\((\d{1,3}),(\d{1,3})\)"
    result = sum(int(a) * int(b) for a, b in re.findall(exp, lines))


assert result == 153469856
print(result)
