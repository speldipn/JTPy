#!/bin/python

a,b,c = input().split()
ia = int(a)
ib = int(b)
ic = int(c)

print((ia+ib)%ic)
print(((ia%ic)+(ib%ic))%ic)
print((ia*ib)%ic)
print(((ia%ic) * (ib%ic))%ic)
