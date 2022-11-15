def f(filename):
    opened = False
    try:
        file = open(filename)
        opened = True
        col = int(file.readline())

        return [int(a) for a in [file.readline() for _ in range(col)]]

    except FileNotFoundError:
        return 'Неправильное имя файла'
    except ValueError:
        return 'Неверное значение'
    except:
        return 'Неопознанная ошибка'
    # finally:
    #     if opened:
    #         file.close()


filename = input('Введите имя файла: ')

f(filename)