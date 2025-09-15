# В зависимост от сезона:
# •	Цената за наем на кораба през пролетта е  3000 лв.;
# •	Цената за наем на кораба през лятото и есента е  4200 лв.;
# •	Цената за наем на кораба през зимата е  2600 лв.
# В зависимост от броя на групата има различна отстъпка:
# •	Ако групата е до 6 човека включително  -  отстъпка от 10%;
# •	Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
# •	Ако групата е от 12 нагоре  -  отстъпка от 25%.
# Рибарите ползват допълнително 5% отстъпка, ако са четен брой, освен ако не е есен - тогава нямат допълнителна отстъпка, която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.

#input
budget = int(input())
season = input()
fishermans = int(input())
price = 0
discount = 0
extra_discount = 0
if season == "Spring":
    price = 3000

elif season == "Summer" or season == "Autumn":
    price = 4200

elif season == "Winter":
    price = 2600


if fishermans <= 6:
    discount = 0.10
elif fishermans <= 11:
    discount = 0.15
else:
    discount = 0.25

if fishermans % 2 == 0 and season != "Autumn":
    extra_discount = 0.05


ammount = price * (1 - discount) * (1-extra_discount)
if ammount <= budget:
    print(f"Yes! You have {budget - ammount:.2f} leva left.")
else:
    print(f"Not enough money! You need {ammount - budget:.2f} leva.")