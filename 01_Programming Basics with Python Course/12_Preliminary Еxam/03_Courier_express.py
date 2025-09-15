#input
price = 0
overcharge = 0
total_money = 0
shipment_weight = float(input())
type_of_service = input()
distance_in_km = int(input())
#calculations
if type_of_service == "standard":
    if shipment_weight < 1:
        price = 0.03
    elif 1 <= shipment_weight < 10:
        price = 0.05
    elif 10 <= shipment_weight < 40:
        price = 0.10
    elif 40 <= shipment_weight < 90:
        price = 0.15
    elif 90 <= shipment_weight < 150:
        price = 0.20
elif type_of_service == "express":
    if shipment_weight < 1:
        price = 0.03
        overcharge = price * 0.8
    elif 1<= shipment_weight < 10:
        price = 0.05
        overcharge = price * 0.4

    elif 10 <= shipment_weight < 40:
        price = 0.10
        overcharge = price * 0.05
    elif 40<= shipment_weight < 90:
        price = 0.15
        overcharge = price * 0.02
    if 90 <= shipment_weight < 150:
        price = 0.20
        overcharge = price * 0.01
transport_price = distance_in_km * price
overcharge_per_km = shipment_weight * overcharge
total_with_overcharge = overcharge_per_km * distance_in_km
total = transport_price + total_with_overcharge






print(f"The delivery of your shipment with weight of {shipment_weight:.3f} kg. would cost {total:.2f} lv.")



