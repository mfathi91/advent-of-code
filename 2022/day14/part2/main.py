import os
from pathlib import Path
from typing import List, Tuple, Set
from cave import Cave


def read_lines(file_name: str) -> List[str]:
    file = Path(f'{os.path.realpath(__file__)}').parent.parent.joinpath(file_name)
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def parse_rocks(lines: List[str]) -> Set[Tuple[int, int]]:
    rocks = set()
    for line in lines:
        points = line.split('->')
        for i in range(len(points) - 1):
            p1 = points[i].strip().split(',')
            p2 = points[i + 1].strip().split(',')
            x1, y1 = int(p1[1]), int(p1[0])
            x2, y2 = int(p2[1]), int(p2[0])
            dx, dy = x2 - x1, y2 - y1
            for j in range(abs(dx) + 1):
                ddx = j if dx >= 0 else -j
                rocks.add((x1 + ddx, y1))
            for j in range(abs(dy) + 1):
                ddy = j if dy >= 0 else -j
                rocks.add((x1, y1 + ddy))
    return rocks


def main():
    rocks = parse_rocks(read_lines('input'))
    cave = Cave(rocks)
    print(cave.sand())

if __name__ == '__main__':
    main()
