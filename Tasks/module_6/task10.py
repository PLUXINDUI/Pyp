stroka = input()
word = stroka[:stroka.find('h')]
word += stroka[stroka.rfind('h')+1:]

print(word)