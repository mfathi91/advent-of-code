import os

NUM_EASY_DIGITS = [
    2,    # Number of segments of 1
    4,    # Number of segments of 4
    3,    # Number of segments of 7
    7,    # Number of segments of 8
]


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        num_easy_digits = 0
        for line in f:
            for digit in line.split('|')[1].split(' '):
                if len(digit.replace('\r', '').replace('\n', '')) in NUM_EASY_DIGITS:
                    num_easy_digits += 1
        print(num_easy_digits)    # 383


if __name__ == '__main__':
    main()
