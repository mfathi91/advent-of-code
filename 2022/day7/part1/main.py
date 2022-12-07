import os
import re
from pathlib import Path
from typing import List
from directory import Directory


def read_lines(file_name: str) -> List[str]:
    file = Path(f'{os.path.realpath(__file__)}').parent.parent.joinpath(file_name)
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def get_children(directory: Directory):
    children = []
    for child in directory.children:
        children.append(child)
        for grand_child in get_children(child):
            children.append(grand_child)
    return children


def main():
    lines = read_lines('input')

    root_dir = Directory('/', None)
    curr_dir = root_dir
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('$ cd'):
            result = re.search('^\\$ cd (.*)$', line)
            if not result:
                raise RuntimeError('Invalid line format detected')
            if result.group(1) == '/':
                curr_dir = root_dir
            elif result.group(1) == '..':
                curr_dir = curr_dir.parent if curr_dir.parent is not None else root_dir
            else:
                curr_dir = curr_dir.get_child(result.group(1))
            i += 1

        elif line == '$ ls':
            children = []
            files_size = 0
            i += 1
            while i < len(lines):
                ls_line = lines[i]
                if ls_line.startswith('$'):
                    break
                if ls_line.startswith('dir'):
                    children.append(ls_line.split()[1])
                else:
                    files_size += int(ls_line.split()[0])
                i += 1
            curr_dir.add_info(children, files_size)
            print(curr_dir)

    s = 0
    for directory in get_children(root_dir):
        if directory.get_size() < 100000:
            s += directory.get_size()
    print(s)  # 1449447


if __name__ == '__main__':
    main()
