a = {"read": "R", "write": "W", "execute": "X"}
files_list: dict[str, str] = dict([input().split() for i in range(0, int(input('Кол-во файлов: ')))])

for k in range(0, int(input('Кол-во операций: '))):

    operations, filename = input().split()

    if a[operations] in files_list.get(filename, ""):
        print("OK")
    else:
        print("DENIED")
