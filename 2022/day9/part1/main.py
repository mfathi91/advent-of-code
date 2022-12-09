import os
from pathlib import Path
from typing import List
from headtail import HeadTail


def read_lines(file_name: str) -> List[str]:
    file = Path(f'{os.path.realpath(__file__)}').parent.parent.joinpath(file_name)
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def main():
    head_tail = HeadTail()
    for line in read_lines('input'):
        parts = line.split()
        direction = parts[0]
        steps = int(parts[1])
        head_tail.move(direction, steps)
    print(len(head_tail.get_seen_coordinates()))  # 5779


if __name__ == '__main__':
    main()
