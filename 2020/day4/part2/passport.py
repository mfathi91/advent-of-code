import re

class Passport:

    BYR_REGEX = '^[0-9]{4}$'
    IYR_REGEX = '^[0-9]{4}$'
    EYR_REGEX = '^[0-9]{4}$'
    HGT_REGEX = '^([0-9]{2,3})(cm|in)$'
    HCL_REGEX = '^#[a-f0-9]{6}$'
    ECL_REGEX = '^(amb|blu|brn|gry|grn|hzl|oth)$'
    PID_REGEX = '^[0-9]{9}$'

    def __init__(self, line: str):
        self.info = {}
        for field in line.split(' '):
            key_value = field.split(':')
            self.info[key_value[0]] = key_value[1]


    def is_valid(self) -> bool:
        size = len(self.info)
        return (size == 8 or (size == 7 and 'cid' not in self.info)) and \
            self._is_byr_valid() and \
            self._is_iyr_valid() and \
            self._is_eyr_valid() and \
            self._is_hgt_valid() and \
            self._is_hcl_valid() and \
            self._is_ecl_valid() and \
            self._is_pid_valid()


    def _is_byr_valid(self):
        result = re.search(self.BYR_REGEX, self.info['byr'])
        return result and 1920 <= int(result.group(0)) <= 2002


    def _is_iyr_valid(self):
        result = re.search(self.BYR_REGEX, self.info['iyr'])
        return result and 2010 <= int(result.group(0)) <= 2020


    def _is_eyr_valid(self):
        result = re.search(self.BYR_REGEX, self.info['eyr'])
        return result and 2020 <= int(result.group(0)) <= 2030


    def _is_hgt_valid(self):
        is_cm = self.info['hgt'].endswith('cm')
        is_in = self.info['hgt'].endswith('in')
        result = re.search(self.HGT_REGEX, self.info['hgt'])
        if result:
            val = int(result.group(1))
            return result and (is_cm and 150 <= val <= 193) or (is_in and 59 <= val <= 76)
        else:
            return False


    def _is_hcl_valid(self):
        return re.search(self.HCL_REGEX, self.info['hcl'])


    def _is_ecl_valid(self):
        return re.search(self.ECL_REGEX, self.info['ecl'])


    def _is_pid_valid(self):
        return re.search(self.PID_REGEX, self.info['pid'])


    def __str__(self):
        return self.info
