# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/21

from ...base import StrSplitSolution, answer
import operator


class Solution(StrSplitSolution):
    _year = 2022
    _day = 21

    class Monkey():
        def __init__(self, key: str, phrase: str):
            self.val1 = self.val2 = None
            self.key = key.strip(":")
            self.number = None

            if phrase.isnumeric():
                self.inDegree = 0
                self.number = int(phrase)
                return

            self.inDegree = 2
            self.neighbor1, self.operation, self.neighbor2 = phrase.split(" ")
            match self.operation:
                case "+": 
                    self.operation = operator.add
                case "-": 
                    self.operation = operator.sub
                case "*": 
                    self.operation = operator.mul
                case "/": 
                    self.operation = operator.truediv

        def __hash__(self):
            return self.key

        def listen(self, key: str, value: int):
            if self.neighbor1 == key:
                self.val1 = value
                self.inDegree -= 1
            elif self.neighbor2 == key:
                self.val2 = value
                self.inDegree -= 1
            else:
                raise KeyError

            if self.val1 is not None and self.val2 is not None:
                self.number = self.operation(self.val1, self.val2)

        def shout(self) -> tuple[str, int]:
            if self.number is None:
                raise ValueError("Monkey cannot calculate number")
            return self.key, self.number

        def getNeighbors(self) -> tuple[str, str]:
            return self.neighbor1, self.neighbor2




    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
