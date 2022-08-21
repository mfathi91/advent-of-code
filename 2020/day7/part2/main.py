import os
import re
from pathlib import Path
from bag import Bag


def read_lines(file_name: str):
    lines = []
    file_path = os.path.join(Path(os.path.realpath(__file__)).parent.parent, file_name)
    with open(file_path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


REGEX1 = '^([a-z ]*) bags contain no other bags.$'

FIELD_0_REGEX = '^.* bags contain ([0-9]+) ([a-z ]+) bags?'
FIELD_N_REGEX = '^([0-9]+) ([a-z ]+) bags?'

def get_bag_by_name(bags, name):
    for bag in bags:
        if bag.name==name:
            return bag
    raise AssertionError(f'No bag with name "{name}" found')


def get_bags(lines):

    bags = []
    for line in lines:
        bags.append(Bag(line[:line.find(' bags contain')]))

    for idx, bag in enumerate(bags):
        line = lines[idx]
        if not line.endswith('contain no other bags.'):
            fields = lines[idx].split(', ')
            field_0_result = re.search(FIELD_0_REGEX, fields[0])
            assert field_0_result
            field_0_bag_count = int(field_0_result.group(1))
            field_0_bag_name = field_0_result.group(2)
            assert field_0_bag_count > 0
            assert field_0_bag_name
            bag.add_child(get_bag_by_name(bags, field_0_bag_name), field_0_bag_count)
            for field in fields[1:]:
                field_n_result = re.search(FIELD_N_REGEX, field)
                assert field_n_result
                field_n_bag_count = int(field_n_result.group(1))
                field_n_bag_name = field_n_result.group(2)
                assert field_n_bag_count > 0
                assert field_n_bag_name
                bag.add_child(get_bag_by_name(bags, field_n_bag_name), field_n_bag_count)

    return bags


def main():
    lines = read_lines('input')
    bags = get_bags(lines)
    shiny_gold_bag = get_bag_by_name(bags, 'shiny gold')
    print (shiny_gold_bag.children_count())  # 20189


if __name__ == '__main__':
    main()
