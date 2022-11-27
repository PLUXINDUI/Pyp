num = [int(s) for s in input('Числа: ').split()]
count = len(num)

for i in range(0, count - 1,2):
    print(num[i+1], num[i])

if count % 2 != 0:
    print(num[count-1])