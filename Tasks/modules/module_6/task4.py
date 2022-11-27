num = [s for s in input("Числа: ").split()]
max_num = -100000
min_num = 100000
max_index = 0
min_index = 0

for i in range(0, len(num)):
    if int(num[i]) > int(max_num):
        max_num = num[i]
        max_index = i
    if int(num[i]) < int(min_num):
        min_num = num[i]
        min_index = i

num[max_index] = min_num
num[min_index] = max_num

print(" ".join(num))