#!/usr/bin/python

odd = [1, 3, 5, 7, 9]
print(odd)

a = []
print(a)
b = [1, 2, 3]
print(b)
c = ["Life", "is", "too", "short"]
print(c)
d = [1, 2, "Life", "is"]
print(d)
e = [1, 2, ["Life", "is"]]
print e
print e[2], e[2][0], e[2][1]

a = [1, 2, 3, 4, 5]
print a[0:2]

## problem
print a[1:3]

## sum
a = [1, 2, 3]
b = [4, 5, 6]
print a + b

## multiple
print a * 3

## length
print len(a)

## problem
print "{0} {1}".format(a[2], "hi")
print "%d %s" % (a[2], "hi")
print str(a[2]) + " hi"

a = [1, 2, 3]
print a
del a[:2]
print a
a.append(1)
print a
a.append(2)
print a

## sort
a.sort()
print a

a = ['c', 'b', 'a']
print a
a.sort()
print a

## reverse
a.reverse()
print a

print a.index('a')
print a.index('c')

## insert
a.insert(1, 'd')
print a

a.remove('d')
print a

a = [1, 2, 3, 4, 5]
print a

print(a.pop())
print(a, len(a))
print a.count(3)
b = [6, 7, 8]
#a.extend(b)
a += b
print a, len(a)


