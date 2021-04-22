from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self):
        self.title = None
        self._cloth = None

    @abstractmethod
    def cloth(self):
        pass

    def __add__(self, other):
        example = self.__class__()
        example._cloth = self.cloth + other.cloth
        return example


class Coat(Clothes):
    def __init__(self, size=0):
        super().__init__()
        self.size = size

    @property
    def cloth(self):
        if self._cloth is None:
            self._cloth = self.size / 6.5 + 0.5
        return self._cloth


class Costume(Clothes):
    def __init__(self, height=0):
        super().__init__()
        self.height = height

    @property
    def cloth(self):
        if self._cloth is None:
            self._cloth = self.height * 2 + 0.3
        return self._cloth


coat = Coat(450)
coat.title = "Расход ткани на пальто"
costume = Costume(80)
costume.title = "Расход ткани на костюм"
clothes = coat + costume

print(f"{coat.title}: {coat.cloth:.2f}")
print(f"{costume.title}: {costume.cloth:.2f}")
print(f"Общий расход ткани равен: {clothes.cloth:.2f}")
