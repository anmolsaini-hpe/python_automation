list1=[-10, -8, 2, 4, 6]
list2=[ 4, 16, 36, 64, 100]
list3=[]

def data(list1):
    for i in list1:
        j= i*i
        list3.append(j)
    print(sorted(list3))




data(list1)