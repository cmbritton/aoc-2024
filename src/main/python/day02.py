#!/usr/bin/env python3
"""
Day 2: Red-Nosed Reports

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
    def _init_data(data: list[str]) -> Any:
        return [[int(x) for x in line.split(' ')] for line in data]

    @staticmethod
    def _is_report_safe(report: list[int]) -> bool:
        ascending = descending = False
        for a, b in pairwise(report):
            if not 1 <= abs(a - b) <= 3:
                return False
            if a < b:
                ascending = True
            elif a > b:
                descending = True
            if ascending and descending:
                return False

        return True

    @staticmethod
    def _is_dampened_report_safe(report: list[int]) -> bool:
        return any(Solver._is_report_safe(report[:i] + report[i + 1:]) for i in
                   range(len(report)))

    def solve_part_1(self, data: Any, **kwargs) -> int:
        reports = Solver._init_data(data)
        return sum(1 for report in reports if Solver._is_report_safe(report))

    def solve_part_2(self, data: Any, **kwargs) -> int:
        reports = Solver._init_data(data)
        return sum(1 for report in reports if Solver._is_report_safe(
                report) or Solver._is_dampened_report_safe(report))

    def get_day(self):
        return DAY


def main() -> None:
    solver = Solver()
    solver.run_part_1()

    solver = Solver()
    solver.run_part_2()


if __name__ == "__main__":
    main()
