from pathlib import Path

result = 0


def solve(line):
    seq = list(map(int, line.split()))
    diffs = []
    while any(seq):
        diffs.append(seq)
        tmp_seq = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
        seq = tmp_seq
    return sum(i[-1] for i in diffs)


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    for line in lines:
        result += solve(line)

assert result == 1882395907
print(result)
