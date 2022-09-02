import os
import re
from pathlib import Path


def read_lines(file_name: str):
    lines = []
    file_path = os.path.join(Path(os.path.realpath(__file__)).parent.parent, file_name)
    with open(file_path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def main():
    lines = read_lines('input')
    int_lines = [int(l) for l in lines]
    int_lines.sort()

    print(int_lines)

    one_jolt_count = 0
    three_jolt_count = 0
    prev_num = 0
    for num in int_lines:
        diff = num - prev_num
        if diff == 1:
            one_jolt_count += 1
        elif diff == 3:
            three_jolt_count += 1

        prev_num = num

    print(one_jolt_count * (three_jolt_count + 1))


if __name__ == '__main__':
    main()
