import random

def hall(iterations: int) -> str:
    '''
    :param iterations: количество итерация для определения парадокса
    :return: результат эскперемент
    '''
    count:int = 0
    count_changed_choice:int = 0

    for i in range(0, iterations):
        a = [0, 0, 1]
        player_choice: int = random.choice(a)
        if player_choice == 1:
            count += 1
        else:
            a.remove(0)
            a.remove(player_choice)
            if a[0] == 1:
                count_changed_choice += 1
    return f'не меняя выбор:{count} меняя выбор:{count_changed_choice} вероятность выигрыша '\
           f'со своим выбором: {(count*100)/ (count + count_changed_choice)} %'