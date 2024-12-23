#!/usr/bin/env python3
"""
Day 9: Disk Fragmenter

https://adventofcode.com/2024/day/9
"""
from typing import Any

from src.main.python.util import AbstractSolver

DAY = '09'


class Segment(object):

    def __init__(self, start: int, count) -> None:
        super().__init__()
        self.start = start
        self.count = count


class File(object):

    def __init__(self, file_id: int, segment_list: list[Segment]) -> None:
        super().__init__()
        self.file_id = file_id
        self.segment_list = segment_list


class Disk(object):

    def __init__(self) -> None:
        super().__init__()
        self.files_by_id = dict()
        self.files_by_position = dict()
        self.free_space = dict()

    def checksum(self) -> int:
        return 0

    def merge_free_space(self) -> int:
        return 0


class Solver(AbstractSolver):

    def __init__(self) -> None:
        super().__init__()
        self.disk = Disk()

    def init_data(self, data: list[str]) -> None:
        file_id = 0
        file_segment_start = 0
        free_segment_start = 0
        for i in range(len(data) - 1, 2):
            file_block_count, free_block_count = int(data[i]), int(data[i + 1])
            file = File(file_id,
                        [Segment(file_segment_start, file_block_count)])
            self.disk.files_by_id[file_id] = file
            self.disk.files_by_position[file_segment_start] = file
            self.disk.free_space[free_segment_start] = Segment(
                free_segment_start, free_block_count)
            file_segment_start = file_segment_start + file_block_count
            free_segment_start = free_segment_start + free_block_count

    def solve_part_1(self, data: Any, **kwargs) -> int:
        self.init_data(data)
        return self.disk.checksum()

    def solve_part_2(self, data: Any, **kwargs) -> int:
        return -1

    def get_day(self):
        return DAY


def main() -> None:
    solver = Solver()
    solver.run_part_1()

    solver = Solver()
    solver.run_part_2()


if __name__ == "__main__":
    main()
