from pathlib import Path

result = 0


def hash(s, current=0):
    if s == "":
        return current
    c = s[0]
    current += ord(c)
    current *= 17
    current %= 256
    return hash(s[1:], current)


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split(",")
    for line in lines:
        result += hash(line)


assert result == 508552
print(result)
