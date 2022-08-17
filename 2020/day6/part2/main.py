import os
from pathlib import Path

def read_lines(file_name: str):
    lines = []
    file_path = os.path.join(Path(os.path.realpath(__file__)).parent.parent, file_name)
    with open(file_path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def get_groups_answers(lines):
    groups_answers = []
    lines_size = len(lines)
    curr_group = []
    for idx, line in enumerate(lines):
        if line:
            curr_group.append(line)

        if not line or idx==lines_size-1:
            groups_answers.append(list(curr_group))
            curr_group.clear()
    return groups_answers


def main():
    lines = read_lines('input')
    lines_size = len(lines)

    count = 0
    for group_answers in get_groups_answers(lines):
        everyone_answers = set(group_answers[0])
        for answer in group_answers:
            everyone_answers = everyone_answers.intersection(set(answer))

        count += len(everyone_answers)

    print(count)  # 3476


if __name__ == '__main__':
    main()
