from pathlib import Path

NUM_MAP = [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', None, '1', '2', '3', '4', '5', '6', '7', '8', '9']

result = 0

with open(Path(__file__).parent / "input.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        left = right = 0
        left_index = 1e3
        right_index = -1
        for index_i, i in enumerate(NUM_MAP):
            if i:
                l_index = line.find(i)
                r_index = line.rfind(i)
                if l_index != -1 and l_index < left_index:
                    left_index = l_index
                    left = index_i % 10
                if r_index > right_index:
                    right_index = r_index
                    right = index_i % 10
        num = left * 10 + right
        result += num

assert result == 54418
print(result)
