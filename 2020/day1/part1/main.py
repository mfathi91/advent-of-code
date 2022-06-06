import os
from pathlib import Path


def read_lines(file_name: str):
    lines = []
    file_path = os.path.join(Path(__file__).parent.parent, file_name)
    with open(file_path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def get_2020_multiplication():
    lines = read_lines('input')
    for idx1, line1 in enumerate(lines):
        for idx2, line2 in enumerate(lines):
            if idx1 != idx2 and (int(line1) + int(line2)) == 2020:
                return int(line1) * int(line2)


if __name__ == '__main__':
    print(get_2020_multiplication())  # 913824
