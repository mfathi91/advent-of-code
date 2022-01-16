import os
from collections import OrderedDict
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


def multiple_entry_allowed(node: str):
    allowed = True
    for ch in node:
        if ch.islower():
            allowed = False
            break
    return allowed


def get_paths(current_path: List[str], node_map) -> List[List[str]]:
    paths = []
    current_node = current_path[-1]
    for adjacent_node in node_map[current_node]:
        if adjacent_node not in current_path or multiple_entry_allowed(adjacent_node):
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


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        lines = [line.rstrip() for line in f]
        node_map = parse_nodes(lines)
        for node, adjacent_nodes in node_map.items():
            if node == 'start':
                num_paths = 0
                for adjacent_node in adjacent_nodes:
                    num_paths += len(get_paths([adjacent_node], node_map))

                print(num_paths)    # 5212


if __name__ == '__main__':
    main()
