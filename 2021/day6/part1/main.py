import os
import lantern_fish


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        fishes = []
        for fish_timer in f.readline().split(','):
            fishes.append(lantern_fish.LanternFish(int(fish_timer)))

        for day in range(80):
            for fish in fishes:
                fish.next_day()

        number = 0
        for fish in fishes:
            number += fish.get_number()
        print(number)    # 371379


if __name__ == '__main__':
    main()
