# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/9

from ...base import StrSplitSolution, answer
from collections import namedtuple
from dataclasses import dataclass
from functools import cache
from math import sqrt, atan2

@dataclass(frozen=True)
class Point():
    x: int
    y: int

    def getRectArea(self, other) -> int:
        # Area of a rectangle from opposite corners
        return (abs(self.x - other.x) + 1) * (abs(self.y - other.y) + 1)

    def __sub__(self, other) -> int:
        # Euclidian Distance
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

@dataclass(frozen=True)
class Vector():
    start: Point
    end: Point

    #cross product self x other
    def __mul__(self, other) -> int:
        pass





class Solution(StrSplitSolution):
    _year = 2025
    _day = 9

    def parseInput(self):
        self.input = [Point(*map(int, row.split(","))) for row in self.input]

    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    def solve(self) -> tuple[int, int]:
        self.parseInput()
        


            




