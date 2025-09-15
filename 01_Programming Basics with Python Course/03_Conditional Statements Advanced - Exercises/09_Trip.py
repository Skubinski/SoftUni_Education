# •	При 100 лв. или по-малко - някъде в България:
# o	Лято - 30% от бюджета;
# o	Зима - 70% от бюджета.
# •	При 1000 лв. или по малко - някъде на Балканите:
# o	Лято - 40% от бюджета;
# o	Зима - 80% от бюджета.
# •	При повече от 1000 лв. - някъде из Европа:
# o	При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.
budget = float(input())
season = input()

where = ""
hotel_or_camp = ""
if budget <= 100:
    where = "Bulgaria"
    if season == "summer":
        budget *= 0.30
        hotel_or_camp = "Camp"
    elif season == "winter":
        budget *= 0.70
        hotel_or_camp = "Hotel"
elif 100 < budget <= 1000:
    where = "Balkans"
    if season == "summer":
        budget *= 0.40
        hotel_or_camp = "Camp"
    elif season == "winter":
        budget *= 0.80
        hotel_or_camp = "Hotel"
elif budget > 1000:
    where = "Europe"
    if season == "summer":
        budget *= 0.90
        hotel_or_camp = "Hotel"
    elif season == "winter":
        budget *= 0.90
        hotel_or_camp = "Hotel"



print(f"Somewhere in {where}")
print(f"{hotel_or_camp} - {budget:.2f}")

