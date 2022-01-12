import os

OPEN_SH = {'(': ')',
           '[': ']',
           '{': '}',
           '<': '>'}

CLOSE_CH = {')': ('(', 1),
            ']': ('[', 2),
            '}': ('{', 3),
            '>': ('<', 4)}


def is_corrupted(line: str):
    corrupted = False
    stack = []
    for ch in line:
        if ch in OPEN_SH:
            stack.append(ch)
        else:
            if CLOSE_CH[ch][0] != stack[-1]:
                corrupted = True
                break
            else:
                stack.pop()
    return corrupted


def remove_corrupted_lines(lines: list):
    for line in list(lines):
        if is_corrupted(line):
            lines.remove(line)


def get_completion_string(line: str):
    stack = []
    for ch in line:
        if ch in OPEN_SH:
            stack.append(ch)
        else:
            stack.pop()

    completion_string = ''
    for ch in reversed(stack):
        completion_string += OPEN_SH[ch]
    return completion_string


def get_total_point(completion_string: str):
    total_points = 0
    for cs in completion_string:
        total_points = (total_points * 5) + CLOSE_CH[cs][1]
    return total_points


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        lines = [line.rstrip() for line in f]
        remove_corrupted_lines(lines)
        total_points = []
        for line in lines:
            completion_strings = get_completion_string(line)
            total_points.append(get_total_point(completion_strings))

        middle_index = len(total_points) // 2
        print(sorted(total_points)[middle_index])    # 3249889609


if __name__ == '__main__':
    main()
