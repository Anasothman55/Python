from rich import print




def fun(*args):
  return sum(args)

print(fun(1, 2, 3, 4)) 
print(fun(5, 10, 15))   

def funk(**kwargs):
  for k, val in kwargs.items():
    print(k, val)

funk(a=1, b=2, c=3)






def fun(arg1, *argv):
  print("First argument :", arg1)
  for arg in argv:
    print("Argument *argv :", arg)
fun('Hello', 'Welcome', 'to', 'GeeksforGeeks')







def fun(*args, **kwargs):
  print(f"Positional arguments: {args}")
  print(f"Keyword arguments: {kwargs}")

fun(1, 2, 3, a=4, b=5)
