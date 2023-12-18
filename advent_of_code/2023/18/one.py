from pathlib import Path

result = 0

commands = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

x = 0
y = 0
perimeter = 0
area = 0


def draw(line):
    global x, y, perimeter, area
    command, step, color = line.split()
    dx, dy = commands[command]
    step = int(step)
    dx, dy = step * dx, step * dy
    x, y = x + dx, y + dy
    perimeter += step
    area += y * dx


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    for line in lines:
        draw(line)
    result = area + perimeter // 2 + 1


assert result == 47675
print(result)
