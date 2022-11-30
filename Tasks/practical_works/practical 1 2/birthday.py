import random

def birthday(count:int, iterations=1000) -> str:
    '''
    :param count: количество людей
    :param iterations: количество повторений
    :return: результаты эксперемента
    '''
    days = [day for day in range(0, 364)]

    par: int = 0
    ok: int  = 0

    for it in range(0, iterations + 1):
        day_data = []

        for i in range(0, count+1):
            day_data.append(random.choice(days))

        for i in range(0, count):
            if day_data.count(day_data[i]) == 1:
                ok += 1
                pass

            for k in range(0, count):
                if k == i:
                    pass
                if day_data[k] == day_data[i]:
                    par += 1

    return f'совпадения: {par} ' \
           f'не совпадения: {ok} ' \
           f'вероятность: {(par*100)/ (ok+par)}%'

