POINTS_NEEDED = 1250.5
actor_name = input()
points_from_academy = float(input())
number_of_ocenqvashti = int(input())
total_points = points_from_academy
for _ in range (number_of_ocenqvashti):
     judge_name = input()
     points = float(input())
     total_points += len(judge_name) * points / 2

     if total_points > POINTS_NEEDED:
          print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
          break
else:
     print(f"Sorry, {actor_name} you need {1250.5 - total_points:.1f} more!")
