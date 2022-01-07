import os
import lantern_fish


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        timers = []
        for timer in f.readline().split(','):
            timers.append(int(timer))

        fish = lantern_fish.LanternFish(timers)
        for day in range(256):
            fish.next_day()

        print(fish.get_number())    # 1674303997472


if __name__ == '__main__':
    main()
