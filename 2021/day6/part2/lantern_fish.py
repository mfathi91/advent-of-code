from collections import OrderedDict


class LanternFish:

    CREATION_TIMER = 8
    RESURRECTION_TIMER = 6

    def __init__(self, timers: list):
        self.timer_fish_number = OrderedDict([
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0),
            (5, 0),
            (6, 0),
            (7, 0),
            (8, 0)])
        for timer in timers:
            self.timer_fish_number[timer] += 1

    def next_day(self):
        timer_over_number = self.timer_fish_number[0]
        for key in self.timer_fish_number:
            if key == self.RESURRECTION_TIMER:
                self.timer_fish_number[key] = self.timer_fish_number[key + 1] + timer_over_number
            elif key == self.CREATION_TIMER:
                self.timer_fish_number[key] = timer_over_number
            else:
                self.timer_fish_number[key] = self.timer_fish_number[key + 1]

    def get_number(self):
        number = 0
        for timer in self.timer_fish_number.values():
            number += timer
        return number
