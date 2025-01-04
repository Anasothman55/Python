
# Parent Class: Person
class Person:
  def __init__(self, name, idnumber):
    self.name = name
    self.idnumber = idnumber

# Child Class: Employee
class Employee(Person):
  def __init__(self, name, idnumber, salary, post):
    super().__init__(name, idnumber)  # Calls Person's __init__()
    self.salary = salary
    self.post = post
