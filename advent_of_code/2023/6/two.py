from pathlib import Path
import math


def floor(x):
    return int(x) if x % 1 else int(x) - 1


def ceil(x):
    return int(x) + 1


def race(time, distance):
    det = math.sqrt(time**2 - 4 * distance)
    return floor((time + det) / 2) - ceil((time - det) / 2) + 1


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    time = int("".join(lines[0].split(":")[-1].split()))
    distance = int("".join(lines[1].split(":")[-1].split()))
    result = race(time, distance)

assert result == 36530883
print(result)
