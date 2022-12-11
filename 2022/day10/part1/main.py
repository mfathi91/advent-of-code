import os
from pathlib import Path
from typing import List
from cpu import Cpu


def read_lines(file_name: str) -> List[str]:
    file = Path(f'{os.path.realpath(__file__)}').parent.parent.joinpath(file_name)
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def main():
    instructions = read_lines('input')
    cpu = Cpu(instructions)
    cpu.run()
    print(cpu.get_signal_strength())  # 13740


if __name__ == '__main__':
    main()
