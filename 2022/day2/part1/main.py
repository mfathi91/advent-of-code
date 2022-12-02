import os
from pathlib import Path
from typing import List


def read_lines(file_name: str) -> List[str]:
    file = Path(f'{os.path.realpath(__file__)}').parent.parent.joinpath(file_name)
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


me_rpc = {
    'X': ('ROCK', 1),
    'Y': ('PAPER', 2),
    'Z': ('SCISSORS', 3)
}

opponent_rpc = {
    'A': ('ROCK', 1),
    'B': ('PAPER', 2),
    'C': ('SCISSORS', 3)
}


def get_score(opponent_raw: str, me_raw: str) -> int:
    opponent = opponent_rpc[opponent_raw][0]
    me = me_rpc[me_raw][0]
    shape_score = me_rpc[me_raw][1]
    if opponent == 'ROCK':
        round_score = 3 if me == 'ROCK' else (6 if me == 'PAPER' else 0)
    elif opponent == 'PAPER':
        round_score = 0 if me == 'ROCK' else (3 if me == 'PAPER' else 6)
    elif opponent == 'SCISSORS':
        round_score = 6 if me == 'ROCK' else (0 if me == 'PAPER' else 3)
    else:
        raise ValueError(f'Unknown move {opponent}')
    return shape_score + round_score


def main():
    score = 0
    for line in read_lines('input'):
        opponent = line[0]
        me = line[2]
        score += get_score(opponent, me)
    print(score)  # 12156


if __name__ == '__main__':
    main()
