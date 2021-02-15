#!/usr/bin/python

for i in range(8): # 0 1 2 3 4 5 6 7
  sum = 0
  for j in range(8): # 0 1 2 3 4 5 6 7
    if(j < i):
      print("%s " % sum, end='')
      sum += i
  print()


# 
# 0
# 0 2
# 0 3 6
# 0 4 8 12
# 0 5 10 15 20

