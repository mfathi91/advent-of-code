import os
import octopus
from radar import Radar
from collections import OrderedDict


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        octopus_map = OrderedDict()
        for i, line in enumerate(f):
            for j, ch in enumerate(line.rstrip()):
                octopus_map[(j, i)] = octopus.Octopus(int(ch))

        radar = Radar(octopus_map)
        for i in range(100):
            radar.next_step()
        print(radar.get_num_flashes())    # 1608


if __name__ == '__main__':
    main()
