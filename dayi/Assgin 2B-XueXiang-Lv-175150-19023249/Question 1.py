print("Name:XueXiang Lv  Student ID:175150  Massey ID:19023249")
        #Name:XueXiang Lv  Student ID:175150  Massey ID:19023249

moviefile=open("movietitles.txt","r")
line=moviefile.readlines()
def Notempty():
    a=0
    for i in line:
        if i!=None:
            a+=1
    return a
def Numberofwords():
    A=[]
    t=0
    for i in line:
        i=i.replace(","," ")
        i=i.replace("!"," ")
        i=i.replace("?"," ")
        i=i.replace("."," ")
        i=i.replace(":"," ")
        A=i.split()
        del A[-1]
        for j in A:
            t+=1
    return t
def Unique():
    global C,d
    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    m=0
    q=0
    d=0
    for i in line:
        i=i.replace(","," ")
        i=i.replace("!"," ")
        i=i.replace("?"," ")
        i=i.replace("."," ")
        i=i.replace(":"," ")
        A=i.split()
        del A[-1]
        for j in A:
                B.append(j)
    for t in B:
        t=t.lower()
        for w in range(len(B)):
            if (t == B[w].lower()):
                m+=1
        if m==1:
            C.append(t)
            q+=1
            m=0
        else:
            D.append(t)
            m=0
            continue
    E=D
    D=[]
    for e in E:
        if e in D:
            continue
        else:
            d+=1
            D.append(e)
    return q
print("the number of  non-empty lines in the file is: %s"%Notempty())
print("the total number of words in the movie titles is: %s"%Numberofwords())
print("the average number of words per title is: %0.3f"%(Numberofwords()/Notempty()))
print("the number of unique words in the titles is %s"%Unique())
print("the number of duplicate words is %s"%d)
C.sort()
print(C[0:5])
print(C[50:55])
print(C[500:505])
print(C[-5:])
