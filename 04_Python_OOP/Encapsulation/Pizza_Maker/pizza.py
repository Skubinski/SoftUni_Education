from topping import Topping
from dough import Dough
class Pizza:
    def __init__(self, name, dough: Dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Cannot be empty")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("Should add dough")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("Cannot be <= 0")
        self.__toppings_capacity = value

    def add_topping(self, topping: Topping):
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
            return

        if len(self.toppings) < self.toppings_capacity:
            self.toppings[topping.topping_type] = topping.weight
            return

        raise ValueError("Not enough space for topping")

    def calculate_total_weight(self):
        total_weight = sum([value for key, value in self.toppings.items() ])
        total_weight += self.dough.weight
        return total_weight