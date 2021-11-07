#!/bin/python

a,b = input().split()

ia = int(a)
ib = int(b)

if ia > ib:
    print(">")
elif ia < ib:
    print("<")
else:
    print("==")
