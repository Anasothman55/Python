from rich import print



a = 9
b = 5
c = 9

print(a == b) #? => false
print(a == c) #? => true

print(a != b) #? => true
print(a != c) #? => false

print(a > b)  #? => true
print(b > a)  #? => false

print(a < b)  #? => false
print(b < a)  #? => true

print(a >= b) #? => true
print(a >= c) #? => true
print(b >= a) #? => false

print(a <= b) #? => false
print(a <= c) #? => true
print(b <= a) #? => true

print('-------------')

a = 5
print(1 < a < 10) #? => true
print(10 > a <= 9) #? => true
print(5 != a > 4) #? => false
print(a < 10 < a*10 == 50) #? => true



































































