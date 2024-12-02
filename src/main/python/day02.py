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

    def _is_report_safe(self, report: list[int]) -> bool:
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

        return safe

    def _is_dampened_report_safe(self, report: list[int]) -> bool:
        # 4 5 6 2
        safe = False
        for i in range(len(report)):
            dampened_report = report[:i] + report[i + 1:]
            if self._is_report_safe(dampened_report):
                safe = True
                break
        return safe

    def solve_part_1(self, data: Any, **kwargs) -> int:
        reports = Solver.init_data(data)
        total = 0
        for report in reports:
            if self._is_report_safe(report):
                total += 1
        return total

    def solve_part_2(self, data: Any, **kwargs) -> int:
        reports = Solver.init_data(data)
        total = 0
        for report in reports:
            if (self._is_report_safe(report)
                    or self._is_dampened_report_safe(report)):
                total += 1

        return total

    def get_day(self):
        return DAY


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
