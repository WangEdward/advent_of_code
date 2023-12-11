from pathlib import Path

result = 0


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    galaxies = []
    rows = list(range(len(lines)))
    columns = list(range(len(lines[0])))
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            if c == "#":
                galaxies.append((x, y))
                rows.remove(x) if x in rows else None
                columns.remove(y) if y in columns else None

    new_galaxies = []
    for x, y in galaxies:
        x = x + 999999 * sum(row < x for row in rows)
        y = y + 999999 * sum(column < y for column in columns)
        new_galaxies.append((x, y))

    for index_i, i in enumerate(new_galaxies):
        for j in new_galaxies[index_i:]:
            result += abs(i[0] - j[0]) + abs(i[1] - j[1])


assert result == 568914596391
print(result)
