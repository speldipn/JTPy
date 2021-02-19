def add(a, b):
  return a + b

print(add(10, 20))

print("=" * 20)
def add(a, b):
  print("%d + %d = %d" %(a, b, a + b))

add(20, 30)


print("=" * 20)
def add(a=10, b=20):
  print("%d %d" % (a, b))

add(20, 30)
add(40)
add()

print("=" * 20)
def add_many(*args): # * makes parameters to tuple
  result = 0
  for i in args:
    result += i
  return result

print(add_many(10, 20, 30))

print("=" * 20)
def add_mul(choice, *args):
  if choice == "add":
    result = 0
    for i in args:
      result += i
  elif choice == "mul":
    result = 1
    for i in args:
      result *= i

  return result

print(add_mul("add", 1,2,3,4,5))
print(add_mul("mul", 2,3,4))

print("=" * 20)
def print_kwargs(**kwargs):
  print(kwargs)

print_kwargs(a=1, b=2)

print("=" * 20)
def print_mul(a, b):
  return a+b, a*b

(sum, mul) = print_mul(10, 20)
print(sum, type(sum), mul, type(mul))

result = print_mul(10, 20)
print(result)
print(result[0], result[1])

# lambda
add = lambda x, y: x + y
print(add(20,30))

## input
#inputData = input("input:")
#print(inputData)

print('Life' 'is' 'too' 'short')

for i in range(1, 10):
  print(i, end=' ')

print()

## file
f = open('sample.txt', 'r')
print(f.read())
f.close()

## challenge
f = open('./neo.txt', 'w')
f.write("neo\n")
f.write("joon young oh\n")
f.close()

f = open('./new.txt', 'w')
for i in range(1, 11):
  data = '%d번째 줄입니다\n' % i
  #data = '%d번째 줄입니다' % i
  f.write(data)
f.close()

## read lien
f = open('new.txt', 'r')
#while True:
#  line = f.readline()
#  if not line: break
#  print(line, end='')
#f.close()

#lines = f.readlines()
#for line in lines:
#  print(line, end='')
#f.close()

## with(auto close)
with open('new.txt', 'r') as f:
  lines = f.readlines()
  for line in lines:
    print(line, end='')


