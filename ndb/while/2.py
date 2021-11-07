
s = []

def isOut(a):
    if(a > 0 and a < 10):
        return False
    else:
        return True

while True:
    try:
        a,b = input().split()
    except:
        break

    ia=int(a)
    ib=int(b)
    if(isOut(ia) or isOut(ib)):
        break

    s.append(ia+ib)

for i in range(len(s)):
    print(s[i])

