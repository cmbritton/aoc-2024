#!/usr/bin/env python3
"""
Day 1: Something

https://adventofcode.com/2024/day/1
"""
from dataclasses import dataclass
from typing import Any

from src.main.python.util import AbstractSolver


@dataclass
class MyData:
    value: str


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()

    def solve_part_1(self, data: Any, **kwargs) -> int:
        return 0

    def solve_part_2(self, data: Any, **kwargs) -> int:
        return 0


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
