motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' # Modefing a elemen in list.
print(motorcycles)

motorcycles.append("honda") # Appending Elements to the End of a List. 
print(motorcycles)

motorcycles.insert(1, "motobicane") # Insert Elements into a List at any position. 
print(motorcycles)

del motorcycles[0] # Removing an Item Using the del Statement: By index
print(motorcycles)

motorcycles.pop(1) # Removing an Item Using the pop() Method: by index and return value
print(motorcycles)

motorcycles.remove("yamaha") # Removing an Item Using the pop() Method: by value of item
print(motorcycles)