from Violent import openfile
import time

start3 = time.time()
list,list2 = openfile()
graphlist3 = [[0 for i in range(int(list[0]))] for j in range(int(list[0]))]
for j in list2:
    graphlist3[int(j[0])-1][int(j[1])-1] = 1
    graphlist3[int(j[1])-1][int(j[0])-1] = 1
Vlist3 = [i for i in range(1,len(graphlist3)+1)]
def Greedy_tow_deletepoint(Vlist3):
    IndependentSet = []

    while Vlist3 != []:
        EveryPoint = []
        for i in range(len(graphlist3)):
            sides = 0
            for j in graphlist3[i]:
                if j == 1:
                    sides+=1
            EveryPoint.append(sides)
        maxP = max(EveryPoint)
        if max(EveryPoint) == 0:
            break

        IndependentSet.append(EveryPoint.index(maxP)+1)
        Vlist3.remove(EveryPoint.index(maxP)+1)
        points = [EveryPoint.index(maxP)]
        for i in range(len(graphlist3)):
            if graphlist3[EveryPoint.index(maxP)][i] == 1:
                points.append(i)
        for i in range(len(graphlist3)):
            for j in points:
                if graphlist3[j][i] == 1:
                    graphlist3[j][i] = 0
    return IndependentSet

print("Second Greedy:",Greedy_tow_deletepoint(Vlist3))
end3 = time.time()
print("Second Greedy time:",end3-start3,"\n")
