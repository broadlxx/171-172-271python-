import operator
inf = float('inf')
mainlist=[[inf,3,inf,7,inf,inf,2,inf,inf],
       [3,inf,3,inf,inf,inf,inf,12,inf],
       [inf,3,inf,5,1,inf,inf,inf,2],
       [7,inf,5,inf,inf,inf,6,inf,inf],
       [inf,inf,1,inf,inf,5,0,4,inf],
       [inf,inf,inf,inf,5,inf,inf,inf,inf],
       [2,inf,inf,6,0,inf,inf,inf,inf],
       [inf,12,inf,inf,4,inf,inf,inf,8],
       [inf,inf,2,inf,inf,inf,inf,8,inf]]

def Two_Verticies_Weight(a,b):
    if (mainlist[a][b] != inf):
        return mainlist[a][b]
    else:
        countlist = []
        count = 0
        for i in range(len(mainlist[a])):
            if(mainlist[a][i] != inf):
                count = count+mainlist[a][i]
                for j in range(len(mainlist[a])):    
                    if(mainlist[i][j] != inf)and(j == b):
                        count = count+mainlist[i][j]
                        countlist.append(count)
                        count = 0
        countlist.sort(reverse = False)
        return countlist[0]

def Find_weight(c):
        verticies = []
        a = []
        #count = 0
        for i in range(len(mainlist)):
            for j in range(len(mainlist)):
                if(mainlist[i][j] == c):
                     verticies.append(i)
                     verticies.append(j)
                     print(verticies,end=" ")
                     verticies = []
        #             count += mainlist[i][j]
        #             if (count == c):
        #                 count = 0
        #                 verticies.append(i)
        #                 verticies.append(j)
        #                 verticies.sort(reverse = False)
        #                 a.append(verticies)

def Find_MaxandMin():
    big = mainlist[0][1]
    small = mainlist[0][1]
    for i in mainlist:
        for j in i:
            if j==inf:
                pass
            else:
                if j >= big:
                    small = j
    return (big,small)

def Find_minverticies():
    min1 = []
    count = 0
    for i in range(len(mainlist)):
        min1.append(count)
        count = 0
        for j in range(len(mainlist)):
            if(mainlist[i][j] != inf):
                count += mainlist[i][j]
    min1.pop(min1[0])
    print(min1.index(min(min1)),"is the minimum verticies.The edge associated weight",min(min1))


def Find_allWeight(d):
    allweight = []
    num = 0
    for i in mainlist[d]:
        if (i == inf):
            num += 1
            pass
        else:
            allweight.append((num,i))
            num += 1
    allweight.sort(key=operator.itemgetter(1))
    return allweight

while True:
    print("\t")
    c = input("Commod:")
    if c.lower()=='a':
        a = int(input("first number"))
        b = int(input("second number"))
        print(Two_Verticies_Weight(a,b))
    elif c.lower() == 'b':
        n = int(input("which weight:"))
        Find_weight(n)
    elif c.lower() == 'c':
       print(Find_MaxandMin())
    elif c.lower() == 'd':
        Find_minverticies()
    elif c.lower() == 'e':
        d = int(input("which number do your want to know all its weight"))
        for i in Find_allWeight(d):
            print(i,end=" ")





