from typing import List, Tuple


def get_books(name: str) -> List[Tuple[str, str, str, int, float]]:
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
    plusprice: list = []
    for book in books:
        price = book[3] * book[4]
        if price >= 500:
            plusprice.append((book[0], price))
        else:
            plusprice.append((book[0], price + 100))
    return plusprice


print((get_books('python')))
print(get_totals(get_books('python')))
