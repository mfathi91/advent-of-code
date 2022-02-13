import os
import sys
import timeit
from collections import OrderedDict
from typing import List, Dict, Tuple
from board import Board


def parse_risk_map(lines: List[str]):
    risk_map = OrderedDict()
    for y_idx, line in enumerate(lines):
        for x_idx, ch in enumerate(line):
            risk_map[(x_idx, y_idx)] = int(ch)
    return risk_map


def replicate_risk_map(risk_map: Dict[Tuple[int, int], int], n_replications) -> Dict[Tuple[int, int], int]:
    new_risk_map = {}
    size = max([coordinate[0] for coordinate in risk_map]) + 1
    for coordinate in risk_map:
        for i in range(n_replications):
            for j in range(n_replications):
                x, y = coordinate[0] + (i * size), coordinate[1] + (j * size)
                old_risk = risk_map[coordinate]
                new_risk_candidate = old_risk + i + j
                new_risk = new_risk_candidate if new_risk_candidate < 10 else new_risk_candidate - 9
                new_risk_map[(x, y)] = new_risk
    return new_risk_map


def print_board(risk_map: Dict[Tuple[int, int], int]):
    size = max([coordinate[0] for coordinate in risk_map])
    for i in range(size + 1):
        row = ''
        for j in range(size + 1):
            row += str(risk_map[(j, i)])
        print(row)


def main():
    sys.setrecursionlimit(1100)
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test')
    with open(input_file) as f:
        lines = [line.rstrip() for line in f]
        risk_map = parse_risk_map(lines)
        risk_map = replicate_risk_map(risk_map, 5)
        print_board(risk_map)
        board = Board(risk_map)
        print(board.find_lowest_risk())    #


if __name__ == '__main__':
    start = timeit.default_timer()
    main()
    end = timeit.default_timer()
    print('Time elapsed: ', end - start)
