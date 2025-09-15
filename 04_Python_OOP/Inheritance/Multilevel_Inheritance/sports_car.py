from car import Car
class SportsCar(Car):
    def race(self):
        return "racing..."


sp_car = SportsCar()
print(sp_car.race())
print(sp_car.drive())
print(sp_car.move())