IVANCHO_AGE = 18
money = float(input())
year = int(input())
money_spent = 0
for years in range(1800, year+1):

    if years % 2 == 0:
        money_spent += 12000
    else:
        money_spent += 12000 + 50 * (years - 1800 + 18)
if money_spent <= money:
    print(f"Yes! He will live a carefree life and will have {money - money_spent :.2f} dollars left.")
else:
    print(f"He will need {money_spent - money :.2f} dollars to survive.")