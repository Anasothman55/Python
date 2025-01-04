from rich import print




list1 = [1, 2, 3, 4, 5]
str1 = "Hello World"
dict1 = {1: "Geeks", 2:"for", 3:"geeks"}

print(2 in list1)
print('O' in str1)
print(3 in dict1)




# initialized some sequences
list1 = [1, 2, 3, 4, 5]
str1 = "Hello World"
dict1 = {1: "Geeks", 2:"for", 3:"geeks"}

print(2 not in list1)
print('O' not in str1)
print(3 not in dict1)


print("---------------------------------")

# import module
import operator

print(operator.contains([1, 2, 3, 4, 5], 2))
print(operator.contains("Hello World", 'O'))
print(operator.contains({1, 2, 3, 4, 5}, 6))
print(operator.contains({1: "Geeks", 2:"for", 3:"geeks"}.values(), "geeks"))
print(operator.contains((1, 2, 3, 4, 5), 9))



print('-------------------------------')

# Python program to illustrate the use
# of 'is' identity operator
num1 = 5
num2 = 5
a = [1, 2, 3]
b = [1, 2, 3]
c = a
s1 = "hello world"
s2 = "hello world"
print(num1 is num2)
print(a is b)
print(a is c)
print(s1 is s2)
print(id(s1))
print(id(s2))




num1 = 5
num2 = 5
a = [1, 2, 3]
b = [1, 2, 3]
c = a
s1 = "hello world"
s2 = "hello world"
print(num1 is not num2)
print(a is not b)
print(a is not c)
print(s1 is not s2)
print(s1 is not s1)




# Python program to illustrate the use
# of 'is' and '==' operators
a = [1, 2, 3]
b = [1, 2, 3]

# using 'is' and '==' operators
print(a is b)
print(a == b)








