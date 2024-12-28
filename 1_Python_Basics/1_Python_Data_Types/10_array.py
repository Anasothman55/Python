import array as arr
from rich import print


a = arr.array('i', [1, 2, 3])
#? i minig it just accep int
print(a[0])
a.append(5)
print(a)




a = arr.array('i', [1, 2, 3])
for i in range(0, 3):
  print(a[i], end=" ")





a = arr.array('i', [1, 2, 3])
print("Integer Array before insertion:", *a)
a.insert(1, 4)
print("Integer Array after insertion:", *a)




a = arr.array('i', [1, 2, 3, 4, 5, 6])
print(a[0])
print(a[3])
b = arr.array('d', [2.5, 3.2, 3.3])
print(b[1])
print(b[2])





arrs = arr.array('i', [1, 2, 3, 1, 5])
arrs.remove(1)
print(arrs)
arrs.pop(2)
print(arrs)





l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = arr.array('i', l)
Sliced_array = a[3:8]
print(Sliced_array)
Sliced_array = a[5:]
print(Sliced_array)
Sliced_array = a[:]
print(Sliced_array)




arrs = arr.array('i', [1, 2, 3, 1, 2, 5])

print(arrs.index(2))
print(arrs.index(1))





arrs = arr.array('i', [1, 2, 3, 1, 2, 5])
arrs[2] = 6
print(arrs)
arrs[4] = 8
print(arrs)




arrs = arr.array('i', [1, 2, 3, 4, 2, 5, 2])
count = arrs.count(2)
print("Number of occurrences of 2:", count)





arrs = arr.array('i', [1, 2, 3, 4, 5])
arrs.reverse()
print("Reversed array:", *arrs)





a = arr.array('i', [1, 2, 3,4,5])
a.extend([6,7,8,9,10])
print(a)
























