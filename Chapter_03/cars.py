cars = ['BMW', 'Audi', 'Toyota', 'Honda', 'Mercedes', 'Volkswagen']
print(f"I would like to own a {cars[3].title()} car.")
print("+=================+")
cars.sort() # Sorting By Alphabetical, and it's change itself
print(cars)
cars.sort(reverse = True) # Sorting By  Reverse Alphabetical
print(cars)
print("+=================+")
print(sorted(cars))
print("+=================+")
# Printing a List in Reverse Order
cars = ['BMW', 'Audi', 'Toyota', 'Honda', 'Mercedes', 'Volkswagen']
print(cars)
cars.reverse()
print(cars)
print("+======================+")
print(f"Lenght of list cars: {len(cars)}")