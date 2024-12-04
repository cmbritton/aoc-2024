#!/usr/bin/env python3
"""
Day 4: Ceres Search

https://adventofcode.com/2024/day/4
"""
import re
from typing import Any

from src.main.python.util import AbstractSolver

DAY = '04'

PATTERN = r'(?=XMAS)'


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def diagonals_top_to_bottom(matrix: list[str]) -> list[str]:
        n = len(matrix)
        new_rows = []

        for col in range(n):
            new_row = []
            for row in range(n):
                new_row.append(matrix[row][col])
            new_rows.append(''.join(new_row))

        return new_rows

    @staticmethod
    def diagonals_bottom_to_top(matrix: list[str]) -> list[str]:
        n = len(matrix)
        new_rows = []

        for col in range(len(matrix)):
            new_row = []
            for row in range(n - 1, -1, -1):
                new_row.append(matrix[row][col])
            new_rows.append(''.join(new_row))

        return new_rows

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
            for row in range(n - 1, col - 1, -1):
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

    @staticmethod
    def diagonals_lr_to_ul(matrix: list[str]) -> list[str]:
        n = len(matrix)
        new_rows = []

        for col in range(n - 1, -1, -1):
            new_row = []
            offset = 0
            for row in range(n - 1, n - col - 2, -1):
                new_row.append(matrix[row][col - offset])
                offset += 1
            new_rows.append(''.join(new_row))

        for row in range(n - 2, -1, -1):
            new_row = []
            offset = 0
            for col in range(n - 1, n - row - 2, -1):
                new_row.append(matrix[row - offset][col])
                offset += 1
            new_rows.append(''.join(new_row))

        return new_rows

    @staticmethod
    def reverse_data(data: list[str]) -> list[str]:
        return [row[::-1] for row in data]

    @staticmethod
    def count_data_matches(data: list[str]) -> int:
        count = 0
        for row in data:
            count += len(re.findall(PATTERN, row))
        return count

    @staticmethod
    def is_x_mas(data, row, col) -> bool:
        ra = row - 1  # row above
        rb = row + 1  # row below
        cl = col - 1  # column left
        cr = col + 1  # column right
        return (((data[ra][cl] == 'M' and data[rb][cr] == 'S') or
                 (data[ra][cl] == 'S' and data[rb][cr] == 'M')) and
                ((data[rb][cl] == 'M' and data[ra][cr] == 'S') or
                 (data[rb][cl] == 'S' and data[ra][cr] == 'M')))

    def solve_part_1(self, data: Any, **kwargs) -> int:
        reversed_data = Solver.reverse_data(data)
        top_to_bottom_data = Solver.diagonals_top_to_bottom(data)
        bottom_to_top_data = Solver.diagonals_bottom_to_top(data)
        ul_to_lr_data = Solver.diagonals_ul_to_lr(data)
        ll_to_ur_data = Solver.diagonals_ll_to_ur(data)
        ur_to_ll_data = Solver.diagonals_ur_to_ll(data)
        lr_to_ul_data = Solver.diagonals_lr_to_ul(data)

        return self.count_data_matches(data) + \
            self.count_data_matches(reversed_data) + \
            self.count_data_matches(top_to_bottom_data) + \
            self.count_data_matches(bottom_to_top_data) + \
            self.count_data_matches(ul_to_lr_data) + \
            self.count_data_matches(ll_to_ur_data) + \
            self.count_data_matches(ur_to_ll_data) + \
            self.count_data_matches(lr_to_ul_data)

    def solve_part_2(self, data: Any, **kwargs) -> int:
        total = 0
        for row in range(1, len(data) - 1):
            for col in range(1, len(data) - 1):
                if data[row][col] == 'A':
                    if Solver.is_x_mas(data, row, col):
                        total += 1

        return total

    def get_day(self):
        return DAY


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
