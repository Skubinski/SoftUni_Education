from .animal import Mammal
class Mouse(Mammal):
    ALLOWED_FOOD = ["Vegetable", "Fruit"]
    WEIGHT_INCREMENTED = 0.10
    def __init__(self, name, weight, food_eaten, living_region):
        super().__init__(name, weight, food_eaten, living_region)

    def make_sound(self):
        return "Squeak"

class Dog(Mammal):
    ALLOWED_FOOD = ["Meat"]
    WEIGHT_INCREMENTED = 0.40
    def __init__(self, name, weight, food_eaten, living_region):
        super().__init__(name, weight, food_eaten, living_region)

    def make_sound(self):
        return "Woof!"

class Cat(Mammal):
    ALLOWED_FOOD = ["Vegetable", "Meat"]
    WEIGHT_INCREMENTED = 0.30
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight,  living_region)

    def make_sound(self):
        return "Meow"

class Tiger(Mammal):
    ALLOWED_FOOD = ["Meat"]
    WEIGHT_INCREMENTED = 1.00
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"