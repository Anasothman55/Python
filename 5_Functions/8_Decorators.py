from ast import Call
from rich import print





def shout(text): 
  return text.upper() 
print(shout('Hello')) 
yell = shout 
print(yell('Hello'))





def shout(text): 
  return text.upper() 
def whisper(text): 
  return text.lower() 
def greet(func): 
  greeting = func("""Hi, I am created by a function passed as an argument.""") 
  print (greeting) 
greet(shout) 
greet(whisper)




print("----------------------------")



# defining a decorator
def hello_decorator(func):
  def inner1():
    print("Hello, this is before function execution")
    func()
    print("This is after function execution")
  return inner1
def function_to_be_used():
  print("This is inside the function !!")
function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()




print("---------------------------")

import asyncio
import math
from typing import Callable, Awaitable
import time

def calculate_time(func: Callable):
  async def inner1(*args, **kwargs):
    begin = time.time()
    result = await func(*args, **kwargs)
    end = time.time()
    print("Total time taken in : ", func.__name__, end - begin)
    return result
  return inner1

@calculate_time 
async def factorials(num,d):
  await asyncio.sleep(d) 
  print(math.factorial(num))

async def main():
  await asyncio.gather(
    factorials(10,4),
    factorials(10,6),
    factorials(10,2)
  )

asyncio.run(main())


print("----------------------------")



def hello_decorator(func):
  def inner1(*args, **kwargs):
    print("before Execution")
    returned_value = func(*args, **kwargs)
    print("after Execution")
    return returned_value
  return inner1
@hello_decorator
def sum_two_numbers(a, b):
  print("Inside the function")
  return a + b

a, b = 1, 2
print("Sum =", sum_two_numbers(a, b))






# code for testing decorator chaining 
def decor1(func: Callable): 
  def inner(): 
    x = func() 
    return x * x 
  return inner 

def decor(func): 
  def inner(): 
    x = func() 
    return 2 * x 
  return inner 

@decor1
@decor
def num(): 
  return 10

@decor
@decor1
def num2():
  return 10

print(num()) 
print(num2())















