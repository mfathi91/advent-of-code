import os
import re
from pathlib import Path


def read_lines(file_name: str):
    lines = []
    file_path = os.path.join(Path(__file__).parent.parent, file_name)
    with open(file_path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def main():
    valid_password_count = 0
    pattern = '([0-9]{1,2})-([0-9]{1,2}) ([a-z]{1,}): ([a-z]*)'
    for line in read_lines('input'):
        match = re.match(pattern, line)
        if not match:
            raise ValueError('Invalid line f{line}')
        min_allowed_freq = match.group(1)
        max_allowed_freq = match.group(2)
        character = match.group(3)
        password = match.group(4)
        freq = password.count(character)
        if int(min_allowed_freq) <= freq <= int(max_allowed_freq):
            valid_password_count += 1

    print(valid_password_count)    # 548


if __name__ == '__main__':
    main()
