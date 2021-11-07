import sys

cn = int(sys.stdin.readline().rstrip())
n = []
s = []

def getScore(s):
    t = 0
    s1 = 0
    for i in range(len(s)):
        if s[i] == "O":
            s1 += 1
        else:
            s1 = 0
        t += s1
    return t

for i in range(cn):
    n.append(sys.stdin.readline().rstrip())

for i in range(len(n)):
    s.append(getScore(n[i]))

for i in range(len(s)):
    print(s[i])


