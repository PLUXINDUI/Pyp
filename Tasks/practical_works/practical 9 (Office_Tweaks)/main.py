from functions import *


def start() -> str:
    '''
    Функция отвечает за вызов нужных функций из файла functions
    '''
    while True:
        commands = ['\n''0. Сменить рабочий каталог', '1. Преобразовать PDF в Docx', '2. Преобразовать Docx в PDF',
                    '3. Произвести сжатие изображения', '4. Удалить группу файлов', '5. Выход' '\n']
        list_commands = range(6)
        start_dir = directory()
        print(start_dir, '\nВыберите действие: ', *commands, sep='\n')
        a = int(input('Ваш выбор: '))
        while a not in list_commands:
            a = int(input())
        if a == 0:
            print(change_directory())
        elif a == 1:
            print(P2D())
        elif a == 2:
            print(D2P())
        elif a == 3:
            print(photo())
        elif a == 4:
            menu_delite_file()
        else:
            return '\nРабота программы завершена'


print(start())
