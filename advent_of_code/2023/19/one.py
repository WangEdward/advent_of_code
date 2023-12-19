from pathlib import Path

result = 0


all_rules = {}
other_rules = {}


def store(line):
    name, rules = line.split("{")
    rules = rules[:-1].split(",")
    all_rules[name] = {}
    other_rules[name] = rules.pop()
    for i in rules:
        eq, go = i.split(":")
        all_rules[name][eq] = go


def solve(line):
    line = line[1:-1].split(",")
    for i in line:
        exec(i, globals())
    current = "in"
    while True:
        for rule, dst in all_rules[current].items():
            if eval(rule):
                current = dst
                break
        else:
            current = other_rules[current]

        if current == "A":
            return x + m + a + s
        if current == "R":
            return 0


with open(Path(__file__).parent / "input.txt") as f:
    commands, datas = f.read().split("\n\n")
    for line in commands.split("\n"):
        store(line)
    for line in datas.split("\n"):
        result += solve(line)


assert result == 432434
print(result)
