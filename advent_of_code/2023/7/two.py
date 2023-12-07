from pathlib import Path
from collections import Counter, defaultdict

result = 0

cards = defaultdict(list)


def calc_power(card_str):
    num_j = card_str.count("J")
    card = sorted(
        Counter(card_str.replace("J", "")).items(),
        key=lambda item: item[1],
        reverse=True,
    )
    if num_j == 5:
        return 6
    match card[0][1] + num_j:
        case 5:
            return 6
        case 4:
            return 5
        case 3:
            return 4 if card[1][1] == 2 else 3
        case 2:
            return 2 if card[1][1] == 2 else 1
        case 1:
            return 0
    return


def parse_card_str(card_str):
    card_str = (
        card_str.replace("T", "B").replace("K", "Y").replace("A", "Z").replace("J", "1")
    )
    return card_str


def parse_line(line):
    card_str, bid = line.split()
    power = calc_power(card_str)
    cards[power].append((parse_card_str(card_str), bid))


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.read().split("\n")
    for line in lines:
        parse_line(line)

    for power, card in cards.items():
        cards[power] = sorted(card, key=lambda item: item[0])

    count = 1
    for i in range(7):
        for card in cards[i]:
            result += int(card[1]) * count
            count += 1

assert result == 253473930
print(result)
