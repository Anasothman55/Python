from rich import print

a = [10, 20, 15]
print(a)



# List of integers
a = [1, 2, 3, 4, 5]
# List of strings
b = ['apple', 'banana', 'cherry']
# Mixed data types
c = [1, 'hello', 3.14, True]
print(a)
print(b)
print(c)


# From a tuple to list
a = list((1, 2, 3, 'apple', 4.5))  
print(a)


# Create a list [2, 2, 2, 2, 2]
a = [2] * 5
# Create a list [0, 0, 0, 0, 0, 0, 0]
b = [0] * 7
print(a)
print(b)




a = [10, 20, 30, 40, 50]
# Access first element
print(a[0])    
# Access last element
print(a[-1])



# Initialize an empty list
a = []
# Adding 10 to end of list
a.append(10)  
print("After append(10):", a)  
# Inserting 5 at index 0
a.insert(0, 5)
print("After insert(0, 5):", a) 
# Adding multiple elements  [15, 20, 25] at the end
a.extend([15, 20, 25])  
a.extend((15, 20, 25))  
a.extend("anas")  
print("After extend([15, 20, 25]):", a)
#? result : [5, 10, 15, 20, 25, 15, 20, 25, 'a', 'n', 'a', 's']


a = [10, 20, 30, 40, 50]
# Change the second element
a[1] = 25 
print(a)

del a

a = [10, 20, 30, 40, 50]
# Removes the first occurrence of 30
a.remove(30)  
print("After remove(30):", a)
# Removes the element at index 1 (20)
popped_val = a.pop(1) 
print("Popped element:", popped_val)
print("After pop(1):", a) 
# Deletes the first element (10)
del a[0]  
print("After del a[0]:", a)



a = ['apple', 'banana', 'cherry']
# Iterating over the list
for item in a:
  print(item)

import copy

main_matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

main_matrix2 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16]
]
# Access element at row 2, column 3
print(main_matrix[1][2])

print("matrix".ljust(50,"-"))

matrix = copy.deepcopy(main_matrix)
for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    if i == j:
      matrix[i][j] = 0
    print(matrix[i][j], end=" ")
  print()

print("".ljust(20,"+"))
matrix = copy.deepcopy(main_matrix)
for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    if i != j:
      matrix[i][j] = 0
    print(matrix[i][j], end=" ")
  print()

print("".ljust(20,"+"))
matrix = copy.deepcopy(main_matrix)
for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    if i + j == len(matrix) - 1 :
      matrix[i][j] = 0
    print(matrix[i][j], end=" ")
  print()

print("".ljust(20,"+"))
matrix = copy.deepcopy(main_matrix)
for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    if i + j != len(matrix) - 1 :
      matrix[i][j] = 0
    print(matrix[i][j], end=" ")
  print()

print("".ljust(20,"+"))
matrix = copy.deepcopy(main_matrix)
for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    if i <= j:
      matrix[i][j] = 0
    print(matrix[i][j], end=" ")
  print()

"""
  ?  i > j
1 2 3
0 5 6
0 0 9
  ?  i >= j
0 2 3
0 0 6
0 0 0
  ?  i >= j
1 0 0
4 5 0
7 8 9
  ?  i >= j
0 0 0
4 0 0
7 8 0
"""


print("".ljust(20, "+"))
matrix = copy.deepcopy(main_matrix2)
for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    if not ((i == j) or (i + j == len(matrix) - 1)):
      matrix[i][j] = 0
    print(str(matrix[i][j]).center(3, " "), end="  ")
  print()
print("matrix".ljust(50, "-"))

from operator import length_hint

#? length_hint() is not guaranteed to be accurate—it provides a hint or estimation
#? it jsut use when wwe can't use len() function
a = [1, 2, 3, 4, 5]
length = length_hint(a)
print(length)


a = [10, 24, 76, 23, 12]
# Max() will return the largest in 'a'
print(max(a))


from functools import reduce
a = [10, 24, 76, 23, 12]  
# Find the largest number using reduce
largest = reduce(lambda x, y: x if x > y else y, a)
print(largest)

"""
Initial Step: The reduce function starts with the first two elements of the list a. These elements
Summary:
The process can be visualized as
  Compare 10 and 24 → 24
  Compare 24(x) and 76 → 76
  Compare 76 and 23 → 76
  Compare 76 and 12 → 76
The largest number is 76.
"""


a = [10, 20, 30, 40, 50]
a[0], a[4] = a[4], a[0]
print(a)

del a


a = [10, 20, 30, 40, 50]
# Check if 30 exists using any() function
flag = any(x == 30 for x in a)
print(flag)



fruits = ["apple", "banana","cherry","apple"]
print(fruits.index("cherry"))



list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
# Will print index of '4' in sublist
# having index from 4 to 8.
print(list1.index(4, 4, 8))



list1 = [6, 8, 5, 6, 1, 2]
# Will print index of '6' in sublist
# having index from 1 to end of the list.
print(list1.index(6, 1))



a = [1, 2, 2, 3, 4, 4, 5]
# Remove duplicates by converting to a set
a = list(set(a))
print(a)


a = [10, 20, 30, 40]
res = sum(a)
print(res)
sum_of_list = reduce(lambda x,y: x+y ,a)
print(sum_of_list)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)




a = [5, 1, 5, 6]
a.sort()
print(a)
b = [5, 2, 9, 6]
bs = sorted(b)
f = list(filter(lambda  x : x > 5 , b))
print(b)
print(bs)
f.sort()
print(f)



a = [1, -5, 10, 6, 3, -4, -9]
# Sorting by absolute values in descending order
sa = sorted(a, key=abs, reverse=True)
print("Sorted by absolute values:", sa)
print(list(map(lambda  x : abs(x) , sa)))



# List of tuples
a = [(1, 'one'), (3, 'three'), (2, 'two')]
# Sorting by the second element of each tuple
sa = sorted(a, key=lambda x: x[1])
print("Sorted by second element:", sa)



test_list = [5, 6, 3, 8, 2, 1, 7, 1]
print("The original list : " + str(test_list))
sublist = [8, 2, 1]
res = False

for idx in range(len(test_list) - len(sublist) + 1):
  if test_list[idx: idx + len(sublist)] == sublist:
    res = True
    break
print("Is sublist present in list ? : " + str(res))





