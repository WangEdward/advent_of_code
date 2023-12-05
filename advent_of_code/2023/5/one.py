from pathlib import Path

result = 0


def parse_block(block):
    rules = {}
    lines = block.split("\n")
    name = lines.pop(0)
    for line in lines:
        dst, src, _range = list(map(int, line.split()))
        rules[(src, src + _range)] = dst - src

    global seeds
    new_seeds = []
    for seed in seeds:
        for k in rules:
            if k[0] <= seed < k[1]:
                new_seeds.append(seed + rules[k])
                break
        else:
            new_seeds.append(seed)
    seeds = new_seeds


with open(Path(__file__).parent / "input.txt") as f:
    blocks = f.read().split("\n\n")
    seeds = list(map(int, blocks.pop(0)[7:].split()))
    for block in blocks:
        parse_block(block)
    result = min(seeds)

assert result == 510109797
print(result)
