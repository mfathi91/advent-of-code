class Forest:

    def __init__(self, trees):
        self.trees = trees
        self.rows_len = len(trees)
        self.columns_len = len(trees[0])

    def is_tree_visible(self, x, y):
        # Top visible
        for row in range(x):
            if self.trees[row][y] >= self.trees[x][y]:
                break
        else:
            return True

        # Right visible
        for column in range(y+1, self.columns_len):
            if self.trees[x][column] >= self.trees[x][y]:
                break
        else:
            return True

        # Down visible
        for row in range(x + 1, self.rows_len):
            if self.trees[row][y] >= self.trees[x][y]:
                break
        else:
            return True

        # Left visible
        for column in range(y):
            if self.trees[x][column] >= self.trees[x][y]:
                break
        else:
            return True

        return False

    def count_visible_trees(self) -> int:
        visible = 0
        for row in range(self.rows_len):
            for column in range(self.columns_len):
                if row == 0 or column == 0 or row == self.rows_len - 1 or column == self.columns_len - 1:
                    visible += 1
                else:
                    if self.is_tree_visible(row, column):
                        visible += 1
        return visible
