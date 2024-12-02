#!/usr/bin/env python3
"""
Day 2: TBD

https://adventofcode.com/2024/day/2
"""
from itertools import pairwise
from typing import Any

from src.main.python.util import AbstractSolver

DAY = '02'


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def init_data(data: list[str]) -> Any:
        reports = []
        for line in data:
            reports.append([int(x) for x in line.split(' ')])
        return reports

    def solve_part_1(self, data: Any, **kwargs) -> int:
        reports = Solver.init_data(data)
        total = 0
        for report in reports:
            safe = True
            ascending = False
            descending = False
            for a, b in pairwise(report):
                diff = a - b
                if abs(diff) < 1 or abs(diff) > 3 or diff == 0:
                    safe = False
                    break
                if a < b:
                    ascending = True
                elif a > b:
                    descending = True
                if ascending and descending:
                    safe = False
                    break
            if safe:
                total += 1
        return total

    def solve_part_2(self, data: Any, **kwargs) -> int:
        return 0

    def get_day(self):
        return DAY


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
