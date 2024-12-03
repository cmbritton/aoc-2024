#!/usr/bin/env python3
"""
Day 2: Mull It Over

https://adventofcode.com/2024/day/3
"""
import re
from typing import Any

from src.main.python.util import AbstractSolver

PATTERN = r"(mul)\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"

DAY = '03'


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()

    def solve_part_1(self, data: Any, **kwargs) -> int:
        total = 0
        for line in data:
            m = re.findall(PATTERN, line)
            total += sum(int(x[1]) * int(x[2]) for x in m if x[0] == 'mul')
            # for x in m:
            #     if x[0] == 'mul':
            #         total += int(x[1]) * int(x[2])

        return total

    def solve_part_2(self, data: Any, **kwargs) -> int:
        total = 0
        enabled = True
        for line in data:
            m = re.findall(PATTERN, line)
            for x in m:
                if x[3] == 'do()':
                    enabled = True
                elif x[4] == "don't()":
                    enabled = False
                elif enabled:
                    total += int(x[1]) * int(x[2])

        return total

    # 70553436 is wrong

    def get_day(self):
        return DAY


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
