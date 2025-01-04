from rich import print

# lambda it like arrow fuction in JS



s1 = 'GeeksforGeeks'
s2 = lambda x: x.upper()
print(s2(s1))





# Example: Check if a number is positive, negative, or zero
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(5))   
print(n(-3))  
print(n(0))






# Using lambda
sq = lambda x: x ** 2
print(sq(3))
# Using def
def sqdef(x):
  return x ** 2
print(sqdef(3))





li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
  print(i())





# Example: Check if a number is even or odd
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(4))  
print(check(7))




# Example: Perform addition and multiplication in a single line
calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)


print("--------------------")

# Example: Filter even numbers from a list
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))



n2 = [1, 2, 3, 4, 5, 6]
multi = list(map(lambda x: x*2,n2))
print(multi)



from functools import reduce


n3 = [1, 2, 3, 4, 5, 6]
sume = reduce(lambda x,y: x + y,n3, 100)
print(sume)





a = [1, 2, 3, 4, 5, 6]
c = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, a)))
print(c)






import functools
# importing operator for operator functions
import operator
# initializing list
a = [1, 3, 5, 6, 2]
# using reduce with add to compute sum of list
print(functools.reduce(operator.add, a))
# using reduce with mul to compute product
print(functools.reduce(operator.mul, a))
# using reduce with add to concatenate string
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))




