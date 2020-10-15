from myClasses.Vehicle import Vehicle


class Auto(Vehicle):
    def __init__(self, brand, weight, color, power, nb_doors=5):
        super().__init__(brand, weight, color)
        self.nb_doors = nb_doors
        self.power = power

    def __str__(self):
        return "(brand={0}, weight={1}, nb_doors={2} color={3} power={4})".format(self.brand, self.weight, self.nb_doors, self.color, self._power)

    def _get_power(self):
        return self._power

    def _set_power(self, val):
        self._power = val

    power = property(_get_power, _set_power)