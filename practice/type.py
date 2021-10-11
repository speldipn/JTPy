##!/usr/bin/python

## Integer
a = 0x80
print(a)

print(7 / 4)
print(7 // 4)
print(7 % 4)

print(14 // 3)
print(14 % 3)

## String
a = "Hello World"
print(a, len(a))

multiline = """
  Life is too short
  You need pyhton
  """
print(multiline)

head = "Python"
tail = " is fun!"
print(head + tail)

a = 10
print(head * 2)

print("=" * 50)
print("My program")
print("=" * 50)

## problem
print(len("You need python"))

a = "Life is to short, You need Python"
print(a[3])
print(a[0])
print(a[12])
print(a[-1])
print(a[-0])

b = a[0] + a[1] + a[2] + a[3]
print(b)

print(a[0:4])
print(a[19:])
print(a[:17])
print(a[19:-7])

a = "Pithon"
b = a[0] + 'y' +  a[2:]
print(b)

## Using string format
print("I eat %d apples" % 3)
print("%s is %d" % ("Three", 3))
print("Power is %d%%" % 98)
print("%10s is greeting" % "hi")
print("%0.4f" % 3.141592)
print("%10.4f" % 3.141592)
print("I eat {0} apples".format(3))
print("{0} is {1}".format("Three", 3))
print("I ate {number} apples, so I was sick for {day} days".format(number=10, day=3))
print("I ate {0} apples, so I was sick for {day} days".format(10, day=3))
print("{0:<10}".format("hi"))
print("{0:=<10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:=^10}".format("hi"))
print("{0:0.4f}".format(3.141592))
print("{0:10.4f}".format(3.141592))
print("{{ and }}".format())
name = "Hong"
age = 30
##print(f"I'm {name} and {age}")
print("{0:!^12}".format("python"))
##print(f'{"python":!^12}')

a = "hobby"
print(a.count('b'))
print(a.find('b'))
print(a.find('k'))

a = "Life is too short"
print(a.index('t'))
##print(a.index('a')

## split and merging
result = ",".join("abcd")
print(result, type(result))

## Upper and lower
a = "hi"
print(a.upper())
a = "HI"
print(a.lower())

## strip
a = "  hi  "
print(a)
a = " hi "
print(a.lstrip())
a = " hi "
print(a.rstrip())
a = " hi "
print(a.strip())

## replace
a = "Life is too short"
b = a.replace("Life", "Your leg")
print(a, b)

## split
a =  "Life is too short"
b = a.split()
print(b)
print(",".join(b))

