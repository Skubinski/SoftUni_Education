# #input

contract_time = input()
contract_type = input()
mobile_network = input()
months = int(input())
price = 0


#calculations

if contract_time == "one":
    if contract_type == "Small":
        price = 9.98
    elif contract_type == "Middle":
        price = 18.99
    elif contract_type == "Large":
        price = 25.98
    elif contract_type == "ExtraLarge":
        price = 35.99

elif contract_time == "two":
    if contract_type == "Small":
        price = 8.58
    elif contract_type == "Middle":
        price = 17.09
    elif contract_type == "Large":
        price = 23.59
    elif contract_type == "ExtraLarge":
        price = 31.79

if mobile_network == "yes":
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85

if contract_time == "two":
    price = price - (price * 3.75 / 100)

print(f"{price * months:.2f} lv.")



