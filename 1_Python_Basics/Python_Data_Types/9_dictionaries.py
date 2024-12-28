
import math
from rich.console import Console
from rich import print

console = Console()

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)




# create dictionary using dict() constructor
d2 = dict(a = "Geeks", b = "for", c = "Geeks")
print(d2)

#? class to dict  
class Test:
  def __init__(self, name, age , address):
    self.name = name
    self.age = age
    self.address = address
t=  Test("anas othman", 21, "saidsadq")
t_dict = t.__dict__ 
print(t_dict)



d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }
# Access using key
print(d["name"])
# Access using get()
print(d.get("age" , None))




d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# Adding a new key-value pair
d["age"] = 22
d.update({"name": "anas"})
# Updating an existing value
d[1] = "Python dict"
print(d)




d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22, "name":"anas"}
# Using del to remove an item
del d["age"]
print(d)
# Using pop() to remove an item and return the value
val = d.pop(1)
print(val)
# Using popitem to removes and returns
# the last key-value pair.
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
print(d)
d.clear()
print(d)




d = {1: 'Geeks', 2: 'For', 'age':22}
for key in d:
  print(key, end="  ")
print()
for value in d.values():
  print(value, end="  ")
print()
for key, value in d.items():
  print(f"{key}: {value}", end="  ")
print()



d = {
  1: 'Geeks',
  2: 'For',
  3: {
    'A': 'Welcome',
    'B': 'To',
    'C': 'Geeks'
  }
}
console.print(d)



#? length

d ={'Name':'Steve', 'Age':30, 'Designation':'Programmer'}
print(len(d))

d = {"a": 1, "b": 2, "c": 3}
length = len([key for key in d])
print(length)

d = {"a": 1, "b": 2, "c": 3}
length = sum(1 for i in d)
print(length)

d = {
  "person1": {"name": "John", "age": 25},
  "person2": {"name": "Alice", "age": 30},
  "person3": {"name": "Bob", "age": 22}
}
length = len(d)
print(length)




# Example dictionary
d = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
print(key in d)
print(key in d.values())
print(('a', 1) in d.items())
key = 'g'
print(key in d)




def checkKey(dic: dict, key):
  if key in dic.keys():
    print("Present, ", end =" ")
    print("value =", dic[key])
  else:
    print("Not present")
dic = {'a': 100, 'b':200, 'c':300}
key = 'b'
checkKey(dic, key)
key = 'w'
checkKey(dic, key)



d = {'a': 100, 'b':200, 'c':300}
print(d.get('sjh', math.nan))
if d.get('b') == None:
  print("Not Present")
else:
  print("Present")



d = {'Aman': 110, 'Rajesh': 440, 'Suraj': 990}
try:
  d["Kamal"]
  print('Found')
except Exception as ex:
  print(f"{ex} don't founde")




# Creating a sample dictionary
d = {'name': 'geeks', 'age': 21, 'place': 'India'}
# Using setdefault() method
val = d.setdefault('name', 'Default Name')
print("Name:", val)
# Using setdefault() for a key not present in the dictionary
country_value = d.setdefault('country', 'Unknown')
print("Country:", country_value)





from collections import defaultdict, Counter
# Crating a defaultdict with a default value of 'Unknown'
d = defaultdict(lambda: 'Unknown key', {'name': 'geeks', 'age': 21, 'place': 'India'})
# Accessing value using bracket notation
print(d)
country_value = d['place']
print("Country:", country_value)
print(d['anas'])




# Initializing dictionary
test_dict = {"Arushi": 22, "Mani": 21, "Haritha": 21}
print("The dictionary before performing remove is : ", test_dict)
del test_dict['Mani']
print("The dictionary after remove is : ", test_dict)
#del test_dict['Mani'] #! => KeyError: 'Mani'





# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
print("The dictionary before performing remove is : " + str(test_dict))
removed_value = test_dict.pop('Mani')
print("The dictionary after remove is : " + str(test_dict))
print("The removed key's value is : " + str(removed_value))
print('\r')
removed_value = test_dict.pop('Manjeet', 'No Key found')
print("The dictionary after remove is : " + str(test_dict))
print("The removed key's value is : " + str(removed_value))




# Initializing dictionary 
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
print("The dictionary before performing\remove is : " + str(test_dict))
new_dict = {key: val for key, val in test_dict.items() if key != 'Mani'}
print("The dictionary after remove is : " + str(new_dict))



# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
print("The dictionary before performing remove is : \n" + str(test_dict))
a_dict = {key: test_dict[key] for key in test_dict if key != 'Mani'}
print("The dictionary after performing remove is : ", a_dict)

print("\n")

# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
print(test_dict)
y = {}
for key, value in test_dict.items():
  if key != 'Arushi':
    y[key] = value
print(y)





# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
print(test_dict)
del test_dict
try:
  print(test_dict)
except :
  print('Deleted!')




# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
print(test_dict)
test_dict.clear()
print("Length", len(test_dict))
print(test_dict)



test_dict = {1 : 'Gfg is best for geeks', 2 : 'Gfg is good', 3 : 'I love Gfg'}
print("The original dictionary : " + str(test_dict))
sub_list = ['love', 'good']
res = dict()
for key, val in test_dict.items():
  if any(ele in val for ele in sub_list):
    res[key] = val
print("Filtered Dictionary : " + str(res)) 





test_dict = {1 : 'Gfg is best for geeks', 2 : 'Gfg is good', 3 : 'I love Gfg'}
print("The original dictionary : " + str(test_dict))
sub_list = ['love', 'good']
res = {key : val for key, val in test_dict.items() if not any(ele in val for ele in sub_list)}
print("Filtered Dictionary : " + str(res)) 




test_dict = {1: 'Gfg is love', 2: 'Gfg is good'}
sub_list = ['love', 'good']
for key, value in list(test_dict.items()):
	for sub in sub_list:
		if sub in value:
			test_dict.pop(key)
print(test_dict)





# Import reduce from functools
from functools import reduce
test_dict = {1 : 'Gfg is best for geeks', 2 : 'Gfg is good', 3 : 'I love Gfg'}
print("The original dictionary : " + str(test_dict))
sub_list = ['love', 'good']
res = reduce(lambda d, k: {**d, k: test_dict[k]}, filter(lambda k: not any(sub in test_dict[k] for sub in sub_list), test_dict), {})
print("Filtered Dictionary : " + str(res))
#This code is contributed by Jyothi pinjala.




def returnSum(myDict):
	list = []
	for i in myDict:
		list.append(myDict[i])
	final = sum(list)
	return final
# Driver Function
dicts = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dicts))
print(sum(dicts.values()))




def returnSum(dicts: dict) -> int:
	sum = 0
	for i in dicts.values():
		sum = sum + i
	return sum


# Driver Function
dicts = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dicts))



def returnSum(dict: dict) -> int:
	return sum(dict.values())
dicts = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dicts))




import functools
dic = {'a': 100, 'b': 200, 'c': 300}
sum_dic = functools.reduce(lambda ac,k: ac+dic[k], dic, 0)
print("Sum :", sum_dic)




def returnSum(myDict: dict) -> int:
	return sum(myDict[key] for key in myDict)
dicts = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dicts))




import numpy as np
def returnSum(dict):
	values = np.array(list(dict.values()))
	return np.sum(values)
dict1 = {'a': 100, 'b': 200, 'c': 300}
print("Sum:", returnSum(dict1))




print('\n-------------------------------------\n')

test_dict = {'Gfg' : 2, 'for' : 1, 'CS' : 2}
print("The original dictionary is : " + str(test_dict))
temps = max(test_dict.values())
res = [key for key in test_dict if test_dict[key] == temps]
print("Keys with maximum values are : " + str(res))




test_dict = {'Gfg' : 2, 'for' : 1, 'CS' : 2}
print("The original dictionary is : " + str(test_dict))
res = [key for key in test_dict if all(test_dict[temp] <= test_dict[key] for temp in test_dict)]
print("Keys with maximum values are : " + str(res))





d = {'CS': 2, 'Gfg': 2, 'for': 1}
max_val = max(d.values())
max_keys = []
for key in d:
	if d[key] == max_val:
		max_keys.append(key)
print("Keys with maximum values are :", max_keys)





test_dict = {'Gfg': 2, 'for': 1, 'CS': 2}
print("The original dictionary is: " + str(test_dict))
max_val = max(test_dict.values())
res = list(filter(lambda x: test_dict[x] == max_val, test_dict))
print("Keys with maximum values are: " + str(res))



print("".ljust(50,"-"))




test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
print("The original dictionary is : " + str(test_dict))
temp = []
res = dict()
for key, val in test_dict.items():
	if val not in temp:
		temp.append(val)
		res[key] = val
print("The dictionary after values removal : " + str(res))





test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
print("The original dictionary is : " + str(test_dict))
temp = {val: key for key, val in test_dict.items()}
res = {val: key for key, val in temp.items()}
print("The dictionary after values removal : " + str(res))




test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
print("The original dictionary is : " + str(test_dict))
res = {}
for key, val in test_dict.items():
	res.setdefault(val, key)
print("The dictionary after values removal : " +str(dict((v, k) for k, v in res.items())))





test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
print("The original dictionary is : " + str(test_dict))
unique_values = set(test_dict.values())
res = {}
for val in unique_values:
	for key in test_dict.keys():
		if test_dict[key] == val:
			res[key] = val
			break
print("The dictionary after values removal : " + str(res))





from collections import defaultdict
test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
print("The original dictionary is : " + str(test_dict))
d = defaultdict(list)
for k, v in test_dict.items():
	d[v].append(k)
print(d)
res = {k: v[0] for k, v in d.items()}
print("The dictionary after values removal : " + str(res))



print('-----------------------------------------------------')


test_dict = {'tough': 1, 'to': 2, 'do': 3, 'todays': 4, 'work': 5}
print("The original dictionary : " + str(test_dict))
test_pref = 'to'
res = {key: val for key, val in test_dict.items() if key.startswith(test_pref)}
print("Filtered dictionary keys are : " + str(res))





test_dict = {'tough': 1, 'to': 2, 'do': 3, 'todays': 4, 'work': 5}
print("The original dictionary : " + str(test_dict))
test_pref = 'to'
res = dict(filter(lambda item: item[0].startswith(test_pref), test_dict.items()))
print("Filtered dictionary keys are : " + str(res))





test_dict = {'tough' : 1, 'to' : 2, 'do' : 3, 'todays' : 4, 'work' : 5}
print("The original dictionary : " + str(test_dict))
test_pref = 'to'
res = {key:val for key, val in test_dict.items() if key.find(test_pref)==0}
print("Filtered dictionary keys are : " + str(res))





test_dict = {'tough': 1, 'to': 2, 'do': 3, 'todays': 4, 'work': 5}
print("The original dictionary : " + str(test_dict))
test_pref = 'to'
res=dict()
for i in list(test_dict.keys()):
	if(i[:len(test_pref)]==test_pref):
		res[i]=test_dict[i]
print("Filtered dictionary keys are : " + str(res))




print('\n------------------------------------------\n')


from collections import Counter
a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
b = Counter(a)
print(b)





from collections import defaultdict
a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
b = defaultdict(int)
for c in a:
  b[c] += 1
print(dict(b))





a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
b = {}
for c in a:
  if c in b:
    b[c] += 1
  else:
    b[c] = 1
print(b)




a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
b = list(set(a))
c = {item: a.count(item) for item in b}
print(c)



print("\n-------------------------------------------------------------\n")


"""
def checkEqual(a, b):
  if len(a) != len(b):
    return False
  return sorted(a) == sorted(b)

a = [3, 5, 2, 5, 2]
b = [2, 3, 5, 5, 2]
if checkEqual(a, b):
  print("true")
else:
  print("false")
"""


def checkEqual(a, b):
  n, m = len(a), len(b)
  if n != m:
    return False

  mp = {}
  for num in a:
    mp[num] = mp.get(num, 0) + 1

  for num in b:
    if num not in mp:
      return False
    if mp[num] == 0:
      return False
    mp[num] -= 1
  return True

a = [3, 5, 2, 5, 2]
b = [2, 3, 5, 5, 2]
if checkEqual(a, b):
  print("true")
else:
  print("false")


print("\n-------------------------------------------------------------\n")


# Python Program to find max distance between two occurrences
# in array by exploring all pairs

def maxDistance(arr):
  res = 0
  for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
      if arr[i] == arr[j]:
        res = max(res, j - i)
  return res

arr = [1, 2, 4, 1, 3, 4, 2, 5, 6, 5]
print(maxDistance(arr))

del maxDistance


def maxDistance(arr):
  mp = {}
  res = 0
  for i in range(len(arr)):
    if arr[i] not in mp:
      mp[arr[i]] = i
    else:
      res = max(res, i - mp[arr[i]])
  return res
arr = [1, 1, 2, 2, 2, 1]
print(maxDistance(arr))


print("-----------------------------------")



def countPairs(arr, target):
  n = len(arr)
  cnt = 0
  for i in range(n):
    for j in range(i + 1, n):
      if arr[i] + arr[j] == target:
        cnt += 1
  return cnt
arr = [1, 5, 7, -1, 5]
target = 6
print(countPairs(arr, target))




def countPairs(arr, target):
  freq = {}
  cnt = 0
  for i in range(len(arr)):
    if (target - arr[i]) in freq:
      cnt += freq[target - arr[i]] 
    freq[arr[i]] = freq.get(arr[i], 0) + 1 
    print(freq)
  return cnt
arr = [1, 5, 7, -1, 5] 
target = 6 
print(countPairs(arr, target))



print("-----------------------------------")





def find3Numbers(arr, sum):
  n = len(arr)
  for i in range(n - 2):
    for j in range(i + 1, n - 1):
      for k in range(j + 1, n):
        if arr[i] + arr[j] + arr[k] == sum:
          print(f"Triplet is {arr[i]}, {arr[j]}, {arr[k]}")
          return True
  return False
arr = [1, 4, 45, 6, 10, 8]
sum = 22
find3Numbers(arr, sum)


print("-----------------------------------")






















































