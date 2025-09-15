number_of_cities = int(input())
total_profit = 0
for city in range(1, number_of_cities + 1):
    name = input()
    earned_money = float(input())
    expenses = float(input())
    if city % 5 ==0:
        earned_money -= earned_money * 0.1
    elif city % 3 == 0:
        expenses += expenses * 0.5
    profit = earned_money - expenses
    total_profit += profit
    print(f"In {name} Burger Bus earned {profit:.2f} leva.")
print(f"Burger Bus total profit: {total_profit:.2f} leva.")
