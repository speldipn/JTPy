#!/usr/bin/python

t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

#del t3[0] # Not support item deletion

#t3[0] = 10 # Not supprot item assignment

t1 = (1, 2, 'a', 'b')
print t1

t2 = (3, 4)

print(t1 + t2)
print t2 * 3

t1 = (1, 2, 3)
print t1

## add tuple
print t1 + (4,)
