#!/usr/bin/env python3
"""
Day 4: TBD

https://adventofcode.com/2024/day/4
"""
from typing import Any

from src.main.python.util import AbstractSolver

DAY = '04'


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()

    def solve_part_1(self, data: Any, **kwargs) -> int:
        return 0

    def solve_part_2(self, data: Any, **kwargs) -> int:
        return 0

    def get_day(self):
        return DAY


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
