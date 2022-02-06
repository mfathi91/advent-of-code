from typing import Dict, Tuple, List


class Board:

    def __init__(self, risk_map: Dict[Tuple[int, int], int]):
        self.risk_map = risk_map
        self.size = max([coordinate[0] for coordinate in risk_map])
        self.min_risk_tmp_cache = {}
        self.min_risk_cache = {}

    @staticmethod
    def get_min(a, b):
        if a is None:
            return b
        elif b is None:
            return a
        else:
            return min(a, b)

    @staticmethod
    def get_adjacent_coordinates(coordinate: Tuple[int, int], risk_map: Dict[Tuple[int, int], int]) -> \
            List[Tuple[int, int]]:
        x, y = coordinate[0], coordinate[1]
        adjacent_coordinates = []
        if (x - 1, y) in risk_map:
            adjacent_coordinates.append((x - 1, y))
        if (x, y - 1) in risk_map:
            adjacent_coordinates.append((x, y - 1))
        if (x + 1, y) in risk_map:
            adjacent_coordinates.append((x + 1, y))
        if (x, y + 1) in risk_map:
            adjacent_coordinates.append((x, y + 1))
        return adjacent_coordinates

    def find_lowest_risk(self):
        for box_size in reversed(range(self.size)):
            coordinates = [cs for cs in self.risk_map if (cs[0] >= box_size) and (cs[1] >= box_size)]
            risk_map_box = {}
            for coordinate in coordinates:
                risk_map_box[coordinate] = self.risk_map[coordinate]

            self.find_lowest_risk_in_box((self.size, box_size), risk_map_box)
            self.find_lowest_risk_in_box((box_size, self.size), risk_map_box)

            for coordinate in coordinates:
                if coordinate != (self.size, self.size):
                    self.min_risk_cache[coordinate] = self.min_risk_tmp_cache[coordinate]
        return self.min_risk_cache[(0, 0)]

    def find_lowest_risk_in_box(self, curr_coordinate: Tuple[int, int], risk_map: Dict[Tuple[int, int], int]) -> int:
        adj_risk_map = dict(risk_map)
        del adj_risk_map[curr_coordinate]
        min_risk = None
        for adj_coordinate in self.get_adjacent_coordinates(curr_coordinate, adj_risk_map):
            min_risk_candidate = self.min_risk_cache.get(adj_coordinate, None)
            if min_risk_candidate is None:
                if adj_coordinate == (self.size, self.size):
                    min_risk = self.get_min(min_risk, adj_risk_map[adj_coordinate])
                else:
                    adj_risk = self.find_lowest_risk_in_box(adj_coordinate, adj_risk_map)
                    min_risk = self.get_min(min_risk, adj_risk + risk_map[adj_coordinate])
            else:
                min_risk = self.get_min(min_risk, min_risk_candidate + risk_map[adj_coordinate])

        self.min_risk_tmp_cache[curr_coordinate] = self.get_min(min_risk, self.min_risk_tmp_cache.get(curr_coordinate))
        return min_risk
