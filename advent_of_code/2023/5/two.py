from pathlib import Path

result = 0


def two_min(a, b):  # sourcery skip: min-max-identity
    return a if a < b else b


def two_max(a, b):  # sourcery skip: min-max-identity
    return a if a > b else b


def normalize(a, b):
    return (a, b) if a < b else None


def parse_block(block):
    rules = {}
    lines = block.split("\n")
    name = lines.pop(0)
    for line in lines:
        dst, src, _range = list(map(int, line.split()))
        rules[(src, src + _range)] = dst - src
    rules = sorted(rules.items(), key=lambda x: x[0][0])

    global seeds
    new_seeds = []
    while seeds:
        seed = seeds.pop(0)
        for bound, offset in rules:
            left = normalize(seed[0], two_min(bound[0], seed[1]))
            new_seeds.append(left) if left else None
            middle = normalize(
                two_max(bound[0], seed[0]) + offset, two_min(bound[1], seed[1]) + offset
            )
            new_seeds.append(middle) if middle else None
            right = normalize(two_max(bound[1], seed[0]), seed[1])
            if not (seed := right):
                break
        else:
            new_seeds.append(seed)
    seeds = new_seeds


with open(Path(__file__).parent / "input.txt") as f:
    blocks = f.read().split("\n\n")
    seeds_raw = list(map(int, blocks.pop(0)[7:].split()))
    seeds = []
    while seeds_raw:
        seeds.append((seeds_raw[0], seeds_raw[0] + seeds_raw[1]))
        seeds_raw = seeds_raw[2:]
    for block in blocks:
        parse_block(block)
    result = min(seeds)[0]

assert result == 9622622
print(result)
