# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/6

from ...base import StrSplitSolution, answer
from re import split
from operator import add, mul
from functools import reduce


class Solution(StrSplitSolution):
    _year = 2025
    _day = 6

    def shiftDigit(self, acc, curr):
        if curr == " ":
            return acc
        else:
            return acc * 10 + curr

    @answer(4771265398012)
    def part_1(self) -> int:
        self.input2 = self.input[:]
        operators = [add if x == "+" else mul for x in self.input.pop().split()]
        accumulator = map(int,self.input.pop().split())
        while self.input:
            current = map(int,self.input.pop().split())
            accumulator = map(lambda a, b, opp: opp(a,b), accumulator, current, operators)
        return sum(accumulator)

    @answer(10695785245101)
    def part_2(self) -> int:
        solution = 0
        self.input = self.input2
        operators = self.input.pop()
        accumulator = [0] * len(self.input[0])
        for row in self.input:
            current = map(lambda x: int(x) if x.isdigit() else " ",row)
            accumulator = map(self.shiftDigit, accumulator, current)
        operators = [add if x == "+" else mul for x in operators.split()]
        groups = [[]]
        for num in accumulator:
            if num == 0:
                groups.append([])
            else:
                groups[-1].append(num)

        
        return sum(map(lambda opp, group: reduce(opp, group), operators, groups))



    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
