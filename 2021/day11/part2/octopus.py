class Octopus:

    def __init__(self, energy: int):
        self.energy = energy
        #self.inform_adjacent_octopuses = False
        self.total_flashed = 0

    def next_step(self):
        if self.energy == 9:
            self.energy = 0
            #self.inform_adjacent_octopuses = True
            self.total_flashed += 1
        else:
            self.energy += 1

    def is_flashing(self):
        return self.energy == 0

    def adjacent_octopus_flashed(self):
        if not self.is_flashing():
            if self.energy == 9:
                self.energy = 0
                self.total_flashed += 1
            else:
                self.energy += 1

    def __str__(self):
        return f'{self.energy}'
