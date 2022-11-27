list = []
iter = 0

col = int(input())

for i in range(0,col):
    words = input().split()

    for k in words:
        list.append(k)

list = sorted(list)

for slovo in list:
    if list.count(slovo) > iter:
        a = slovo
        iter = list .count(slovo)

print(a)
