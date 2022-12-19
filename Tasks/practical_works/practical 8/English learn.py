import operator
from typing import Any, Dict

import pymorphy2
import translate

morph = pymorphy2.MorphAnalyzer()
en_translator = translate.Translator(from_lang='ru', to_lang='en')


def get_english_phrasebook(file_name: str) -> None:
    '''
    :param file_name:
    :return:
    '''
    with open(file_name, encoding='utf-8') as file:
        list = file.read().split()
        write_dict_to_file('ru+eng.txt', get_sorted_dict(normalize_words_list(list)))


def write_dict_to_file(file_name: str, book: dict) -> None:
    '''
    :param file_name:
    :param book:
    :return:
    '''
    with open(file_name, encoding='utf-8', mode='w') as file:
        for word in book:
            if len(word) > 1 or word.lower() == 'я':
                file.write(f'{word} | {en_translator.translate(word)} | {book[word]}\n')


def get_sorted_dict(words: list) -> Dict[Any, Any]:
    '''
    :param words:
    :return:
    '''
    output = {}
    for word in words:
        output[word] = str(words.count(word))
    return dict(sorted(output.items(), key=operator.itemgetter(1), reverse=True))


def normalize_words_list(words_list: list) -> list:
    '''
    :param words_list:
    :return:
    '''
    for i in range(0, len(words_list)):
        words_list[i] = "".join(a for a in words_list[i] if a.isalpha())
        words_list[i] = get_normal_form(words_list[i])
    return words_list


def get_normal_form(word: str) -> str:
    '''
    :param word: слово из текста
    :return: слово, приведенное в начальную форму или инфинитив
    '''
    return morph.parse(word)[0].normal_form


get_english_phrasebook('ru.txt')