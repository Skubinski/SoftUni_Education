#input
from math import ceil, floor
paint_boxes = int(input())
wallpapers = int(input())
gloves_price = float(input())
painter_price = float(input())

PAINT_BOX_PRICE = 21.50
WALLPAPERS_PRICE = 5.20
needed_gloves = ceil(wallpapers * 0.35)
needed_painters = floor(paint_boxes * 0.48)
total_money = paint_boxes * PAINT_BOX_PRICE + wallpapers * WALLPAPERS_PRICE + gloves_price * needed_gloves + painter_price * needed_painters
delivery_cost = total_money / 15
print(f"This delivery will cost {delivery_cost:.2f} lv.")


