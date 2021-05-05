class Road():

    mass_squar = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_road (self, height):
        result = self._length * self._width * self.mass_squar * height
        return result

mass = Road(20, 5000)
print(f'Масса всей дороги: {int(mass.mass_road(5) / 1000)} тонн')