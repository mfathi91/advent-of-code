import os
from pathlib import Path
from typing import List


def read_lines(file_name: str) -> List[str]:
    file = Path(f'{os.path.realpath(__file__)}').parent.parent.joinpath(file_name)
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    s = 0
    group = []
    for i, line in enumerate(read_lines('input')):
        group.append(line)
        if (i + 1) % 3 == 0:
            intersection = set(group[0]).intersection(group[1]).intersection(group[2])
            common_char = next(iter(intersection))
            s = s + chars.index(common_char) + 1
            group.clear()
    print(s)  # 2425


if __name__ == '__main__':
    main()
