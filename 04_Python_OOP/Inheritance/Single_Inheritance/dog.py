from animal import Animal
class Dog(Animal):
    def bark(self):
        return f"barking..."

dog = Dog()
print(dog.bark())
print(dog.eat())
