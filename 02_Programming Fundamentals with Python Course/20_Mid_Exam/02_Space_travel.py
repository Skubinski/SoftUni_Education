def travel (travel_route, fuel, ammunition):
    splitted_route = travel_route.split("||")
    for command in splitted_route:
        command = command.split()
        if command[0] == "Travel":
            fuel -= int(command[1])
            if int(fuel) >= 0:
                print(f"The spaceship travelled {command[1]} light-years.")
            else:
                print("Mission failed.")
                break
        elif command[0] == "Enemy":
            if int(ammunition) >= int(command[1]):
                ammunition -= int(command[1])
                print(f"An enemy with {command[1]} armour is defeated.")
            elif int(fuel) >= int(command[1]) * 2:
                fuel -= int(command[1]) * 2
                print(f"An enemy with {command[1]} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
        elif command[0] == "Repair":
            fuel += int(command[1])
            ammunition += int(command[1]) * 2
            print(f"Ammunitions added: {int(command[1]) * 2}.")
            print(f"Fuel added: {command[1]}.")
        elif command[0] == "Titan":
            print("You have reached Titan, all passengers are safe.")
            break







route = input()
starting_amount_of_fuel = int(input())
starting_amount_of_ammunition = int(input())
travel(route, starting_amount_of_fuel, starting_amount_of_ammunition)
