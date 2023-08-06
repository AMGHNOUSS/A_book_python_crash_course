cat = {'redouane': 'cat'}
dog = {'ali': 'dog'}
turtle = {'abdellah': 'turtle'}

pets = [cat, dog, turtle]
for values in pets:
    for key, value in values.items():
        print(f"The owner of {value.title()} is : {key.title()}")