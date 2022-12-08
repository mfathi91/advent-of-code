class Forest:

    def __init__(self, trees):
        self.trees = trees
        self.rows_len = len(trees)
        self.columns_len = len(trees[0])

    def get_scenic_score_of_tree(self, x, y):
        top_score = 0
        for row in range(x - 1, -1, -1):
            top_score += 1
            if self.trees[row][y] >= self.trees[x][y]:
                break

        right_score = 0
        for column in range(y + 1, self.columns_len):
            right_score += 1
            if self.trees[x][column] >= self.trees[x][y]:
                break

        down_score = 0
        for row in range(x + 1, self.rows_len):
            down_score += 1
            if self.trees[row][y] >= self.trees[x][y]:
                break

        left_score = 0
        for column in range(y - 1, -1, -1):
            left_score += 1
            if self.trees[x][column] >= self.trees[x][y]:
                break

        return top_score * right_score * down_score * left_score

    def max_scenic_score(self) -> int:
        max_scenic_score = 0
        for row in range(self.rows_len):
            for column in range(self.columns_len):
                if row != 0 and column != 0 and row != self.rows_len - 1 and column != self.columns_len - 1:
                    max_scenic_score = max(max_scenic_score, self.get_scenic_score_of_tree(row, column))
        return max_scenic_score
