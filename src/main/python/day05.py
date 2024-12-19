#!/usr/bin/env python3
"""
Day 5: Print Queue

https://adventofcode.com/2024/day/5
"""
from typing import Any

from src.main.python.util import AbstractSolver

DAY = '05'


# class PageNum:
# 
#     def __init__(self, page_num: int) -> None:
#         super().__init__()
#         self.page_num = page_num
# 
#     def __lt__(self, other):
#         idx1 = self.get_index()
#         idx2 = self.get_index()
#         return idx1 < idx2
# 
#     def __le__(self, other):
#         idx1 = self.get_index()
#         idx2 = self.get_index()
#         return idx1 <= idx2
# 
#     def __eq__(self, other):
#         return self.page_num == other.page_num
# 
#     def __ne__(self, other):
#         return self.page_num != other.page_num
# 
#     def __gt__(self, other):
#         idx1 = self.get_index()
#         idx2 = self.get_index()
#         return idx1 > idx2
# 
#     def __ge__(self, other):
#         idx1 = self.get_index()
#         idx2 = self.get_index()
#         return idx1 >= idx2
# 
#     def __repr__(self) -> str:
#         return str(self.page_num)
# 
#     def get_index(self) -> int:
#         if self.page_num in PageOrderRules.seq:
#             return PageOrderRules.seq.index(self.page_num)
#         return -1


class PageOrderRule:

    def __init__(self, rule_str: str) -> None:
        super().__init__()
        self.rule_str = rule_str
        self.page_1, self.page_2 = [int(x) for x in rule_str.split('|')]

    def __repr__(self) -> str:
        return f'{self.page_1}|{self.page_2}'


class PageOrderRules:

    def __init__(self, page_order_rules: list[PageOrderRule]) -> None:
        super().__init__()
        self.page_order_rules = page_order_rules
        self.seq: list[int] = []
        self.deferred_rules = []
        self.init_rules()

    def _init_rule(self, page_order_rule: PageOrderRule) -> None:
        print(f'\nrule: {page_order_rule}')
        print('\tBEFORE')
        print(f'\t\tseq: {self.seq}')
        print(f'\t\tdeferred_rules: {self.deferred_rules}')
        if not self.seq:
            print(
                f'\t\tfirst rule. adding {page_order_rule.page_1} and '
                f'{page_order_rule.page_2}')
            self.seq.append(page_order_rule.page_1)
            self.seq.append(page_order_rule.page_2)
            self.deferred_rules.remove(page_order_rule)
            print('\tAFTER')
            print(f'\t\tseq: {self.seq}')
            print(f'\t\tdeferred_rules: {self.deferred_rules}')
            return

        if (page_order_rule.page_1 not in self.seq
                and page_order_rule.page_2 not in self.seq):
            print(
                f'\t\tNeither {page_order_rule.page_1} nor '
                f'{page_order_rule.page_2} in seq')
            print('\t\tNo action taken')
            return

        if (page_order_rule.page_1 in self.seq
                and page_order_rule.page_2 not in self.seq):
            print(
                f'\t\t{page_order_rule.page_1} in seq '
                f'{page_order_rule.page_2} is not')
            idx = self.seq.index(page_order_rule.page_1)
            print(
                f'\t\tadd {page_order_rule.page_2} in seq after '
                f'{self.seq[idx]}')
            self.seq.insert(idx + 1, page_order_rule.page_2)
        elif (page_order_rule.page_1 not in self.seq
              and page_order_rule.page_2 in self.seq):
            print(
                f'\t\t{page_order_rule.page_2} in seq '
                f'{page_order_rule.page_1} is not')
            idx = self.seq.index(page_order_rule.page_2)
            print(
                f'\t\tadd {page_order_rule.page_1} in seq before '
                f'{self.seq[idx]}')
            self.seq.insert(idx, page_order_rule.page_1)
        else:
            print(
                f'\t\tBoth {page_order_rule.page_1} and '
                f'{page_order_rule.page_2} in seq')
            idx_1 = self.seq.index(page_order_rule.page_1)
            idx_2 = self.seq.index(page_order_rule.page_2)
            if idx_1 < idx_2:
                print(
                    f'\t\t{page_order_rule.page_1} is before '
                    f'{page_order_rule.page_2}')
                print(f'\t\tNo action taken')
            else:
                print(
                    f'\t\t{page_order_rule.page_1} is after '
                    f'{page_order_rule.page_2}')
                print(
                    f'\t\tswap {page_order_rule.page_1} and '
                    f'{page_order_rule.page_2} in seq')
                self.seq[idx_1] = page_order_rule.page_2
                self.seq[idx_2] = page_order_rule.page_1

        self.deferred_rules.remove(page_order_rule)
        print('\tAFTER')
        print(f'\t\tseq: {self.seq}')
        print(f'\t\tdeferred_rules: {self.deferred_rules}')

        return

    def init_rules(self) -> None:
        self.deferred_rules = list(self.page_order_rules)
        while self.deferred_rules:
            iter_deferred_rules = list(self.deferred_rules)
            for page_order_rule in iter_deferred_rules:
                self._init_rule(page_order_rule)

        self.deferred_rules = list(self.deferred_rules)
        while self.deferred_rules:
            iter_deferred_rules = list(self.deferred_rules)
            for page_order_rule in iter_deferred_rules:
                self._init_rule(page_order_rule)

        return


# @dataclass(repr=True)
class ManualUpdate:

    def __init__(self, pages_str: str,
                 page_order_rules: PageOrderRules) -> None:
        super().__init__()
        self.pages_str = pages_str
        self.pages = [int(x) for x in pages_str.split(',')]
        self.ordered_pages = []
        self.page_order_rules = page_order_rules

    def is_rule_satisfied(self, page_order_rule: PageOrderRule) -> bool:
        if (page_order_rule.page_1 not in self.pages or
                page_order_rule.page_2 not in self.pages):
            return True

        idx_1 = self.pages.index(page_order_rule.page_1)
        idx_2 = self.pages.index(page_order_rule.page_2)

        return idx_1 < idx_2

    def is_in_order(self) -> bool:
        for page_order_rule in self.page_order_rules.page_order_rules:
            if not self.is_rule_satisfied(page_order_rule):
                print(f'pages: {self.pages}')
                print(f'rule not satisfied: {page_order_rule}')
                print(f'seq: {self.page_order_rules.seq}')
                return False

        return True

    def get_ordered_pages(self) -> list[int]:
        if not self.ordered_pages:
            self.ordered_pages = sorted(self.pages, key=lambda
                x: self.page_order_rules.seq.index(x))
        return self.ordered_pages

    def get_middle_page(self) -> int:
        return self.pages[(len(self.pages) // 2)]


# 4384 is too low
# 4388 is too low

class Solver(AbstractSolver):

    def __init__(self) -> None:
        super().__init__()
        self.page_order_rules: PageOrderRules = None
        self.manual_updates: list[ManualUpdate] = []

    def init_data(self, data: list[str]) -> None:
        reading_rules = True
        page_order_rules = []
        for line in data:
            if line == '':
                reading_rules = False
                self.page_order_rules = PageOrderRules(page_order_rules)
                continue
            if reading_rules:
                page_order_rules.append(PageOrderRule(line))
            else:
                self.manual_updates.append(ManualUpdate(line, self.page_order_rules))

        return

    def solve_part_1(self, data: Any, **kwargs) -> int:
        self.init_data(data)
        return sum(
                update.get_middle_page() for update in
                self.manual_updates if
                update.is_in_order())

    def solve_part_2(self, data: Any, **kwargs) -> int:
        self.init_data(data)
        unordered_updates = []
        for update in self.manual_updates:
            if not update.is_in_order():
                unordered_updates.append(update)

        self.page_order_rules.init_rules()
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
