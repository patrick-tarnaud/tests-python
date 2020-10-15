class Vehicle:

    def __init__(self, brand, weight, color):
        self.brand = brand
        self.weight = weight
        self.color = color

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, val: str):
        self._color = val



