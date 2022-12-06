import os
from pathlib import Path
from typing import List


def read_lines(file_name: str) -> List[str]:
    file = Path(f'{os.path.realpath(__file__)}').parent.parent.joinpath(file_name)
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def main():
    line = read_lines('input')[0]
    queue = []
    index = 0
    for i, ch in enumerate(line):
        queue.append(ch)
        if len(queue) > 14:
            queue.pop(0)
            if len(queue) == len(set(queue)):
                index = i
                break
    print(index + 1)  # 2851


if __name__ == '__main__':
    main()
