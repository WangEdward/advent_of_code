from pathlib import Path

result = 0


all_rules = {}
other_rules = {}

queue = [("in", {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)})]

accepted = []
rejected = []


def store(line):
    name, rules = line.split("{")
    rules = rules[:-1].split(",")
    all_rules[name] = {}
    other_rules[name] = rules.pop()
    for i in rules:
        eq, go = i.split(":")
        all_rules[name][eq] = go


def solve():
    while queue:
        item = queue.pop(0)
        solve_single(item)


def solve_single(item):
    rule_id, data = item
    if rule_id == "A":
        accepted.append(data)
        return
    if rule_id == "R":
        rejected.append(data)
        return
    for rule, dst in all_rules[rule_id].items():
        c = rule[0]
        sign = rule[1]
        val = int(rule[2:])
        assert data[c][0] < val < data[c][1]
        tmp = data.copy()
        if sign == "<":
            tmp[c] = (data[c][0], val - 1)
            data[c] = (val, data[c][1])
        elif sign == ">":
            tmp[c] = (val + 1, data[c][1])
            data[c] = (data[c][0], val)
        queue.append((dst, tmp))
    queue.append((other_rules[rule_id], data))


with open(Path(__file__).parent / "input.txt") as f:
    commands = f.read().split("\n\n")[0]
    for line in commands.split("\n"):
        store(line)
    solve()
    for item in accepted:
        count = 1
        for start, end in item.values():
            count *= end - start + 1
        result += count


assert result == 132557544578569
print(result)
