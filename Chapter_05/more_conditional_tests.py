cars = 'Audi'
if cars == 'Audi':
    print('True')
else:
    print('False')

if cars == 'bmw':
    print("True")
else:
    print('False')

if cars.lower() == 'audi':
    print('True')
else:
    print('False')

age = 22
if age < 40:
    print('young man.')
else:
    print('old man.')

name = 'Redouane'
if name == 'Redouane' and age == 22:
    print('Your data is corrrect')

cars = ['audi', 'bmw', 'toyota']
if 'ford' in cars:
    print("The car exist.")
else:
    print("The car doesn\'t exist.")