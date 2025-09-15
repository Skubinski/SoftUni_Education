#input
type_of_the_animal = input()
if type_of_the_animal == "dog":
    print("mammal")
elif type_of_the_animal == "crocodile" or type_of_the_animal == "tortoise" or type_of_the_animal == "snake":
    print("reptile")
else:
    print("unknown")