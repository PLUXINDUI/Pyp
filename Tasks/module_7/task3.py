dict = {}

col = int(input())

for i in range(0, col):
    name, voices = input().split()

    if name in dict:
        dict[name] = str(int(voices) + int(dict[name]))
    else:
        dict[name] = voices

for name, voices in sorted(dict.items()):
    print(name + ' ' + voices)
