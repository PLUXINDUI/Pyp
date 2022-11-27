num = [s for s in input('Числа: ').split()]
nums = []
for i in range(0, len(num) - 1):
    if int(num[i]) < int(num[i + 1]):
        nums.append(num[i + 1])

print(" ".join(nums))