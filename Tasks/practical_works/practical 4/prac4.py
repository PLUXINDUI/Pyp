def read_file(filename):
    out = {}
    with open(filename, encoding='UTF-8', mode='r') as f:
        words = (f.read().split(' '))

    for i in range(0, len(words)):
        words[i] = words[i].lower()
        words[i] = "".join(s for s in words[i] if s.isalpha())

    out = set(words)

    return list(out)

def save_file(filename, words):
    words = sorted(words)
    with open(filename, encoding='utf-8', mode='w') as f:
        f.write(f'Количество уникальных слов: ' + str(len(words)))
        f.write('\n'.join(words))