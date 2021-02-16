a = 1
b = "python"
c = 'neo'
d = [1,2,3]
e = 'a' # string

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))

print("id(a)",id(a))
print("id(b)",id(b))
print("id(c)",id(c))
print("id(d)",id(d))
print("id(e)",id(e))

print("d[0]", id(d[0]))
print("d[1]", id(d[1]))
print("d[2]", id(d[2]))

a = [1,2,3]
b = a
print(a, b)
print(id(a), id(b))
print(id(a) == id(b))
a[0] = 10
print(a, b)

## slicing
print("=" * 50)
a = [1,2,3]
b = a[:]
c = a
print("b", b)
a[1] = 4
print("a", a)
print("b", b)
print("c", c)
print(id(a), id(b), id(c))
print("a == c", id(a) == id(c))
print("a == b", id(a) == id(b))
print("b == c", id(b) == id(c))

## copy
from copy import copy
print("=" * 50)
a = [1,2,3]
b = copy(a) # equal to b=a[:]
c = a
print(a, id(a))
print(b, id(b))
print(b is a)
print(c is a)

# declare multiple variables
a, b = ('python', 'life')
print(a, type(a), b, type(b))
# tuple
c = (a, b) = 'python', 'life'
print(a, type(a), b, type(b))
print(c, type(c))
# list
c = [a,b] = ['python', 'life']
print(a, type(a), b, type(b))
print(c, type(c))
a = b = 'python'
print(a, type(a), b, type(b))

# swap variables
print("=" * 50)
a = 3
b = 5
print(a,b)
a, b = b, a
print(a,b)

# challenge
a = [1,2,3]
b = [1,2,3]
print(a is b)
print(id(a), id(b))
