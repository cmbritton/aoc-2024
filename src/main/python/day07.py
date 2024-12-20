#!/usr/bin/env python3
"""
Day 7: Bridge Repair

https://adventofcode.com/2024/day/7
"""
from itertools import product
from typing import Any

from src.main.python.util import AbstractSolver

DAY = '07'


class Solver(AbstractSolver):

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def calc(terms: list[int], ops: tuple[str, ...]) -> int:
        result = terms[0]
        for idx, term in enumerate(terms[1:]):
            if ops[idx] == '+':
                result += term
            elif ops[idx] == '*':
                result *= term
            else:
                result = int(str(result) + str(term))
        return result

    def solve(self, line: str, operators: list[str]) -> int:
        vals = [int(x) for x in line.replace(':', '').split(' ')]
        for ops in product(operators, repeat=len(vals[1:]) - 1):
            if self.calc(vals[1:], ops) == vals[0]:
                return vals[0]
        return 0

    def solve_part_1(self, data: Any, **kwargs) -> int:
        total = 0
        for line in data:
            total += self.solve(line, ['+', '*'])
        return total

    def solve_part_2(self, data: Any, **kwargs) -> int:
        total = 0
        for line in data:
            total += self.solve(line, ['+', '*', '||'])
        return total

    def get_day(self):
        return DAY


def main() -> None:
    solver = Solver()
    solver.run_part_1()

    solver = Solver()
    solver.run_part_2()


if __name__ == "__main__":
    main()
