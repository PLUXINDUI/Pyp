from manager import locked_symbol


def lock_word(word: str) -> str:
    '''
    :param word: незашифрованное слово
    :return: зашифрованное слово
    '''
    word_list: list = [a for a in word]
    output: str = ''

    for i in range(0, len(word)):
        word_list[i] = locked_symbol

    return output.join(word_list)


def unlock_part_of_word(unlocked_word: str, locked_word: str, part: str) -> str:
    '''
    :param unlocked_word: незашифрованное слово
    :param locked_word: зашифрованное слово с котрытми частями
    :param part: буква, которую нужно открыть
    :return: слово после открытия буквы
    '''
    all_part_indexs: list = []

    locked_word_list: list = [a for a in locked_word]
    output: str = ''

    for i in range(0, len(unlocked_word)):
        if unlocked_word[i] == part:
            all_part_indexs.append(i)

    for j in all_part_indexs:
        locked_word_list[j] = part

    return output.join(locked_word_list)