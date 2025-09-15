from vehicle import Vehicle
from familyCar import FamilyCar

v = Vehicle(50, 150)
print(v.DEFAULT_FUEL_CONSUMPTION)
print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)
print(v.fuel)
print(v.horse_power)
print(v.fuel_consumption)
v.drive(100)
print(v.fuel)
fc = FamilyCar(150, 150)
fc.drive(50)
print(fc.fuel)
fc.drive(50)
print(fc.fuel)
print(fc.__class__.__bases__[0].__name__)