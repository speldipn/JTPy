import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
print(pickle.dump(data, f))
f.close()

import os
print(os.environ)

print('=' * 50)
print(os.environ['PATH'])
print(os.getcwd())
print(os.system('ls -l'))

import glob
print(glob.glob("game/*"))

import tempfile
filename = tempfile.mktemp()
print(filename)

import time
print("time.time() -> ", time.time())
print("time.localtime(time.time()) -> ", time.localtime(time.time()))
print("time.asctime(time.localtime(time.time())) -> ", time.asctime(time.localtime(time.time())))
print("time.ctime() -> ", time.ctime())
print("time.strftime(\"%Y %m %d\", time.localtime(time.time())) -> ", time.strftime("%Y %m %d", time.localtime(time.time())))

#for i in range(10):
#  print(i)
#  time.sleep(1) # sec

import calendar

#print(calendar.calendar(2021))
print(calendar.prmonth(2021, 2))
print(calendar.weekday(2021, 2, 15)) # 0(monday) ~ 6(sunday)
print(calendar.monthrange(2021, 3)) # weekday of 1day of month, total days count

import random
#for i in range(5):
#  print(int(random.random() * 10))

for i in range(5):
  print(random.randint(1, 10)) # range 1 ~ 10

print("=" * 50)
for i in range(5):
  print(random.randint(1, 55)) # range 1 ~ 55

print("=" * 50)
#count = 0
#for i in range(10000):
#  num = random.randint(1, 10)
#  if num == 0: print("zero!"); break
#  print(count, num)
#  count += 1

def random_pop(data):
  number = random.randint(0, len(data)-1)
  return data.pop(number)

if __name__ == '__main__':
  data = [1,2,3,4,5] # this logic, must need to consecutive numbers.. 1,2,3,4(o) but 1,2,4,5(x)
  while data: print(random_pop(data))

print("=" * 50, "shuffle")
data = [1,2,3,4,5]
print(data)
random.shuffle(data)
print(data)

#import webbrowser
#webbrowser.open("https://google.com")

