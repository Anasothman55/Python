from rich import print






# Python program to illustrate nested functions 
def outerFunction(text): 
  text = text 
  def innerFunction(): 
    print(text) 
  innerFunction() 
outerFunction('Hey !')





# Python program to 
# demonstrate accessing of
# variables of nested functions

def f1():
  s = 'I love GeeksforGeeks'
  def f2():
    s = 'Me too'
    print(s)
  f2()
  print(s)
# Driver's code
f1()





# Python program to 
# demonstrate accessing of
# variables of nested functions

def f1():
  s = ['I love GeeksforGeeks']
  def f2():
    s[0] = 'Me too'
    print(s)
  f2()
  print(s)
# Driver's code
f1()






# Python program to 
# demonstrate accessing of
# variables of nested functions

def f1():
  s = 'I love GeeksforGeeks'
  def f2():
    nonlocal s
    s = 'Me too'
    print(s)
  f2()
  print(s)
# Driver's code
f1()





# Python program to 
# demonstrate accessing of
# variables of nested functions

def f1():
  f1.s = 'I love GeeksforGeeks'
  def f2():
    f1.s = 'Me too'
    print(f1.s)
  f2()
  print(f1.s)
# Driver's code
f1()




print("--------------------------")

# Python program to illustrate 
# closures 
import logging 
logging.basicConfig(filename ='example.log', level = logging.INFO) 
  

def logger(func): 
  def log_func(*args): 
    logging.info( 
      'Running "{}" with arguments {}'.format(func.__name__, args)) 
    print(func(*args)) 
  return log_func               

def add(x, y): 
  return x + y 

def sub(x, y): 
  return x-y 

add_logger = logger(add) 
sub_logger = logger(sub) 
  
add_logger(3, 3) 
add_logger(4, 5) 
  
sub_logger(10, 5) 
sub_logger(20, 10)




