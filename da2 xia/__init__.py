from building import *

# speed test - use "python optimizer.py" to run
if __name__ == "__main__":
    import timeit
    test_size = 1 # set to 100 to check time for speed race
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

    for bone in range(0,origin):
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
            allfood[origin+s][origin+s-r] += max(allfood[origin+s-1][origin+s-r],allfood[origin+s][origin+s-r-1])
            allfood[origin+s-r][origin+s] += max(allfood[origin+s-r-1][origin+s],allfood[origin+s-r][origin+s-1])
            allfood[origin+s][origin-s-r] += max(allfood[origin+s-1][origin-s-r],allfood[origin+s][origin-s-r-1])
            allfood[origin+s-r][origin-s] += max(allfood[origin+s-r-1][origin-s],allfood[origin+s-r][origin-s+1])
            allfood[origin-s][origin+s-r] += max(allfood[origin-s+1][origin+s-r],allfood[origin-s][origin+s-r-1])
            allfood[origin-s-r][origin+s] += max(allfood[origin-s-r+1][origin+s],allfood[origin-s-r][origin+s-1])
            allfood[origin-s][origin-s-r] += max(allfood[origin-s+1][origin-s-r],allfood[origin-s][origin-s-r+1])
            allfood[origin-s-r][origin-s] += max(allfood[origin-s-r+1][origin-s],allfood[origin-s-r][origin-s+1])
    # for i in allfood:
    #     print(i)

    maxfood = max(allfood[0][0],allfood[n-1][0],allfood[0][n-1],allfood[n-1][n-1])
    # print("-------------------------------")

    """returns the maximum number of food that can be collected from given building"""
    return maxfood# dummy implementation - replace

def compare(rowlist,collist,rowlist1,collist1):
    for i in rowlist:
        for j in collist:
            if i[0]>=j[0] and i[1]>j[1]:
                    if j in collist1:
                        collist1.remove(j)
            elif i[0]==j[0] and i[1]==j[1]:
                if j in collist1:
                    collist1.remove(j)
            elif i[0]>j[0] and i[1]>=j[1]:
                if j in collist1:
                    collist1.remove(j)
            elif i[0]<=j[0] and i[1]<j[1]:
                if i in rowlist1:
                    rowlist1.remove(i)
            elif i[0]<j[0] and i[1]<=j[1]:
                if i in rowlist1:
                    rowlist1.remove(i)
            else:
                pass
    tot = rowlist1+collist1
    return tot

def max_supplies(building: Building) -> int:
    supply_choose = []
    allsupply = []
    for i in building.rooms:
        supply = []
        for j in i:
            foodandwater = []
            room = []
            foodandwater.append(j.food)
            foodandwater.append(j.water)
            room.append(foodandwater)
            supply.append(room)
            # print(supply)
        allsupply.append(supply)
    sizenum = len(allsupply)
    origin = int((sizenum+1)/2-1)
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
        row=[]# Points on the diagonal line
        col=[]
        for a1 in allsupply[origin+i-1][origin+i]:
            row.append(a1)
        for a2 in allsupply[origin+i][origin+i-1]:
            col.append(a2)
        row1=row
        col1=col
        c1 = compare(row,col,row1,col1)
        copy1=[]
        for x in c1:
            copy1.append([x[0] + allsupply[origin+i][origin+i][0][0], x[1] + allsupply[origin+i][origin+i][0][1]])
        allsupply[origin+i][origin+i] = copy1

        for j in range(1,origin-i+1):
            row2 = []
            col2 = []
            for b1 in allsupply[origin+i-1][origin+i+j]:
                row2.append(b1)
            for b2 in allsupply[origin+i][origin+i+j-1]:
                col2.append(b2)
            row3 = row2
            col3 = col2
            p2 = compare(row2,col2,row3,col3)
            copy2 = []
            for y in p2:
                copy2.append([y[0]+allsupply[origin+i][origin+i+j][0][0],y[1]+allsupply[origin+i][origin+i+j][0][1]])
            allsupply[origin+i][origin+i+j] = copy2

        for t in range(1,origin-i+1):
            row4 = []
            col4 = []
            for e in allsupply[origin+i+t-1][origin+i]:
                row4.append(e)
            row5 = row4
            for q in allsupply[origin+i+t][origin+i-1]:
                col4.append(q)
            col5 = col4
            p3 = compare(row4,col4,row5,col5)
            copy3 = []
            for z in p3:
                copy3.append([z[0] + allsupply[origin+i+t][origin+i][0][0], z[1] + allsupply[origin+i+t][origin+i] [0][1]])
            allsupply[origin+i+t][origin+i] = copy3

    listn=[]
    for number in allsupply[sizenum-1][sizenum-1]:
        if number[0]<=number[1]:
            listn.append(number[0])
        else:
            listn.append(number[1])
    supply_choose.append(max(listn))
    for i in allsupply:
        print(i)
    print("yyyyyyyyyyyyyy")





    """returns the maximum of min(food,water) that can be collected from given building"""
    return max(supply_choose) # dummy implementation - replace
