n=int(input('Введите число:'))
my_list=[1,0,1]
for i in range (2, n+2):
    my_list.append(my_list[i-1]+my_list[i])
for i in range (n):
    my_list.insert(0, my_list[1]-my_list[0])
print (my_list)
