from abc import ABC, abstractmethod

class Cloth(ABC):

    @abstractmethod
    def size(self):
        pass
    @abstractmethod
    def height(self):
        pass

class Coat(Cloth):
    def __init__(self, size):
        self.v = size
    def height(self):
        pass
    @property
    def size(self):
        return print(f'Ткани на пошив пальто потребуется: {round(self.v/6.5 + 0.5, 2)} кв.м')

class Suit(Cloth):
    def __init__(self, height):
        self.h = height
    @property
    def height(self):
        return print(f'Ткани на пошив костюма потребуется: {2 * self.h+0.3} кв.м')
    def size(self):
        pass


coat_1 = Coat(42)
coat_1.size
suit_1 = Suit(1.87)
suit_1.height
