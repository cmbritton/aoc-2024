#!/usr/bin/env python3
"""
Day 2: TBD

https://adventofcode.com/2024/day/2
"""
from typing import Any

from src.main.python.util import AbstractSolver

DAY = '02'


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def init_data(data: list[str]) -> Any:
        return data

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
