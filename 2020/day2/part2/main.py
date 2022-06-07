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
        first_position = int(match.group(1))
        second_position = int(match.group(2))
        character = match.group(3)
        password = match.group(4)
        first_position_match = password[first_position - 1] == character
        second_position_match = password[second_position - 1] == character
        if (first_position_match or second_position_match) and not (first_position_match and second_position_match):
            valid_password_count += 1

    print(valid_password_count)    # 502


if __name__ == '__main__':
    main()
