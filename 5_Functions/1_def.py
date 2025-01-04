





# defining function
def func():
  print("Hello")  
func()






def subNumbers(x, y):
  return (x-y)
a = 90
b = 50
res = subNumbers(a, b)
print("subtraction of ", a, " and ", b, " is ", res)





def fun(n):
  x = 2
  count = 0
  while count < n:
    for d in range(2, int(x ** 0.5) + 1):
      if x % d == 0:
        break 
    else:
      print(x)
      count += 1
    x += 1
n = 10
fun(n)



print("--------------------")


def fun(func, arg):
  return func(arg)
  
def square(x):
  return x ** 2
res = fun(square, 5)
print(res)






def fun(*args):
  for arg in args:
    print(arg)
fun(1, 2, 3, 4, 5)





print("-------------------")




def fun(**kwargs):
  for k, val in kwargs.items():
    print(f"{k}: {val}")

fun(name="Alice", age=30, city="New York")







class Person:
  def __init__(self, name, age):
    self.name = name  
    self.age = age   
  def greet(self):
    print(f"Name - {self.name} and Age - {self.age}.")
  @staticmethod
  def static_method():
    print("This is a static method")

p1 = Person("Alice", 30)
p1.greet()

Person.static_method()




def fun1(msg):
  def fun2():
    return f"Message: {msg}"
  return fun2
fun3 = fun1("Hello, World!")
print(fun3())






