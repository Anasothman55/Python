from rich import print



x = 10

match x:
  case 8:
    print("x is 8")
  case 1:
    print("x are 1")
  case _:
    print("x is something else")





def num_check(x):
  match x:
    case 10 | 20 | 30:  # Matches 10, 20, or 30
      print(f"Matched: {x}")
    case _:
      print("No match found")

num_check(10)
num_check(20)
num_check(25)



del num_check

def num_check(x):
  match x:
    case 10 if x % 2 == 0:  # Match 10 only if it's even
      print("Matched 10 and it's even!")
    case 10:
      print("Matched 10, but it's not even.")
    case _:
      print("No match found")

num_check(10)
num_check(15)




print('--------------------------')


def process(data):
  match data:
    case [x, y]:  
      print(f"Two-element list: {x}, {y}")
    case [x, y, z]:  
      print(f"Three-element list: {x}, {y}, {z}")
    case _:
      print("Unknown data format")
process([1, 2])
process([1, 2, 3])
process([1, 2, 3, 4])




print("---------------------------------")




def person(person):
  match person:
    case {"name": name, "age": age}:  
      print(f"Name: {name}, Age: {age}")
    case {"name": name}:  
      print(f"Name: {name}")
    case _:
      print("Unknown format")
person({"name": "Alice", "age": 25})
person({"name": "Bob"})
person({"city": "New York"})







