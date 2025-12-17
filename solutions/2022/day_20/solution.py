# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/20

from ...base import IntSplitSolution, answer

class DllNode():
    def __init__(self, originalPos = None, val= None, prev = None, next = None):
        self.originalPos = originalPos
        self.val = val
        self.prev = prev
        self.next = next
    
    def __del__(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    def __hash__(self):
        return self.originalPos

    def __repr__(self):
        return "pos:" + self.originalPos + " val: " + self.val

    def __str__(self):
        return "[pos: {} val: {}]".format(self.originalPos, self.val)
    

class DoublyLinkedList():
    def __init__(self, nodevals):
        self.nodes = []
        for i, num in enumerate(nodevals):
            self.nodes.append(DllNode(i, num))

        for i in range(len(self.nodes) - 1):
            self.nodes[i].next = self.nodes[i+1]

        for i in range(1, len(self.nodes)):
            self.nodes[i].prev = self.nodes[i - 1]

        self.nodes[-1].next = self.nodes[0]
        self.nodes[0].prev = self.nodes[-1]

        self.nodeDict = {hash(node): node for node in self.nodes}
    
    def __str__(self):
        return "<->".join([str(node) for node in self.nodes])

class Solution(IntSplitSolution):
    _year = 2022
    _day = 20

    # @answer(1234)
    def part_1(self) -> int:
        nodes = DoublyLinkedList(self.input)
        assert(all([node.val == num for node, num in zip(nodes.nodes, self.input)]))
        print(nodes)
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
