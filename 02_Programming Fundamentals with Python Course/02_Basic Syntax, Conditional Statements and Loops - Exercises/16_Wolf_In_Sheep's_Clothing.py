animals = input()
animal_list = animals.split(", ")
sheep_counter = 0
first_animal = len(animal_list)-1
for i in range(len(animal_list)-1,-1,-1):

    current_animal = animal_list[i]
    if animal_list[first_animal] == "wolf":
        print("Please go away and stop eating my sheep")
        break


    if current_animal == "wolf":
        print(f"Oi! Sheep number {sheep_counter}! You are about to be eaten by a wolf!")
        break
    sheep_counter += 1