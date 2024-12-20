# [Advent of Code 2023](https://adventofcode.com/2023)

My solutions to Advent of Code (AoC) 2024 puzzles.

Some programmers aim to solve each puzzle in as few lines of code as possible.
Others create really cool animations of puzzle solutions. There are some
extremely skilled people in both camps.

I try to write understandable, maintainable, and extendable object-oriented
code.

## Development Environment

Here's what I use.

### Platform-Independent

* [IntelliJ IDEA](https://www.jetbrains.com/idea/)
* [Python](https://www.python.org/)
* [pipenv](https://pipenv.pypa.io/en/latest/)

### Platform-Specific

* [Windows 10 Pro](https://www.microsoft.com/en-us/software-download/windows10)
* [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) running
  an [Ubuntu 22.04 LTS](https://ubuntu.com/) distribution.

## Setup
Edit the `.env` file to match your environment. Then, run:

    pipenv install

## Run a Daily Puzzle

Run a single puzzle with:

    pipenv run day08.py

## Running Unit Tests

    pipenv run test

## Code Evolution

The logic for each solution is in the `dayxx._init_data`, `dayxx.solve_part_1`,
and `dayxx.solve_part_2` methods. Everything else is common code for reading
puzzle data, testing, outputting results, etc.

Most puzzle solutions follow a pattern you can discern from the commit
messages.

Any commit whose message begins with `WIP` is a work-in-progress checkpoint.
That version may not even work.

Commit messages that look like `Day 8 part 1 works` indicate the revision
that first achieved the correct answer. It might be sloppy. It might be slow.

Messages that contain the word `cleanup` indicate a revision where I removed
commented out lines of code, print statements, etc.

Messages with the word `refactor` mark a revision where I refactored the
original solution to improve readability, performance, or use some language
feature that I was not familiar with enough to use in my initial solution. 

## Results

No answers here! Just elapsed times for each puzzle solution.

| Puzzle                                                        | Part 1 Elapsed Time | Part 2 Elapsed Time |
|---------------------------------------------------------------|--------------------:|--------------------:|
| [Day  1: Historian Hysteria](https://adventofcode.com/2024/1) |   1.86 milliseconds |   4.18 milliseconds |
| [Day  2: Red-Nosed Reports](https://adventofcode.com/2024/2)  |   2.10 milliseconds |   4.40 milliseconds |
| [Day  3: Mull It Over](https://adventofcode.com/2024/3)       |   2.03 milliseconds | 858.20 microseconds |
| [Day  4: Ceres Search](https://adventofcode.com/2024/4)       |  18.74 milliseconds |   1.98 milliseconds |
| [Day  5: Print Queue](https://adventofcode.com/2024/5)        | 106.13 milliseconds | 104.39 milliseconds |
| [Day  6: Guard Gallivant](https://adventofcode.com/2024/6)    |  17.37 milliseconds |      224.51 seconds |
| [Day  7: Bridge Repair](https://adventofcode.com/2024/7)      | 159.46 milliseconds |            Unsolved |
| [Day  8: Unavailable](https://adventofcode.com/2024/8)        |            Unsolved |            Unsolved |
| [Day  9: Unavailable](https://adventofcode.com/2024/9)        |            Unsolved |            Unsolved |
| [Day 10: Unavailable](https://adventofcode.com/2024/10)       |            Unsolved |            Unsolved |
| [Day 11: Unavailable](https://adventofcode.com/2024/11)       |            Unsolved |            Unsolved |
| [Day 12: Unavailable](https://adventofcode.com/2024/12)       |            Unsolved |            Unsolved |
| [Day 13: Unavailable](https://adventofcode.com/2024/13)       |            Unsolved |            Unsolved |
| [Day 14: Unavailable](https://adventofcode.com/2024/14)       |            Unsolved |            Unsolved |
| [Day 15: Unavailable](https://adventofcode.com/2024/15)       |            Unsolved |            Unsolved |
| [Day 16: Unavailable](https://adventofcode.com/2024/16)       |            Unsolved |            Unsolved |
| [Day 17: Unavailable](https://adventofcode.com/2024/17)       |            Unsolved |            Unsolved |
| [Day 18: Unavailable](https://adventofcode.com/2024/18)       |            Unsolved |            Unsolved |
| [Day 19: Unavailable](https://adventofcode.com/2024/19)       |            Unsolved |            Unsolved |
| [Day 20: Unavailable](https://adventofcode.com/2024/20)       |            Unsolved |            Unsolved |
| [Day 21: Unavailable](https://adventofcode.com/2024/21)       |            Unsolved |            Unsolved |
| [Day 22: Unavailable](https://adventofcode.com/2024/22)       |            Unsolved |            Unsolved |
| [Day 23: Unavailable](https://adventofcode.com/2024/23)       |            Unsolved |            Unsolved |
| [Day 24: Unavailable](https://adventofcode.com/2024/24)       |            Unsolved |            Unsolved |
| [Day 25: Unavailable](https://adventofcode.com/2024/25)       |            Unsolved |            Unsolved |
