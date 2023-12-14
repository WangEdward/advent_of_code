from pathlib import Path

result = 0


def cycle(grid):
    grid = list(map(list, grid))
    for _ in range(4):
        for x in range(width):
            empty = 0
            for y in range(width):
                match grid[y][x]:
                    case "O":
                        grid[y][x] = "."
                        grid[empty][x] = "O"
                        empty += 1
                    case "#":
                        empty = y + 1
        grid = list(map(list, zip(*grid[::-1])))
    return tuple(map(tuple, grid))


def solve(grid):
    results = {}
    for index in range(1000000000):
        grid = cycle(grid)
        if grid in results:
            last_index = results[grid]
            break
        else:
            results[grid] = index
    repeat = index - last_index
    reminder = (1000000000 - 1 - last_index) % repeat
    grid = list(results.keys())[list(results.values()).index(last_index + reminder)]
    return sum((width - index) * line.count("O") for index, line in enumerate(grid))


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    width = len(lines[0])
    assert width == len(lines)
    result = solve(lines)


assert result == 102509
print(result)
