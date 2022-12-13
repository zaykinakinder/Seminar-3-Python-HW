my_list=['kehbgi','i12390hfiysvb','ughsvijn9872342','leiguhsbv982374er']
symbol = input ('Введедите символ: ')

print (my_list)
for i in range (len(my_list)):
    my_list[i]=my_list[i].replace(f'{symbol}','A')
    
print(my_list)