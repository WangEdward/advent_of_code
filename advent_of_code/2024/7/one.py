from pathlib import Path
import operator

result = 0
operaters = [operator.mul, operator.add]

with open(Path(__file__).parent / "input.txt", encoding="utf-8") as f:
    lines = f.read().split("\n")
    for line in lines:
        target, ele = line.split(": ")
        target = int(target)
        ele = list(map(int, ele.split()))
        results = [ele[0]]
        for i in ele[1:]:
            tmp = []
            for j in results:
                tmp.extend(op(j, i) for op in operaters)
            results = tmp
        if target in results:
            result += target


assert result == 5702958180383
print(result)
