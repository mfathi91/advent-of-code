import os
import re
from collections import OrderedDict
from pathlib import Path
from typing import List, Dict
from monkey import Monkey


def read_lines(file_name: str) -> List[str]:
    file = Path(f'{os.path.realpath(__file__)}').parent.parent.joinpath(file_name)
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def parse_monkey(lines: List[str]) -> Monkey:
    monkey_id = int(re.search('^Monkey ([0-9]):$', lines[0]).group(1))
    items = [int(i) for i in re.search('^Starting items: (.*)$', lines[1]).group(1).split(', ')]

    operation = re.search('^Operation: new = old (. .+)$', lines[2]).group(1)
    arithmetic = operation.split()[0]
    operand = operation.split()[1]
    if operand == 'old':
        operation_fn = (lambda x: (x * x)//3) if arithmetic == '*' else (lambda y: (y + y)//3)
    else:
        operation_fn = (lambda x: (x * int(operand))//3) if arithmetic == '*' else (lambda y: (y + int(operand))//3)

    divisible = int(re.search('^Test: divisible by ([0-9]+)$', lines[3]).group(1))
    monkey_true = int(re.search('^If true: throw to monkey ([0-9]+)$', lines[4]).group(1))
    monkey_false = int(re.search('^If false: throw to monkey ([0-9]+)$', lines[5]).group(1))
    next_monkey_fn = lambda x: monkey_true if (x % divisible == 0) else monkey_false
    return Monkey(monkey_id, items, operation_fn, next_monkey_fn)


def main():
    monkeys: Dict[int, Monkey] = OrderedDict()

    # Parse monkeys
    monkey_lines: List[str] = []
    lines = read_lines('input')
    for i, line in enumerate(lines):
        if line == '' or i == len(lines) - 1:
            if i == len(lines) - 1:
                monkey_lines.append(line)
            new_monkey = parse_monkey(monkey_lines)
            monkeys[new_monkey.monkey_id] = new_monkey
            monkey_lines.clear()
        else:
            monkey_lines.append(line)

    # Play 20 rounds
    for r in range(20):
        for monkey in monkeys.values():
            throw_items = monkey.play()
            for next_m_id, next_items in throw_items.items():
                [monkeys[next_m_id].items.append(ni) for ni in next_items]

    inspected = sorted([m.inspected for m in monkeys.values()])
    print(inspected[-1] * inspected[-2])  # 110888


if __name__ == '__main__':
    main()
