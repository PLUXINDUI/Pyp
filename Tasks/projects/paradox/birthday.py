import random

def birthday(count, iterations=1000):
    days = [day for day in range(0, 364)]

    par = 0
    ok = 0

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
           f'вероятность: {(par*100)/ (ok+par)}'

