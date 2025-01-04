from rich import print
import math



class Car:
  def __init__(self, brand, model):
    self.brand = brand  # Set instance attribute
    self.model = model  # Set instance attribute
  def display(self):
    return {
      "brand": self.brand,
      "model": self.model
    }
car1 = Car("Toyota", "Corolla")
print(car1.display())  # Output: This car is a Toyota Corolla






class gfg:
  def __init__(self, topic):
    self._topic = topic  
  def topic(self):
    print("Topic:", self._topic) 
ins = gfg("Python")
ins.topic()





class Circle:
  def __init__(self, r):
    self.r = r
  def area(self):
    a = math.pi * self.r ** 2
    return round(a,2)
ins = Circle(5)
print("Area of the circle:", ins.area())







# Python program to illustrate functions 
# can be passed as arguments to other functions 
def shout(text): 
	return text.upper() 
def whisper(text): 
	return text.lower() 
def greet(func): 
	# storing the function in a variable 
	greeting = func("""Hi, I am created by a function passed as an argument.""") 
	print (greeting) 

greet(shout) 
greet(whisper) 





# Python program to illustrate functions 
# Functions can return another function 
def create_adder(x): 
	def adder(y): 
		return x+y 
	return adder 
add_15 = create_adder(15) #? x == 15
print (add_15(10)) #? y == 10











