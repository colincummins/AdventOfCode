# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/20

from ...base import IntSplitSolution, answer
from collections import deque, namedtuple


class Solution(IntSplitSolution):
    _year = 2022
    _day = 20

    def decrypt(self, key = 1, mixes = 1) -> int:
        solution = 0
        EncryptNode = namedtuple('Node', ['index', 'shift'])
        instructions = deque([EncryptNode(i, shift * key) for i, shift in enumerate(self.input)])
        for _ in range(mixes):
            for i in range(len(self.input)):
                while instructions[-1].index != i:
                    instructions.rotate(1)
                currInstruction = instructions.pop()
                instructions.rotate(-currInstruction.shift)
                instructions.append(currInstruction)
        
        while instructions[0].shift != 0:
            instructions.rotate(1)

        for i in range(1,4):
            solution += instructions[i * 1000 % len(instructions)].shift

        return solution

    # @answer(1234)
    def part_1(self) -> int:
        pass
        
    # @answer(1234)
    def part_2(self) -> int:
        pass

    @answer((19070, 14773357352059))
    def solve(self) -> tuple[int, int]:
        return self.decrypt(), self.decrypt(811589153, 10)

