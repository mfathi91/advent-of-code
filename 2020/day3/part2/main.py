import os
from pathlib import Path


def read_lines(file_name: str):
    lines = []
    file_path = os.path.join(Path(__file__).parent.parent, file_name)
    with open(file_path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def main():
    lines = read_lines('input')
    tree_count_list = []
    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        coordinate = (0, 0)
        tree_count = 0
        while True:
            curr_x = coordinate[1]
            curr_y = coordinate[0]
            if lines[curr_y][curr_x] == '#':
                tree_count += 1
            new_x = curr_x + slope[0]
            new_x = new_x - len(lines[0]) if new_x >= len(lines[0]) else new_x
            new_y = curr_y + slope[1]
            coordinate = (new_y, new_x)
            if coordinate[0] >= len(lines):
                tree_count_list.append(tree_count)
                break

    product = 1
    for tc in tree_count_list:
        product *= tc

    print(product)    # 1478615040


if __name__ == '__main__':
    main()
