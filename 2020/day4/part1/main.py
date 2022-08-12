import os
from pathlib import Path
from passport import Passport
from typing import List

def read_lines(file_name: str):
    lines = []
    file_path = os.path.join(Path(os.path.realpath(__file__)).parent.parent, file_name)
    with open(file_path) as file:
        for line in file:
            lines.append(line.strip())
    return lines

def get_passports(lines: List[str]):
    passports = []
    passport_start_idx = 0
    last_line_idx = len(lines) - 1
    for curr_idx, line in enumerate(lines):
        if not line or curr_idx==last_line_idx:
            passport_end_idx = curr_idx + 1 if curr_idx == last_line_idx else curr_idx
            new_passport = Passport(' '.join(lines[passport_start_idx:passport_end_idx]))
            passports.append(new_passport)
            passport_start_idx = curr_idx + 1
    return passports

def main():
    lines = read_lines('input')
    passports = get_passports(lines)
#    breakpoint()
    valid_count = 0
    for passport in passports:
        if passport.is_valid():
            valid_count += 1
    print(valid_count)

if __name__ == '__main__':
    main()
