from rich import print



# Example of an exception
n = 10
try:
  res = n / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
  print("Can't be divided by zero!\n", str(e))




try:
  n = 0
  res = 100 / n
except ZeroDivisionError:
  print("You can't divide by zero!")
except ValueError:
  print("Enter a valid number!")
else:
  print("Result is", res)
finally:
  print("Execution complete.")






# Python code to illustrate
# working of try() 
def divide(x, y):
  try:
    # Floor Division : Gives only Fractional Part as Answer
    result = x // y
    print("Yeah ! Your answer is :", result)
  except ZeroDivisionError:
    print("Sorry ! You are dividing by zero ")
# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)







import math

try:
  result = math.exp(1000)  # Exponential function with a large argument
except OverflowError as e:
  print(e)






class MyClass:
  pass
obj = MyClass()
try:
  obj.some_attribute
except AttributeError as e:
  print(e)




try:
  
  li = [1] * (10**10)
  print(li)
except Exception as e:
  print(str(e))







#!  User-defined Exceptions in Python with Examples





# Step 1: Define a custom exception class
class InvalidAgeError(Exception):
  def __init__(self, age, msg="Age must be between 0 and 120"):
    self.age = age
    self.msg = msg
    super().__init__(self.msg)
  def __str__(self):
    return f'{self.age} -> {self.msg}'
# Step 2: Use the custom exception in your code
def set_age(age):
  if age < 0 or age > 120:
    raise InvalidAgeError(age)
  else:
    print(f"Age set to: {age}")
# Step 3: Handling the custom exception
try:
  set_age(150)  # This will raise the custom exception
except InvalidAgeError as e:
  print(e)






