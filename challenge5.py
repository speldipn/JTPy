import sys
import os
import time
import random
import glob

## Q1
print("=" * 50, "Q1")
class OutOfRange(Exception):
  def __str__(self):
    return "Out of value range"

class Calc(OutOfRange):
  def __init__(self):
    self.result = 0

  def add(self, v):
    try :
      if self.result + v > 100: 
        raise OutOfRange

      self.result += v
      return self.result

    except OutOfRange as e:
      print(e)

  def sub(self, v):
    self.result -= v
    return self.result

calc = Calc()
print(calc.add(10))
print(calc.sub(5))

## Q2
print("=" * 50, "Q2")
cal = Calc()
cal.add(50)
cal.add(60)
print(cal.result)

## Q3
print("=" * 50, "Q3")
# 1. False
print(all([1,2,abs(-3)-3]))

# 2. True
print(chr(ord('a')) == 'a')

## Q4
print("=" * 50, "Q4")
nums = [1, -2, 3, -5, 8, -3]
print(list(filter(lambda n: n > 0, nums)))

## Q5
print("=" * 50, "Q5")
v = hex(234)
print(v)
print(int(v, 16))

## Q6
print("=" * 50, "Q6")
print(list(map(lambda n: n * 3, [1,2,3,4])))

## Q7
print("=" * 50, "Q7")
nums = [-8,2,7,5,-3,5,0,1]
print(max(nums) + min(nums))

## Q8
print("=" * 50, "Q8")
print(round(17/3, 4))

## Q9
print("=" * 50, "Q9")
result = 0
for n in sys.argv[1:]:
  result += int(n)
print(result)

## Q10
print("=" * 50, "Q10")
os.chdir("./neo")
f = os.popen('ls')
print(f.read())
f.close()
os.chdir("../")

## Q11
print("=" * 50, "Q11")
print(glob.glob("./*.py"))


## Q12
# case 1
print("=" * 50, "Q12")
s = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))
print(s)

# case 2
print(time.strftime("%Y/%m/%d %H:%M:%S"))

## Q13 
## Caution: number duplication
print("=" * 50, "Q13")
result = []
while True:
  n = int(random.randint(1, 45))

  if n not in result:
    result.append(n)

  if len(result) > 5: break

print(result)
