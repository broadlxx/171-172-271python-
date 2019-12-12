
start = int(input("A start value:"))
for i in range(start):
    if i == 0:
        for j in range(start * 2):
            print("*",end = '')
    elif i == start:
        for j in range(start * 2):
            print("*",end = '')
    else:
        print("*",end = '')
        for k in range(start * 2):
            print(" ",end = '')
        print("*")


start = int(input("A start value:"))
if start%2==0:
    start = start+1
else:
    for i in range(start):
        if i%2==0:
             for i in range(start*2):
                 print(" ",end="")
             print()
        else :
            continue
        for j in range(start*2):
             print("○",end="")


A = int(input("Line:"))
for i in range(A):
    for j in range(i):
        print(A,end=" ")
        A+=1
    print()
