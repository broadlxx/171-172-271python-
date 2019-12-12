from building import *

# speed test - use "python optimizer.py" to run
if __name__ == "__main__":
    import timeit
    test_size = 20 # set to 100 to check time for speed race
    t1 = timeit.repeat(stmt="optimizer.max_food(b)", setup="import gc, building, optimizer; b = building.random_building({0}, True); gc.collect()".format(test_size), repeat=3, number=1)
    t2 = timeit.repeat(stmt="optimizer.max_supplies(b)", setup="import gc, building, optimizer; b = building.random_building({0}, False); gc.collect()".format(test_size), repeat=3, number=1)
    # some calculation that takes ~1 sec on my machine
    tref = timeit.repeat(stmt="for i in range(1000000): a=i^2", setup="import gc; gc.collect()", repeat=3, number=19)
    print("max_food(n={0}) = {1} ({3} normalized), max_supplies(n={0}) = {2} ({4} normalized)".format(test_size, min(t1), min(t2), min(t1) / min(tref), min(t2) / min(tref)))

def max_food(building: Building) -> int:
    allfood=[]
    for i in building.rooms:
        row=[]
        for j in i:
            row.append(j.food)
        allfood.append(row)
        # print(row)
    n=len(allfood)
    origin=int((n+1)/2-1)
    # print("---------------------")

    for bone in range(0,origin): #Initialization skeleton
        allfood[origin][origin+bone+1] += allfood[origin][origin+bone]
        allfood[origin+bone+1][origin] += allfood[origin+bone][origin]
        allfood[origin][origin-bone-1] += allfood[origin][origin-bone]
        allfood[origin-bone-1][origin] += allfood[origin-bone][origin]
    for s in range(1,origin+1):
        allfood[origin+s][origin+s] += max(allfood[origin+s][origin+s-1],allfood[origin+s-1][origin+s])
        allfood[origin+s][origin-s] += max(allfood[origin+s][origin-s+1],allfood[origin+s-1][origin-s])
        allfood[origin-s][origin+s] += max(allfood[origin-s][origin+s-1],allfood[origin-s+1][origin+s])
        allfood[origin-s][origin-s] += max(allfood[origin-s][origin-s+1],allfood[origin-s+1][origin-s])
        for r in range(1,origin-s+1):
            allfood[origin+s][origin+s+r] += max(allfood[origin+s-1][origin+s+r],allfood[origin+s][origin+s+r-1])
            allfood[origin+s+r][origin+s] += max(allfood[origin+s+r-1][origin+s],allfood[origin+s+r][origin+s-1])
            allfood[origin+s][origin-s-r] += max(allfood[origin+s-1][origin-s-r],allfood[origin+s][origin-s-r+1])
            allfood[origin+s+r][origin-s] += max(allfood[origin+s+r-1][origin-s],allfood[origin+s+r][origin-s+1])
            allfood[origin-s][origin+s+r] += max(allfood[origin-s+1][origin+s+r],allfood[origin-s][origin+s+r-1])
            allfood[origin-s-r][origin+s] += max(allfood[origin-s-r+1][origin+s],allfood[origin-s-r][origin+s-1])
            allfood[origin-s][origin-s-r] += max(allfood[origin-s+1][origin-s-r],allfood[origin-s][origin-s-r+1])
            allfood[origin-s-r][origin-s] += max(allfood[origin-s-r+1][origin-s],allfood[origin-s-r][origin-s+1])

    maxfood = max(allfood[0][0],allfood[n-1][0],allfood[0][n-1],allfood[n-1][n-1])
    # print("-------------------------------")

    """returns the maximum number of food that can be collected from given building"""
    return maxfood# dummy implementation - replace

def max_supplies(building: Building) -> int:
    allsupply = []
    supply_choose = []
    for i in building.rooms:# Add all data to the list
        supply = []
        for j in i:
            foodandwater = []
            room = []
            foodandwater.append(j.food)
            foodandwater.append(j.water)
            room.append(foodandwater)
            supply.append(room)
        allsupply.append(supply)
    sizenum = len(allsupply)
    origin = int(building.size)
    for bone in range(1, origin+1):
        allsupply[origin][origin+bone][0][0] += allsupply[origin][origin+bone-1][0][0]
        allsupply[origin][origin+bone][0][1] += allsupply[origin][origin+bone-1][0][1]
        allsupply[origin+bone][origin][0][0] += allsupply[origin+bone-1][origin][0][0]
        allsupply[origin+bone][origin][0][1] += allsupply[origin+bone-1][origin][0][1]
        allsupply[origin][origin-bone][0][0] += allsupply[origin][origin-bone+1][0][0]
        allsupply[origin][origin-bone][0][0] += allsupply[origin][origin-bone+1][0][0]
        allsupply[origin-bone][origin][0][0] += allsupply[origin-bone+1][origin][0][0]
        allsupply[origin-bone][origin][0][0] += allsupply[origin-bone+1][origin][0][0]
# In the Delta Quadrant
    for i in range(1,origin+1): #
        Drowlist=allsupply[origin+i-1][origin+i]#Points on the diagonal line
        Dcollist=allsupply[origin+i][origin+i-1]
        Drowlist1=Drowlist#Cloning a list of adjacent lattices
        Dcollist1=Dcollist
        for Di in Drowlist:#Remove duplicate and smaller data
            for Dj in Dcollist:
                if Di[0]>=Dj[0] and Di[1]>=Dj[1]:
                    if Dj in Dcollist1:
                        Dcollist1.remove(Dj)
                elif Di[0]<=Dj[0] and Di[1]<=Dj[1]:
                    if Di in Drowlist1:
                        Drowlist1.remove(Di)
        Dp1 =  Drowlist1+Dcollist1
        Dcopy1=[]
        for x in Dp1:
            #Data summation
            Dcopy1.append([x[0] + allsupply[origin+i][origin+i][0][0], x[1] + allsupply[origin+i][origin+i][0][1]])
        allsupply[origin+i][origin+i] = Dcopy1#Update this room list
        for j in range(1,origin-i+1):#The point next to the diagonal
            Drowlist2 = allsupply[origin+i-1][origin+i+j]#
            Dcollist2 = allsupply[origin+i][origin+i+j-1]
            Drowlist3 = Drowlist2#clone
            Dcollist3 = Dcollist2
            for Di in Drowlist2:
                for Dj in Dcollist2:
                    if Di[0]>=Dj[0] and Di[1]>=Dj[1]:
                        if Dj in Dcollist3:
                            Dcollist3.remove(Dj)
                    elif Di[0]<=Dj[0] and Di[1]<=Dj[1]:
                        if Di in Drowlist3:
                            Drowlist3.remove(Di)
            Dp2 = Drowlist3+Dcollist3
            Dcopy2 = []
            for y in Dp2:
                Dcopy2.append([y[0]+allsupply[origin+i][origin+i+j][0][0],y[1]+allsupply[origin+i][origin+i+j][0][1]])
            allsupply[origin+i][origin+i+j] = Dcopy2
            Drowlist4 = allsupply[origin+i+j-1][origin+i]
            Dcollist4 = allsupply[origin+i+j][origin+i-1]
            Dcollist5 = Dcollist4
            Drowlist5 = Drowlist4
            for Di in Drowlist4:
                for Dj in Dcollist4:
                    if Di[0]>=Dj[0] and Di[1]>=Dj[1]:
                        if Dj in Dcollist5:
                            Dcollist5.remove(Dj)
                    elif Di[0]<=Dj[0] and Di[1]<=Dj[1]:
                        if Di in Drowlist5:
                            Drowlist5.remove(Di)
            Dp3 = Dcollist5+Drowlist5
            Dcopy3 = []
            for z in Dp3:
                Dcopy3.append([z[0] + allsupply[origin+i+j][origin+i][0][0], z[1] + allsupply[origin+i+j][origin+i] [0][1]])
            allsupply[origin+i+j][origin+i] = Dcopy3
# In the first quatarnt
    for i in range(1,origin+1):
        Frowlist=allsupply[origin-i+1][origin+i]
        Fcollist=allsupply[origin-i][origin+i-1]
        Frowlist1=Frowlist
        Fcollist1=Fcollist
        for Fi in Frowlist:
            for Fj in Fcollist:
                if Fi[0]>=Fj[0] and Fi[1]>=Fj[1]:
                    if Fj in Fcollist1:
                        Fcollist1.remove(Fj)
                elif Fi[0]<=Fj[0] and Fi[1]<=Fj[1]:
                    if Fi in Frowlist1:
                        Frowlist1.remove(Fi)
        Fp1 =  Frowlist1+Fcollist1
        Fcopy1=[]
        for x in Fp1:
            Fcopy1.append([x[0] + allsupply[origin-i][origin+i][0][0], x[1] + allsupply[origin-i][origin+i][0][1]])
        allsupply[origin-i][origin+i] = Fcopy1
        for j in range(1,origin-i+1):
            Frowlist2 = allsupply[origin-i+1][origin+i+j]
            Fcollist2 = allsupply[origin-i][origin+i+j-1]
            Frowlist3 = Frowlist2
            Fcollist3 = Fcollist2
            for Fi in Frowlist2:
                for Fj in Fcollist2:
                    if Fi[0]>=Fj[0] and Fi[1]>=Fj[1]:
                        if Fj in Fcollist3:
                            Fcollist3.remove(Fj)
                    elif Fi[0]<=Fj[0] and Fi[1]<=Fj[1]:
                        if Fi in Frowlist3:
                            Frowlist3.remove(Fi)
            Fp2 = Fcollist3 + Frowlist3
            Fcopy2 = []
            for y in Fp2:
                Fcopy2.append([y[0]+allsupply[origin-i][origin+i+j][0][0],y[1]+allsupply[origin-i][origin+i+j][0][1]])
            allsupply[origin-i][origin+i+j] = Fcopy2
            Frowlist4 = allsupply[origin-i-j+1][origin+i]
            Fcollist4 = allsupply[origin-i-j][origin+i-1]
            Fcollist5 = Fcollist4
            Frowlist5 = Frowlist4
            for Fi in Frowlist4:
                for Fj in Fcollist4:
                    if Fi[0]>=Fj[0] and Fi[1]>=Fj[1]:
                        if Fj in Fcollist5:
                            Fcollist5.remove(Fj)
                    elif Fi[0]<=Fj[0] and Fi[1]<=Fj[1]:
                        if Fi in Frowlist5:
                            Frowlist5.remove(Fi)
            Fp3 = Fcollist5+Frowlist5
            Fcopy3 = []
            for z in Fp3:
                Fcopy3.append([z[0] + allsupply[origin-i-j][origin+i][0][0], z[1] + allsupply[origin-i-j][origin+i] [0][1]])
            allsupply[origin-i-j][origin+i] = Fcopy3
# In the second quatarnt
    for i in range(1,origin+1):
        Srowlist = allsupply[origin-i+1][origin-i]
        Scollist = allsupply[origin-i][origin-i+1]
        Srowlist1=Srowlist
        Scollist1=Scollist
        for Si in Srowlist:
            for Sj in Scollist:
                if Si[0]>=Sj[0] and Si[1]>=Sj[1]:
                        if Sj in Scollist1:
                            Scollist1.remove(Sj)
                elif Si[0]<=Sj[0] and Si[1]<=Sj[1]:
                    if Si in Srowlist1:
                        Srowlist1.remove(Si)
        Sp1 = Scollist1+Srowlist1
        Scopy1=[]
        for x in Sp1:
            Scopy1.append([x[0] + allsupply[origin-i][origin-i][0][0], x[1] + allsupply[origin-i][origin-i][0][1]])
        allsupply[origin-i][origin-i] = Scopy1
        for j in range(1,origin-i+1):
            Srowlist2 = allsupply[origin-i+1][origin-i-j]
            Scollist2 = allsupply[origin-i][origin-i-j+1]
            Srowlist3 = Srowlist2
            Scollist3 = Scollist2
            for Si in Srowlist2:
                for Sj in Scollist2:
                    if Si[0]>=Sj[0] and Si[1]>=Sj[1]:
                            if Sj in Scollist3:
                                Scollist3.remove(Sj)
                    elif Si[0]<=Sj[0] and Si[1]<=Sj[1]:
                        if Si in Srowlist3:
                            Srowlist3.remove(Si)
            Sp2 = Srowlist3+Scollist3
            Scopy2 = []
            for y in Sp2:
                Scopy2.append([y[0]+allsupply[origin-i][origin-i-j][0][0],y[1]+allsupply[origin-i][origin-i-j][0][1]])
            allsupply[origin-i][origin-i-j] = Scopy2
            Srowlist4 = allsupply[origin-i-j+1][origin-i]
            Scollist4 =  allsupply[origin-i-j][origin-i+1]
            Scollist5 = Scollist4
            Srowlist5 = Srowlist4
            for Si in Srowlist4:
                for Sj in Scollist4:
                    if Si[0]>=Sj[0] and Si[1]>=Sj[1]:
                            if Sj in Scollist5:
                                Scollist5.remove(Sj)
                    elif Si[0]<=Sj[0] and Si[1]<=Sj[1]:
                        if Si in Srowlist5:
                            Srowlist5.remove(Si)
            Sp3 = Scollist5+Srowlist5
            Scopy3 = []
            for z in Sp3:
                Scopy3.append([z[0] + allsupply[origin-i-j][origin-i][0][0], z[1] + allsupply[origin-i-j][origin-i] [0][1]])
            allsupply[origin-i-j][origin-i] = Scopy3
# In the third quatarnt
    for i in range(1,origin+1):
        Trowlist = allsupply[origin+i-1][origin-i]
        Tcollist = allsupply[origin+i][origin-i+1]
        Trowlist1=Trowlist
        Tcollist1=Tcollist
        for Ti in Trowlist:
            for Tj in Tcollist:
                if Ti[0]>=Tj[0] and Ti[1]>=Tj[1]:
                        if Tj in Tcollist1:
                            Tcollist1.remove(Tj)
                elif Ti[0]<=Tj[0] and Ti[1]<=Tj[1]:
                    if Ti in Trowlist1:
                        Trowlist1.remove(Ti)
        Tp1 = Tcollist1+Trowlist1
        Tcopy1=[]
        for x in Tp1:
            Tcopy1.append([x[0] + allsupply[origin+i][origin-i][0][0], x[1] + allsupply[origin+i][origin-i][0][1]])
        allsupply[origin+i][origin-i] = Tcopy1

        for j in range(1,origin-i+1):
            Trowlist2 = allsupply[origin+i-1][origin-i-j]
            Tcollist2 = allsupply[origin+i][origin-i-j+1]
            Trowlist3 = Trowlist2
            Tcollist3 = Tcollist2
            for Ti in Trowlist2:
                for Tj in Tcollist2:
                    if Ti[0]>=Tj[0] and Ti[1]>=Tj[1]:
                            if Tj in Tcollist3:
                                Tcollist3.remove(Tj)
                    elif Ti[0]<=Tj[0] and Ti[1]<=Tj[1]:
                        if Ti in Trowlist3:
                            Trowlist3.remove(Ti)
            Tp2 = Tcollist3+Trowlist3
            Tcopy2 = []
            for y in Tp2:
                Tcopy2.append([y[0]+allsupply[origin+i][origin-i-j][0][0],y[1]+allsupply[origin+i][origin-i-j][0][1]])
            allsupply[origin+i][origin-i-j] = Tcopy2
            Trowlist4 = allsupply[origin+i+j-1][origin-i]
            Tcollist4 = allsupply[origin+i+j][origin-i+1]
            Tcollist5 = Tcollist4
            Trowlist5 = Trowlist4
            for Ti in Trowlist4:
                for Tj in Tcollist4:
                    if Ti[0]>=Tj[0] and Ti[1]>=Tj[1]:
                            if Tj in Tcollist5:
                                Tcollist5.remove(Tj)
                    elif Ti[0]<=Tj[0] and Ti[1]<=Tj[1]:
                        if Ti in Trowlist5:
                            Trowlist5.remove(Ti)
            Tp3 = Tcollist5+Trowlist5
            Tcopy3 = []
            for z in Tp3:
                Tcopy3.append([z[0] + allsupply[origin+i+j][origin-i][0][0], z[1] + allsupply[origin+i+j][origin-i] [0][1]])
            allsupply[origin+i+j][origin-i] = Tcopy3

    Dlistn=[]
    for number in allsupply[sizenum-1][sizenum-1]: #Take out the smaller ones in each list
        if number[0]<=number[1]:
            Dlistn.append(number[0])
        else:
            Dlistn.append(number[1])
    supply_choose.append(max(Dlistn)) #Take out the maximum of them.
    Flistn=[]
    for number in allsupply[0][sizenum-1]:
        if number[0]<=number[1]:
            Flistn.append(number[0])
        else:
            Flistn.append(number[1])
    supply_choose.append(max(Flistn))
    Slistn=[]
    for number in allsupply[0][0]:
        if number[0]<=number[1]:
            Slistn.append(number[0])
        else:
            Slistn.append(number[1])
    supply_choose.append(max(Slistn))
    Tlistn=[]
    for number in allsupply[sizenum-1][0]:
        if number[0]<=number[1]:
            Tlistn.append(number[0])
        else:
            Tlistn.append(number[1])
    supply_choose.append(max(Tlistn))#Take out the maximum of them.

    """returns the maximum of min(food,water) that can be collected from given building"""
    return max(supply_choose)
