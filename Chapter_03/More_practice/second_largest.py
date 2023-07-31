# Python program to find second largest
# number in a list
 
# list of numbers - length of
list1 = [10, 20, 4, 45, 99, 66, 88]

num_max = list1[0]
second_max = list1[0]
for i in range(1, len(list1)):
    if num_max < list1[i]:
        num_max = list1[i]
for i in range(1, len(list1)):
    if (second_max < list1[i] < num_max):
        second_max = list1[i]
print(f"The second largest number in list is : {second_max}")