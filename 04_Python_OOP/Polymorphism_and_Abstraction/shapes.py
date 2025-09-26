import math
from abc import ABC, abstractmethod
from math import pi
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        return ""

    @abstractmethod
    def calculate_perimeter(self):
        return ""

class Circle(Shape):
    def __init__(self, r):
        self.__radius = r

    def calculate_area(self):
        return math.pi * self.__radius * self.__radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius

class Rectangle(Shape):
    def __init__(self, h, w):
        self.height = h
        self.width = w

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * self.height + 2 * self.width

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

r = Rectangle(10, 20)
print(r.calculate_area())
print(r.calculate_perimeter())


