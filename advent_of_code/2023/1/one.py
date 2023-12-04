from pathlib import Path
import re

REGEX = r"[1-9]"

result = 0

with open(Path(__file__).parent / "input.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        nums = re.findall(REGEX, line)
        num = f"{nums[0]}{nums[-1]}"
        result += int(num)


assert result == 54304
print(result)
