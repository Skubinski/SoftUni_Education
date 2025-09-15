baggage_capacity = float(input())
command = input()
baggage_number = 0
total_baggage = 0
while command != "End":
    current_baggage = float(command)
    # baggage_number += 1
    # if baggage_number % 3 == 2:
    #     current_baggage = current_baggage + (current_baggage * 0.10)
    # total_baggage += current_baggage

    total_baggage += current_baggage
    if total_baggage >= baggage_capacity:
        break
    baggage_number += 1
    if baggage_number % 3 == 2:
        current_baggage = current_baggage + (current_baggage * 0.10)
    # total_baggage += current_baggage


    command = input()
if total_baggage >= baggage_capacity:
    print("No more space!")
    print(f"Statistic: {baggage_number} suitcases loaded.")
else:
    print("Congratulations! All suitcases are loaded!")
    print(f"Statistic: {baggage_number} suitcases loaded.")