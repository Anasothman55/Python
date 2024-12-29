from rich import print

s = ["Geeks", "for", "Geeks"]

for i in s:
  print(i)



print("---------------")


s = "Geeks"
for i in s:
  print(i)

print("---------------")

for i in range(0, 10, 2):
  print(i)


print("----------------")

for i in 'geeksforgeeks':
  if i == 'e' or i == 's':
    continue
  print(i)


print("------------")
for i in 'geeksforgeeks':
  if i == 'e' or i == 's':
    break
print(i)


print('------------------------------')
# An empty loop
for i in 'geeksforgeeks':
  pass
print(i)


print('------------------')



for i in range(1, 4):
  print(i)
else:  
  print("No Break\n")


print('-------------------------')

li = ["eat", "sleep", "repeat"]
for i, v in enumerate(li):
  print (i, v)


for i in range(1, 4):
  for j in range(1, 4):
    print(i, j)




a = ["shirt", "sock", "pants", "sock", "towel"]
b = []
for i in a:
  if i == "sock":
    continue
  else:
    print(f"Washing {i}")
b.append("socks")
print(f"Washing {b}")




for i in range(1, 8):
  d = 3 + (i - 1) * 0.5
  print(f"Day {i}: Run {d:.2f} miles")



number = 255
print(f"Decimal: {number:d}")    # Output: 255
print(f"Binary: {number:b}")     # Output: 11111111
print(f"Octal: {number:o}")      # Output: 377
print(f"Hexadecimal: {number:x}")  # Output: ff
print(f"Hexadecimal: {number:X}")  # Output: FF


success_rate = 0.875
print(f"Success rate: {success_rate:.1%}")  # Output: 87.50%


number = 42
out = f"{number:-d}"
print(f"Always show sign: {number:+d}")  # Output: +42
print(f"Space for positive:", out)  # Output:  42


large_number = 1234567.89
print(f"With commas: {large_number:,.2f}")  # Output: 1,234,567.89











