import math


a = True
print(type(a))

b = False
print(type(b))




# Returns False as x is None
x = None
print(bool(x))
# Returns False as x is an empty sequence
x = ()
print(bool(x))
# Returns False as x is an empty mapping
x = {}
print(bool(x))
# Returns False as x is 0
x = 0.0 # Numeric zero (0, 0.0, 0j)
print(bool(x))
# Returns True as x is a non empty string
x = 'GeeksforGeeks'
print(bool(x))

n = math.nan
print(bool(n)) # return true


var1 = 0
print(bool(var1)) # return false

var2 = 1
print(bool(var2)) # return true

var3 = -9.7
print(bool(var3)) # return true


a = 5
b = 3
c = 8

if a > b or b < c:
  print("True")



a = 0
b = 2
c = 4

if a > b and b<c:
  print(True)
else:
  print(False)

if a and b and c:
  print("True")
else:
  print("False")



a = 0

if not a:
  print("This are False")


a = 0
b = 1

if a == 0:
  print(True)
  
if a == b:
  print(True)

if a != b:
  print(True)



x = 10
y = 10


if x is y:
  print(True)
else:
  print(False)

print(id(x) is id(y)) # return false
















