a = int(input())
answer = ''
i = 1
while i ** 2 <= a:
    answer += str(i ** 2) + ' '
    i += 1

print(answer)