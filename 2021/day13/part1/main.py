import os
import re
from typing import Tuple, Set, List


def parse_paper(lines: List[str]) -> Set[Tuple]:
    paper = set()
    for line in lines:
        if not line:
            break
        x = int(line.split(',')[0])
        y = int(line.split(',')[1])
        paper.add((x, y))
    return paper


def parse_fold_instructions(lines: List[str]) -> List[Tuple]:
    fold_instructions = []
    fold_instructions_start = False
    for line in lines:
        if fold_instructions_start:
            instruction = re.findall('[x|y]=[0-9]+', line)[0]
            xy, value = instruction.split('=')[0], int(instruction.split('=')[1])
            fold_instructions.append((xy, value))
        if not line:
            fold_instructions_start = True

    return fold_instructions


def fold(paper: Set[Tuple], fold_command: str, fold_from: int) -> Set[Tuple]:
    folded_paper = set()
    for dot in paper:
        x, y = dot[0], dot[1]
        if fold_command == 'x':
            if x >= fold_from:
                folded_paper.add((2 * fold_from - x, y))
            else:
                folded_paper.add((x, y))

        elif fold_command == 'y':
            if y >= fold_from:
                folded_paper.add((x, 2 * fold_from - y))
            else:
                folded_paper.add((x, y))
    return folded_paper


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        lines = [line.rstrip() for line in f]
        paper = parse_paper(lines)
        fold_instruction = parse_fold_instructions(lines)[0]
        folded_paper = fold(paper, fold_instruction[0], fold_instruction[1])
        print(len(folded_paper))    # 638


if __name__ == '__main__':
    main()
