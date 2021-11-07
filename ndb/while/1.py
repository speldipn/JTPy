
s = []

while True:
    a,b = input().split()
    ia=int(a)
    ib=int(b)
    if(ia == 0 and ib == 0):
        break
    s.append(ia+ib)

for i in range(len(s)):
    print(s[i])

