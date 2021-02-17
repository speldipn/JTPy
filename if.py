money = True
if money: 
  print("Taxi")
  print("Riding")
else:
   print("??")

age = 30

if age > 50 or age < 29:
  print("A")
else:
  print("B")

print(1 in [1,2,3])
print(1 not in [1,2,3])

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
  print("Use taxi")
else:
  print("Walking")

print('d' in ('a', 'b', 'c'))

if 'money' in pocket:
  pass
else:
  print("Nothing")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
  print("Taxi")
else:
  if card:
    print("Taxi2")
  else:
    print("Walking")

score = 60
message = "success" if score >= 60 else "failure"
print(message)

treeHit = 0
while treeHit < 10: 
  treeHit = treeHit + 1
  print("tree %d" % treeHit)
#  if treeHit == 5: break
  if treeHit == 10:
    print("End of tree")

print("End of treeHit")


#print("=" * 50)
#print("Input")
#inputData = input()
#print(inputData)

## challenge
num=1
while num <= 10:
  if not num % 3 == 0:
    print(num)
  num += 1

## infinite loop
num=1
#while True:
#  print(num)
#  num += 1
#  if num > 100: break


print("=" * 50)
test_list = ['one', 'two', 'three']
for i in test_list:
  print(i)

a = [(1, 2), (3, 4), (5, 6)]
for (first, second) in a:
  print(first, second)

## range
#a = range(10)
#print(a)
#for i in a: print(i)

for i in range(10): print(i)
print("=" * 50)
for i in range(1, 11): print(i)

print("=" * 50)
## challenge
sum = 0
for i in range(1,101): sum += i
print("sum:", sum)

## gugudan
for i in range(1, 10): 
  for j in range(1, 10): 
    print("%d x %d = %d" % (i, j, i*j))
    #print("{0} x {1} = {2}".format(i, j, i) )
  print("=" * 10)

