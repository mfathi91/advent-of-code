import os
from pathlib import Path
from typing import List
from hill import Hill


def read_lines(file_name: str) -> List[str]:
    file = Path(f'{os.path.realpath(__file__)}').parent.parent.joinpath(file_name)
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def main():
    lines = read_lines('input')
    h = Hill(lines)
    print(h.climb())


if __name__ == '__main__':
    main()
