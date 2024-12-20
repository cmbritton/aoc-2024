#!/usr/bin/env python3
"""
Day 8: Resonant Collinearity

https://adventofcode.com/2024/day/7
"""
from collections import namedtuple, defaultdict
from itertools import permutations
from typing import Any

from src.main.python.util import AbstractSolver

DAY = '08'

Pos = namedtuple('Pos', ['x', 'y'])
Ant = namedtuple('Ant', ['pos', 'freq'])


class Solver(AbstractSolver):

    def __init__(self) -> None:
        super().__init__()
        self.antennas = defaultdict(list)
        self.antinodes = defaultdict(set)
        self.size = 0

    def init_data(self, data: list[str]) -> None:
        self.size = len(data)
        grid = [list(row) for row in data]
        for x in range(self.size):
            for y in range(self.size):
                if grid[x][y] != '.':
                    pos = Pos(x=x, y=y)
                    self.antennas[grid[x][y]].append(Ant(pos, freq=grid[x][y]))

    def find_antinodes_for_nodes(self, a1: Ant, a2: Ant) -> None:
        dist = Pos(x=a2.pos.x - a1.pos.x, y=a2.pos.y - a1.pos.y)

        p1 = Pos(x=a1.pos.x + dist.x, y=a1.pos.y + dist.y)
        if p1.x >= 0 and p1.x < self.size and p1.y >= 0 and p1.y < self.size:
            if p1 not in [a1.pos, a2.pos]:
                self.antinodes[a1.freq].add(p1)

        p1 = Pos(x=a1.pos.x - dist.x, y=a1.pos.y - dist.y)
        if p1.x >= 0 and p1.x < self.size and p1.y >= 0 and p1.y < self.size:
            if p1 not in [a1.pos, a2.pos]:
                self.antinodes[a1.freq].add(p1)

        p1 = Pos(x=a2.pos.x + dist.x, y=a2.pos.y + dist.y)
        if p1.x >= 0 and p1.x < self.size and p1.y >= 0 and p1.y < self.size:
            if p1 not in [a1.pos, a2.pos]:
                self.antinodes[a1.freq].add(p1)

        p1 = Pos(x=a2.pos.x - dist.x, y=a2.pos.y - dist.y)
        if p1.x >= 0 and p1.x < self.size and p1.y >= 0 and p1.y < self.size:
            if p1 not in [a1.pos, a2.pos]:
                self.antinodes[a1.freq].add(p1)


    def find_antinodes(self, freq: str, ants: list[Ant]) -> None:
        for a1, a2 in permutations(ants, 2):
            self.find_antinodes_for_nodes(a1, a2)

    def print_antinodes(self) -> None:
        print()
        for x in range(self.size):
            for y in range(self.size):
                pos = Pos(x=x, y=y)
                if pos in self.antinodes['0'] or pos in self.antinodes['A']:
                    print('#', end='')
                else:
                    print('.', end='')
            print()

    def solve_part_1(self, data: Any, **kwargs) -> int:
        self.init_data(data)
        for freq in self.antennas:
            self.find_antinodes(freq, self.antennas[freq])

        # self.print_antinodes()
        locs = set()
        for freq in self.antinodes:
            locs.update(self.antinodes[freq])
        return len(locs)

    def solve_part_2(self, data: Any, **kwargs) -> int:
        return 0

    def get_day(self):
        return DAY


def main() -> None:
    solver = Solver()
    solver.run_part_1()

    solver = Solver()
    solver.run_part_2()


if __name__ == "__main__":
    main()
