
from rich import print






# Parent class
class Animal:
  def __init__(self, name):
    self.name = name
  def speak(self):
    pass

class Dog(Animal):
  def speak(self):
    return f"{self.name} barks!" 
dog = Dog("Buddy")
print(dog.speak())





# A Python program to demonstrate inheritance
class Person(object):
  # Constructor
  def __init__(self, name, id):
    self.name = name
    self.id = id

  # To check if this person is an employee
  def Display(self):
    print(self.name, self.id)
emp = Person("Satyam", 102) # An Object of Person
emp.Display()






class Emp(Person):
  def Print(self):
    print("Emp class called")
Emp_details = Emp("Mayank", 103)
# calling parent class function
Emp_details.Display()
# Calling child class function
Emp_details.Print()






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






# Parent Class: Person
class Person:
  def __init__(self, name, idnumber):
    self.name = name
    self.idnumber = idnumber
  def display(self):
    print(self.name)
    print(self.idnumber)
# Child Class: Employee
class Employee(Person):
  """
  this class are inheritance from Person class 
  the object of Employee class will have all the attributes of Person class
  name = employee name
  idnumber = employee id number
  salary = employee salary
  post = employee post
  """
  def __init__(self, name:str, idnumber:int, salary:float, post:str):
    super().__init__(name, idnumber)  # Using super() to call Person's __init__()
    self.salary = salary
    self.post = post
  def __str__(self):
    return str({
      "name": self.name,
      "idnumber": self.idnumber,
      "salary": self.salary,
      "post": self.post
    })

emp1 = Employee("anas",28,600,"IT")
print(emp1)




print("------------------------")

del Employee
del Person

# 1. Single Inheritance
class Person:
  def __init__(self, name):
    self.name = name
class Employee(Person):  # Employee inherits from Person
  """inherite from person"""
  def __init__(self, name, salary):
    super().__init__(name)
    self.salary = salary
# 2. Multiple Inheritance
class Job:
  def __init__(self, salary):
    self.salary = salary
class EmployeePersonJob(Employee, Job):  # Inherits from both Employee and Job
  """inherite from Employee and Job"""
  def __init__(self, name, salary):
    Employee.__init__(self, name, salary)  # Initialize Employee
    Job.__init__(self, salary)            # Initialize Job
# 3. Multilevel Inheritance
class Manager(EmployeePersonJob):  # Inherits from EmployeePersonJob
  """inherite from EmployeePersonJob"""
  def __init__(self, name, salary, department):
    EmployeePersonJob.__init__(self, name, salary)  # Explicitly initialize EmployeePersonJob
    self.department = department
# 4. Hierarchical Inheritance
class AssistantManager(EmployeePersonJob):  # Inherits from EmployeePersonJob
  """inherite from EmployeePersonJob"""
  def __init__(self, name, salary, team_size):
    EmployeePersonJob.__init__(self, name, salary)  # Explicitly initialize EmployeePersonJob
    self.team_size = team_size
# 5. Hybrid Inheritance (Multiple + Multilevel)
class SeniorManager(Manager, AssistantManager):  # Inherits from both Manager and AssistantManager
  """inherite from Manager and AssistantManager"""
  def __init__(self, name, salary, department, team_size):
    Manager.__init__(self, name, salary, department)        # Initialize Manager
    AssistantManager.__init__(self, name, salary, team_size)  # Initialize AssistantManager
# Creating objects to show inheritance
# Single Inheritance
emp = Employee("John", 40000)
print(emp.name, emp.salary)
# Multiple Inheritance
emp2 = EmployeePersonJob("Alice", 50000)
print(emp2.name, emp2.salary)
# Multilevel Inheritance
mgr = Manager("Bob", 60000, "HR")
print(mgr.name, mgr.salary, mgr.department)
# Hierarchical Inheritance
asst_mgr = AssistantManager("Charlie", 45000, 10)
print(asst_mgr.name, asst_mgr.salary, asst_mgr.team_size)
# Hybrid Inheritance
sen_mgr = SeniorManager("David", 70000, "Finance", 20)
print(sen_mgr.name, sen_mgr.salary, sen_mgr.department, sen_mgr.team_size)

print(vars(sen_mgr)) #? => {'name': 'David', 'salary': 70000, 'department': 'Finance', 'team_size': 20}






















