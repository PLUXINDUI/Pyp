a = input('')
if a.count('f')==1:
    print(a.find('f'))
elif a.count('f')>1:
    print(a.find('f'), a.rindex('f'))
else:
    print(-1)