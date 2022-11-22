import prac4
'''
Вывод уникальных слов в нижнем регистре в алфавитном порядке из файла
'''
print(prac4.read_file('data.txt'))
prac4.save_file('count.txt', prac4.read_file('data.txt'))