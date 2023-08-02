my_foods = ['pizza', 'falafel', 'carrot cake']

# Coping a list to another list
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(f"\t{food}")

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"\t{food}")