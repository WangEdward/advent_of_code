from pathlib import Path
import re
from dataclasses import dataclass

ORDER_REGEX = r"Game (\d+)"
RED_REGEX = r"(\d+) red"
GREEN_REGEX = r"(\d+) green"
BLUE_REGEX = r"(\d+) blue"


@dataclass
class Game:
    order: int
    red: int
    green: int
    blue: int

    def is_valid(self):
        return self.red <= 12 and self.green <= 13 and self.blue <= 14

    def order_or_zero(self):
        return self.order if self.is_valid() else 0


games = []
result = 0


def parse_input(line: str) -> Game:
    order = int(re.findall(ORDER_REGEX, line)[0])

    red = re.findall(RED_REGEX, line)
    red = max(int(num) for num in red)

    green = re.findall(GREEN_REGEX, line)
    green = max(int(num) for num in green)

    blue = re.findall(BLUE_REGEX, line)
    blue = max(int(num) for num in blue)

    game = Game(order=order, red=red, green=green, blue=blue)
    games.append(game)
    return game


with open(Path(__file__).parent / "input.txt") as f:
    lines = f.readlines()
    for line in lines:
        game = parse_input(line)
        result += game.order_or_zero()

print(result)
