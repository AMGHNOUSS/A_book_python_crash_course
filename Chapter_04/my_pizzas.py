pizzas = ['greek', 'sicilian', 'roman', 'neapolitan']
friend_pizzas = pizzas[:]

pizzas.append('chigaco')
friend_pizzas.append('detroit')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())