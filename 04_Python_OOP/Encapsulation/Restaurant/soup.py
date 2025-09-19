from starter import Starter
class Soup(Starter):
    GRAMS = 22
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)