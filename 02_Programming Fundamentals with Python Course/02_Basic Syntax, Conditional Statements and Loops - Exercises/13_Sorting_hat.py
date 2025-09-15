command = input()
while command != "Welcome!":
    counter = 0
    name = command
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    for char in range(len(name)):
        counter += 1
    if counter < 5:
        print(f"{name} goes to Gryffindor.")
    elif counter == 5:
        print(f"{name} goes to Slytherin.")
    elif counter == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")



    command = input()
if command == "Welcome!":
    print("Welcome to Hogwarts.")