from rich import print






def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n-1)
print(factorial(5))






count = 0
def fibonacci(n):
  global count
  count += 1
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
print(f"the function recall himself {count} time")



print("-------------------")


def tail_fact(n, acc=1):
  if n == 0:
    return acc
  else:
    return tail_fact(n-1, acc * n)
def nontail_fact(n):
  if n == 1:
    return 1
  else:
    return n * nontail_fact(n-1)
print(tail_fact(5))  
print(nontail_fact(5))

