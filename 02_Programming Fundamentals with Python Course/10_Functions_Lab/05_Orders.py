def price_counter (product, quantity):
    if product == 'coffee':
        return quantity * 1.5
    elif product == 'water':
        return quantity * 1.0
    elif product == 'coke':
        return quantity * 1.4
    elif product =='snacks':
        return quantity * 2
product = input()
quantity = int(input())
result = price_counter(product, quantity)
print(f"{result:.2f}")
