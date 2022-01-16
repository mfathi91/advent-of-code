import os
from collections import OrderedDict, Counter
from typing import List


def parse_nodes(lines: List[str]):
    node_map = OrderedDict()
    for line in lines:
        node1 = line.split('-')[0]
        node2 = line.split('-')[1]
        node1_adjacent_nodes = node_map[node1] if node1 in node_map else []
        node2_adjacent_nodes = node_map[node2] if node2 in node_map else []
        if node2 != 'start':
            node1_adjacent_nodes.append(node2)
        if node1 != 'start':
            node2_adjacent_nodes.append(node1)
        node_map[node1] = node1_adjacent_nodes
        node_map[node2] = node2_adjacent_nodes

    return node_map


def is_small_cave(cave: str):
    for ch in cave:
        if ch.isupper():
            return False
    return True


def can_enter(cave: str, current_path: List[str]):
    if not is_small_cave(cave):
        return True
    else:
        current_path_copy = list(current_path)
        current_path_copy.append(cave)
        small_caves = [c for c in current_path_copy if is_small_cave(c)]
        small_cave_count_map = Counter(small_caves)
        return not (len([sc for sc in small_cave_count_map.values() if sc > 1]) > 1 or
                    current_path_copy.count(cave) > 2)


def get_paths(current_path: List[str], node_map) -> List[List[str]]:
    paths = []
    current_node = current_path[-1]
    for adjacent_node in node_map[current_node]:
        if can_enter(adjacent_node, current_path):
            new_path = list(current_path)
            new_path.append(adjacent_node)
            if adjacent_node == 'end':
                paths.append(new_path)

            if adjacent_node != 'end':
                adjacent_paths = get_paths(new_path, node_map)
                for adjacent_path in adjacent_paths:
                    if 'end' in adjacent_path:
                        paths.append(adjacent_path)
    return paths


def filter_multiple_small_cave_paths(paths: List[List[str]]):
    filtered_paths = []
    for path in paths:
        small_cave_count_map = {}
        for cave in path:
            if is_small_cave(cave):
                small_cave_count_map[cave] = small_cave_count_map.get(cave, 0) + 1

        has_multiple_small_caves = len([sc for sc in small_cave_count_map.values() if sc > 1]) > 1
        if not has_multiple_small_caves:
            filtered_paths.append(path)

    return filtered_paths


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        lines = [line.rstrip() for line in f]
        node_map = parse_nodes(lines)
        for node, adjacent_nodes in node_map.items():
            if node == 'start':
                num_paths = 0
                for adjacent_node in adjacent_nodes:
                    paths = get_paths([adjacent_node], node_map)
                    num_paths += len(paths)
                print(num_paths)    # 134862


if __name__ == '__main__':
    main()
