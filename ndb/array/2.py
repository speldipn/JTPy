nums = []
for i in range(9):
    nums.append(int(input()))
m = sorted(nums)[len(nums)-1]
print(m)
print(nums.index(m)+1)
