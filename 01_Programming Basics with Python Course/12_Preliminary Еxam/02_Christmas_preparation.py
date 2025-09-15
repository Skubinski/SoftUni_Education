#input
PACKAGING_PAPER_PRICE = 5.80
CLOTH_PRICE = 7.20
GLUE_PRICE = 1.20

packaging_paper_count = int(input())
cloth_count = int(input())
glue_l = float(input())
discount = int(input())

needed_money = (packaging_paper_count * PACKAGING_PAPER_PRICE) + (cloth_count * CLOTH_PRICE) + (glue_l * GLUE_PRICE)
total_money_needed_with_discount = needed_money - (needed_money * discount / 100)
print(f"{total_money_needed_with_discount:.3f}")
