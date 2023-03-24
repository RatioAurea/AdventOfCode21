import math


class Fish:

    def __init__(self, days_to_reproduce, day_of_birth):
        self.days_to_reproduce = days_to_reproduce     # dana koliko ribi treba da se razmnozi
        self.day_of_birth = day_of_birth     # dan na cijem kraju riba postoji
        self.contributed = False

    def contribution1(self, days_to_reproduce, day_of_birth):
        contribution = 0
        if day_of_birth + days_to_reproduce <= 80:
            contribution = 1 + math.floor((80 - days_to_reproduce - day_of_birth) / 7)
        return contribution

    def contribution2(self, days_to_reproduce, day_of_birth):
        contribution = 1 + math.floor((80 - days_to_reproduce - 1) / 7)
        return contribution
