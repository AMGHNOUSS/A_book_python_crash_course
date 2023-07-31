# Python – Remove empty List from List

# Initializing list
test_list = [5, 6, [], 3, [], [], 9]

# Printing original list
print(test_list)
test, res = [], []
for i in range(0, len(test_list)):
    if test != test_list[i]:
        res.append(test_list[i])
print(res)
