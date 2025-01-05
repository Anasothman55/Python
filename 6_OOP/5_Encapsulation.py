
from rich import print




class Public:
  def __init__(self):
    self.name = "John"  # Public attribute

  def display_name(self):
    print(self.name)  # Public method

obj = Public()
obj.display_name()  # Accessible
print(obj.name)  # Accessible





print("------------------")
# program to illustrate private access modifier in a class

class Geek:
  # private members
  __name = None
  __roll = None
  __branch = None
  # constructor
  def __init__(self, name, roll, branch):
    self.__name = name
    self.__roll = roll
    self.__branch = branch
  # private member function
  def __displayDetails(self):
    # accessing private data members
    print("Name:", self.__name)
    print("Roll:", self.__roll)
    print("Branch:", self.__branch)
  # public member function
  def accessPrivateFunction(self):
    # accessing private member function
    self.__displayDetails()

# creating object
obj = Geek("R2J", 1706256, "Information Technology")

# Throws error
# obj.__name
# obj.__roll
# obj.__branch
# obj.__displayDetails()

# To access private members of a class
print(obj._Geek__name)
print(obj._Geek__roll)
print(obj._Geek__branch)
obj._Geek__displayDetails()

print("")
# calling public member function of the class
obj.accessPrivateFunction()








print("------------------------")

# program to illustrate access modifiers of a class

# super class
class Super:
  # public data member
  var1 = None
  # protected data member
  _var2 = None
  # private data member
  __var3 = None
  # constructor
  def __init__(self, var1, var2, var3):
    self.var1 = var1
    self._var2 = var2
    self.__var3 = var3
  # public member function
  def displayPublicMembers(self):
    # accessing public data members
    print("Public Data Member:", self.var1)
  # protected member function
  def _displayProtectedMembers(self):
    # accessing protected data members
    print("Protected Data Member:", self._var2)
  # private member function
  def __displayPrivateMembers(self):
    # accessing private data members
    print("Private Data Member:", self.__var3)
  # public member function
  def accessPrivateMembers(self):
    # accessing private member function
    self.__displayPrivateMembers()
# derived class
class Sub(Super):
    # constructor
  def __init__(self, var1, var2, var3):
    Super.__init__(self, var1, var2, var3)
    # public member function
  def accessProtectedMembers(self):
    # accessing protected member functions of super class
    self._displayProtectedMembers()

# creating objects of the derived class
obj = Sub("Geeks", 4, "Geeks!")

# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()
print()

# Can also be accessed using
obj._displayProtectedMembers()
obj._Super__displayPrivateMembers()
print()

# Object can access protected member
print("Object is accessing protected member:", obj._var2)
print("Object is accessing private member:", obj._Super__var3)

# object can not access private member, so it will generate Attribute error
# print(obj.__var3)
