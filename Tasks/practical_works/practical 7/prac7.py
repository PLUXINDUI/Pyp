from typing import List, Tuple


def get_books(name: str) -> List[Tuple[str, str, str, int, float]]:
    '''
    Функция находит и составляет лист из книг из файла по кодовым словам
    :param name: название или часть названия книги
    :return: список книг, которые подошли по названию, и все их характеристики
    '''
    books: list = []
    name: str = name.lower()
    with open('books.csv', "r", encoding='utf-8') as f:
        f.readline()
        for line in f:
            isbn, title, author, quantity, price = line.strip().split("|")
            if name in title.lower():
                books.append((isbn, title, author, int(quantity), float(price)))
    return books


def get_totals(books: List[Tuple[str, str, str, int, float]]) -> List[Tuple[str, float]]:
    '''
    К книгам, чья общая цена меньше 500, функция прибаляет 100
    :param books: список книг из прошлой функции
    :return: список из номера книги и обновленной цены
    '''
    plusprice: list = []
    for book in books:
        price = book[3] * book[4]
        if price >= 500:
            plusprice.append((book[0], price))
        else:
            plusprice.append((book[0], price + 100))
    return plusprice


print(get_books('python'))
print(get_totals(get_books('python')))
