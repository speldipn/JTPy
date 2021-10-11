## problem1
subjects = {"국어" : 80, "영어": 75, "수학": 55}
sum = 0
for score in subjects.values():
  sum += score
print(sum / len(subjects))

## problem2
num=13
if(num%2==0):
  print("짝수")
else:
  print("홀수")

## problem3
pin = "881120-1068234"
yymmdd = pin[:6]
num = pin[7:]
print(yymmdd, num)

## problem4
pin = "881120-1068234"
if(pin[7] == 1):
  print("men")
else:
  print("woman")

## problem5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)
b = a.split(":")
print("#".join(b))

## problem6
a = [1,3,5,4,2]
a.sort()
print(a)
a.reverse()
print(a)

## problem7
a = ['Life', 'is', 'too', 'short']
result = "%s %s %s %s" %(a[0], a[1], a[2], a[3])
result2 = "{0} {1} {2} {3}".format(a[0], a[1], a[2], a[3])
result3 = " ".join(a)
print("result ", result, type(result))
print("result2", result2, type(result2))
print("result3", result3, type(result3))

## problem8
a = (1,2,3)
a = a + (4,)
print(a)

## problem9
# 3
# Don't use list type as key that was changed by user

## problem10
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

## problem11
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
print(aSet)
b = list(aSet)
print(b, type(b))

## problem12
a = b = [1,2,3]
print(a, b)
a[1] = 4
print(a, b)
print(a is b)
