def read_file(filename: str) -> list:
    '''
    :param filename: имя файла, где находиться текст
    :return: списком уникальных слов в нижнем регистре
    '''
    with open(filename, encoding='UTF-8', mode='r') as f:
        words: list = (f.read().split(' '))

    for i in range(0, len(words)):
        words[i] = words[i].lower()
        words[i] = "".join(s for s in words[i] if s.isalpha())

    out: set = set(words)
    return list(out)


def save_file(filename: str, words: list) -> None:
    '''
    :param filename: имя файла, где находиться текст
    :param words: список уникальных слов в нижнем регистре
    '''
    words: list = sorted(words)
    with open(filename, encoding='utf-8', mode='w') as f:
        f.write(f'Количество уникальных слов: ' + str(len(words)) + '\n')
        f.write('\n'.join(words))
