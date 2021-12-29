import os

script_directory = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(script_directory, 'input')

with open(input_path, 'r') as input_file:
    lines = input_file.read().splitlines()
    normalized_depths = []
    for i in range(len(lines)):
        if len(lines) > i + 2:
            normalized_depths.append(int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2]))

    prev_normalized_depth = None
    increased_depth = 0
    for stabilized_depth in normalized_depths:
        if prev_normalized_depth is not None and stabilized_depth > prev_normalized_depth:
            increased_depth += 1
        prev_normalized_depth = stabilized_depth

    print(increased_depth)    # 1822
