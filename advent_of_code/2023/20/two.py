from pathlib import Path
from collections import defaultdict
from math import lcm

result = 0

rules = {}
conjunctions = defaultdict(set)

queue = []
results = {}

count = 0


def store(line):
    src, dst = line.split(" -> ")
    dst = dst.split(", ")
    rules[src[1:]] = [dst, src[0], False]


def solve():
    while queue:
        item = queue.pop(0)
        solve_single(item)


def solve_single(item):
    pulse, dst, src = item
    if dst in rules:
        dsts, t, on = rules[dst]
        match t:
            case "%":
                if not pulse:
                    on = not on
                    enqueue(on, dsts, dst)
            case "&":
                if pulse:
                    conjunctions[dst].discard(src)
                else:
                    conjunctions[dst].add(src)
                enqueue(bool(len(conjunctions[dst])), dsts, dst)
            case "b":
                enqueue(pulse, dsts, dst)
        rules[dst][2] = on
    elif (
        dst == "rx"
        and (len(conjunctions[src]) == 3)
        and tuple(conjunctions[src]) not in results.keys()
    ):
        global count
        results[tuple(conjunctions[src])] = count


def enqueue(pulse, dsts, src):
    for i in dsts:
        queue.append((pulse, i, src))


def init():
    conj = {k for (k, v) in rules.items() if v[1] == "&"}
    for k, v in rules.items():
        for dst in v[0]:
            if dst in conj:
                conjunctions[dst].add(k)


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    for line in lines:
        store(line)
    init()
    while len(results) != 4:
        count += 1
        queue = [(False, "roadcaster", "but")]
        solve()
    result = lcm(*results.values())


assert result == 244151741342687
print(result)
