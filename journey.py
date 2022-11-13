budget = float(input())
season = input()

country = ""
place_to_stay = ""

if budget <= 100:
    country = "Bulgaria"
    if season == "summer":
        place_to_stay = "Camp"
        budget *= 0.3
    else:
        place_to_stay = "Hotel"
        budget *= 0.7
elif budget <= 1000:
    country = "Balkans"
    if season == "summer":
        place_to_stay = "Camp"
        budget *= 0.4
    else:
        place_to_stay = "Hotel"
        budget *= 0.8
elif budget > 1000:
    country = "Europe"
    place_to_stay = "Hotel"
    budget *= 0.9

print(f"Somewhere in {country}")
print(f"{place_to_stay} - {budget:.2f}")