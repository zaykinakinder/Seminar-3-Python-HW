text = ['Первое число - 1, второе число - 2, сумма 3 чи']
sub_text =input ('Введите подстроку:')
count = 0
for i in range (len(text)):
    if text [i:i+len(sub_text)]== sub_text:
        count+=1
        
print(f'Подстрока {sub_text} встречается в заданном текстк {count} раз')
print(text.coun
