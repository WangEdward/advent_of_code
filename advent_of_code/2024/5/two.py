from pathlib import Path
from collections import defaultdict
from functools import cmp_to_key

result = 0

with open(Path(__file__).parent / "input.txt", encoding="utf-8") as f:
    rules, updates = f.read().split("\n\n")
    dl = defaultdict(set)
    for rule in rules.split("\n"):
        a, b = rule.split("|")
        dl[b].add(a)
    for update in updates.split("\n"):
        ups = update.split(",")
        tmp = ups.copy()
        ups.sort(key=cmp_to_key(lambda a, b: -1 if a in dl[b] else 1))
        result += int(ups[len(ups) // 2]) if tmp != ups else 0


assert result == 5900
print(result)
