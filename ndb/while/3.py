n = int(input())

c = 0
n1 = n
while True:
   n2 = int(n1 / 10) + (n1 % 10)
   n3 = (n1 % 10) * 10 + (n2 % 10)
   c += 1
   if(n == n3):
       break
   n1 = n3

print(c)
