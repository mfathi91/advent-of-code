class Space:
    def __init__(self, lines: list):
        self.max_x = max([line.start_point.x for line in lines] + [line.end_point.x for line in lines])
        self.max_y = max([line.start_point.y for line in lines] + [line.end_point.y for line in lines])
        self.lines = list(lines)

    def get_dangerous_points(self, danger_limit: int):
        space = [[0 for column in range(self.max_x + 1)] for row in range(self.max_y + 1)]
        for line in self.lines:
            if line.is_vertical_horizontal():
                for point in line.get_crossing_points():
                    space[point.y][point.x] += 1

        num_dangerous_points = 0
        for row in range(len(space)):
            for column in range(len(space[0])):
                if space[row][column] >= danger_limit:
                    num_dangerous_points += 1

        return num_dangerous_points
