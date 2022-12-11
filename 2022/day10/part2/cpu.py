from typing import List


class Cpu:

    def __init__(self, instructions: List[str]):
        self.instructions = instructions
        self.clock = 0
        self.x_register = 1
        self.pixels = {}

    def _add_pixel(self):
        pixel_row = self.clock // 40
        lit = (self.clock % 40) in [self.x_register - 1, self.x_register, self.x_register + 1]
        line = self.pixels.get(pixel_row, '')
        line = f'{line}{"#" if lit else "."}'
        self.pixels[pixel_row] = line

    def run(self):
        for instruction in self.instructions:
            self._add_pixel()
            if instruction == 'noop':
                self.clock += 1

            elif instruction.startswith('addx'):
                self.clock += 1
                self._add_pixel()
                self.clock += 1
                self.x_register += int(instruction.split()[1])
            else:
                raise RuntimeError(f'Unknown instruction: {instruction}')

    def get_pixels(self):
        lines = ''
        for line_number in range(6):
            lines += f'{self.pixels[line_number]}\n'
        return lines
