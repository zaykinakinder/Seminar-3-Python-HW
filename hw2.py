import random 

size = int(input('Введите размер списка:'))
my_list = [random.randint(0,10)for _ in range (size)]
print(my_list)

if size%2==0:
    center = int(len(my_list)/2)
else:
    center = int(len(my_list)/2)
new_list= []
for i in range (center):
    new_list.append(my_list[i]*my_list[len(my_list)-1-i])
    
print(new_list)    