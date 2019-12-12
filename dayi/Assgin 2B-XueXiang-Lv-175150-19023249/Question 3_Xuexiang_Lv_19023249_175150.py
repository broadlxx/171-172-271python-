print("Name:XueXiang Lv  Student ID:175150  Massey ID:19023249")
        #Name:XueXiang Lv  Student ID:175150  Massey ID:19023249

ste=[]
filename=input("")
def add(): #this function is add some words
    while True:
        a=input(">")
        if a!="#":
            ste.append(a)
        else:
            break
def delete():#This function is delete a word
    global ste
    A=[]
    n1=int(input("What line do you want to modify?"))
    n2=int(input("What words do you want to delete in this line?"))
    if n1>len(ste):
            print("too height")
    for i in range(len(ste)):
        if i==n1-1:
            A=ste[i].split()
            del A[n2-1]
        ste[n1].append(A)
def replace():   #This function is replace one of rows
    global ste
    n1=int(input("What line do you want to modify?"))
    if n1>len(ste):
            return "too height"
    for i in range(len(ste)):
        if i==n1-1:
            A=input("Replacement   :")
            ste[i]=A
def find():   #This function is replace one of the words in a row
    global ste
    a=input("Find string :")
    b=input("Replace with:")
    for i in range(len(ste)):
        if a in ste[i]:
            ste[i]=ste[i].replace(a,b)
def Clear():   #This function is clear one lines
    global ste
    n=int(input("What line do you want to delete?"))
    for i in range(len(ste)):
        if i==n-1:
            del ste[i]
def Save():   #This function is save into a file
    file=open(filename,"w")
    for i in ste:
        file.write("%s\n"%i)
print("*** TinyEd commands ***")
while True:
    if ste==[]:
        print("")
    else:
        for i in range(len(ste)):
            print("%s ) %s"%(i+1,ste[i]))

    print("a   Add - Start adding lines. A single # on a line by itself exits add. ")
    print("d   Delete a numbered line ")
    print("r   replace a line ")
    print("f   Find & replace a string ")
    print("c   Clear ")
    print("s   Save ")
    print("q   Quit")
    choice=input(":")
    if choice=="a":
        add()
    elif choice=="d":
        delete()
    elif choice=="r":
        replace()
    elif choice=="f":
        find()
    elif choice=="c":
        Clear()
    elif choice=="s":
        Save()
    elif choice=="q":
        break
    else:
        continue
