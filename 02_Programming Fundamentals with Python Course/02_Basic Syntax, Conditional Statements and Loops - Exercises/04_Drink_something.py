age = int(input())
level = ""
if age <= 14:
    level = "kid"
elif 14 < age <= 18:
    level = "teen"
elif 18 < age <= 21:
    level = "young adult"
else:
    level = "adult"

if level == "kid":
    print("drink toddy")
elif level == "teen":
    print("drink coke")
elif level == "young adult":
    print("drink beer")
else:
    print("drink whisky")






