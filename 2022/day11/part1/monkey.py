from typing import List, Dict


class Monkey:

    def __init__(self, monkey_id: int, starting_items: List[int], operation_fn, next_monkey_fn):
        self.monkey_id = monkey_id
        self.items = starting_items
        self.operation_fn = operation_fn
        self.next_monkey_fn = next_monkey_fn
        self.inspected = 0

    def play(self) -> Dict[int, List[int]]:
        throw_items = {}
        while len(self.items) > 0:
            item = self.items.pop(0)
            new_worry_level = self.operation_fn(item)
            next_monkey = self.next_monkey_fn(new_worry_level)
            if next_monkey not in throw_items:
                throw_items[next_monkey] = []
            throw_items[next_monkey].append(new_worry_level)
            self.inspected += 1
        return throw_items
