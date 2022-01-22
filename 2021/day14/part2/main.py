import os
import re
import copy
from typing import Dict
from collections import OrderedDict


def apply_rules(rules_count: Dict[str, int], rules: Dict[str, str]):
    for rule, count in copy.deepcopy(rules_count).items():
        if rules_count[rule] > 0:
            new_char = rules[rule]
            new_rule1 = rule[0] + new_char
            new_rule2 = new_char + rule[1]
            rules_count[new_rule1] = rules_count.get(new_rule1, 0) + count
            rules_count[new_rule2] = rules_count.get(new_rule2, 0) + count
            rules_count[rule] = rules_count[rule] - count if rules_count[rule] > 0 else 0


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        lines = [line.rstrip() for line in f]
        template = lines[0]
        rules = OrderedDict()
        for line in lines[2:]:
            rule_elements = re.findall('[A-Z]+', line)
            rules[rule_elements[0]] = rule_elements[1]

        rules_count = {}
        for i in range(len(template)):
            if i + 1 < len(template):
                pair = template[i:i+2]
                rules_count[pair] = rules_count.get(pair, 0) + 1

        for i in range(40):
            apply_rules(rules_count, rules)

        letter_freq = {}
        for rule, count in rules_count.items():
            letter_freq[rule[1]] = letter_freq.get(rule[1], 0) + count

        letter_freq[template[0]] += 1

        sorted_letter_freq = sorted(letter_freq.values())
        print(sorted_letter_freq[-1] - sorted_letter_freq[0])


if __name__ == '__main__':
    main()
