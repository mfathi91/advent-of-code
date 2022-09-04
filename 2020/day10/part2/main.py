import os
import re
from pathlib import Path
from typing import List, Dict


def read_lines(file_name: str):
    lines = []
    file_path = os.path.join(Path(os.path.realpath(__file__)).parent.parent, file_name)
    with open(file_path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def paths_from(numbers:List[int], idx: int, paths_cache:Dict[int, int]) -> int:
    if idx == len(numbers) - 1:
        return 1

    if idx in paths_cache:
        return paths_cache[idx]

    paths = 0
    for i in range(idx+1, idx+4):
        if i < len(numbers) and numbers[i] <= numbers[idx] + 3:
            paths_calculated = paths_from(numbers, i, paths_cache)
            paths_cache[i] = paths_calculated
            paths += paths_calculated

    return paths


def main():
    lines = read_lines('input')
    int_lines = [int(l) for l in lines]
    int_lines.append(0)
    int_lines.append(max(int_lines)+3)
    int_lines.sort()
    print(paths_from(int_lines, 0, {}))   # 226775649501184


if __name__ == '__main__':
    main()
