def plunder(day, daily, expected):
    gattered_plunder = 0
    for i in range(1, day + 1):
        gattered_plunder += daily
        if i % 3 == 0:
            additional_plunder = daily * 0.5

            gattered_plunder += additional_plunder
        if i % 5 == 0:
            losed_plunder = gattered_plunder * 0.3
            gattered_plunder -= losed_plunder
    if gattered_plunder >= expected:
        return f"Ahoy! {gattered_plunder:.2f} plunder gained."
    return f"Collected only {gattered_plunder / expected_plunder * 100:.2f}% of the plunder."



days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
print(plunder(days, daily_plunder, expected_plunder))