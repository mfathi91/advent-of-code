class HeadTail:

    def __init__(self):
        self.head_coordinate = (0, 0)
        self.tail_coordinate = (0, 0)
        self.seen = set()
        self.seen.add((0, 0))

    def _adjacent(self) -> bool:
        diff_x = abs(self.head_coordinate[0] - self.tail_coordinate[0])
        diff_y = abs(self.head_coordinate[1] - self.tail_coordinate[1])
        return True if diff_x <= 1 and diff_y <= 1 else False

    def _move_head(self, direction):
        if direction == 'R':
            self.head_coordinate = (self.head_coordinate[0] + 1, self.head_coordinate[1])
        elif direction == 'U':
            self.head_coordinate = (self.head_coordinate[0], self.head_coordinate[1] + 1)
        elif direction == 'L':
            self.head_coordinate = (self.head_coordinate[0] - 1, self.head_coordinate[1])
        elif direction == 'D':
            self.head_coordinate = (self.head_coordinate[0], self.head_coordinate[1] - 1)
        else:
            raise ValueError(f'Unknown direction {direction}')

    def _move_tail(self):
        while not self._adjacent():
            diff_x = self.head_coordinate[0] - self.tail_coordinate[0]
            diff_y = self.head_coordinate[1] - self.tail_coordinate[1]
            if abs(diff_x) > 1:
                x_step = 1 if diff_x > 0 else -1
                self.tail_coordinate = (self.tail_coordinate[0] + x_step, self.tail_coordinate[1] + diff_y)
                self.seen.add(self.tail_coordinate)
            elif abs(diff_y) > 1:
                y_step = 1 if diff_y > 0 else -1
                self.tail_coordinate = (self.tail_coordinate[0] + diff_x, self.tail_coordinate[1] + y_step)
                self.seen.add(self.tail_coordinate)
            else:
                raise RuntimeError('Invalid state')

    def move(self, direction: str, steps: int):
        for step in range(steps):
            self._move_head(direction)
            if not self._adjacent():
                self._move_tail()

    def get_seen_coordinates(self):
        return self.seen

