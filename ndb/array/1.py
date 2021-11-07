n = int(input())
data = input().split()

nums = []
for i in range(n):
    nums.append(int(data[i]))

print(sorted(nums)[0], sorted(nums)[n-1])
