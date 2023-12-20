from pathlib import Path
from collections import defaultdict

result = 0

results = []
rules = {}
conjunctions = defaultdict(set)

queue = []


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
    results[-1][pulse] += 1
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


def enqueue(pulse, dsts, src):
    for i in dsts:
        queue.append((pulse, i, src))


last_f = []


def reset():
    global queue
    results.append([0, 0])
    queue = [(False, "roadcaster", "but")]
    f_status = []
    for k, item in rules.items():
        if item[1] == "%":
            f_status.append(item[2])
        else:
            rules[k][2] = False
    if f_status in last_f or len(last_f) > 999:
        return len(last_f)
    last_f.append(f_status)
    return False


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
    while not (count := reset()):
        solve()
    a_count = b_count = 0
    for a, b in results:
        a_count += a
        b_count += b
    result = a_count * b_count * (1000 // count) ** 2


assert result == 743871576
print(result)
