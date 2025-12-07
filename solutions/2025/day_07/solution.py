# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/7

from ...base import StrSplitSolution, answer
from collections import deque


class Solution(StrSplitSolution):
    _year = 2025
    _day = 7
    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    @answer((1651, 108924003331749))
    def solve(self) -> tuple[int, int]:

        rowLength = len(self.input[0])
        split = 0
        curr = [0] * rowLength
        curr[self.input[0].find("S")] = 1

        for row in self.input:
            buffer = [0] * rowLength
            for i in range(rowLength):
                if row[i]=="^" and curr[i] > 0:
                    buffer[i + 1] += curr[i]
                    buffer[i - 1] += curr[i]
                    split += 1
                elif curr[i]:
                    buffer[i] += curr[i]
            curr = buffer


        return (split, sum(curr))

