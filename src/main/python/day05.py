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

    def __init__(self, rule_str: str) -> None:
        super().__init__()
        self.rule_str = rule_str
        self.page_1, self.page_2 = [int(x) for x in rule_str.split('|')]

    def __repr__(self) -> str:
        return f'{self.page_1}|{self.page_2}'

# @dataclass
class PageOrderRules:

    def __init__(self) -> None:
        super().__init__()
        self.page_order_rules = []
        self.seq = []
        self.deferred_rules = []

    def append(self, page_order_rule: PageOrderRule) -> None:
        self.page_order_rules.append(page_order_rule)

    def _init_rule(self, page_order_rule: PageOrderRule) -> None:
        if not self.seq:
            self.seq.append(page_order_rule.page_1)
            self.seq.append(page_order_rule.page_2)
            self.deferred_rules.remove(page_order_rule)
            return

        if (page_order_rule.page_1 not in self.seq
                and page_order_rule.page_2 not in self.seq):
            return

        if (page_order_rule.page_1 in self.seq
                and page_order_rule.page_2 not in self.seq):
            idx = self.seq.index(page_order_rule.page_1)
            self.seq.insert(idx + 1, page_order_rule.page_2)

        if (page_order_rule.page_1 not in self.seq
                and page_order_rule.page_2 in self.seq):
            idx = self.seq.index(page_order_rule.page_2)
            self.seq.insert(idx, page_order_rule.page_1)

        self.deferred_rules.remove(page_order_rule)

        return

    def init_rules(self) -> None:
        self.deferred_rules = list(self.page_order_rules)
        while self.deferred_rules:
            iter_deferred_rules = list(self.deferred_rules)
            for page_order_rule in iter_deferred_rules:
                self._init_rule(page_order_rule)

        return

# @dataclass(repr=True)
class ManualUpdate:

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

    def is_in_order(self, page_order_rules: PageOrderRules) -> bool:
        for page_order_rule in page_order_rules.page_order_rules:
            if not self.is_rule_satisfied(page_order_rule):
                return False

        return True

    def get_ordered_pages(self, page_order_rules: PageOrderRules) -> list[int]:
        ordered_update = list(page_order_rules.seq)
        iter_ordered_update = list(ordered_update)
        for page in iter_ordered_update:
            if page not in self.pages:
                ordered_update.remove(page)

        for page in self.pages:
            if page not in ordered_update:
                ordered_update.append(page)

        return ordered_update

    def get_middle_page(self) -> int:
        return self.pages[(len(self.pages) // 2)]


class Solver(AbstractSolver):

    def __init__(self) -> None:
        super().__init__()
        self.page_order_rules: PageOrderRules = PageOrderRules()
        self.manual_updates: list[ManualUpdate] = []

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
        self.init_data(data)
        unordered_updates = []
        for update in self.manual_updates:
            if not update.is_in_order(self.page_order_rules):
                unordered_updates.append(update)

        self.page_order_rules.init_rules()
        total = 0
        for update in unordered_updates:
            ordered_pages = update.get_ordered_pages(self.page_order_rules)
            total += ordered_pages[(len(ordered_pages) // 2)]
        return total

    def get_day(self):
        return DAY


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
