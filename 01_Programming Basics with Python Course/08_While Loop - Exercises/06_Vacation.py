#input
days_money_spent = 0
days = 0
needed_money = float(input())
saved_money = float(input())
total_money = saved_money

while True:
    action = input()
    current_ammount = float(input())
    days += 1



    if action == "spend":
        total_money -= current_ammount
        days_money_spent +=1
        if total_money < 0:
            total_money = 0

        if days_money_spent >= 5:
            break
    elif action == "save":
        days_money_spent = 0
        total_money += current_ammount
        if total_money >= needed_money:
            break
if total_money >= needed_money:
    print(f"You saved the money for {days} days.")
else:
    print(f"You can't save the money.")
    print(f"{days}")

