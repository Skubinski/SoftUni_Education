numbers = input().split(", ")

number_of_beggars = int(input())
beggers_collections = [0] * number_of_beggars
counter = 0
while counter < number_of_beggars:
    for k in range(counter, len(numbers), number_of_beggars):
        beggers_collections[counter] += int(numbers[k])
    counter += 1
print(beggers_collections)