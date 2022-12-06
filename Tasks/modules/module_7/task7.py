from typing import Dict

slova: Dict[str, str] = {}

for i in range(0, int(input('Количество строк со словами: '))):
    for words in input().split():
        slova[words] = slova.get(words, 0) + 1

for key in sorted(slova, key=slova.get, reverse=True):
    print(key, slova[key])
