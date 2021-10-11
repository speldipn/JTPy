#f = open('aaa.txt', 'r')
#f.close()

## divide by zero
try:
  result = 3 / 0
except ZeroDivisionError as e:
  print(e)

## out of range
try:
  a = [1,2,3]
  print(a[3])
except IndexError as e:
  print(e)

try:
  a = [1,2,3]
  result = a[0] / 0
  #result = a[3]
except (ZeroDivisionError, IndexError) as e:
  print(e)

class Bird:
  def fly(self):
    #raise NotImplementedError
    print("very fast")

bird = Bird()
bird.fly()


class Eagle:
  pass

eagle = Eagle()
print(eagle, type(eagle))

## make exception
class MyError(Exception):
  def __str__(self): # exception string!
    return "Not valid"

def testExcept():
  raise MyError

try:
  testExcept()
except MyError as e:
  print(e)

