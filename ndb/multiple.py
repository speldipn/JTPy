#!/bin/python

import math

a,b = input().split()

total = 0
ia = int(a)
for n in reversed(range(len(b))):
    c = ia * int(b[n])
    total += c * math.pow(10, len(b)-1-n)
    print(int(c))

print(int(total))
