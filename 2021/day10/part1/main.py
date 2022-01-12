import os

OPEN_SH = {'(': ')',
           '[': ']',
           '{': '}',
           '<': '>'}

CLOSE_CH = {')': ('(', 3),
            ']': ('[', 57),
            '}': ('{', 1197),
            '>': ('<', 25137)}


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        syntax_error_score = 0
        for line in [line.rstrip() for line in f]:
            stack = []
            for ch in line:
                if ch in OPEN_SH:
                    stack.append(ch)
                else:
                    if CLOSE_CH[ch][0] != stack[-1]:
                        syntax_error_score += CLOSE_CH[ch][1]
                        break
                    else:
                        stack.pop()
        print(syntax_error_score)    # 370407


if __name__ == '__main__':
    main()
