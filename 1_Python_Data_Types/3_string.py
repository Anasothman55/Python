
from sys import _xoptions
from rich.console import Console

console = Console()

message = 'This is a string in Python'
message = "This is also a string"

# And when a string contains double quotes, you can use the single quotes:
message = '"Beautiful is better than ugly.". Said Tim Peters'


help_message = '''
Usage: mysql command
  -h hostname     
  -d database name
  -u username
  -p password 
'''

console.print(help_message)


name = 'John'
message = f'Hi {name}'
console.print(message)

#? When you place the string literals next to each other, Python automatically concatenates them into one string. For example:
greeting = 'Good ' 'Morning!'
console.print(greeting)

greeting = 'Good'
time = 'Afternoon'

greeting = greeting + ' ' +time + '!'
console.print(greeting)


#? the code like this makk tuple
greeting = 'Good ' ,'Morning!'
console.print(greeting)



str1 = "Python String"
console.print(str1[0]) # P
console.print(str1[1]) # y

str2 = "Python String"
console.print(str2[-1])  # g
console.print(str2[-2])  # n


indexing = '''
+---+---+---+---+---+---+---+---+---+---+---+---+---+
| P | y | t | h | o | n |   | S | t | r | i | n | g | 
+---+---+---+---+---+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7   8   9   10  11  12
-13  -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1 
'''
console.print(indexing)

str3 = "Python String"
str_len = len(str3)
console.print(str_len)




#? Slicing strings


str4 = "Python String"
console.print(str4[0:20: 2])

#? string[start:end:jump]


str5 = "C" + str4[1:] if str4.lower().startswith("p") else str4
console.print(str5)


s = "Hello World"

print(s.upper())   # output: HELLO WORLD
print(s.lower())   # output: hello world


s = "  gfa   a"
console.print(s.strip(" a"))
console.print(s.lstrip(" a"))
console.print(s.rstrip(" a"))


s = "Python is fun are so fundemental"
# Replaces 'fun' with 'awesome' it will replase even if 'fun' is part of another word
print(s.replace("fun", "awesome"))

import re

s = "Python is fun are so fundemental"
# Replace only the standalone word "fun"
result = re.sub(r"\bfun\b", "awesome", s)
print(result)


s = "Hello "
print(s * 3)

name = "Alice"
age = 22
print(f"Name: {name}, Age: {age}")



print("-------------------------------------------")
#? python string method

# Python3 program to show the
# working of upper() function
text = 'geeKs For geEkS'

# upper() function to convert
# string to upper case
print("\nConverted String: upper")
print(text.upper())

# lower() function to convert
# string to lower case
print("\nConverted String: lower")
print(text.lower())

# converts the first character to 
# upper case and rest to lower case 
print("\nConverted String: title")
print(text.title())

# swaps the case of all characters in the string
# upper case character to lowercase and viceversa
print("\nConverted String: swapcase")
print(text.swapcase())

# convert the first character of a string to uppercase
print("\nConverted String: capitalize")
print(text.capitalize())

# original string never changes
print("\nOriginal String")
print(text)



text2 = "my name anas"
print(text2.center(24,"-"))


# count(substring, start index, end index) 
c= "this text I use it for count method it count a number of letter in string like the string have 10:a"
console.print(c.lower().count('a')) # => 3
console.print(c.lower().count('b',1, 52)) # => 1
console.print(c.lower().count('i')) # => 8
console.print(c.count('i')) # => 7



print("\nend with it return true and false\n")
#? end with it return true and false
text = "geeks for geeks."

result = text.endswith('for geeks')
print (result) # returns False
result = text.endswith('geeks.')
print (result) # returns True
result = text.endswith('for geeks.')
print (result) # returns True
result = text.endswith('geeks for geeks.')
print (result) # returns True



#? finde and it case Sensitive we should use lower() 
s = "Python programming"
index = s.find("prog", 4)
index = s.rfind("prog", 4)
print(index)



s = "Python programming"
position = s.index("prog", 4)
position = s.rindex("prog", 4)
print(position)

#? index and find dpo same thing but find return -1 if not found and index raise error if not found



#? is all alphanumric
s = "Python123"
res = s.isalnum()
console.print(res)



#? isdecimal() Returns true if all characters in a string are decimal
#? isdigit() Returns “True” if all characters in the string are digits
#? isnumeric() Returns “True” if all characters in the string are numeric characters, and there is
print("Ⅷ".isnumeric())

print("\u0031".encode())



jon = "anas othman"
console.print("-".join(jon))



#? partition
string = "light attracts bug iy"
print(string.partition(' '))
print(string.rpartition(' '))

string = "gold is heavy"
# 'is' as partition
print(string.partition('is'))


url = "https://www.example.com/index.html"
result = url.partition("//")
result = result[2].partition("/")
print(result[0]) #? output => www.example.com

