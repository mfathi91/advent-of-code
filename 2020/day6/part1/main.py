import os
from pathlib import Path

def read_lines(file_name: str):
    lines = []
    file_path = os.path.join(Path(os.path.realpath(__file__)).parent.parent, file_name)
    with open(file_path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def main():
    lines = read_lines('input')
    lines_size = len(lines)

    count = 0
    group_answers = set()
    for idx, line in enumerate(lines):
        if line:
            for ch in line:
                group_answers.add(ch)

        if not line or idx==lines_size-1:
            count += len(group_answers)
            group_answers.clear()

    print(count)  # 6686


if __name__ == '__main__':
    main()
