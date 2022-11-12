stroka = input()
dlina=len(stroka)

print(stroka[dlina//2 + dlina%2 :] + stroka[: dlina//2 +dlina%2])
