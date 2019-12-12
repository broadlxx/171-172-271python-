A = int(input("The start value:"))
B = int(input("The end value:"))
L=1
count=0
for i in range(A,B+1):
    print(i,end=" ")
    count+=1
    if (L==count):
        print()
        L+=1
        count=0
    else:
        continue


A = int(input("Line:"))
for i in range(A):
    for j in range(i):
        print(A,end="\t")
        A+=1
    print()
