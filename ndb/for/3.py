#!/bin/python

import sys

n = int(input())
out = []

for i in range(n):
    x, y = sys.stdin.readline().rstrip().split()
    out.append(int(x) + int(y))

for i in range(len(out)):
    print(out[i])


