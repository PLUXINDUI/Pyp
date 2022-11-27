words = input().split(' ')
stroka = ""

for word in words:
    print(stroka.count(word), end = " ")
    stroka += word