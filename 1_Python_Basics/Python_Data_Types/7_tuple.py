from itertools import count
from rich import print
# Creating an empty Tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)

# Creating a Tuple
# with the use of string
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1)

# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

set1 = {1, 2, 4, 5, 6}
print("\nTuple using List: ")
print(tuple(set1))

# Creating a Tuple
# with the use of built-in function
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1[0])






# Creating a Tuple
# with Mixed Datatype
Tuple1 = (5, 'Welcome', 7, 'Geeks', True)
print("\nTuple with Mixed Datatypes: ")
print(Tuple1)

# Creating a Tuple
# with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

# Creating a Tuple
# with repetition
Tuple1 = ('Geeks',) * 3
print("\nTuple with repetition: ")
print(Tuple1)

# Creating a Tuple
# with the use of loop
Tuple1 = ('Geeks')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
  Tuple1 = (Tuple1,)
  print(Tuple1)



# Tuple unpacking
Tuple1 = ("Geeks", "For", "Geeks")
t = [*Tuple1]
print("\n",t)
# This line unpack
# values of Tuple1
a, b, c = Tuple1
print("\nValues after unpacking: ")
print(a)
print(b)
print(c)




# Concatenation of tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Geeks', 'For', 'Geeks')
Tuple3 = Tuple1 + Tuple2
# Printing first Tuple
print("Tuple 1: ")
print(Tuple1)
# Printing Second Tuple 
print("\nTuple2: ")
print(Tuple2)
# Printing Final Tuple
print("\nTuples after Concatenation: ")
print(Tuple3)





# with Numbers
Tuple1 = tuple('GEEKSFORGEEKS')
# Removing First element
print("Removal of First Element: ")
print(Tuple1[1:])
# Reversing the Tuple
print("\nTuple after sequence of Element is reversed: ")
print(Tuple1[::-1])
# Printing elements of a Range
print("\nPrinting elements between Range 4-9: ")
print(Tuple1[4:9])



# Deleting a Tuple

try:
  Tuple1 = (0, 1, 2, 3, 4)
  del Tuple1

  print(Tuple1)
except Exception as e:
  print(str(e))



Tuple = ("anas","othman","ezzat","lat","marwan", "yousf","lat")
print(Tuple.index("marwan"))
print(Tuple.count("lat"))

print(all(Tuple))

Tuple1 = (4,5,6,0)
print(all(Tuple1))
print(any(Tuple1))
print(len(Tuple1))

obj  = dict(enumerate(Tuple1))
print(obj)

print(max(Tuple1))
print(min(Tuple1))
print(sum(Tuple1))

print(Tuple)
print(sorted(Tuple, key=len ))

