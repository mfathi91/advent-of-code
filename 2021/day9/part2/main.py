import os
from collections import OrderedDict


def get_adjacent_coordinates(coordinate: tuple, heightmap: dict):
    adjacent_values = {}
    x = coordinate[0]
    y = coordinate[1]
    if (x - 1, y) in heightmap:
        adjacent_values[(x - 1, y)] = heightmap[(x - 1, y)]
    if (x, y - 1) in heightmap:
        adjacent_values[(x, y - 1)] = heightmap[(x, y - 1)]
    if (x + 1, y) in heightmap:
        adjacent_values[(x + 1, y)] = heightmap[(x + 1, y)]
    if (x, y + 1) in heightmap:
        adjacent_values[(x, y + 1)] = heightmap[(x, y + 1)]
    return adjacent_values


def get_basin(coordinate: tuple, heightmap: dict):
    x, y = coordinate[0], coordinate[1]
    curr_coordinate_value = heightmap[(x, y)]
    basin_size = 1
    del heightmap[(x, y)]
    adjacent_coordinates = get_adjacent_coordinates((x, y), heightmap)
    for adj_coordinate, coordinate_value in adjacent_coordinates.items():
        if adj_coordinate in heightmap and coordinate_value != 9 and coordinate_value > curr_coordinate_value:
            basin_size += get_basin(adj_coordinate, heightmap)

    return basin_size


def get_basins(heightmap: dict):
    basins_size = []
    for coordinate, value in heightmap.items():
        is_low_point = True
        for key, adjacent_value in get_adjacent_coordinates(coordinate, heightmap).items():
            if value >= adjacent_value:
                is_low_point = False
                break
        if is_low_point:
            basins_size.append(get_basin(coordinate, dict(heightmap)))

    return basins_size


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
        heightmap = OrderedDict()
        for i, row in enumerate(lines):
            for j, number in enumerate(row):
                heightmap[(j, i)] = int(row[j])

        basins = sorted(get_basins(heightmap), reverse=True)
        print(basins[0] * basins[1] * basins[2])


if __name__ == '__main__':
    main()
