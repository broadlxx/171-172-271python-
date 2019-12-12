start = int(input("A start value:"))
if start%2==0:
    start = start+1
    for i in range(start):
        if (i==0)or(i==start-1):
             for j in range(start*2):
                print("○",end="\t")
        elif (i+1)%2==0:
            print()
        else:
            print("○",end="\t")
            for t in range(start-1):
                print("\t",end="\t")
            print("○")
        print()
else:
    for i in range(start):
        if (i==0)or(i==start*2-1):
             for j in range(start*2):
                print("○",end="\t")
        elif (i+1)%2==0:
                 print()
        else:
            print("○",end="\t")
            for t in range(start-1):
                print("\t",end="\t")
            print("○")
        print()

