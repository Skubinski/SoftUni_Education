tabs_in_browser = int(input())
salary = float(input())
FACEBOOK_FINE = 150
INSTAGRAM_FINE = 100
REDDIT_FINE = 50
fine = 0
for _ in range(tabs_in_browser):
    tab = input()
    if tab == "Facebook":
        salary -= FACEBOOK_FINE

    elif tab == "Instagram":
        salary -= INSTAGRAM_FINE

    elif tab == "Reddit":
        salary -= REDDIT_FINE
    if salary <= 0:
        break
if salary > 0:
    print(f"{int(salary)}")
else:
    print(f"You have lost your salary.")
