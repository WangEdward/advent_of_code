from pathlib import Path
from collections import defaultdict

result = 0

with open(Path(__file__).parent / "input.txt", encoding="utf-8") as f:
    rules, updates = f.read().split("\n\n")
    dl = defaultdict(set)
    dr = defaultdict(set)
    for rule in rules.split("\n"):
        a, b = rule.split("|")
        dl[b].add(a)
        dr[a].add(b)
    for update in updates.split("\n"):
        ups = update.split(",")
        for i, u in enumerate(ups):
            if set(ups[:i]) - dl[u] or set(ups[i + 1 :]) - dr[u]:
                break
        else:
            result += int(ups[len(ups) // 2])


assert result == 4662
print(result)
