import sys

nums = []
with open(sys.argv[1]) as f:
    for line in f:
        nums.append([int(x) for x in line.split()][0])
res = round(sum(nums) / len(nums))
a = 0
for i in range(0, len(nums)):
    a += abs(res - nums[i])
if (a > 20):
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
else:
    print(a)
