import random
import time

def openfile():

    filenum = random.randint(1,12)
    file = "testgraph" + str(filenum) + ".txt"
    print(file)
    f = open(file,"r")
    # print("testgraph11.txt")
    # f = open("testgraph11.txt","r")
    list = f.read()
    list = list.split("\n")
    for i in list:
        if i == '':
            list.remove(i)
    list2 = []
    for i in list[2:len(list)]:
        x = i.split()
        if x!=[]:
            list2.append(x)
    return list,list2

list,list2 = openfile()
start1 = time.time()
Vlist = [i for i in range(1,int(list[0])+1)]
graphlist = [[0 for i in range(int(list[0]))] for j in range(int(list[0]))]
for j in list2:
    graphlist[int(j[0])-1][int(j[1])-1] = 1
    graphlist[int(j[1])-1][int(j[0])-1] = 1
for a in range(int(list[0])):
    graphlist[a][a] = 1
# def MaxInd(Vlist):
#     stepcount=0
#     max=MaxIndependent(Vlist)
#     while(stepcount<int(list[0])):
#         result=MaxIndependent(Vlist)
#         if len(result)>len(max):
#             max=result
#         else:
#             pass
#         stepcount+=1
#     return (max)
def MaxIndependent(Vlist):
    if len(Vlist)==0:
        return None
    chooseV=random.choice(Vlist)
    possiblelist1=[]
    possiblelist2=[]
    for i in Vlist:
        if i!=chooseV:
            possiblelist2.append(i)
    for i in Vlist:
        if graphlist[chooseV-1][i-1]==1:
            pass
        else:
            possiblelist1.append(i)
    chooseVlist=[]
    chooseVlist.append(chooseV)

    value=MaxIndependent(possiblelist1)
    if value!=None:
        choicelist=value+chooseVlist
    else:
        choicelist=chooseVlist
    notchoicelist=MaxIndependent(possiblelist2)

    if choicelist!=None and notchoicelist!=None:
        if len(choicelist)>len(notchoicelist):
            return choicelist
        else:
            return notchoicelist
    if choicelist != None and notchoicelist == None:
        return choicelist

print("Violent solution:",MaxIndependent(Vlist))
end1 = time.time()
print("Violent solution time:",end1-start1,"\n")





