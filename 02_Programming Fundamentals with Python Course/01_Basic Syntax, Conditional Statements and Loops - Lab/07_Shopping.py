budget = int(input())
total_ammount = 0
while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    current_ammount = float(command)
    total_ammount += current_ammount
    if total_ammount > budget:
        print("You went in overdraft!")
        break