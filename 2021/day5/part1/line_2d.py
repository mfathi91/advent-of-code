import point_2d


class Line:
    def __init__(self, start_point: point_2d.Point, end_point: point_2d.Point):
        self.start_point = start_point
        self.end_point = end_point

    def __str__(self):
        return f'{self.start_point.x},{self.start_point.y} -> {self.end_point.x},{self.end_point.y}'

    def is_vertical_horizontal(self):
        return True if self.start_point.x == self.end_point.x or \
                       self.start_point.y == self.end_point.y else False

    def get_crossing_points(self):
        crossing_points = []
        crossing_xs = []
        crossing_ys = []
        if self.end_point.x > self.start_point.x:
            crossing_xs = range(self.start_point.x, self.end_point.x + 1)
        elif self.start_point.x > self.end_point.x:
            crossing_xs = range(self.start_point.x, self.end_point.x - 1, -1)
        else:
            crossing_xs = [self.start_point.x]

        if self.end_point.y > self.start_point.y:
            crossing_ys = range(self.start_point.y, self.end_point.y + 1)
        elif self.start_point.y > self.end_point.y:
            crossing_ys = range(self.start_point.y, self.end_point.y - 1, -1)
        else:
            crossing_ys = [self.start_point.y]

        for x in crossing_xs:
            for y in crossing_ys:
                crossing_points.append(point_2d.Point(x, y))
        return crossing_points
