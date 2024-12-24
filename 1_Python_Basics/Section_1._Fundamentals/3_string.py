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



str = "Python String"
console.print(str[0]) # P
console.print(str[1]) # y

str = "Python String"
console.print(str[-1])  # g
console.print(str[-2])  # n


indexing = '''
+---+---+---+---+---+---+---+---+---+---+---+---+---+
| P | y | t | h | o | n |   | S | t | r | i | n | g | 
+---+---+---+---+---+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7   8   9   10  11  12
-13  -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1 
'''
console.print(indexing)

str = "Python String"
str_len = len(str)
console.print(str_len)












