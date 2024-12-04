from pathlib import Path

result = 0


def check(x):
    return "".join(x).count("XMAS") + "".join(x).count("SAMX")


with open(Path(__file__).parent / "input.txt", encoding="utf-8") as f:
    lines = f.read().split("\n")
    rows = lines.copy()
    row_n = len(rows)
    result += sum(check(row) for row in rows)
    cols = list(zip(*lines))
    col_n = len(cols)
    result += sum(check(col) for col in cols)
    for i in range(row_n + col_n - 1):
        l = []
        r = []
        for j in range(i + 1):
            if 0 <= j < row_n and 0 <= i - j < col_n:
                l.append(lines[j][i - j])
            if 0 <= j < col_n and 0 <= row_n - 1 - (i - j) < row_n:
                r.append(lines[row_n - 1 - (i - j)][j])
        result += check(l) + check(r)


assert result == 2639
print(result)
