from Violent import openfile
import time

list,list2 = openfile()
start2 = time.time()
Vlist2 = [i for i in range(1,int(list[0])+1)]
graphlist2 = [[0 for i in range(int(list[0]))] for j in range(int(list[0]))]

for j in list2:
    graphlist2[int(j[0])-1][int(j[1])-1] = 1
    graphlist2[int(j[1])-1][int(j[0])-1] = 1
def Greedy_one_deleteside(Vlist2):
    Vercover = []
    while Vlist2 != []:
        EveryEdge = []
        for i in range(len(graphlist2)):
            sides = 0
            for j in graphlist2[i]:
                if j == 1:
                    sides+=1
            EveryEdge.append(sides)
        maxV = max(EveryEdge)
        if max(EveryEdge) == 0:
            break

        Vercover.append(EveryEdge.index(maxV)+1)
        Vlist2.remove(EveryEdge.index(maxV)+1)

        for j in Vlist2:
            if graphlist2[EveryEdge.index(maxV)][j-1] == 1:
                graphlist2[EveryEdge.index(maxV)][j-1] = 0
                graphlist2[j-1][EveryEdge.index(maxV)] = 0
        # print(graphlist2)
    return  Vercover

GREED = []
print("Vertice cover:",Greedy_one_deleteside(Vlist2))
for i in Vlist2:
    if i not in Greedy_one_deleteside(Vlist2):
        GREED.append(i)
print("First Greedy :",GREED)
end2 = time.time()
print("First Greedy time:",end2-start2,"\n")
