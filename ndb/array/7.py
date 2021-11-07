import sys

#f = open("input.txt")
#cn = int(f.readline())
cn = int(sys.stdin.readline())
n = []
s = []
avg = []

def getAverage(s):
    t = 0
    for i in range(len(s)):
        t += int(s[i])
    return t / len(s)

for i in range(cn):
    l = sys.stdin.readline()
    #l = f.readline()
    ls = l.split()[1:]
    n.append(l)
    avg.append(getAverage(ls))

for i in range(len(n)):
    ns = n[i].split()[1:]
    c = 0
    for j in range(len(ns)):
        if int(ns[j]) > avg[i]:
            c += 1
    v = round(c/len(ns) * 100, 3)
    s.append("%.3f%%" % v)

for i in range(len(s)):
    print(s[i])
