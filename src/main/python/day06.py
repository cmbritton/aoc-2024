#!/usr/bin/env python3
"""
Day 6: Guard Gallivant

https://adventofcode.com/2024/day/6
"""
from collections import namedtuple
from enum import Enum
from typing import Any

from src.main.python.util import AbstractSolver

DAY = '06'

Pos = namedtuple('Pos', ['x', 'y', 'dir'])


class Direction(Enum):
    UP = '^'
    RIGHT = '>'
    DOWN = 'v'
    LEFT = '<'


class Lab(object):

    def __init__(self, floor: list[list[str]]) -> None:
        super().__init__()
        self.floor = floor
        self.max_idx = len(floor) - 1

    def find_start(self) -> Pos:
        for i, row in enumerate(self.floor):
            for j, col in enumerate(row):
                if col == '^':
                    return Pos(x=i, y=j, dir=Direction.UP)

        raise ValueError('No starting point found')


class Guard(object):

    def __init__(self, lab: Lab) -> None:
        super().__init__()
        self.lab = lab
        self.pos = Pos(x=0, y=0, dir=Direction.UP)
        self.visited = set()
        self.is_loop = False

    def set_start_pos(self, pos: Pos) -> None:
        self.pos = pos
        self.visited.add(self.pos)
        return

    def _step(self) -> Pos:
        if self.pos.dir == Direction.UP:
            new_pos = Pos(x=self.pos.x - 1, y=self.pos.y, dir=self.pos.dir)
        elif self.pos.dir == Direction.RIGHT:
            new_pos = Pos(x=self.pos.x, y=self.pos.y + 1, dir=self.pos.dir)
        elif self.pos.dir == Direction.DOWN:
            new_pos = Pos(x=self.pos.x + 1, y=self.pos.y, dir=self.pos.dir)
        else:  # self.pos.dir == Direction.LEFT
            new_pos = Pos(x=self.pos.x, y=self.pos.y - 1, dir=self.pos.dir)

        return new_pos

    def step(self) -> None:
        self.pos = self._step()
        if self.pos in self.visited:
            self.is_loop = True
        if not self.is_out_of_lab():
            self.visited.add(self.pos)
        return

    def is_direction_up(self) -> bool:
        return self.pos.dir == Direction.UP

    def is_direction_right(self) -> bool:
        return self.pos.dir == Direction.RIGHT

    def is_direction_down(self) -> bool:
        return self.pos.dir == Direction.DOWN

    def is_direction_left(self) -> bool:
        return self.pos.dir == Direction.LEFT

    def _is_in_lab(self, pos: Pos) -> bool:
        return 0 <= pos.x <= self.lab.max_idx \
            and 0 <= pos.y <= self.lab.max_idx

    def is_in_lab(self) -> bool:
        return self._is_in_lab(self.pos)

    def _is_out_of_lab(self, pos: Pos) -> bool:
        return not self._is_in_lab(pos)

    def is_out_of_lab(self) -> bool:
        return self._is_out_of_lab(self.pos)

    def turn_right(self) -> None:
        if self.is_direction_up():
            self.pos = Pos(self.pos.x, self.pos.y, Direction.RIGHT)
        elif self.is_direction_right():
            self.pos = Pos(self.pos.x, self.pos.y, Direction.DOWN)
        elif self.is_direction_down():
            self.pos = Pos(self.pos.x, self.pos.y, Direction.LEFT)
        else:  # self.is_direction_left()
            self.pos = Pos(self.pos.x, self.pos.y, Direction.UP)
        return

    def sees_obstacle(self) -> bool:
        next_step = self._step()
        if self._is_out_of_lab(next_step):
            return False
        if self.lab.floor[next_step.x][next_step.y] == '#':
            return True
        return False


class Solver(AbstractSolver):

    def __init__(self) -> None:
        super().__init__()
        self.guard = None
        self.lab = None

    def init_data(self, data: list[str]) -> None:
        grid = [list(row) for row in data]
        self.lab = Lab(grid)
        self.guard = Guard(self.lab)
        self.guard.set_start_pos(self.lab.find_start())
        return

    def is_loop(self) -> bool:
        while not self.guard.is_out_of_lab():
            if self.guard.sees_obstacle():
                self.guard.turn_right()
            else:
                self.guard.step()
                if self.guard.is_loop:
                    return True
        return False

    def solve_part_1(self, data: Any, **kwargs) -> int:
        self.init_data(data)

        while not self.guard.is_out_of_lab():
            if self.guard.sees_obstacle():
                self.guard.turn_right()
            else:
                self.guard.step()

        visited = set()
        for pos in self.guard.visited:
            visited.add((pos.x, pos.y))
        return len(visited)

    def solve_part_2(self, data: Any, **kwargs) -> int:
        self.init_data(data)
        total = x = 0
        while x <= self.lab.max_idx:
            y = 0
            while y <= self.lab.max_idx:
                if self.lab.floor[x][y] == '.':
                    self.lab.floor[x][y] = '#'
                    self.guard = Guard(self.lab)
                    self.guard.set_start_pos(self.lab.find_start())
                    if self.is_loop():
                        total += 1
                    self.lab.floor[x][y] = '.'
                y += 1
            x += 1

        return total

    def get_day(self):
        return DAY


def main() -> None:
    solver = Solver()
    solver.run_part_1()

    solver = Solver()
    solver.run_part_2()


if __name__ == "__main__":
    main()
