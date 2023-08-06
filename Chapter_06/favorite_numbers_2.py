favorite_numbers = {'redouane': [1, 2 ,6], 'hamza': [4, 3], 'brahim': [3, 5, 9], 'said': [10, 33], 'yassine': [12, 16]}
for key, value in favorite_numbers.items():
    print(f"{key.title()}'s favorite numbers are :")
    for i in value:
        print(f"\t{i}")