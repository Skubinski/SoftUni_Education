#input
budget = float(input())
number_of_videocards = int(input())
number_of_processors = int(input())
number_of_ram = int(input())

#prices

VIDEOCARDS = 250
processors = (number_of_videocards * VIDEOCARDS) * 0.35
ram = (number_of_videocards * VIDEOCARDS) * 0.10
#calculations

needed_money = number_of_videocards * VIDEOCARDS + number_of_processors * processors + number_of_ram * ram

#conditions
discount = 0

if number_of_processors < number_of_videocards:
    discount = 0.15
    needed_money_with_discount = needed_money * (1 - discount)


if needed_money_with_discount <= budget:
    print(f"You have {budget - needed_money_with_discount:.2f} leva left!")
else:
    print(f"Not enough money! You need {needed_money_with_discount - budget:.2f} leva more!")