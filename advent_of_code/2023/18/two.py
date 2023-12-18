from pathlib import Path

result = 0

commands = {
    "3": (-1, 0),
    "1": (1, 0),
    "2": (0, -1),
    "0": (0, 1),
}

x = 0
y = 0
perimeter = 0
area = 0


def draw(line):
    global x, y, perimeter, area
    color = line.split()[2]
    command = color[7]
    step = int(color[2:7], 16)
    dx, dy = commands[command]
    dx, dy = step * dx, step * dy
    x, y = x + dx, y + dy
    perimeter += step
    area += y * dx


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    for line in lines:
        draw(line)
    result = area + perimeter // 2 + 1


assert result == 122103860427465
print(result)
