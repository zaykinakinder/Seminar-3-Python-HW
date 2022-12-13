my_list=['123','i12390hfiysvb','ughsvijn9872342','leiguhsbv982374er']
number = input('insert number: ')
count = 0
print(my_list)
for i in range (len(my_list)):
    if my_list[i] == number:
        count += 1
    if count ==2:
        print (f'Символ {number}, присутствует в строке {i}')
        break
else:
    if count == 1:
         print (f'Искомое значение {number}, не повторяе')
    else:
         print(f'Искомое значение {number} не найден')