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
        reports = []
        for line in data:
            reports.append([int(x) for x in line.split(' ')])
        return reports

    @staticmethod
    def _is_report_safe(report: list[int]) -> bool:
        ascending = False
        descending = False
        for a, b in pairwise(report):
            if not 1 <= abs(a - b) <= 3:
                return False
            ascending |= a < b
            descending |= a > b
            if ascending and descending:
                return False

        return True

    @staticmethod
    def _is_dampened_report_safe(report: list[int]) -> bool:
        for i in range(len(report)):
            dampened_report = report[:i] + report[i + 1:]
            if Solver._is_report_safe(dampened_report):
                return True

        return False

    def solve_part_1(self, data: Any, **kwargs) -> int:
        reports = Solver._init_data(data)
        total = 0
        for report in reports:
            if Solver._is_report_safe(report):
                total += 1
        return total

    def solve_part_2(self, data: Any, **kwargs) -> int:
        reports = Solver._init_data(data)
        total = 0
        for report in reports:
            if (Solver._is_report_safe(report)
                    or Solver._is_dampened_report_safe(report)):
                total += 1

        return total

    def get_day(self):
        return DAY


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
