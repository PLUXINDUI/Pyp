num = [int(s) for s in input('Числа: ').split()]
nums = set()

for num in num:
    if num in nums:
        print("ДА")
    else:
        print("НЕT")
        nums.add(num)