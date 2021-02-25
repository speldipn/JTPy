# Solve 1
print("*" * 10)
a="a:b:c:d"
b = a.replace(":", '#')
print(b)

# Solve 2
print("*" * 10)
a = {'A': 90, 'B': 80}
a['C'] = 70
print(a['C'])

# Solve 3
print("*" * 10)
a = [1,2,3]
print(a)
b = a + [4,5]
a.extend([4,5])
print(a, b) 

# Solve 4
print("*" * 50)
A = [50,55,67,82,45,33,90,87,100,25]
print(A)
result = 0
for v in A:
  result += v
print("sum:", result)

# Solve 5
print("*" * 50)
def __fibonacci(n):
  if n == 1: return 0
  elif n == 2: return 1
  else : return __fibonacci(n-1) + __fibonacci(n-2)

def fibonacci(n):
  i = 1
  while i <= n:
    print(__fibonacci(i), end=' ')
    i += 1

  print()

fibonacci(10)

# Solve 6
#print("*" * 50)
#nums = input("input:")
#result = 0
#for v in nums.split(","):
#  result += int(v)
#print("sum:", result)

# Solve 7
#print("*" * 50)
#num = input("gugudan:")
#for n in range(1, 10):
#  print("{0} x {1} = {2}".format(num, n, int(num) * n))

# Solve 8
#print("*" * 50)
fd = open("result.txt", "r")
lines = []
for line in fd.readlines():
  lines.append(line)
fd.close()

fd = open("result.txt", "w")
for line in reversed(lines):
  fd.write(line)

fd.close()

# Solve 9
#print("*" * 50)
f = open("sample.txt", "r")
result = 0
lineCount = 0
for v in f.readlines():
  result += int(v)
  lineCount += 1

print(result // lineCount)

# Solve 10
print("*" * 50)
class Calculator:
  def __init__(this, list):
    this.list = list

  def sum(this):
    result = 0
    for v in this.list:
      result += v
    return result

  def avg(this):
    result = 0
    for v in this.list:
      result += v
    return result / len(this.list)


cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())

# Solve 11
# import module

# Solve 12
 #IndexError !!

# Solve 13
print("*" * 50)

def dashInsert(num): 
  result = num[0]
  for n in range(1, len(num)):
    prev = num[n-1]
    cur = num[n]
    if int(prev) % 2 == 0 and int(cur) % 2 == 0:
      result += '*'
    elif int(prev) % 2 == 1 and int(cur) % 2 == 1:
      result += '-'
    result += cur
  return result

print("4546793")
print(dashInsert("4546793"))

# Solve 14
print("*" * 50)
a = "aaabbcccccca"
print(a)

def encode(s):
  l = list(s)
  result = ""
  count = 0
  first = l[0]
  n = 0

  while n < len(l):
    if l[n] == first:
      count += 1
    else:
      result += "{0}{1}".format(first, count)
      count = 1
      first = l[n]
    n += 1

  if count > 0:
      result += "{0}{1}".format(first, count)

  return result


print(encode(a))

# Solve 15
print("*" * 50)
def dupleNumber(n):
  print(n, end=' ')
  target = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  l = list(n)
  for i in range(0, len(target)):
    try:
      l.remove(target[i])
    except:
      return False

  if len(l) > 0: 
    return False

  return True

print(dupleNumber("0123456789"))
print(dupleNumber("01234"))
print(dupleNumber("01234567890"))
print(dupleNumber("6789012345"))
print(dupleNumber("012322456789"))

# Solve 16
print("*" * 50)

