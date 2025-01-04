from rich import print






def f():
  s = "I love Geeksforgeeks"
  print(s)
f()

#? print(s) -> NameError: name 's' is not defined






def f():
  print("Inside Function", s)
# Global scope
s = "I love Geeksforgeeks"
f()
print("Outside Function", s)



print("--------------------")


# This function has a variable with
# name same as s.
def f():
  s = "Me too."
  print(s)
s = "I love Geeksforgeeks"
f()
print(s)



del s
del f


print("-----------")


# This function modifies the global variable 's'
def f():
  global s
  s += ' GFG'
  print(s)
  s = "Look for Geeksforgeeks Python Section"
  print(s) 
s = "Python is great!" 
f()
print(s)














