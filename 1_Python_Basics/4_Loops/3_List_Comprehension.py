from rich import print





a = [2,3,4,5]
res = [val ** 2 for val in a]
print(res)





a = [1, 2, 3, 4, 5]
res = [val for val in a if val % 2 == 0]
print(res)




a = [i for i in range(10)]
print(a)





coordinates = [(x, y) for x in range(3) for y in range(3)]
print(coordinates)




mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [val for row in mat for val in row]
print(res)



















