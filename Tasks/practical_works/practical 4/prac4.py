def read_file(data):
    itext={}
    with open(data, encoding='utf-8') as file:
        c = file.read().split(' ')
        for i in range(0, len(c)):
            c[i]=c[i].lower()

        otext=set(c)
        return(otext)

print(read_file(data))


    # words = read_file('data.txt')