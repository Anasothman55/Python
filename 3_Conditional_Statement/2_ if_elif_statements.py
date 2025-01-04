from rich import print



if 10 > 5:
  print("10 greater than 5")
print("Program ended")




# if..else statement example
x = 3
if x == 4:
  print("Yes")
else:
  print("No")




# if..else chain statement
letter = "A"
if letter == "B":
  print("letter is B")
else:
  if letter == "C":
    print("letter is C")
  else:
    if letter == "A":
      print("letter is A")
    else:
      print("letter isn't A, B and C")




num = 10
if num > 5:
  print("Bigger than 5")
  if num <= 15:
    print("Between 5 and 15")



n = -5
res = "Positive" if n > 0  else "Negative"
print(res)




x = 15
res = "Greater than 20" if x > 20 else "Greater than 10"
print(res)



n = 7
res = ("Odd", "Even")[n % 2 == 0]
print(res)



a = 10
b = 20
max = {True: a, False: b}[a > b]
print(max)




a = 10
b = 20
max = (lambda x, y: x if x > y else y)(a, b)
print(max)





a = 10
b = 20
print("a is greater" if a > b else "b is greater")


