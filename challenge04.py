## Q1
def is_odd(number):
  if number % 2 == 1:
    return True
  else:
    return False

print(3, is_odd(3))
print(4, is_odd(4))

## Q2
def avg_numbers(*numbers):
  result = 0
  for n in numbers:
    result += n
    
  return result / len(numbers)

print(avg_numbers(10, 20, 30))
print(avg_numbers(10, 20, 30, 40))
print(avg_numbers(10, 50))

## Q3
#input1 = int(input("first num:"))
#input2 = int(input("second num:"))

#total = input1 + input2
#print("sum: %d" % total)

## Q4
# 3
print("you""need""python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))

## Q5
#f1 = open("test.txt", "w")
#f1.write("Life is too short")
#f1.close()

#f2 = open("test.txt", "r")
#print(f2.read())
#f2.close()

## Q6
#user_input = input('input:')
#f = open('test.txt', 'a')
#f.write(user_input)
#f.write('\n')
#f.close()

## Q7
f = open('test.txt', 'r')
body = f.read()
f.close

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()


