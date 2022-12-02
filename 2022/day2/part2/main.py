import os
from pathlib import Path
from typing import List


def read_lines(file_name: str) -> List[str]:
    file = Path(f'{os.path.realpath(__file__)}').parent.parent.joinpath(file_name)
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


me_rpc = {
    'X': 'LOSE',
    'Y': 'DRAW',
    'Z': 'WIN'
}

opponent_rpc = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS'
}

shape_score = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3
}


def get_score(opponent_raw: str, round_result_raw: str) -> int:
    opponent = opponent_rpc[opponent_raw]
    round_result = me_rpc[round_result_raw]
    if round_result == 'LOSE':
        shape_to_play = 'SCISSORS' if opponent == 'ROCK' else ('ROCK' if opponent == 'PAPER' else 'PAPER')
        return shape_score[shape_to_play]
    elif round_result == 'DRAW':
        shape_to_play = 'ROCK' if opponent == 'ROCK' else ('PAPER' if opponent == 'PAPER' else 'SCISSORS')
        return shape_score[shape_to_play] + 3
    elif round_result == 'WIN':
        shape_to_play = 'PAPER' if opponent == 'ROCK' else ('SCISSORS' if opponent == 'PAPER' else 'ROCK')
        return shape_score[shape_to_play] + 6


def main():
    score = 0
    for line in read_lines('input'):
        opponent = line[0]
        me = line[2]
        score += get_score(opponent, me)
    print(score)  # 10835


if __name__ == '__main__':
    main()
