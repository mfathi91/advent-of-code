import os
from pathlib import Path
from typing import List, Set


def read_lines(file_name: str) -> List[str]:
    file = Path(f'{os.path.realpath(__file__)}').parent.parent.joinpath(file_name)
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def section_to_set(section: str) -> Set[int]:
    start_end = section.split('-')
    start = int(start_end[0])
    end = int(start_end[1])
    return set(range(start, end + 1))


def main():
    s = 0
    for line in read_lines('input'):
        sections = line.split(',')
        set1 = section_to_set(sections[0])
        set2 = section_to_set(sections[1])
        if set1.issubset(set2) or set2.issubset(set1):
            s += 1

    print(s)  # 584


if __name__ == '__main__':
    main()
