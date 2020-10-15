class Duree:
    def __init__(self, minutes: int, secondes: int):
        self.minutes = minutes
        self.secondes = secondes

    def __str__(self):
        return '{:02}:{:02}'.format(self.minutes, self.secondes)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, Duree):
            secondes = Duree.secondes(self.minutes) + self.secondes + Duree.secondes(other.minutes) + other.secondes
        elif isinstance(other, int):
            secondes = Duree.secondes(self.minutes) + self.secondes + other

        minutes = secondes // 60
        secondes = secondes % 60

        return Duree(minutes, secondes)

    def __radd__(self, other):
        return self + other

    @staticmethod
    def secondes(minutes) -> int:
        return minutes * 60
