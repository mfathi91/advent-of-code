import os
import re
from pathlib import Path
from typing import List
from directory import Directory


def read_lines(file_name: str) -> List[str]:
    file = Path(f'{os.path.realpath(__file__)}').parent.parent.joinpath(file_name)
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


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

    total_space = 70_000_000
    expected_min_free_space = 30_000_000
    actual_free_space = total_space - root_dir.get_size()

    candidates = []
    for child_dir in root_dir.get_children():
        if actual_free_space + child_dir.get_size() >= expected_min_free_space:
            candidates.append(child_dir.get_size())

    print(min(candidates))  # 8679207


if __name__ == '__main__':
    main()
