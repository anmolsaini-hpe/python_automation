
s = ["h","e","l","l","o"]

new_list=[]

for i in s[::-1]:

    new_list.append(f'"{i}"')

s=str(new_list).replace("'","")
print(s)