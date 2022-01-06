import os
import re
import space_2d
import line_2d
import point_2d


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        lines = []
        for input_line in f.read().splitlines():
            parsed_line = re.findall('[0-9]+', input_line)
            start_point = point_2d.Point(int(parsed_line[0]), int(parsed_line[1]))
            end_point = point_2d.Point(int(parsed_line[2]), int(parsed_line[3]))
            line = line_2d.Line(start_point, end_point)
            lines.append(line)

        print(space_2d.Space(lines).get_dangerous_points(2))    # 6841


if __name__ == '__main__':
    main()
