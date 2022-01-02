class Board:

    def __init__(self, rows):
        self.rows = list(rows)
        columns = [[0 for i in range(5)] for j in range(5)]
        for i in range(5):
            for j in range(5):
                columns[i][j] = rows[j][i]
        self.columns = columns

    def row_or_column_contains_all(self, numbers):
        for row in self.rows:
            if set(row).issubset(numbers):
                return True
        for column in self.columns:
            if set(column).issubset(numbers):
                return True
        return False

    def get_unmarked_numbers_sum(self, numbers):
        unmarked_numbers_sum = 0
        board_all_numbers = set()
        for row in self.rows:
            for elem in row:
                board_all_numbers.add(elem)
        unmarked_numbers = board_all_numbers - set(numbers)

        for unmarked_number in unmarked_numbers:
            unmarked_numbers_sum += int(unmarked_number)

        return unmarked_numbers_sum

    def __str__(self):
        string = ''
        for row in self.rows:
            string += ' '.join(row)
            string += '\n'
        return string
