import os
import re
import seven_segment


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        sum_total = 0
        for line in f:
            input_part1_raw = line.split('|')[0]
            input_part1 = re.findall('[a-z]+', input_part1_raw)
            ss = seven_segment.SevenSegment.identify_wiring(input_part1)
            input_part2_raw = line.split('|')[1]
            input_part2 = re.findall('[a-z]+', input_part2_raw)
            sum_total += ss.get_number(input_part2)

        print(sum_total)


if __name__ == '__main__':
    main()
