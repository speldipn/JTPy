#!/bin/python

import time

a = [3,2,1]
#a.sort()
#print(a)

start_time = time.time()
b = sorted(a)
end_time = time.time()

print(a, b, end_time-start_time)
