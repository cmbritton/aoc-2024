#!/usr/bin/env python3
import os.path

from src.main.python.day09 import Solver

ANSWER_PART_1_EXAMPLE = -1
ANSWER_PART_2_EXAMPLE = -1
ANSWER_PART_1 = -1
ANSWER_PART_2 = -1


def test_part_1_example():
    solver = Solver()
    data_file_path = os.path.join(os.environ.get('TEST_RESOURCES_DIR_PATH'),
                                  f'day{solver.get_day()}-example.data')
    answer = solver.part_1(data_file_path)
    assert answer == ANSWER_PART_1_EXAMPLE


def test_part_2_example():
    solver = Solver()
    data_file_path = os.path.join(os.environ.get('TEST_RESOURCES_DIR_PATH'),
                                  f'day{solver.get_day()}-example.data')
    answer = solver.part_2(data_file_path)
    assert answer == ANSWER_PART_2_EXAMPLE


def test_part_1():
    solver = Solver()
    data_file_path = os.path.join(os.environ.get('RESOURCES_DIR_PATH'),
                                  f'day{solver.get_day()}.data')
    answer = solver.part_1(data_file_path)
    assert answer == ANSWER_PART_1


def test_part_2():
    solver = Solver()
    data_file_path = os.path.join(os.environ.get('RESOURCES_DIR_PATH'),
                                  f'day{solver.get_day()}.data')
    answer = solver.part_2(data_file_path)
    assert answer == ANSWER_PART_2
