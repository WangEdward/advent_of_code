import re
from pathlib import Path

result = 0

with open(Path(__file__).parent / "input.txt", encoding="utf-8") as f:
    lines = f.read()
    exp = r"mul\((\d{1,3}),(\d{1,3})\)"
    # re.finditer returns an iterator yielding match objects
    # https://docs.python.org/3/library/re.html#match-objects
    for m in re.finditer(exp, lines):
        cur = m.start(0)
        do_index = lines.rfind("do()", 0, cur)
        dont_index = lines.rfind("don't()", 0, cur)
        # equal when both not found
        if do_index >= dont_index:
            result += int(m.group(1)) * int(m.group(2))


assert result == 77055967
print(result)
