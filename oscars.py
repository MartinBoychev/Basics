name_actor = input()
points = float(input())
count_jury = int(input())
sum_points = points

for _ in range(0, count_jury):
    actors = input()
    points_from_actors = float(input())
    final_points = (len(actors) * points_from_actors) / 2
    sum_points += final_points
    if sum_points > 1250.5:
        break

diff = 1250.5 - sum_points
if sum_points < 1250.5:
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {sum_points:.1f}!")
