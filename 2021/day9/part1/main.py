import os
from collections import OrderedDict


def get_adjacent_values(coordinate: tuple, heightmap: dict):
    adjacent_values = []
    coordinate_x = coordinate[0]
    coordinate_y = coordinate[1]
    if (coordinate_x - 1, coordinate_y) in heightmap:
        adjacent_values.append(heightmap[(coordinate_x - 1, coordinate_y)])
    if (coordinate_x, coordinate_y - 1) in heightmap:
        adjacent_values.append(heightmap[(coordinate_x, coordinate_y - 1)])
    if (coordinate_x + 1, coordinate_y) in heightmap:
        adjacent_values.append(heightmap[(coordinate_x + 1, coordinate_y)])
    if (coordinate_x, coordinate_y + 1) in heightmap:
        adjacent_values.append(heightmap[(coordinate_x, coordinate_y + 1)])
    return adjacent_values


def get_low_points(heightmap: dict):
    low_points = []
    for coordinate, value in heightmap.items():
        is_low_point = True
        for adjacent_value in get_adjacent_values(coordinate, heightmap):
            if value >= adjacent_value:
                is_low_point = False
                break
        if is_low_point:
            low_points.append(value)

    return low_points


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
        heightmap = OrderedDict()
        for i, row in enumerate(lines):
            for j, number in enumerate(row):
                heightmap[(i, j)] = int(row[j])

        risk_levels = [rl + 1 for rl in get_low_points(heightmap)]
        print(sum(risk_levels))    # 539


if __name__ == '__main__':
    main()
