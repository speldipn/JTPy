a,b = input().split()
ia = int(a)
ib = int(b)

h = 0
m = 0

down = (ib - 45) < 0
if down:
    h = (ia - 1)%24
    m = abs((ib - 45) % 60)
else:
    h = ia
    m = ib - 45

print(h, m)

