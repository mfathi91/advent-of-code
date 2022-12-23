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
# 1 means valid, -1 means invalid and 0 means equal
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


def main():
    lines = read_lines('input')
    s = 0
    i = 0
    while i < len(lines):
        if lines[i]:
            if compare(to_list(lines[i]), to_list(lines[i + 1])) == 1:
                s += (i // 3) + 1
            i += 2
        else:
            i += 1
    print(s)


if __name__ == '__main__':
    main()
