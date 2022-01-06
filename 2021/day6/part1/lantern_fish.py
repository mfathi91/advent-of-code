class LanternFish:

    CREATION_TIMER = 8
    RESURRECTION_TIMER = 6

    def __init__(self, timer):
        self.timer = timer
        self.children = []

    def next_day(self):
        for child in self.children:
            child.next_day()

        if self.timer == 0:
            self.timer = self.RESURRECTION_TIMER
            self.children.append(LanternFish(self.CREATION_TIMER))
        else:
            self.timer -= 1

    def get_number(self):
        number = 1
        for child in self.children:
            number += child.get_number()
        return number
