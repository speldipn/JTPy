n = int(input())

s = []

for i in range(n):
    a,b = input().split()
    ia = int(a)
    ib = int(b)
    s.append("Case #%d: %d + %d = %d" % (i+1, ia, ib, ia+ib))

for i in range(len(s)):
    print(s[i])
