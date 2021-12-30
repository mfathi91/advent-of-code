import os

input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')

with open(input_file) as lines:
    horizontal_position = 0
    vertical_position = 0
    for line in lines:
        line_elements = line.split()
        command = line_elements[0]
        command_value = int(line_elements[1])
        if command == 'forward':
            horizontal_position += command_value
        elif command == 'up':
            vertical_position -= command_value
        elif command == 'down':
            vertical_position += command_value

    print(horizontal_position * vertical_position)    # 1693300
