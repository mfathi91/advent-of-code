import os


def get_min_fuel_to_align(numbers: list):
    min_distance = None
    for destination in numbers:
        min_distance_candidate = 0
        for source in numbers:
            min_distance_candidate += abs(destination - source)
        if min_distance is None or min_distance_candidate < min_distance:
            min_distance = min_distance_candidate
    return min_distance


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        numbers = []
        for number in f.readline().split(','):
            numbers.append(int(number))
        print(get_min_fuel_to_align(numbers))    # 364898


if __name__ == '__main__':
    main()
