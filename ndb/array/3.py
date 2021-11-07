n = 1

for i in range(3):
    n *= int(input())

r = [0,0,0,0,0,0,0,0,0,0]
c = 0
while n > 0:
    r[int(n%10)] += 1
    n = int(n / 10)
    c += 1

for i in range(len(r)):
    print(r[i])
