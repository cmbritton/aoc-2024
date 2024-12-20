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

    def test_set_collinear_antinode(self, p1: Pos, dist: Pos,
                                    freq: str) -> None:
        while 0 <= p1.x < self.size and 0 <= p1.y < self.size:
            self.antinodes[freq].add(p1)
            p1 = Pos(x=p1.x + dist.x, y=p1.y + dist.y)

    def find_collinear_antinodes_for_nodes(self, a1: Ant, a2: Ant) -> None:
        dist = Pos(x=a2.pos.x - a1.pos.x, y=a2.pos.y - a1.pos.y)

        p1 = Pos(x=a1.pos.x + dist.x, y=a1.pos.y + dist.y)
        self.test_set_collinear_antinode(p1, dist, a1.freq)

        p1 = Pos(x=a1.pos.x - dist.x, y=a1.pos.y - dist.y)
        self.test_set_collinear_antinode(p1, Pos(x=0 - dist.x, y=0 - dist.y),
                                         a1.freq)

        p1 = Pos(x=a2.pos.x + dist.x, y=a2.pos.y + dist.y)
        self.test_set_collinear_antinode(p1, dist, a2.freq)

        p1 = Pos(x=a2.pos.x - dist.x, y=a2.pos.y - dist.y)
        self.test_set_collinear_antinode(p1, Pos(x=0 - dist.x, y=0 - dist.y),
                                         a2.freq)

    def test_set_resonate_antinode(self, p1: Pos, ant_pair: tuple[Pos, Pos],
                                   freq: str) -> None:
        if 0 <= p1.x < self.size and 0 <= p1.y < self.size:
            if p1 not in ant_pair:
                self.antinodes[freq].add(p1)

    def find_resonate_antinodes_for_nodes(self, a1: Ant, a2: Ant) -> None:
        dist = Pos(x=a2.pos.x - a1.pos.x, y=a2.pos.y - a1.pos.y)

        p1 = Pos(x=a1.pos.x + dist.x, y=a1.pos.y + dist.y)
        self.test_set_resonate_antinode(p1, (a1.pos, a2.pos), a1.freq)

        p1 = Pos(x=a1.pos.x - dist.x, y=a1.pos.y - dist.y)
        self.test_set_resonate_antinode(p1, (a1.pos, a2.pos), a1.freq)

        p1 = Pos(x=a2.pos.x + dist.x, y=a2.pos.y + dist.y)
        self.test_set_resonate_antinode(p1, (a1.pos, a2.pos), a1.freq)

        p1 = Pos(x=a2.pos.x - dist.x, y=a2.pos.y - dist.y)
        self.test_set_resonate_antinode(p1, (a1.pos, a2.pos), a1.freq)

    def find_collinear_antinodes(self, freq: str, ants: list[Ant]) -> None:
        for a1, a2 in permutations(ants, 2):
            self.find_collinear_antinodes_for_nodes(a1, a2)

    def find_resonate_antinodes(self, freq: str, ants: list[Ant]) -> None:
        for a1, a2 in permutations(ants, 2):
            self.find_resonate_antinodes_for_nodes(a1, a2)

    def solve_part_1(self, data: Any, **kwargs) -> int:
        self.init_data(data)
        for freq in self.antennas:
            self.find_resonate_antinodes(freq, self.antennas[freq])

        locs = set()
        for freq in self.antinodes:
            locs.update(self.antinodes[freq])
        return len(locs)

    def solve_part_2(self, data: Any, **kwargs) -> int:
        self.init_data(data)
        for freq in self.antennas:
            self.find_collinear_antinodes(freq, self.antennas[freq])

        locs = set()
        for freq in self.antinodes:
            locs.update(self.antinodes[freq])
        return len(locs)

    def get_day(self):
        return DAY


def main() -> None:
    solver = Solver()
    solver.run_part_1()

    solver = Solver()
    solver.run_part_2()


if __name__ == "__main__":
    main()
