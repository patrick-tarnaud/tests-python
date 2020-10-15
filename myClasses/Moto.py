from myClasses.Vehicle import Vehicle

class Moto(Vehicle):
    def __init__(self, brand, weight, speed, color):
        super().__init__(brand, weight, color)
        self.speed = speed

    def __str__(self):
        return "(brand={0}, weight={1}, speed={2} color={3})".format(self.brand, self.weight, self.speed, self.color)
