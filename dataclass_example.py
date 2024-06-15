from __future__ import annotations
from typing import Tuple
from dataclasses import dataclass


@dataclass(frozen=True)
class CubeGame:
    draws: Tuple[CubeGameDraw]


@dataclass(frozen=True)
class CubeGameDraw:
    red: int
    green: int
    blue: int

    def value(self):
        return self.red * self.green * self.blue


draw = CubeGameDraw(4, 2, 1)
draw2 = CubeGameDraw(4, 2, 1)
game = CubeGame(draw, draw2)

print(draw)
print(draw == draw2)
print(game)
