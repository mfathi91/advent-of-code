import os
from pathlib import Path
from typing import List


def read_lines(file_name: str) -> List[str]:
    file = Path(f'{os.path.realpath(__file__)}').parent.parent.joinpath(file_name)
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def main():
    calories = []
    curr_calorie = 0
    lines = read_lines('input')
    for i, line in enumerate(lines):
        if line == '':
            calories.append(curr_calorie)
            curr_calorie = 0
        else:
            curr_calorie += int(line)

        if i == len(lines) - 1:
            calories.append(curr_calorie)

    print(max(calories))  # 74394


if __name__ == '__main__':
    main()