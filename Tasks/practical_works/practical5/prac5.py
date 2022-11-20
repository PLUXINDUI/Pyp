def f(filename):
    try:
        file = open(filename)
        col = int(file.readline())
        chisl = file.read().splitlines()

        if len(chisl)>col:
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
    finally:
        try:
            file.close()
        except:
            pass