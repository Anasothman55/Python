from rich import print




from abc import ABC, abstractmethod
# Define an abstract class
class Animal(ABC):
  @abstractmethod #! Abstract methods act as placeholders that force subclasses to implement them.
  def sound(self):
    pass  # This is an abstract method, no implementation here.

# Concrete subclass of Animal
class Dog(Animal):
  def sound(self):
    return "Bark"  # Providing the implementation of the abstract method

# Create an instance of Dog

dog = Dog()
print(dog.sound())  # Output: Bark



del Dog
del Animal



class Animal(ABC):
  @abstractmethod
  def make_sound(self):
    pass  # Abstract method, to be implemented by subclasses
  def move(self):
    return "Moving"  # Concrete method with implementation


class Dog(Animal):
  def make_sound(self):
    return "Bark"  # Providing the implementation of the abstract method

# Create an instance of Dog

dog = Dog()
print(dog.move())  # Output: Bark








class Animal(ABC):
  @property
  @abstractmethod
  def species(self):
    pass  # Abstract property, must be implemented by subclasses

class Dog(Animal):
  @property
  def species(self):
    return "Canine"

# Instantiate the concrete subclass
dog = Dog()
print(dog.species)















