import os
from pathlib import Path
from typing import List


def read_lines(file_name: str) -> List[str]:
    file = Path(f'{os.path.realpath(__file__)}').parent.parent.joinpath(file_name)
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def to_list(packet: str):
    result = []
    packet = packet[1:-1]
    stack = []
    next_packet = ''
    i = 0
    while i < len(packet):
        c = packet[i]
        if c == '[':
            stack.append('[')
        elif c == ']':
            stack.pop()
            if len(stack) == 0:
                next_packet += c
                result.append(to_list(next_packet))
                next_packet = ''

        if len(stack) > 0:
            next_packet += c
        elif 48 <= ord(c) <= 57:
            if i + 1 < len(packet) and 48 <= ord(packet[i + 1]) <= 57:
                result.append(int(packet[i:i + 2]))
                i += 1
            else:
                result.append(int(c))
        i += 1

    return result


# Compare two lists.
# 1 means smaller, -1 means bigger and 0 means equal
def compare(p1: List, p2: List) -> int:
    i = 0
    while i < len(p1) and i < len(p2):
        e1 = p1[i]
        e2 = p2[i]
        if type(e1) == type(e2) == int:
            if e1 < e2:
                return 1
            elif e1 > e2:
                return -1
        elif type(e1) == type(e2) == list:
            c = compare(e1, e2)
            if c == 1:
                return 1
            elif c == -1:
                return -1
        else:
            if type(e1) == int and type(e2) == list:
                c = compare([e1], e2)
            elif type(e1) == list and type(e2) == int:
                c = compare(e1, [e2])
            else:
                raise RuntimeError(f'Unknown types e1, e2: {type(e1)} {type(e2)}')
            if c == 1:
                return 1
            elif c == -1:
                return -1
        i += 1
    if len(p1) == len(p2):
        return 0
    elif len(p1) < len(p2):
        return 1
    else:
        return -1


def sort(packets: List):
    for i in range(len(packets) - 1):
        for j in range(len(packets) - i - 1):
            p1 = packets[j]
            p2 = packets[j + 1]
            if compare(p1, p2) == -1:
                packets[j], packets[j + 1] = packets[j + 1], packets[j]


def main():
    lines = read_lines('input')
    packets = []
    for line in lines:
        if line:
            packets.append(to_list(line))

    dividers = [[[2]], [[6]]]
    [packets.append(d) for d in dividers]
    sort(packets)

    indexes = []
    for i, p in enumerate(packets):
        if p in dividers:
            indexes.append(i + 1)
    print(indexes[0] * indexes[1])


if __name__ == '__main__':
    main()
