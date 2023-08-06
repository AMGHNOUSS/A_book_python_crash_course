person_1 = {'first_name': 'Hamza', 'last_name':'Al kadi', 'age': 22, 'city': 'Laayoune'}
person_2 = {'first_name': 'John', 'last_name':'destin', 'age': 24, 'city': 'new yotk'}

people = [person_1, person_2]

for value in people:
    print(f"{value['first_name'].title()} {value['last_name'].upper()}, his age is {value['age']} and he lives in {value['city'].title()}")