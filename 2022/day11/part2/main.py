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


def get_all_divisible(lines: List[str]):
    divisible_list = []
    for line in lines:
        result = re.search('^Test: divisible by ([0-9]+)$', line)
        if result:
            divisible_list.append(int(result.group(1)))
    return divisible_list


def parse_monkey(lines: List[str], factor: int) -> Monkey:
    monkey_id = int(re.search('^Monkey ([0-9]):$', lines[0]).group(1))
    items = [int(i) for i in re.search('^Starting items: (.*)$', lines[1]).group(1).split(', ')]

    divisible = int(re.search('^Test: divisible by ([0-9]+)$', lines[3]).group(1))
    monkey_true = int(re.search('^If true: throw to monkey ([0-9]+)$', lines[4]).group(1))
    monkey_false = int(re.search('^If false: throw to monkey ([0-9]+)$', lines[5]).group(1))
    next_monkey_fn = lambda x: monkey_true if (x % divisible == 0) else monkey_false

    operation = re.search('^Operation: new = old (. .+)$', lines[2]).group(1)
    arithmetic = operation.split()[0]
    operand = operation.split()[1]
    if operand == 'old':
        if arithmetic == '*':
            operation_fn = lambda x: (x * x) % factor
        else:
            operation_fn = lambda x: (x + x) % factor
    else:
        if arithmetic == '*':
            operation_fn = lambda x: (x * (int(operand))) % factor
        else:
            operation_fn = lambda x: (x + int(operand)) % factor

    return Monkey(monkey_id, items, operation_fn, next_monkey_fn)


def main():
    monkeys: Dict[int, Monkey] = OrderedDict()
    lines = read_lines('input')

    factor = 1
    for d in get_all_divisible(lines):
        factor = factor * d

    # Parse monkeys
    monkey_lines: List[str] = []
    for i, line in enumerate(lines):
        if line == '' or i == len(lines) - 1:
            if i == len(lines) - 1:
                monkey_lines.append(line)
            new_monkey = parse_monkey(monkey_lines, factor)
            monkeys[new_monkey.monkey_id] = new_monkey
            monkey_lines.clear()
        else:
            monkey_lines.append(line)

    # Play 10000 rounds
    for r in range(10_000):
        for monkey in monkeys.values():
            throw_items = monkey.play()
            for next_m_id, next_items in throw_items.items():
                [monkeys[next_m_id].items.append(ni) for ni in next_items]

    inspected = sorted([m.inspected for m in monkeys.values()])
    print(inspected[-1] * inspected[-2])  # 25590400731


if __name__ == '__main__':
    main()
