from pathlib import Path

result = 0


def verify(a, b):
    count = 0
    for i in range(min(len(a), len(b))):
        if a[-i - 1] != b[i]:
            count += sum(a != b for a, b in zip(a[-i - 1], b[i]))
            if count > 1:
                return False
    return count == 1


def solve(block):
    lines = block.split("\n")
    for j in range(2):
        for i in range(1, len(lines)):
            count = sum(a != b for a, b in zip(lines[i], lines[i - 1]))
            if count <= 1 and verify(lines[:i], lines[i:]):
                return i if j == 1 else i * 100
        lines = list(zip(*lines))


with open(Path(__file__).parent / "input.txt") as f:
    blocks = f.read().split("\n\n")
    for block in blocks:
        result += solve(block)


assert result == 28806
print(result)
