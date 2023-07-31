# Swap elements in String list
# using replace() + list comprehension
 
# Initializing list
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
res = []
# printing original lists
print(f"The original list is :  {test_list}")
for i in range(0, len(test_list)):
    txt = test_list[i]
    txt = txt.replace('e', '-').replace('G', 'e').replace('-', 'G')
    res.append(txt)
# printing result
print (f"List after performing character swaps : {res}")