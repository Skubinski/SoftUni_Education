#Input
ammount = input()
increase = 0
total_ammount = 0
while ammount != "NoMoreMoney":
    current_ammount = float(ammount)
    increase = current_ammount
    if current_ammount < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {increase:.2f}")
    total_ammount += increase

    ammount = input()

print(f"Total: {total_ammount:.2f}")

