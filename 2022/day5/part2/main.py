import os
import re
from pathlib import Path
from typing import List, Dict


def read_lines(file_name: str) -> List[str]:
    file = Path(f'{os.path.realpath(__file__)}').parent.parent.joinpath(file_name)
    with open(file, 'r') as f:
        return [line.rstrip() for line in f.readlines()]


def get_stack_arrangement(lines: List[str]) -> Dict[int, List[str]]:
    arrangement: Dict[int, List[str]] = {}
    for line in lines:
        # Split the line every 4 characters
        crates = [line[i:i + 4] for i in range(0, len(line), 4)]
        for i, crate in enumerate(crates):
            if i+1 not in arrangement:
                arrangement[i+1] = []
            if crate[1].strip() != '':
                arrangement[i+1].append(crate[1])
    return arrangement


def main():
    load_lines = []
    instructions = []
    for line in read_lines('input'):
        if '[' in line:
            load_lines.append(line)
        elif 'move' in line:
            instructions.append(line)
    stack_arrangement = get_stack_arrangement(list(reversed(load_lines)))
    for instruction in instructions:
        result = re.search('move ([0-9]+) from ([1-9]) to ([1-9])', instruction)
        if not result:
            raise RuntimeError('Invalid line found')
        count = int(result.group(1))
        from_stack = int(result.group(2))
        to_stack = int(result.group(3))
        length = len(stack_arrangement[from_stack])
        sub_stack = list(stack_arrangement[from_stack][length - count:])
        del stack_arrangement[from_stack][length - count:]
        for crate in sub_stack:
            stack_arrangement[to_stack].append(crate)

    string = ''
    for i in range(1, 10):
        string += str(stack_arrangement[i][-1])
    print(string)  # MQTPGLLDN


if __name__ == '__main__':
    main()
