import os
from pathlib import Path

def read_lines(file_name: str):
    lines = []
    file_path = os.path.join(Path(os.path.realpath(__file__)).parent.parent, file_name)
    with open(file_path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def decimal(binary_str: str) -> int:
    val = 0
    for idx, ch in enumerate(binary_str[::-1]):
        val += (2**idx)*int(ch)
    return val

def main():
    lines = read_lines('input')
    seat_ids = []
    for line in lines:
        row = line[0:7].replace('F', '0').replace('B', '1')
        column = line[7:10].replace('L', '0').replace('R', '1')
        seat_ids.append((decimal(row) * 8) + decimal(column))

    for i in range((1*8), (126*8)+1):
        if i not in seat_ids and i-1 in seat_ids and i+1 in seat_ids:
            print(i)  # 554
            break


if __name__ == '__main__':
    main()
