from rich import print
import math



a = 3
b = 5
# a = a + b
a += b
print(a)




a = 3
b = 5
# a = a - b
a -= b
print(a)




a = 3
b = 5
# a = a - b
a -= b
print(a)



a = 3
b = 5
# a = a / b
a /= b
print(a)



a = 3
b = 5
# a = a % b
b %= a
print(b)




a = 3
b = 5
# a = a // b
a //= b
print(a)
print(math.floor(3/5))
print(int(3/5))
print(round(3/5))





a = 3
b = 5
# a = a ** b => 3^5
a **= b
print(a)




a = 3
b = 5
# a = a & b
a &= b
print(a)




print("--------------------------------")


import numpy as np

a = np.array([1, 0, 1, 0])
b = np.array([1, 1, 0, 0])
and_result = np.logical_and(a, b)
or_result = np.logical_or(a, b)
not_result = np.logical_not(a)
xor_result = np.logical_xor(a, b)

print("AND:", and_result)
print("OR:", or_result)
print("NOT:", not_result)
print("XOR:", xor_result)






















