# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/21

from ...base import StrSplitSolution, answer
import operator
from collections import defaultdict, deque

class Monkey():
    def __init__(self, key: str, phrase: str):
        self.key = key
        self.num = None
        self.waiting1 = self.waiting2 = None

        if phrase.isnumeric():
            self.inDegree = 0
            self.num = int(phrase)
            return

        self.inDegree = 2
        self.waiting1, self.operation, self.waiting2 = phrase.split(" ")
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
        return hash(self.key)

    def listen(self, key: str, value: int):
        self.inDegree -= 1
        self.__setattr__(key, value)

        if self.inDegree == 0:
            self.num = self.operation(self.__getattribute__(self.waiting1), self.__getattribute__(self.waiting2))


    def shout(self) -> tuple[str, int]:
        if self.num is None:
            raise ValueError("Monkey doesn't have needed nums")
        return self.key, self.num

    def getWaiting(self) -> tuple[str, str]:
        return (self.waiting1, self.waiting2) if self.waiting1 and self.waiting2 else [] 

    def __repr__(self):
        return self.key



class Solution(StrSplitSolution):
    _year = 2022
    _day = 21

        




    # @answer(1234)
    def part_1(self) -> int:
        neighbors = defaultdict(list)
        jungle = {}
        for line in self.input:
            key, phrase = line.split(": ")
            jungle[key] = Monkey(key, phrase)
        for monkey in jungle.values():
            for neighbor in monkey.getWaiting():
                neighbors[neighbor].append(monkey)

        q = deque(filter(lambda x: x.inDegree == 0, jungle.values()))

        while q:
            curr = q.popleft()
            for neighbor in neighbors[curr.key]:
                neighbor.listen(*curr.shout())
                if neighbor.inDegree == 0:
                    q.append(neighbor)

        print("Final queue:", q)

        return jungle["root"].num


            




    # @answer(1234)
    def part_2(self) -> int:
        neighbors = defaultdict(list)
        jungle = {}
        for line in self.input:
            key, phrase = line.split(": ")
            if key == "humn":
                continue
            jungle[key] = Monkey(key, phrase)
        print("Jungle:", jungle.values())
        for monkey in jungle.values():
            for neighbor in monkey.getWaiting():
                neighbors[neighbor].append(monkey)
        print("Neighbors:", neighbors)

        q = deque(filter(lambda x: x.inDegree == 0, jungle.values()))
        print("Start queue:", q)

        while q:
            curr = q.popleft()
            print("Current Monkey", curr)
            print("Their neighbors:", neighbors[curr.key])
            for neighbor in neighbors[curr.key]:
                print("{} shouts {} to {}".format(*curr.shout(), neighbor.key))
                neighbor.listen(*curr.shout())
                if neighbor.inDegree == 0:
                    print("Neighbor {} has calculated their number: {}".format(neighbor.key, neighbor.num))
                    q.append(neighbor)

        print("Final queue:", q)
        print(vars(jungle["root"]))
        print("Monkeys:", [vars(x) if x.number is None else None for x in jungle.values()])



    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
