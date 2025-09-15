#input
destination = input()


while destination != "End":
    min_budget = float(input())
    current_ammount = 0

    while current_ammount < min_budget:
        saved_money = float(input())
        current_ammount += saved_money
        if current_ammount >= min_budget:
            print(f"Going to {destination}!")
            break
    destination = input()
