import random

size = int(input('Ввелите размер списка:'))
my_list = [round(random.uniform(0,10),3) for _ in range(size)]#uniform - числа с дробью randint - целые числы
print(f'Сгенирированный список: {my_list}')

devine =list(map(lambda x: x%1, my_list))
devine =list(map(lambda x: round(x,3), devine))
print(f'Разница между максимальной и минимальной дробными частями {max(devine)-min(devine)}')
