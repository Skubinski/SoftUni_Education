from abc import ABC, abstractmethod
class Animal(ABC):
    ALLOWED_FOOD = []
    WEIGHT_INCREMENTED = 0.00
    def __init__(self, name, weight, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type not in self.ALLOWED_FOOD:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}"
        food_pieces = food.quantity * self.WEIGHT_INCREMENTED
        self.food_eaten += food.quantity
        self.weight += food_pieces

class Bird(Animal,ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.living_region}, {self.weight}, {self.food_eaten}]"