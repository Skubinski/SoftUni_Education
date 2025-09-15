from animal import Animal
class Dog(Animal):
    def bark(self):
        return "barking..."

dog = Dog()
print(dog.bark())
print(dog.eat())

print(Dog.mro())