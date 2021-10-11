#!/usr/bin/python

dic = {'name': 'neo', 'phone': '01033334444', 'birth': '1118'}
print(dic)

print("=" * 50)
for key in dic.keys():
  print(key)

print("=" * 50)
for value in dic.values():
  print(value)

print("=" * 50)
data = dic['name']
print(data, type(data))

print("=" * 50)
a = {1: 'a'}
print(a)
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1,2,3]
print(a)

del a[1]
print(a)

## Warning! duplication key 
a = {1: 'a', 1: 'b'}
print(a, len(a))

# No apply list key type!
#print("=" * 50)
#a = {[1,2]: 'a'}
#print(a)

print("=" * 50)
a = {'name': 'neo', 'phone': '01122223333', 'birth': '1118'}
print("keys!", a.keys()) # list
print("itmems!", a.items())
print("len:", len(a))
print("name!", a['name'], a.get('name'))
a.clear()
print("clear!", a, len(a))

print("=" * 50)
print(a.get('name'))
print(a.get('name', 'nothing')) # default value
a = {'name': 'neo'}
print('name' in a)
print('age' in a)

print("=" * 50) # challenge 
a = {'name': 'Gildong', 'birth': 1128, 'age': 30}
for key in a.keys():
  print(key, a.get(key))

## Set
print("=" * 50)
s1 = set([1,2,3])
print(s1, type(s1))
s2 = set("Hello")
print(s2)
s1 = set([1,2,3])
l1 = list(s1)
print(l1, len(l1), type(l1))
print(l1[0], l1[1], l1[2])
t1 = tuple(l1)
print(t1, len(t1), type(t1))

## intersection
print("=" * 50)
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2)
print(s1.intersection(s2))


## union
print("=" * 50)
print(s1 | s2)
print(s1.union(s2))

## difference
print("=" * 50)
print(s1 - s2)
print(s1.difference(s2))

## set add
s1 = set([1,2,3])
s1.add(4)
print(s1, len(s1))

## set add many
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1, len(s1))

## set remove
s1 = set([1,2,3])
s1.remove(2)
print(s1, len(s1), type(s1))

