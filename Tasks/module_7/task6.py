goroda: dict[str, str] = {}

for i in range(0, int(input('Страны и их города: '))):
    cities = input().split()
    for city in cities[1:]:
        goroda[city]= cities[0]

cities_list = []

for l in range(0, int(input('Поиск городов: '))):
    cities_list.append(goroda.get(input()))

print(' '.join(cities_list))
