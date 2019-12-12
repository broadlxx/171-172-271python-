def re(list3):
    global list1
    print(list3)
    for i in range(len(list3)):
        list3[i][i] = 1
    for a in list3:
        print()
        for b in a:
            print(b,end=" ")

def se(list4):
    listse = []
    for i in range(0,3):
        listse1=[]
        for j in range(0,3):
            listse1.append(0)
        listse.append(listse1)

    for i in range(0,3):
        for j in range(0,3):
            if list4[i][j] == 1:
                listse[j][i] = 1

    for i in range(0,3):
        for j in range(0,3):
            if(list4[i][j] == 0 and listse[i][j] == 0):
                list4[i][j] = 0
            else:
                list4[i][j] = 1

    for a in list4:
        print()
        for b in a:
            print(b,end=" ")

def te(list5):
    for i in range(0,3):
        for j in range(0,3):
            if(list5[j][i] == 1):
                for a in range(0,3):
                    list5[j][a]=list5[j][a]|list5[i][a]
    for a in list5:
        print()
        for b in a:
            print(b,end=" ")

list1 = []
list2 = []
for i in range(0,3):
    list2=[]
    for j in range(0,3):
        a = int(input())
        list2.append(a)
    list1.append(list2)
list3 = list1
print("re:")
re(list3)
print()
list4 = list1
print("se:")
se(list4)
list5 = list1
print()
print("te:")
te(list5)
