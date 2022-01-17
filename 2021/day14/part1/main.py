import os
import re
from typing import Dict
from collections import Counter


def apply_rules(template: str, rules: Dict[str, str]) -> str:
    new_template = ''
    for i in range(len(template)):
        if len(template) > i + 1:
            pair = template[i:i+2]
            char_to_insert = rules[pair]
            new_template = new_template + pair[0] + char_to_insert
        else:
            new_template += template[i]
    return new_template


def main():
    input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
    with open(input_file) as f:
        lines = [line.rstrip() for line in f]
        template = lines[0]
        rules = {}
        for line in lines[2:]:
            rule_elements = re.findall('[A-Z]+', line)
            rules[rule_elements[0]] = rule_elements[1]

        for i in range(10):
            template = apply_rules(template, rules)

        template_stat = Counter(template).most_common()
        print(template_stat[0][1] - template_stat[-1][1])


if __name__ == '__main__':
    main()
