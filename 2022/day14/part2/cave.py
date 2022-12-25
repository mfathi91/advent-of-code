class Cave:

    def __init__(self, rocks):
        rocks_x = [r[0] for r in rocks]
        rocks_y = [r[1] for r in rocks]
        self.min_x, self.max_x = 0, max(rocks_x) + 2
        self.min_y, self.max_y = 0, max(rocks_y) + 500
        self.grid = {}
        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                c = (x, y)
                self.grid[c] = '#' if (c in rocks or x == self.max_x) else '.'

    def in_grid(self, x, y) -> bool:
        return self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y

    def is_air(self, x, y):
        if x >= self.max_x:
            return False
        return self.grid.get((x, y), '.') == '.'

    def sand(self):
        x, y = 0, 500
        count = 0
        while True:
            if self.is_air(x + 1, y):
                x, y = x + 1, y
                continue
            if self.is_air(x + 1, y - 1):
                x, y = x + 1, y - 1
                continue
            if self.is_air(x + 1, y + 1):
                x, y = x + 1, y + 1
                continue

            if (x, y) == (0, 500):
                return count + 1
            self.grid[(x, y)] = 'o'
            x, y = 0, 500
            count += 1

    def draw(self):
        for x in range(self.min_x, self.max_x + 1):
            line = ''
            for y in range(self.min_y, self.max_y + 1):
                line += self.grid[(x, y)]
            print(line)
