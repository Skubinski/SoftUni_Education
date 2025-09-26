from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def __repr__(self):
        return f"{self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def __repr__(self):
        return f"{self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

    def make_sound(self):
        return "Meow Meow!"


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, "Female")
    
    def make_sound(self):
        return "Meow!"

class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, "Male")

    def make_sound(self):
        return "Hiss!"

dog = Dog("Rocky", 3, "Male")
print(dog.make_sound())
print(dog)
tomcat = Tomcat("Tom", 6)
print(tomcat.make_sound())
print(tomcat)