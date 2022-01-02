import os
import re
import bingo_board


def parse_numbers(lines):
    numbers = []
    for line in lines:
        if line:
            for number in line.split(','):
                numbers.append(number)
        else:
            break
    return numbers


def parse_boards(lines):
    boards = []
    current_board = []
    for i in range(2, len(lines)):
        line = lines[i]
        if line:
            current_board.append(re.findall('[0-9]{1,2}', line))
        else:
            boards.append(bingo_board.Board(current_board))
            current_board.clear()
    boards.append(bingo_board.Board(current_board))
    return boards


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        lines = f.read().splitlines()
        numbers = parse_numbers(lines)
        boards = parse_boards(lines)

        numbers_sublist = []
        for number in numbers:
            numbers_sublist.append(number)
            for board in list(boards):
                if board.row_or_column_contains_all(numbers_sublist):
                    if len(boards) == 1:
                        unmarked_numbers_sum = board.get_unmarked_numbers_sum(numbers_sublist)
                        final_score = unmarked_numbers_sum * int(number)
                        print(final_score)    # 4920
                        return
                    else:
                        boards.remove(board)


if __name__ == '__main__':
    main()
