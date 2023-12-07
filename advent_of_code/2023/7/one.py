from pathlib import Path
from collections import Counter, defaultdict

result = 0

cards = defaultdict(list)


def calc_power(card_str):
    card = sorted(Counter(card_str).items(), key=lambda item: item[1], reverse=True)
    match card[0][1]:
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
    card_str = card_str.replace("T", "B").replace("K", "Y").replace("A", "Z")
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

assert result == 253933213
print(result)
