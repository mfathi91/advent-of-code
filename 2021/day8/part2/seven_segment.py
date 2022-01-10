from collections import OrderedDict


class SevenSegment:

# A method to assign name to segements of 7-segment
#         z z z z
#        y       x
#        y       x
#         w w w w
#        v       u
#        v       u
#         t t t t

    def __init__(self, seven_segment_mapping: dict):
        self.seven_segment_mapping = seven_segment_mapping

    def get_number(self, seven_segments):
        number_string = ''
        for seven_segment in seven_segments:
            number_string += self.seven_segment_mapping[str(sorted(seven_segment))]
        return int(number_string)

    @staticmethod
    def get_diff(str1: str, str2: str):
        diff = set()
        for s in str1:
            if s not in str2:
                diff.add(s)
        for s in str2:
            if s not in str1:
                diff.add(s)
        return diff

    @staticmethod
    def get_commonality(str1: str, str2: str):
        commonality = set()
        for s in str1:
            if s in str2:
                commonality.add(s)
        return commonality

    @staticmethod
    def get_digit_6(digit_1: str, digit_0_6_9: list):
        for digit in digit_0_6_9:
            if len(SevenSegment.get_commonality(digit_1, digit)) == 1:
                return digit
        raise ValueError('Invalid input')

    @staticmethod
    def get_digit_5(digit_6: str, digit_2_3_5: list):
        for digit in digit_2_3_5:
            if len(SevenSegment.get_diff(digit_6, digit)) == 1:
                return digit
        raise ValueError('Invalid input')

    @staticmethod
    def get_digit_3(zxu: str, digit_2_3: list):
        for digit in digit_2_3:
            if len(SevenSegment.get_commonality(zxu, digit)) == 3:
                return digit
        raise ValueError('Invalid input')

    @staticmethod
    def get_digit_9(digit_5: str, digit_0_9: list):
        for digit in digit_0_9:
            if len(SevenSegment.get_diff(digit_5, digit)) == 1:
                return digit
        raise ValueError('Invalid input')

    @staticmethod
    def identify_wiring(seven_segments_input: list):
        length_mapping = OrderedDict()
        # Map length of digits to their representations
        for seven_segment in seven_segments_input:
            if len(seven_segment) in length_mapping:
                existing_values = length_mapping[len(seven_segment)]
                new_values = [seven_segment, existing_values] if type(existing_values) == str \
                    else [seven_segment] + existing_values
                length_mapping[len(seven_segment)] = new_values
            else:
                length_mapping[len(seven_segment)] = seven_segment

        # Find digits that have unique length
        digit_1 = length_mapping[2]
        digit_4 = length_mapping[4]
        digit_7 = length_mapping[3]
        digit_8 = length_mapping[7]

        # Find z by comparing digit 1 and 7
        z = next(iter(SevenSegment.get_diff(digit_1, digit_7)))

        # Find digit 6 by comparing digit 1 and (0, 6, 9)
        digit_6 = SevenSegment.get_digit_6(digit_1, length_mapping[6])
        length_mapping[6].remove(digit_6)
        # Find x and u by comparing digit 1 and 6
        u = next(iter(SevenSegment.get_commonality(digit_1, digit_6)))
        x = next(iter(SevenSegment.get_diff(digit_1, u)))

        # Find digit 5 by comparing digit 6 and (2, 3, 5)
        digit_5 = SevenSegment.get_digit_5(digit_6, length_mapping[5])
        length_mapping[5].remove(digit_5)

        # Find digit 3 by comparing zxu and (2, 3)
        digit_3 = SevenSegment.get_digit_3(z+u+x, length_mapping[5])
        length_mapping[5].remove(digit_3)

        # Find digit 2 as the remaining digit in the corresponding length
        digit_2 = length_mapping[5][0]

        # Find digit 9 by comparing digit 5 and (0, 9)
        digit_9 = SevenSegment.get_digit_9(digit_5, length_mapping[6])
        length_mapping[6].remove(digit_9)

        # Find digit 0 as the remaining digit in the corresponding length
        digit_0 = length_mapping[6][0]

        return SevenSegment({
            str(sorted(digit_0)): '0',
            str(sorted(digit_1)): '1',
            str(sorted(digit_2)): '2',
            str(sorted(digit_3)): '3',
            str(sorted(digit_4)): '4',
            str(sorted(digit_5)): '5',
            str(sorted(digit_6)): '6',
            str(sorted(digit_7)): '7',
            str(sorted(digit_8)): '8',
            str(sorted(digit_9)): '9'
        })
