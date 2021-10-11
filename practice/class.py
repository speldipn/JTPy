
## older
result1 = 0
result2 = 0

def add1(num):
  global result1
  result1 += num
  return result1

def add2(num):
  global result2
  result2 += num
  return result2

print("add1")
print(add1(2))
print(add1(3))

print("add2")
print(add2(8))
print(add2(7))

## class
print("=" * 20)
class Calculator:
  def __init__(self):
    print("Calculator init called")
    self.result = 0

  def add(self, num):
    self.result += num
    return self.result

calc1 = Calculator()
calc2 = Calculator()

print("calc1")
print(calc1.add(3))
print(calc1.add(5))

print("calc2")
print(calc2.add(10))
print(calc2.add(20))

print("=" * 20)

class Cookie:
  pass

a = Cookie()
b = Cookie()
print(a, b)

## Four operator class
class FourCalc:
  def __init__(self):
    print("FourCalc init called")
    self.result = 0

  def add(self, num):
    self.result += num
    return self.result

  def minus(self,num):
    self.result -= num
    return self.result

  def mul(self, num):
    self.result *= num
    return self.result

  def div(self, num):
    self.result /= num
    return self.result

  def pow(self, num):
    self.result **= num
    return self.result


calc = FourCalc()
print(calc, type(calc))
print(calc.add(100))
print(calc.minus(50))
print(calc.mul(2))
print(calc.div(5))

## inheritance
class TempCalc: 
  def call(self):
    print("TempCalc called")

class MoreCalc(FourCalc, TempCalc):
  pass

mCalc = MoreCalc()
print(mCalc.add(10)) # 10
print(mCalc.minus(5)) # 5
print(mCalc.mul(3)) # 15
print(mCalc.div(5)) # 3
print(mCalc.pow(3))
mCalc.call()

