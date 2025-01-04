from rich import print




#? Polymorphism in Built-in Functions
print(len("Hello"))  # String length
print(len([1, 2, 3]))  # List length

print(max(1, 3, 2))  # Maximum of integers
print(max("a", "z", "m"))  # Maximum in strings






def add(a, b):
  return a + b
print(add(3, 4))           # Integer addition
print(add("Hello, ", "World!"))  # String concatenation
print(add([1, 2], [3, 4])) # List concatenation






class Dog:
  def sound(self):
    return "Bark"
class Cat:
  def sound(self):
    return "Meow"
# Polymorphism in action
animals = [Dog(), Cat()]
for animal in animals:
  print(animal.sound())






class Shape:
  def area(self):
    raise NotImplementedError("the shape can't have area")
class Rectangle(Shape):
  def __init__(self, length, width):
    self.length = length
    self.width = width
  def area(self):
    return self.length * self.width
class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
  def area(self):
    return 3.14 * self.radius ** 2
shapes = [Rectangle(2, 3), Circle(5)]
for shape in shapes:
  print(f"Area: {shape.area()}")









