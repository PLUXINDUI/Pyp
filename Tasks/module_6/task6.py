num1 = [s for s in input('Числа: ').split()]
num2 = [s for s in input('Числа: ').split()]
nums = []

for i in range(0, len(num1)):
    for k in range(0,len(num2)):
        if num1[i]==num2[k]:
            nums.append(num1[i])
print(" ".join(nums))