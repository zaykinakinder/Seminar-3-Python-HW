my_list = ['yjgvytu87678', 'guyhkvuk9877','jgygu678','jgkuf7']
number = input('insert number: ')

for item in my_list:
    for char in item:
         if char == number:
             print (f'Символ {number} присутствует в строке {item}')
             break 
else:
             print (f'Символ {number} не присутствует в строке {item}')
           