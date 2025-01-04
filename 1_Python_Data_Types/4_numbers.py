from math import floor
from rich import print

x = 5      # A positive integer
y = -23    # A negative integer
z = 0      # Zero is also considered an integer

# Addition
res = 5 + 3    # Output: 8

# Subtraction
res = 10 - 4   # Output: 6

# Multiplication
res = 7 * 6    # Output: 42

# Division
res = 15 / 4   # Output: 3.75

# Floor Division
res = 15 // 4  # Output: 3

# Modulus (%)
res = 15 % 4   # Output: 3 (because 15 divided by 4 gives remainder 3)

# Exponentiation (**)
res = 2 ** 3   # Output: 8 (because 2 raised to the power of 3 is 8)

# Absolute Value (abs)
res = abs(-10) # Output: 10 (absolute value of -10)

# Round (round)
res = round(3.14159, 2)  # Output: 3.14 (rounds to 2 decimal places)



a = 3.14      # A positive float
b = -0.99     # A negative float
c = 0.0       # A float value that represents zero


# Addition (float)
res = 3.5 + 2.2   # Output: 5.7

# Subtraction (float)
res = 7.8 - 4.3   # Output: 3.5

# Multiplication (float)
res = 5.5 * 2.0   # Output: 11.0

# Division (float)
res = 9.0 / 4.5   # Output: 2.0

# Floor Division (float)
res = 9.6 // 4.5  # Output: 2.0 (it returns the truncated quotient)

# Modulus (%) (float)
res = 9.0 % 4.5   # Output: 0.0 (remainder when divided)

# Exponentiation (float)
res = 2.5 ** 2    # Output: 6.25 (2.5 raised to the power of 2)

# Absolute Value (float)
res = abs(-7.4)   # Output: 7.4 (absolute value)

# Round (float)
res = round(3.14159, 2)  # Output: 3.14 (rounds to 2 decimal places)



#? Python Complex

# Addition (complex)
res = (3 + 4j) + (1 + 2j)   # Output: (4 + 6j)

# Subtraction (complex)
res = (5 + 6j) - (2 + 3j)   # Output: (3 + 3j)

# Multiplication (complex)
res = (2 + 3j) * (1 + 4j)   # Output: (-10 + 11j)

# Division (complex)
res = (8 + 6j) / (2 + 3j)   # Output: (2.0 + 0.0j)

# Exponentiation (complex)
res = (1 + 1j) ** 2    # Output: (0 + 2j) (raises the complex number to the power of 2)

# Absolute Value (complex)
res = abs(3 + 4j)   # Output: 5.0 (absolute value of a complex number, which is sqrt(3^2 + 4^2))

# Conjugate of a complex number
res = (3 + 4j).conjugate()   # Output: (3 - 4j) (negates the imaginary part)

# Real and Imaginary parts of a complex number
real = (3 + 4j).real   # Output: 3.0
imag = (3 + 4j).imag   # Output: 4.0


#Using Built-In Function
a = 2
print(float(a))
b = 5.6
print(floor(b))
print(round(b))
print(int(b))
c = '3'
print(type(int(c)))
d = '5.6'
print(type(float(c)))
e = 5
print(complex(e))
f = 6.5
print(complex(f))

#Using Arithmetic Operations: 
a = 1.6
b = 5
c = a + b
print(c)



# Generating Random Integer
import random
x = random.randint(1, 100)
print(x)  

# Generating Random FLoating Point Integer
x = random.uniform(1.0, 10.0)
print(x)

x = random.random()
print(x)  


# NaN Example
import math


#? {"number": NaN} Json format
n = math.nan
print(type(n)) 
print(n)
print(math.isnan(n))

# Infinity and -Infinity Example
x = float('inf')
y = float('-inf')
print(x)  
print(y)































