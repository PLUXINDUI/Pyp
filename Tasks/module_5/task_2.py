a = int(input())
n = 0

while 2 ** (n + 1) <= a:
    n += 1

print(n, 2 ** n)