posl = 0
col = 0
mx = 0

while (number := int(input("Число: "))) != 0:
    if number == posl:
        col += 1
    else:
        if mx < col:
            mx = col
        col = 1
    posl = number

print(max(mx, col))