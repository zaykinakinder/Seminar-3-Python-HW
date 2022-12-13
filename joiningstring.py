string='abcdef'
print(string)
string=list(string)

print(string)
new_string=[]
for i in range (0,len(string),2):
    new_string.append(string[i]+string[i+1])  
    
    
print (new_string)