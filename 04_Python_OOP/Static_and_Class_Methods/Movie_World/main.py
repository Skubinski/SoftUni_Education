from customer import Customer
from dvd import DVD
from movie_world import MovieWorld

c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

m = MovieWorld("The Best Movie Shop")

m.add_customer(c1)
m.add_customer(c2)

m.add_dvd(d1)
m.add_dvd(d2)

print(m.rent_dvd(1, 1))
print(m.rent_dvd(2, 1))
print(m.rent_dvd(1, 2))

print(m)

print(m.return_dvd(1, 2))
print(m)