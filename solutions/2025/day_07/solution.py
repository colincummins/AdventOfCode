# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/7

from ...base import StrSplitSolution, answer
from collections import deque


class Solution(StrSplitSolution):
    _year = 2025
    _day = 7

    def parseInput(self):
        buffer = []
        for row in self.input:
            num = 0
            for i, node in enumerate(row):
                if node != ".":
                    num |= 1 << i
            buffer.append(num)
        self.input = buffer

    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    #@answer((1234, 4567))
    def solve(self) -> tuple[int, int]:
        self.parseInput()
        print(self.input)
        maxDepth = len(self.input) - 1
        print(maxDepth)
        split = 0
        q = deque()
        q.append((0, self.input[0]))
        #clear first row so it's not interpreted as a reflector
        self.input[0] = 0
        while q:
            buffer = 0
            depth, row = q.popleft()
            print(depth)
            collisions = row & self.input[depth]
            split += collisions.bit_count()
            row ^= collisions
            row |= collisions << 1
            row |= collisions >> 1
            if depth < maxDepth:
                q.append((depth + 1, row))

        return (split, 0)

