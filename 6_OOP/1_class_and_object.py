from calendar import c
from rich import print




class Dog:
  sound = "bark"  

dog1 = Dog()
print(dog1.sound)



del Dog

class Dog:
  species = "Canine"  # Class attribute
  def __init__(self, name, age):
    self.name = name  # Instance attribute
    self.age = age  # Instance attribute

d1 = Dog("charly",6)
print(d1.name)
print(d1.species)


del Dog




class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name} is {self.age} years old."  # Correct: Returning a string
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1)  
print(dog2)



del Dog


print("--------------")

class Dog:
  species = "Canine"
  def __init__(self, name, age):
    self.name = name
    self.age = age
# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)
# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)



print("--------------------------------------")


class Check:
  def __init__(self):
    print("Address of self = ",id(self))
obj = Check()
print("Address of class object = ",id(obj))






class Car():
  def __init__(self, model, color):
    self.model = model
    self.color = color
  def show(self):
    print("Model is", self.model )
    print("color is", self.color )
audi = Car("audi a4", "blue")
ferrari = Car("ferrari 488", "green")
audi.show()     # same output as car.show(audi)
ferrari.show()  # same output as car.show(ferrari)
print("Model for audi is ",audi.model)
print("Colour for ferrari is ",ferrari.color)



print("----------------")




class Counter:
  def __init__(self):
    self.count = 0
  def increment(self, c: int = 1):
    self.count += c
  def decrement(self, c: int = 1):
    self.count -= c
  def get_count(self):
    return self.count

counter = Counter()
counter.increment()
counter.increment(20)
counter.decrement(3)
print(counter.get_count())



print("----------------------")
#? Class and Instance Attributes in Python


class sampleclass:
  count = 0  
  def increase(self):
    sampleclass.count += 1
s1 = sampleclass()
s1.increase()        
print(s1.count)
s2 = sampleclass()
s2.increase()
print(s2.count)
print(sampleclass.count)



# Python program to demonstrate
# instance attributes.
class emp:
  def __init__(self):
    self.name = 'xyz'
    self.salary = 4000
  def show(self):
    print(self.name)
    print(self.salary)
e1 = emp()
print("Dictionary form :", vars(e1))
print(dir(e1))
e1 = vars(e1)
print(e1.keys())



print("----------------------")

#? Create a Python Subclass


#? the Animal class can not use the method sound
class Animal:
  def __init__(self, name):
    self.name = name  
  def sound(self):
    raise NotImplementedError("Subclasses must implement this method")
class Dog(Animal):
  def sound(self):
    return "Woof!"
a = Animal("Generic Animal")  
d = Dog("Buddy")  
print(a.name)  # Output: Generic Animal
print(d.name)    # Output: Buddy
print(d.sound())  # Output: Woof!





class Shape:
  def __init__(self, color):
    self.color = color
  def area(self):
    raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
  def __init__(self, color, radius):
    super().__init__(color) 
    self.radius = radius  
  def area(self):
    return 3.14 * self.radius ** 2
s = Shape("Red")  
c = Circle("Blue", 5)
print(s.color)  # Output: Red
print(c.color)  # Output: Blue
print(c.radius)  # Output: 5
print(c.area())  # Output: 78.5




print("----------------------")



#? Inner Class in Python


class Color:
  def __init__(self): # constructor method
    # object attributes
    self.name = 'Green'
    self.lg = self.Lightgreen()
  def show(self):
    print('Name:', self.name)

  class Lightgreen:# create Inner Lightgreen class
    def __init__(self):
      self.name = 'Light Green'
      self.code = '024avc'
    def display(self):
      print('Name:', self.name)
      print('Code:', self.code)
# create Color class object
outer = Color()
outer.show()
g = outer.lg
# inner class method calling
g.display()






# create outer class
class Doctors:
  def __init__(self):
    self.name = 'Doctor'
    self.den = self.Dentist()
    self.car = self.Cardiologist()
  def show(self):
    print('In outer class')
    print('Name:', self.name)

  class Dentist:# create a 1st Inner class
    def __init__(self):
      self.name = 'Dr. Savita'
      self.degree = 'BDS'
    def display(self):
      print("Name:", self.name)
      print("Degree:", self.degree)

  class Cardiologist: # create a 2nd Inner class
    def __init__(self):
      self.name = 'Dr. Amit'
      self.degree = 'DM'
    def display(self):
      print("Name:", self.name)
      print("Degree:", self.degree)

outer = Doctors() # create a object # of outer class
outer.show()
d1 = outer.den  # of 1st inner class # create a object
d2 = outer.car # of 2nd inner class # create a object
print()
d1.display()
print()
d2.display()







# create an outer class
class Geeksforgeeks:
  def __init__(self):
    self.inner = self.Inner()  # create an inner class object
  def show(self):
    print('This is an outer class')
  class Inner: # create a 1st inner class
    def __init__(self):
      self.innerclassofinner = self.Innerclassofinner() # create an inner class of inner class object
    def show(self):
      print('This is the inner class')
    class Innerclassofinner: # create an inner class of inner
      def show(self):
        print('This is an inner class of inner class')

outer = Geeksforgeeks() # create an outer class object # i.e.Geeksforgeeks class object
outer.show()
print()
gfg1 = outer.inner # create an inner class object
gfg1.show()
print()
gfg2 = outer.inner.innerclassofinner # create an inner class of inner class object
gfg2.show()







#! Python MetaClasses



def init(self, ftype): 
  self.ftype = ftype 
def getFtype(self): 
  return self.ftype  
FoodType = type('FoodType', (object, ), { 
  '__init__': init, 
  'getFtype' : getFtype, 
  }) 
fType = FoodType(ftype ='Vegetarian') 
print(fType.getFtype())






class FoodType(object): 
  def __init__(self, ftype): 
    self.ftype = ftype 
  def getFtype(self): 
    return self.ftype 

class VegType(FoodType):
  def vegFoods(self): 
    return {'Spinach', 'Bitter Guard'} 

def main(): 
  vType = VegType(ftype = 'Vegetarian') 
  print(vType.getFtype()) 
  print(vType.vegFoods()) 

main() 



def init(self, ftype): 
  self.ftype = ftype 
def getFtype(self): 
  return self.ftype  

FoodType = type('FoodType', (object, ), { 
  '__init__': init, 
  'getFtype' : getFtype, 
  }) 

def vegFoods(self): 
  return {'Spinach', 'Bitter Guard'} 

## creating subclass using type 
VegType = type('VegType', (FoodType, ), { 
  'vegFoods' : vegFoods, 
  }) 
vType = VegType(ftype ='Vegetarian') 
print(vType.getFtype()) 
print(vType.vegFoods()) 










#! static method


class MyClass:
  def __init__(self, value):
    self.value = value
  @staticmethod
  def get_max_value(x, y):
    return max(x, y)
# Create an instance of MyClass
obj = MyClass(10)
print(MyClass.get_max_value(20, 30))  
print(obj.get_max_value(20, 30))





# Python program to demonstrate
# use of class method and static method.
from datetime import date

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # a class method to create a Person object by birth year.
  @classmethod
  def fromBirthYear(cls, name, year):
    return cls(name, date.today().year - year)
  # a static method to check if a Person is adult or not.
  @staticmethod
  def isAdult(age):
    return age > 18
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
print(person1.age)
print(person2.age)
# print the result
print(Person.isAdult(22))






class Car:
  def __init__(self, make, model, year):
    #Initialize the Car with specific attributes.
    self.make = make
    self.model = model
    self.year = year
# Creating an instance using the parameterized constructor
car = Car("Honda", "Civic", 2022)
print(car.make)
print(car.model)
print(car.year)















