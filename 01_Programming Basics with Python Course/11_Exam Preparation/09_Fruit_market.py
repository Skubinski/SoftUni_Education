#input
strawbery_price = float(input())
bananas_count = float(input())
oranges_count = float(input())
raspberries_count = float(input())
strawberries_count = float(input())

raspberries_price = strawbery_price / 2
oranges_price = raspberries_price - (raspberries_price * 0.4)
bananas_price = raspberries_price - (raspberries_price * 0.8)

total = strawbery_price * strawberries_count + bananas_price * bananas_count + oranges_price * oranges_count + raspberries_count * raspberries_price
print(f"{total:.2f}")
