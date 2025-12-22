# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/10

from ...base import StrSplitSolution, answer
from collections import deque
from math import inf
from functools import cache
from itertools import combinations
from numpy import array


class Solution(StrSplitSolution):
    _year = 2025
    _day = 10

    def printReg(self, register):
        return "".join(map(lambda x: "." if x == "0" else "#", reversed(bin(register)[2:])))

    def parseLine1(self, line):
        elements = line.split(" ")
        lights = int("".join(map(lambda x: "1" if x=="#" else "0", elements[0].strip("[]")[::-1])),2)
        buttons = []
        for button in elements[1:-1]:
            val = 0
            for reg in map(int, button.strip("()").split(",")):
                val |= 1 << reg
            buttons.append(val)
        joltages = tuple(map(int, elements[-1].strip("{}").split(",")))

        return lights, buttons, joltages

    def parseLine2(self, line):
        elements = line.split(" ")
        joltages = tuple(map(int, elements[-1].strip("{}").split(",")))
        buttons = []
        for button in elements[1:-1]:
            buttonArray = [0] * len(joltages)
            registersTripped =  map(int, button.strip("()").split(","))
            for reg in registersTripped:
                buttonArray[reg] = 1
            buttons.append(array(buttonArray))

        return buttons, joltages


    @answer(401)
    def part_1(self) -> int:
        part1 = 0
        for line in self.input:
            lights, buttons, joltages = self.parseLine1(line)
            visited = set()
            q = deque([(0, 0)])
            while q:
                steps, curr = q.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                if curr == lights:
                    part1 += steps
                    break
                for button in buttons:
                    q.append((steps + 1, button ^ curr))
        return part1

    # @answer(1234)
    def part_2(self) -> int:
        part2solution = 0
        for line in self.input:
            buttons, joltages = self.parseLine2(line)

            buttonCombos = [a + b for a, b in combinations(buttons, 2)]
            self.debug("2-Button Combos", buttonCombos)

            @cache
            def recNumPresses(remainingJoltage: tuple[int]) -> int:
                if any([x < 0 for x in remainingJoltage]):
                    return inf
                if all([x == 0 for x in remainingJoltage]):
                    return 0


            assert recNumPresses((0,0,0,0)) == 0
            assert recNumPresses((-1,0,0,0)) == inf

            recNumPresses.cache_clear()
            self.debug("New Line:")
            self.debug(buttons, joltages)

        return part2solution 

    # @answer((0, 0))
    # def solve(self) -> tuple[int, int]:
    #   pass 

