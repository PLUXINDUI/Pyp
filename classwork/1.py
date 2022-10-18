def f(*args, **kwargs):
    for i in args:
        print(i)
    for i, v in kwargs.items():
        print(i,'=',v)
f(1,76,4,7,4, k=4, l=7)