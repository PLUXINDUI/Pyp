from typing import Union


def f(filename) -> Union[list, str]:
    '''
    :param filename: имя файла
    :return: список чисел
    '''
    try:
        file = open(filename)
        col: int = int(file.readline())
        chisl: list = file.read().splitlines()

        if len(chisl) > col:
            raise Exception('Неправильное количество чисел')
        chisl = [int(chisl[a]) for a in range(0, col)]

        return chisl
    except FileNotFoundError:
        return 'Неправильное имя файла'
    except ValueError:
        return 'Неверное значение'
    except Exception as osh:
        return str(osh)
    except:
        return 'Неизвестная ошибка'
