#!/usr/bin/env python3
"""
Day 8: Resonant Collinearity

https://adventofcode.com/2024/day/7
"""
from typing import Any

from src.main.python.util import AbstractSolver

DAY = '08'


class Solver(AbstractSolver):

    def __init__(self) -> None:
        super().__init__()

    def solve_part_1(self, data: Any, **kwargs) -> int:
        pass

    def solve_part_2(self, data: Any, **kwargs) -> int:
        pass

    def get_day(self):
        return DAY


def main() -> None:
    solver = Solver()
    solver.run_part_1()

    solver = Solver()
    solver.run_part_2()


if __name__ == "__main__":
    main()
