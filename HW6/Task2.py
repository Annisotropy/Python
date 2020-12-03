class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.mass1sm = 10
        self.height = 5

    def mass(self):
        bitumen_mass = self._length * self._width * self.mass1sm * self.height
        return bitumen_mass


road = Road(1, 2)
print(road.mass())

