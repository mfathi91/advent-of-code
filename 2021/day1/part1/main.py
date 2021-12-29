import os

script_directory = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
input_path = os.path.join(script_directory, 'input')

with open(input_path, 'r') as input_file:
    prev_depth = int(input_file.readline())
    increased_count = 0
    for line in input_file:
        current_depth = int(line)
        if current_depth > prev_depth:
            increased_count += 1
        prev_depth = current_depth

print(increased_count)    #1791
