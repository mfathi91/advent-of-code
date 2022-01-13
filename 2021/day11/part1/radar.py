from typing import Dict
from typing import Tuple
from octopus import Octopus


class Radar:

    def __init__(self, octopus_map: dict):
        self.octopus_map = octopus_map

    def next_step(self):
        for octopus in self.octopus_map.values():
            octopus.next_step()

        octopus_map_step = dict(self.octopus_map)
        while True:
            flashing_octopuses = self.get_flashing_octopuses(octopus_map_step)
            if not flashing_octopuses:
                break
            else:
                for coordinate, flashing_octopus in flashing_octopuses.items():
                    adjacent_octopuses = self.get_adjacent_octopuses(octopus_map_step, coordinate)
                    for adj_coordinate, adj_octopus in adjacent_octopuses.items():
                        adj_octopus.adjacent_octopus_flashed()
                    del octopus_map_step[coordinate]

    @staticmethod
    def get_flashing_octopuses(octopus_map: dict) -> Dict[Tuple, Octopus]:
        flashing_octopuses = {}
        for coordinate, octopus in octopus_map.items():
            if octopus.is_flashing():
                flashing_octopuses[coordinate] = octopus
        return flashing_octopuses

    @staticmethod
    def get_adjacent_octopuses(octopus_map, coordinate) -> Dict[Tuple, Octopus]:
        adjacent_octopuses = {}
        x, y = coordinate[0], coordinate[1]
        candidate_coordinates = [(x, y - 1),
                                 (x - 1, y),
                                 (x, y + 1),
                                 (x + 1, y),
                                 (x - 1, y - 1),
                                 (x + 1, y + 1),
                                 (x - 1, y + 1),
                                 (x + 1, y - 1)]
        for candidate_coordinate in candidate_coordinates:
            if candidate_coordinate in octopus_map:
                adjacent_octopuses[candidate_coordinate] = octopus_map[candidate_coordinate]
        return adjacent_octopuses

    def get_num_flashes(self) -> int:
        num_flashes = 0
        for octopus in self.octopus_map.values():
            num_flashes += octopus.total_flashed
        return num_flashes
