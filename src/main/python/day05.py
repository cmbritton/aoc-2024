#!/usr/bin/env python3
"""
Day 5: Print Queue

https://adventofcode.com/2024/day/5
"""
from dataclasses import dataclass
from typing import Any

from src.main.python.util import AbstractSolver

DAY = '05'


@dataclass(repr=True)
class PageOrderRule:
    rule_str: str

    def __init__(self, rule_str: str) -> None:
        super().__init__()
        self.rule_str = rule_str
        self.page_1, self.page_2 = [int(x) for x in rule_str.split('|')]


@dataclass(repr=True)
class ManualUpdate:
    pages_str: str

    def __init__(self, pages_str: str) -> None:
        super().__init__()
        self.pages_str = pages_str
        self.pages = [int(x) for x in pages_str.split(',')]

    def is_rule_satisfied(self, page_order_rule: PageOrderRule) -> bool:
        if (page_order_rule.page_1 not in self.pages or
                page_order_rule.page_2 not in self.pages):
            return True

        idx_1 = self.pages.index(page_order_rule.page_1)
        idx_2 = self.pages.index(page_order_rule.page_2)

        return idx_1 < idx_2

    def is_in_order(self, page_order_rules: list[PageOrderRule]) -> bool:
        for page_order_rule in page_order_rules:
            if not self.is_rule_satisfied(page_order_rule):
                return False

        return True

    def get_middle_page(self) -> int:
        return self.pages[(len(self.pages) // 2)]


class Solver(AbstractSolver):
    page_order_rules: list[PageOrderRule] = []
    manual_updates: list[ManualUpdate] = []

    def __init__(self) -> None:
        super().__init__()

    def init_data(self, data: list[str]) -> None:
        reading_rules = True
        for line in data:
            if line == '':
                reading_rules = False
                continue
            if reading_rules:
                self.page_order_rules.append(PageOrderRule(line))
            else:
                self.manual_updates.append(ManualUpdate(line))

        return

    def solve_part_1(self, data: Any, **kwargs) -> int:
        self.init_data(data)
        return sum(
                update.get_middle_page() for update in self.manual_updates if
                update.is_in_order(self.page_order_rules))

    def solve_part_2(self, data: Any, **kwargs) -> int:
        return 0

    def get_day(self):
        return DAY


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
