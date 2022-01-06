import copy

import point_2d


class Line:
    def __init__(self, start_point: point_2d.Point, end_point: point_2d.Point):
        self.start_point = start_point
        self.end_point = end_point

    def __str__(self):
        return f'{self.start_point.x},{self.start_point.y} -> {self.end_point.x},{self.end_point.y}'

    def get_crossing_points(self):
        crossing_points = []
        moving_point = copy.deepcopy(self.start_point)
        crossing_points.append(moving_point)
        while moving_point != self.end_point:
            next_x = moving_point.x + 1 if moving_point.x < self.end_point.x else \
                moving_point.x - 1 if moving_point.x > self.end_point.x else moving_point.x
            next_y = moving_point.y + 1 if moving_point.y < self.end_point.y else \
                moving_point.y - 1 if moving_point.y > self.end_point.y else moving_point.y
            moving_point = point_2d.Point(next_x, next_y)
            crossing_points.append(moving_point)

        return crossing_points
