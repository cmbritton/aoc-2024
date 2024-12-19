#!/usr/bin/env python3
"""
Day 5: Print Queue

https://adventofcode.com/2024/day/5
"""
from collections import namedtuple
from typing import Any

from src.main.python.util import AbstractSolver

DAY = '05'

Rule = namedtuple('Rule', ['p1', 'p2'])


class ManualUpdate:

    def __init__(self, pages_str: str, rules: list[Rule]) -> None:
        super().__init__()
        self.pages_str = pages_str
        self.pages = [int(x) for x in pages_str.split(',')]
        self.rules = self._elide_rules(rules)
        self.ordered_pages = []
        self.deferred_rules = list(self.rules)
        self.seq = []
        self.init_seq()

    def _elide_rules(self, rules: list[Rule]) -> list[Rule]:
        return [r for r in rules if r.p1 in self.pages and r.p2 in self.pages]

    def _init_seq(self, rule: Rule) -> None:
        if not self.seq:
            self.seq.append(rule.p1)
            self.seq.append(rule.p2)
            self.deferred_rules.remove(rule)
            return

        if rule.p1 not in self.seq and rule.p2 not in self.seq:
            return

        if rule.p1 in self.seq and rule.p2 not in self.seq:
            idx = self.seq.index(rule.p1)
            self.seq.insert(idx + 1, rule.p2)
        elif rule.p1 not in self.seq and rule.p2 in self.seq:
            idx = self.seq.index(rule.p2)
            self.seq.insert(idx, rule.p1)
        else:
            idx_1 = self.seq.index(rule.p1)
            idx_2 = self.seq.index(rule.p2)
            if not idx_1 < idx_2:
                self.seq[idx_1] = rule.p2
                self.seq[idx_2] = rule.p1

        self.deferred_rules.remove(rule)

    def init_seq(self) -> None:
        prev_seq = [-1]
        while prev_seq != self.seq:
            prev_seq = list(self.seq)
            self.deferred_rules = list(self.rules)
            while self.deferred_rules:
                iter_deferred_rules = list(self.deferred_rules)
                for rule in iter_deferred_rules:
                    self._init_seq(rule)

    def is_rule_satisfied(self, rule: Rule) -> bool:
        return self.pages.index(rule.p1) < self.pages.index(rule.p2)

    def is_in_order(self) -> bool:
        for rule in self.rules:
            if not self.is_rule_satisfied(rule):
                return False

        return True

    def get_ordered_pages(self) -> list[int]:
        if not self.ordered_pages:
            self.ordered_pages = sorted(self.pages,
                                        key=lambda x: self.seq.index(x))
        return self.ordered_pages

    def get_middle_page(self) -> int:
        return self.pages[(len(self.pages) // 2)]


class Solver(AbstractSolver):

    def __init__(self) -> None:
        super().__init__()
        self.page_order_rules = []
        self.manual_updates: list[ManualUpdate] = []

    def init_data(self, data: list[str]) -> None:
        reading_rules = True
        for line in data:
            if line == '':
                reading_rules = False
                continue
            if reading_rules:
                p1, p2 = [int(x) for x in line.split('|')]
                rule = Rule(p1, p2)
                self.page_order_rules.append(rule)
            else:
                self.manual_updates.append(
                        ManualUpdate(line, list(self.page_order_rules)))

        return

    def solve_part_1(self, data: Any, **kwargs) -> int:
        self.init_data(data)
        return sum(
                update.get_middle_page() for update in self.manual_updates if
                update.is_in_order())

    def solve_part_2(self, data: Any, **kwargs) -> int:
        self.init_data(data)
        unordered_updates = []
        for update in self.manual_updates:
            if not update.is_in_order():
                unordered_updates.append(update)

        total = 0
        for update in unordered_updates:
            ordered_pages = update.get_ordered_pages()
            total += ordered_pages[(len(ordered_pages) // 2)]
        return total

    def get_day(self):
        return DAY


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
