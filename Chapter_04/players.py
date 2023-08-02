players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[-3:])
print(players[::2])
# Using a loop for slice a list
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
