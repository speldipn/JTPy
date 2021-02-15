#!/usr/bin/python

import sys

print(1 + 2) # 3
print(3 / 2.4) # 1.25
print(3 * 9) # 27

# Integer
a = 1
b = 2
result = a + b
print(result, type(result))

# String
a = "Python"
print(a, type(a))

a = 3
print("a=", a)
if a > 1: 
    print("a is greater than 1")


# for
for a in [1, 2, 3]:
    print(a)

# while
i = 0
while i < 3:
  i = i + 1
  print(i)

# funtion
def add(a, b):
    return a + b

print(add(10, 20))
