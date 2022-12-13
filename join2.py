string='abcdef'

string=list (string)

print(string)

def my_join(list, separator):
    new_string =''
    for i in list:
        new_string+= i+separator
    return new_string[:-len(separator)]
print(my_join(string,'-_-_-'))