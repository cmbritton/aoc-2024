#!/usr/bin/env python3
"""
Day 1: Historian Hysteria

https://adventofcode.com/2024/day/1
"""
import re
from dataclasses import dataclass
from typing import Any

from src.main.python.util import AbstractSolver
from collections import Counter


@dataclass
class MyData:
    value: str


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()

    def init_data(self, data: list[str]) -> Any:
        list1 = []
        list2 = []
        for line in data:
            m = re.search(r'\s*(\S*)\s+(\S*)\s*', line)
            list1.append(int(m.group(1)))
            list2.append(int(m.group(2)))

        return sorted(list1), sorted(list2)

    def solve_part_1(self, data: Any, **kwargs) -> int:
        list1, list2 = self.init_data(data)
        total = 0
        for i in range(len(list1)):
            total += abs(list1[i] - list2[i])
        return total

    def solve_part_2(self, data: Any, **kwargs) -> int:
        list1, list2 = self.init_data(data)
        counter = Counter(list2)
        total = 0
        for i in range(len(list1)):
            total += list1[i] * counter.get(list1[i], 0)
        return total


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
