# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/19

from ...base import StrSplitSolution, answer
from re import findall
from functools import cache


class Solution(StrSplitSolution):
    _year = 2022
    _day = 19
    def extractNums(self, s) -> list[int]:
        pattern = r'\d+'
        return list(map(int,findall(pattern, s)))

    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    def solve(self) -> tuple[int, int]:
        TURN_LIMIT = 25

        @cache
        def tryBlueprint(oreBot, clayBot, obsidianBot, geodeBot, ore, clay, obsidian, geodes, turns) -> int:
            assert(all([x >= 0 for x in [ore, clay, obsidian, geodes]]))
            print(oreBot, clayBot, obsidianBot, geodeBot, ore, clay, obsidian, geodes, turns)
            if turns == TURN_LIMIT:
                print("Time Limit Reached: ", oreBot, clayBot, obsidianBot, geodeBot, ore, clay, obsidian, geodes)
                return geodes

            if geodeRobotOreCost <= ore and geodeRobotObsidianCost <= obsidian:
                print("Building Geode Bot")
                return tryBlueprint(oreBot, clayBot, obsidianBot, geodeBot + 1, ore + oreBot - geodeRobotOreCost, clay + clayBot, obsidian + obsidianBot - geodeRobotObsidianCost, geodes + geodeBot, turns + 1)


            buildOreBot = 0
            buildClayBot = 0
            buildObsidianBot = 0
            wait = 0

            if ore >= oreRobotCost and oreBot <= max(obsidianRobotOreCost, geodeRobotOreCost):
                print("Trying to build oreBot")
                buildOreBot = tryBlueprint(oreBot + 1, clayBot, obsidianBot, geodeBot, ore + oreBot - oreRobotCost, clay + clayBot, obsidian + obsidianBot, geodes + geodeBot, turns + 1)

            if ore >= clayRobotCost and clayBot <= obsidianRobotClayCost:
                print("Trying to build clayBot")
                buildClayBot = tryBlueprint(oreBot, clayBot + 1, obsidianBot, geodeBot, ore + oreBot - clayRobotCost, clay + clayBot, obsidian + obsidianBot, geodes + geodeBot, turns + 1)

            if ore >= obsidianRobotOreCost and clay >= obsidianRobotClayCost and obsidianBot <= geodeRobotObsidianCost:
                print("Trying to build obsidianBot")
                buildObsidianBot = tryBlueprint(oreBot, clayBot, obsidianBot + 1, geodeBot, ore + oreBot - obsidianRobotOreCost, clay + clayBot - obsidianRobotClayCost, obsidian + obsidianBot, geodes + geodeBot, turns + 1)

            if all([x <= hoarding for x in [ore, clay, obsidian]]) and geodeBot == 0:
                print("Try waiting...")
                wait = tryBlueprint(oreBot, clayBot, obsidianBot, geodeBot, ore + oreBot, clay + clayBot, obsidian + obsidianBot, geodes + geodeBot, turns + 1)

            return max(wait, buildOreBot, buildClayBot, buildObsidianBot)
            
        part1 = 0
        line = self.input[0]
        blueprintNum, oreRobotCost, clayRobotCost, obsidianRobotOreCost, obsidianRobotClayCost, geodeRobotOreCost, geodeRobotObsidianCost = self.extractNums(line)
        hoarding = max(oreRobotCost, clayRobotCost, obsidianRobotClayCost, obsidianRobotOreCost, geodeRobotObsidianCost, geodeRobotOreCost) + 1
        print("Hoarding Limits:", hoarding)
        return tryBlueprint(1, 0, 0, 0, 0, 0, 0, 0, 1), 0