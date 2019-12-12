w1=[]
w2=[]
while True:
    a=input("Sentence:")
    a=a.lower()
    a=a.replace(","," ")
    a=a.replace("!"," ")
    a=a.replace("?"," ")
    a=a.replace("."," ")
    a=a.replace(":"," ")
    w1=a.split()
    for e in w1:
        if e in w2:
            continue
        else:
           w2.append(e)
    unique=" ".join(w2)
    print("Unique words:",unique)
    if a=="quit":
        break
    # for q in w2:
    #     print(q,end=" ")
    # print()

