import os
import timeit
from collections import OrderedDict
from typing import List
from board import Board


def parse_risk_map(lines: List[str]):
    risk_map = OrderedDict()
    for y_idx, line in enumerate(lines):
        for x_idx, ch in enumerate(line):
            risk_map[(x_idx, y_idx)] = int(ch)
    return risk_map


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        lines = [line.rstrip() for line in f]
        risk_map = parse_risk_map(lines)
        board = Board(risk_map)
        print(board.find_lowest_risk())    # 537


if __name__ == '__main__':
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print('Time elapsed: ', end - start)
