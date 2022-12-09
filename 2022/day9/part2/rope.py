class Rope:

    def __init__(self):
        self.coordinate = []
        for i in range(10):
            self.coordinate.append((0, 0))
        self.seen_9 = set()
        self.seen_9.add((0, 0))

    def _adjacent(self) -> bool:
        head = self.coordinate[0]
        knot_1 = self.coordinate[1]
        diff_x = abs(head[0] - knot_1[0])
        diff_y = abs(head[1] - knot_1[1])
        return True if diff_x <= 1 and diff_y <= 1 else False

    def _move_head(self, direction):
        old_x = self.coordinate[0][0]
        old_y = self.coordinate[0][1]
        if direction == 'R':
            self.coordinate[0] = (old_x + 1, old_y)
        elif direction == 'U':
            self.coordinate[0] = (old_x, old_y + 1)
        elif direction == 'L':
            self.coordinate[0] = (old_x - 1, old_y)
        elif direction == 'D':
            self.coordinate[0] = (old_x, old_y - 1)
        else:
            raise ValueError(f'Unknown direction {direction}')

    def _move_knots(self):
        while not self._adjacent():
            for i in range(1, 10):
                ahead_knot = self.coordinate[i - 1]
                curr_knot = self.coordinate[i]
                diff_x = ahead_knot[0] - curr_knot[0]
                diff_y = ahead_knot[1] - curr_knot[1]
                if abs(diff_x) > 1:
                    x_step = 1 if diff_x > 0 else -1
                    y_step = 1 if diff_y > 0 else (-1 if diff_y < 0 else 0)
                    self.coordinate[i] = (curr_knot[0] + x_step, curr_knot[1] + y_step)
                    if i == 9:
                        self.seen_9.add(self.coordinate[i])
                elif abs(diff_y) > 1:
                    x_step = 1 if diff_x > 0 else (-1 if diff_x < 0 else 0)
                    y_step = 1 if diff_y > 0 else -1
                    self.coordinate[i] = (curr_knot[0] + x_step, curr_knot[1] + y_step)
                    if i == 9:
                        self.seen_9.add(self.coordinate[i])

    def move(self, direction: str, steps: int):
        for step in range(steps):
            self._move_head(direction)
            if not self._adjacent():
                self._move_knots()

    def get_seen_coordinates(self):
        print(self.coordinate)
        return self.seen_9
