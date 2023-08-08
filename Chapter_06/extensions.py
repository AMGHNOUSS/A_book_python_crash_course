cat = {'redouane': {'gender' : 'cat', 'sex': 'F'}}
dog = {'ali': {'gender' : 'dog', 'sex': 'M'}}
turtle = {'abdellah': {'gender' : 'turtle', 'sex': 'F'}}

pets = [cat, dog, turtle]
for values in pets:
    for key, value in values.items():
        print(f"The owner : {key.title()}")
        for keys, data in value.items():
            print(f"\t{keys.title()} : {data.title()}")