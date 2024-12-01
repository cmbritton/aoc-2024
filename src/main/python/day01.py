#!/usr/bin/env python3
"""
Day 1: Historian Hysteria

https://adventofcode.com/2024/day/1
"""
import re
from collections import Counter
from typing import Any

from src.main.python.util import AbstractSolver

DAY = '01'


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def init_data(data: list[str]) -> Any:
        list1 = []
        list2 = []
        for line in data:
            m = re.search(r'\s*(\S*)\s+(\S*)\s*', line)
            list1.append(int(m.group(1)))
            list2.append(int(m.group(2)))

        return sorted(list1), sorted(list2)

    def solve_part_1(self, data: Any, **kwargs) -> int:
        list1, list2 = Solver.init_data(data)
        return sum([abs(val1 - val2) for val1, val2 in zip(list1, list2)])

    def solve_part_2(self, data: Any, **kwargs) -> int:
        list1, list2 = Solver.init_data(data)
        counter = Counter(list2)
        return sum([val * counter.get(val, 0) for val in list1])

    def get_day(self):
        return DAY


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
