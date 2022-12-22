from queue import PriorityQueue
from string import ascii_lowercase
from typing import List, Tuple


class Hill:

    def __init__(self, lines: List[str]):
        self.rows_len = len(lines)
        self.columns_len = len(lines[0])
        self.grid = [[-1 for _ in range(self.columns_len)] for _ in range(self.rows_len)]
        self.start_coordinate = None
        self.end_coordinate = None
        for i, line in enumerate(lines):
            for j, ch in enumerate(line):
                if ch in ascii_lowercase:
                    self.grid[i][j] = ascii_lowercase.index(ch)
                if ch == 'S':
                    self.grid[i][j] = 0
                    self.start_coordinate = i, j
                if ch == 'E':
                    self.grid[i][j] = 25
                    self.end_coordinate = i, j

    def _neighbors(self, x, y) -> List[Tuple[int, int]]:
        curr_height = self.grid[x][y]
        for neighbor in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
            if 0 <= neighbor[0] < self.rows_len and 0 <= neighbor[1] < self.columns_len:
                if curr_height - self.grid[neighbor[0]][neighbor[1]] <= 1:
                    yield neighbor

    def climb(self):
        visited = [[False for _ in range(self.columns_len)] for _ in range(self.rows_len)]
        q = PriorityQueue()
        q.put((0, self.end_coordinate[0], self.end_coordinate[1]))
        while True:
            steps, x, y = q.get()
            if visited[x][y]:
                continue

            visited[x][y] = True
            if self.grid[x][y] == 0:
                return steps

            for neighbor in self._neighbors(x, y):
                q.put((steps + 1, neighbor[0], neighbor[1]))
