from pathlib import Path
import math

result = 1


def floor(x):
    return int(x) if x % 1 else int(x) - 1


def ceil(x):
    return int(x) + 1


def race(time, distance):
    det = math.sqrt(time**2 - 4 * distance)
    return floor((time + det) / 2) - ceil((time - det) / 2) + 1


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    times = [int(x) for x in lines[0].split(":")[-1].split()]
    distances = [int(x) for x in lines[1].split(":")[-1].split()]
    for time, distance in zip(times, distances):
        result *= race(time, distance)

assert result == 512295
print(result)
