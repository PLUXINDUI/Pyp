def f():
    try:
        a = int(input())
        b = int(input())
        x = a/b
    except:
        return 'Ошибка'
    else:
        return x
    finally:
        print('always')
print(f())