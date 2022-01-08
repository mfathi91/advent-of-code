import os

sigma_cache = {}


def get_sigma(number: int):
    if number in sigma_cache:
        return sigma_cache[number]
    else:
        sigma = 0
        for i in range(number, 0, -1):
            sigma += i
        sigma_cache[number] = sigma
        return sigma


def get_min_fuel_to_align(numbers: list):
    min_distance = None
    for destination in range(max(numbers)):
        min_distance_candidate = 0
        for source in numbers:
            sigma = get_sigma(abs(destination - source))
            min_distance_candidate += sigma
        if min_distance is None or min_distance_candidate < min_distance:
            min_distance = min_distance_candidate
    return min_distance


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        numbers = []
        for number in f.readline().split(','):
            numbers.append(int(number))
        print(get_min_fuel_to_align(numbers))    # 104149091


if __name__ == '__main__':
    main()
