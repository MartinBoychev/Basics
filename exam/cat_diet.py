fat_percent = int(input())
protein_percent = int(input())
percent_carbs = int(input())
calories = int(input())
water_percent = int(input())

grams_fat = (calories * (fat_percent / 100)) / 9
grams_protein = (calories * (protein_percent / 100)) / 4
grams_carbs = (calories * (percent_carbs / 100)) / 4
total = grams_protein + grams_carbs + grams_fat

cal_per_day = calories / total
final_percent = cal_per_day * ((100 - water_percent) / 100)
print(f"{final_percent:.4f}")