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
    for line in read_lines('input'):
        length = len(line)
        first = line[0:int(length / 2)]
        second = line[int(length / 2):]
        intersection = set(first).intersection(second)
        common_char = next(iter(intersection))
        s = s + chars.index(common_char) + 1
    print(s)  # 8053


if __name__ == '__main__':
    main()
