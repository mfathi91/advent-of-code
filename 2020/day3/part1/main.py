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
    tree_count = 0
    coordinate = (0, 0)
    while coordinate[0] < len(lines):
        curr_x = coordinate[1]
        curr_y = coordinate[0]
        if lines[curr_y][curr_x] == '#':
            tree_count += 1
        new_x = curr_x + 3
        new_x = new_x - len(lines[0]) if new_x >= len(lines[0]) else new_x
        new_y = curr_y + 1
        coordinate = (new_y, new_x)

    print(tree_count)    # 191


if __name__ == '__main__':
    main()
