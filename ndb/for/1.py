#!/bin/python

n = int(input())
out = []

for i in range(n):
    x, y = input().split()
    ix = int(x)
    iy = int(y)
    out.append(ix + iy)

for i in range(len(out)):
    print(out[i])
