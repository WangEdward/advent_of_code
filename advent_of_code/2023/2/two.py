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

    def power(self):
        return self.red * self.green * self.blue


games = []
result = 0


def parse_input(line: str):
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
        result += game.power()

assert result == 71585
print(result)
