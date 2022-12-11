from typing import List


class Cpu:

    def __init__(self, instructions: List[str]):
        self.instructions = instructions
        self.clock = 1
        self.x_register = 1
        self.capture_clock = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}

    def _capture_x_if_clock(self):
        if self.clock in self.capture_clock:
            self.capture_clock[self.clock] = self.x_register

    def run(self):
        for instruction in self.instructions:
            self._capture_x_if_clock()
            if instruction == 'noop':
                self.clock += 1

            elif instruction.startswith('addx'):
                self.clock += 1
                self._capture_x_if_clock()
                self.clock += 1
                self.x_register += int(instruction.split()[1])
            else:
                raise RuntimeError(f'Unknown instruction: {instruction}')

    def get_signal_strength(self):
        s = 0
        for k, v in self.capture_clock.items():
            s += k * v
        return s