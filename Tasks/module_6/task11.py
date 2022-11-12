stroka = input()

word = stroka[:stroka.find('h')]
word += stroka[stroka.find('h')+1:stroka.rfind('h')+1][::-1]
word += stroka[stroka.rfind('h'):]

print(word)