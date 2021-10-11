print(abs(-3))
print(abs(-1.2))

print(all([1,2,3]))
print(all([1,2,3,0])) # include zero(false)

print(any([1,2,3,0])) # more than value that include true

print(any([0, ""]))

print(chr(97))

print(dir([1,2,3]))

print(divmod(5,2))
# equal
print(5//2)
print(5%2)

for i, name in enumerate(['body', 'foo', 'bar']):
  print(i, name)

a = [1,2,3]
print(a.index(1))

print(eval('1+2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4,3)'))

def positive(l):
  result = []
  for num in l:
    if num > 0:
      result.append(num)
  return result

a = [1,-3,2,0,-5,6]
print(positive(a))

def simplePositivie(n): 
  if n > 0: return True
  else: return False

print(list(filter(simplePositivie, a)))
print(list(filter(lambda n: n > 0, a)))
print(filter(lambda n: n > 0, a)) # cast list, tuple, set

print(hex(234))
print(hex(3))
print(hex(128))

print(int(3.4))
print(int(3.5))
print(int(3.6))
print(int(3.4))
print(int('3'))
print(int('1A', 16))
print(int('FF', 16))
print(float('1.0'))

class Person: pass
class Student: pass

a = Person()
b = Student()
print(isinstance(a, Person))
print(isinstance(b, Person))

## map
def two_times(numberList):
  result = []
  for number in numberList:
    result.append(number*2)
  return result

result = two_times([1,2,3,4])
print(result)

print(map(lambda n: n * 2, [1,2,3,4])) # cast list, tuple, set
print(list(map(lambda n: n * 2, [1,2,3,4])))

print(max([1,2,3]))
print(min([1,2,3]))
print(oct(34))

print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))
print(ord(' '))
print(ord('\n'))
print(ord('0'))

print(list(range(5)))
print(list(range(1,10)))
print(list(range(1,10,2)))

print(round(4.4)) # 4
print(round(4.5)) # 5 but 4...??
print(round(4.6)) # 5
print(round(5.664, 2))

print(sorted([5,1,3,2,4]))
a = [5,1,3,2,4]
a.sort()
print(a)

print(str(3))
print(str('hi'))
print(str('hi').upper())

print(sum([1,2,3]))
print(sum([4,5,6]))

print(tuple('abc'))
print(tuple([1,2,3]))
print(tuple((1,2,3)))

print(list(zip([1,2,3], [4,5,6])))
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
print(list(zip("abc", "def")))


