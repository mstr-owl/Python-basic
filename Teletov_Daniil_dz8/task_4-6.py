class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, series, make, year):
        self.name = name
        self.series = series
        self.make = make
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'Производитель устройства: {self.name}, модель устройства: {self.series}, колчиство: {self.make}, год: {self.year}.'


class Printer(Equipment):
    def __init__(self, name, series, make, year, color):
        super().__init__(name, series, make, year)
        self.color = color

    def __repr__(self):
        return f'Производитель устройства: {self.name}, модель устройства: {self.series}, колчиство: {self.make}, год: {self.year}, цвет: {self.color}.'

    def action(self):
        return 'Печатает'


class Scaner(Equipment):
    def __init__(self, name, series, make, year):
        super().__init__(name, series, make, year)
    def action(self):
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, series, make, year):
        super().__init__(name, series, make, year)
    def action(self):
        return 'Копирует'


sklad = Sklad()
printer = Printer('sony', 'e-150', 126, 2018, "black")
sklad.add_to(printer)
scaner = Scaner('hp', '321', 43, 2015)
sklad.add_to(scaner)
xerox = Xerox('hp', '257', 54, 2019)
sklad.add_to(xerox)
print(sklad._dict)
scaner = Scaner('samsung', '350', 34, 2020)
sklad.add_to(scaner)
sklad.extract('Scaner')
xerox_1 = Xerox("LG", "e-32", 23, 2017)
sklad.add_to(xerox_1)
print()
print(sklad._dict)
