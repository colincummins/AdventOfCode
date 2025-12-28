# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/12

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 12

    # @answer(1234)
    def part_1(self) -> int:
        goodRegions = 0
        for line in self.input:
            if "x" in line:
                dimensions, packageCounts = line.split(": ")
                dimensions = list(map(int,dimensions.split("x")))
                packageCounts = list(map(int, packageCounts.split(" ")))
                print("Dimensions: {}".format(dimensions))
                print("Package Counts: {}".format(packageCounts))

                if sum(packageCounts) * 7 <= dimensions[0] * dimensions[1]:
                    print("Optimum packing possible")
                    goodRegions += 1



        return(goodRegions)


    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
