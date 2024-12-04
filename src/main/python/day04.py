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

    @staticmethod
    def diagonals_ul_to_lr(matrix: list[str]) -> list[str]:
        n = len(matrix)
        new_rows = []

        for col in range(n):
            new_row = []
            offset = 0
            for row in range(0, n - col):
                new_row.append(matrix[row][col + offset])
                offset += 1
            new_rows.append(''.join(new_row))

        for row in range(1, n):
            new_row = []
            offset = 0
            for col in range(0, n - row):
                new_row.append(matrix[row + offset][col])
                offset += 1
            new_rows.append(''.join(new_row))

        return new_rows

    @staticmethod
    def diagonals_ll_to_ur(matrix: list[str]) -> list[str]:
        n = len(matrix)
        new_rows = []

        for col in range(n):
            new_row = []
            offset = 0
            for row in range(n - col - 1, -1, -1):
                new_row.append(matrix[row][col + offset])
                offset += 1
            new_rows.append(''.join(new_row))

        for row in range(n - 2, -1, -1):
            new_row = []
            offset = 0
            for col in range(0, row + 1):
                new_row.append(matrix[row - offset][col])
                offset += 1
            new_rows.append(''.join(new_row))

        return new_rows

    @staticmethod
    def diagonals_ur_to_ll(matrix: list[str]) -> list[str]:
        n = len(matrix)
        new_rows = []

        for col in range(n - 1, -1, -1):
            new_row = []
            offset = 0
            for row in range(col + 1):
                new_row.append(matrix[row][col - offset])
                offset += 1
            new_rows.append(''.join(new_row))

        for row in range(1, n):
            new_row = []
            offset = 0
            for col in range(n - 1, row - 1, -1):
                new_row.append(matrix[row + offset][col])
                offset += 1
            new_rows.append(''.join(new_row))

        return new_rows

    def solve_part_1(self, data: Any, **kwargs) -> int:
        reversed_data = data[::-1]
        ul_to_lr_data = Solver.diagonals_ul_to_lr(data)
        ll_to_ur_data = Solver.diagonals_ll_to_ur(data)
        ur_to_ll_data = Solver.diagonals_ur_to_ll(data)
        # ll_to_ur_data = ''.join(list(map(list, zip(*data))))
        # ur_to_ll_data = ''.join(list(map(list, zip(*reversed_data)))[::-1])
        # lr_to_ul_data = ''.join(list(map(list, zip(*data)))[::-1])
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
