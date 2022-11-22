import random

locked_symbol: str = '\u25A0'
heart_symbol: str = '\u2764'

current_session_record: int = 0
record: int = 0

with open('record.txt', encoding='UTF-8') as db:
    record = int(db.read())

words_list: list = []
with open('words.txt', encoding='UTF-8') as db:
    words_list = db.read().splitlines()


def get_random_word() -> str:
    '''
    :return: случайно слово из базы данных
    '''
    word: str = random.choice(words_list)
    words_list.remove(word)
    return word


def update_record() -> None:
    '''
    Обновляет рекорд
    '''
    with open('record.txt', encoding='UTF-8', mode='w') as db:
        db.write(str(record))