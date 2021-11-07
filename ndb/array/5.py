
import sys

cn = int(sys.stdin.readline().rstrip())
n = []

data = sys.stdin.readline().split()

for i in range(len(data)):
    n.append(int(data[i]))

n.sort()
m = n[len(n)-1]
s = 0
for i in range(len(n)):
    s += (n[i]/m * 100)

print(s/cn)

