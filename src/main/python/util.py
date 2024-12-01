import os
import re
import sys
import time
from abc import abstractmethod, ABC
from typing import Any


class Timer:
    """
    Track the elapsed time to solve various parts of the puzzle.
    """

    def __init__(self) -> None:
        """
        Create a new Timer and start it.
        """
        self.start_time = time.perf_counter()
        self.end_time = None

    def stop(self) -> None:
        """
        Stop the Timer.
        """
        self.end_time = time.perf_counter()

    def elapsed_time(self) -> str:
        """
        Format a string that represents the elapsed time.

        Scale the elapsed time value to seconds, milliseconds, microseconds,
        or nanoseconds based on the magnitude of the value.

        Returns:
            The string representation of the elapsed time for this Timer.
        """
        if self.end_time is None:
            self.stop()
        t = self.end_time - self.start_time
        unit = 'seconds'
        if t < 1:
            t = t * 1000
            unit = 'milliseconds'
        if t < 1:
            t = t * 1000
            unit = 'microseconds'
        if t < 1:
            t = t * 1000
            unit = 'nanoseconds'

        return f'{t:.2f} {unit}'


class AbstractSolver(ABC):
    def __init__(self) -> None:
        self.data = None

    @abstractmethod
    def solve_part_1(self, data: Any, **kwargs) -> Any:
        pass

    @abstractmethod
    def solve_part_2(self, data: Any, **kwargs) -> Any:
        pass

    def get_day(self):
        return re.search(r'day(\d\d)', sys.argv[-1]).group(1)

    def part_1(self, data_file_path: str = None, **kwargs) -> Any:
        timer = Timer()
        answer = self.solve_part_1(
            self.get_data(self.get_day(), data_file_path), **kwargs)
        timer.stop()

        self.print_info(part='Part 1', timer=timer, answer=answer)

        return answer

    def part_2(self, data_file_path: str = None, **kwargs) -> Any:
        timer = Timer()
        answer = self.solve_part_2(
            self.get_data(self.get_day(), data_file_path), **kwargs)
        timer.stop()

        self.print_info(part='Part 2', timer=timer, answer=answer)

        return answer

    def run(self) -> None:
        day = self.get_day()
        data_file_path = os.path.join(os.environ.get('RESOURCES_DIR_PATH'),
                                      f'day{day}.data')
        self.part_1(data_file_path)
        self.part_2(data_file_path)

    @staticmethod
    def print_info(part: str, timer: Timer, answer: int) -> None:
        print(f'{part}\n'
              f'    Elapsed Time: {timer.elapsed_time()}\n'
              f'          Answer: {answer}')

    @staticmethod
    def get_data(day: str, data_file_path: str = None) -> list[str]:
        if data_file_path:
            path = data_file_path
        else:
            path = os.path.join(os.environ.get('RESOURCES_DIR_PATH'),
                                f'day{day}.data')
        with open(path, 'r') as data_file:
            return data_file.read().splitlines()
