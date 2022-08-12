class Passport:

    def __init__(self, line: str):
        self.info = {}
        for field in line.split(' '):
            key_value = field.split(':')
            self.info[key_value[0]] = key_value[1]

    def is_valid(self) -> bool:
        size = len(self.info)
        optional_cid = self.info.get('cid')
        return True if (size == 8 or (size==7 and not optional_cid)) else False

    def __str__(self):
        return self.info
