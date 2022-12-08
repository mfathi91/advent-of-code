import os
from pathlib import Path
from typing import List
from forest import Forest


def read_lines(file_name: str) -> List[str]:
    file = Path(f'{os.path.realpath(__file__)}').parent.parent.joinpath(file_name)
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def main():
    lines = read_lines('input')
    trees = [[0 for x in range(len(lines))] for y in range(len(lines[0]))]
    for row_idx, row in enumerate(lines):
        for column_idx, tree_height in enumerate(row):
            trees[row_idx][column_idx] = int(tree_height)

    forest = Forest(trees)
    print(forest.max_scenic_score())  # 201600


if __name__ == '__main__':
    main()
