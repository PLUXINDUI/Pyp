try:
    a = int(input())
    b = int(input())
    print(a/b)
except ValueError:
    print('Ошибка в исходных данных!')
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except:
    print('Фатал систем ерор!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
else:
    print('Ошибок нет насяльнике')
finally:
    print('Все всегда чётенько!')

try:
    print(a)
except NameError:
    print('Ошибка вывода')
print("Hello")