count_group = int(input())
musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_people = 0

for _ in range(0, count_group):
    people_per_group = int(input())
    if people_per_group <= 5:
        musala += people_per_group
    elif people_per_group <= 12:
        montblanc += people_per_group
    elif people_per_group <= 25:
        kilimanjaro += people_per_group
    elif people_per_group <= 40:
        k2 += people_per_group
    elif people_per_group > 40:
        everest += people_per_group
    total_people += people_per_group

print(f"{(musala/total_people) * 100:.2f}%")
print(f"{(montblanc/total_people) * 100:.2f}%")
print(f"{(kilimanjaro/total_people) * 100:.2f}%")
print(f"{(k2/total_people) * 100:.2f}%")
print(f"{(everest/total_people) * 100:.2f}%")
