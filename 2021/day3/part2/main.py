import os


def get_most_common_bit(diagnostic_power_list, bit_idx):
    common_bit_indicator = 0
    for diagnostic_power in diagnostic_power_list:
        value_to_add = 1 if diagnostic_power[bit_idx] == '1' else -1
        common_bit_indicator += value_to_add

    return '1' if common_bit_indicator >= 0 else '0'


def negate_bit(bit):
    return '0' if bit == '1' else '1'


def remove_power_if_incompatible(diagnostic_power_list, bit_idx, compatible_bit_value):
    for diagnostic_power in list(diagnostic_power_list):
        if diagnostic_power[bit_idx] != compatible_bit_value:
            diagnostic_power_list.remove(diagnostic_power)


def get_rating(diagnostic_report, bit_criteria):
    rating = ''
    for idx in range(len(diagnostic_report[0])):
        if len(diagnostic_report) == 1:
            rating = diagnostic_report[0]
        else:
            if bit_criteria == 'OXYGEN_GENERATOR_RATING':
                rating_bit_at_idx = get_most_common_bit(diagnostic_report, idx)
            elif bit_criteria == 'CO2_SCRUBBER_RATING':
                rating_bit_at_idx = negate_bit(get_most_common_bit(diagnostic_report, idx))
            else:
                raise ValueError(f'Unknown value for bit_criteria: {bit_criteria}')

            rating += rating_bit_at_idx
            remove_power_if_incompatible(diagnostic_report, idx, rating_bit_at_idx)

    return rating


input_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'input')
with open(input_file) as f:
    lines = f.read().splitlines()
    oxygen_generator_rating = int(get_rating(list(lines), 'OXYGEN_GENERATOR_RATING'), 2)
    co2_scrubber_rating = int(get_rating(list(lines), 'CO2_SCRUBBER_RATING'), 2)
    print(oxygen_generator_rating * co2_scrubber_rating)    # 4996233
