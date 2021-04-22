class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, mass_kg, thickness):
        return (self._length * self._width * mass_kg * thickness)/1000


asphalt = Road(20, 5000)
result_mass = int(asphalt.mass(25, 5))
print(f"Масса асфальта составляет: {result_mass}")
