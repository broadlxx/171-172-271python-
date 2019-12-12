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
    list1=[]

    for i in building.rooms:
        list2=[]
        for j in i:
            list2.append(j.food)
        list1.append(list2)
    n=len(list1)
    m=int((n+1)/2-1)
    for i in range(1,m+1):
        list1[m][m-i]+=list1[m][m-i+1]
        list1[m][m+i]+=list1[m][m+i-1]
        list1[m-i][m]+=list1[m-i+1][m]
        list1[m+i][m]+=list1[m+i-1][m]

    for i in range(1,m+1):
        list1[m-i][m-i]+=max(list1[m-i+1][m-i],list1[m-i][m-i+1])

        for j in range(1,m-i+1):
                list1[m-i][m-i-j]+=max(list1[m-i+1][m-i-j],list1[m-i][m-i-j+1])
        for t in range(1,m-i+1):
                list1[m-i-t][m-i]+=max(list1[m-i-t+1][m-i],list1[m-i-t][m-i+1])


    for i in range(1,m+1):
        list1[m+i][m-i]+=max(list1[m+i-1][m-i],list1[m+i][m-i+1])

        for j in range(1,m-i+1):
                list1[m+i][m-i-j]+=max(list1[m+i-1][m-i-j],list1[m+i][m-i-j+1])
        for t in range(1,m-i+1):
                list1[m+i+t][m-i]+=max(list1[m+i+t-1][m-i],list1[m+i+t][m-i+1])


    for i in range(1,m+1):
        list1[m-i][m+i]+=max(list1[m-i+1][m+i],list1[m-i][m+i-1])

        for j in range(1,m-i+1):
                list1[m-i][m+i+j]+=max(list1[m-i+1][m+i+j],list1[m-i][m+i+j-1])
        for t in range(1,m-i+1):
                list1[m-i-t][m+i]+=max(list1[m-i-t+1][m+i],list1[m-i-t][m+i-1])


    for i in range(1,m+1):
        list1[m+i][m+i]+=max(list1[m+i-1][m+i],list1[m+i][m+i-1])

        for j in range(1,m-i+1):
                list1[m+i][m+i+j]+=max(list1[m+i-1][m+i+j],list1[m+i][m+i+j-1])
        for t in range(1,m-i+1):
                list1[m+i+t][m+i]+=max(list1[m+i+t-1][m+i],list1[m+i+t][m+i-1])
    t=max(list1[0][0],list1[n-1][0],list1[0][n-1],list1[n-1][n-1])
    """returns the maximum number of food that can be collected from given building"""
    return t# dummy implementation - replace

def max_supplies(building: Building) -> int:
    list1 = []
    list_choose=[]
    for aa in building.rooms:
        list2 = []
        for j in aa:
            list3=[]
            list4=[]
            list3.append(j.food)
            list3.append(j.water)
            list4.append(list3)
            list2.append(list4)
        list1.append(list2)
    n = len(list1)
    m = int((n + 1) / 2 - 1)

    for i in range(1, m + 1):
        list1[m][m - i][0][0] += list1[m][m - i + 1][0][0]
        list1[m][m - i][0][1] += list1[m][m - i + 1][0][1]
        list1[m][m + i][0][0]  += list1[m][m + i - 1][0][0]
        list1[m][m + i][0][1] += list1[m][m + i - 1][0][1]
        list1[m - i][m][0][0]+= list1[m - i + 1][m][0][0]
        list1[m - i][m][0][1]  += list1[m - i + 1][m][0][1]
        list1[m + i][m][0][0]+= list1[m + i - 1][m][0][0]
        list1[m + i][m][0][1]  += list1[m + i - 1][m][0][1]

    for i in range(1,m+1):

        list_row=[]
        list_col=[]

        for n1 in list1[m-i+1][m-i]:
            list_row.append(n1)
        list_row1=list_row[:]
        for k in list1[m-i][m-i+1]:
            list_col.append(k)
        list_col1=list_col[:]
        for item1 in list_row:
            for item2 in list_col:
                if item1[0]>=item2[0] and item1[1]>item2[1]:
                    if item2 in list_col1:
                        list_col1.remove(item2)
                elif item1[0]==item2[0] and item1[1]==item2[1]:
                    if item2 in list_col1:
                        list_col1.remove(item2)
                elif item1[0]>item2[0] and item1[1]>=item2[1]:
                    if item2 in list_col1:
                        list_col1.remove(item2)
                elif item1[0]<=item2[0] and item1[1]<item2[1]:
                    if item1 in list_row1:
                        list_row1.remove(item1)
                elif item1[0]<item2[0] and item1[1]<=item2[1]:
                    if item1 in list_row1:
                        list_row1.remove(item1)
                else:
                    pass

        list_final=list_col1+list_row1
        list_c=[]
        for x in list_final:
            list_c.append([x[0] + list1[m - i][m - i ][0][0], x[1] + list1[m - i][m - i ][0][1]])
        list1[m - i][m - i ] = list_c

        for j in range(1,m-i+1):
            list_row2 = []
            list_col2 = []
            for f in list1[m - i + 1][m - i-j]:
                list_row2.append(f)
            list_row3 = list_row2[:]
            for z in list1[m - i][m - i -j+ 1]:
                list_col2.append(z)
            list_col3 = list_col2[:]
            for item3 in list_row2:
                for item4 in list_col2:
                    if item3[0] >= item4[0] and item3[1] > item4[1]:
                        if item4 in list_col3:
                            list_col3.remove(item4)
                    elif item3[0] == item4[0] and item3[1] == item4[1]:
                        if item4 in list_col3:
                            list_col3.remove(item4)
                    elif item3[0] > item4[0] and item3[1] >= item4[1]:
                        if item4 in list_col3:
                            list_col3.remove(item4)
                    elif item3[0] <= item4[0] and item3[1] < item4[1]:
                        if item3 in list_row3:
                            list_row3.remove(item3)
                    elif item3[0] < item4[0] and item3[1] <= item4[1]:
                        if item3 in list_row3:
                            list_row3.remove(item3)
                    else:
                        pass


            list_final1 = list_col3 + list_row3
            list_cc = []

            for y in list_final1:
                list_cc.append([y[0]+list1[m - i][m - i-j][0][0],y[1]+list1[m - i][m - i-j][0][1]])
            list1[m - i][m - i-j] = list_cc

        for t in range(1,m-i+1):
            list_row4 = []
            list_col4 = []

            for e in list1[m - i-t + 1][m - i]:
                list_row4.append(e)
            list_row5 = list_row4[:]
            for q in list1[m - i-t][m - i + 1]:
                list_col4.append(q)
            list_col5 = list_col4[:]

            for item5 in list_row4:
                for item6 in list_col4:
                    if item5[0] >= item6[0] and item5[1] > item6[1]:
                        if item6 in list_col5:
                            list_col5.remove(item6)
                    elif item5[0] == item6[0] and item5[1] == item6[1]:
                        if item6 in list_col5:
                            list_col5.remove(item6)
                    elif item5[0] > item6[0] and item5[1] >= item6[1]:
                        if item6 in list_col5:
                            list_col5.remove(item6)
                    elif item5[0] <= item6[0] and item5[1] < item6[1]:
                        if item5 in list_row5:
                            list_row5.remove(item5)
                    elif item5[0] < item6[0] and item5[1] <= item6[1]:
                        if item5 in list_row5:
                            list_row5.remove(item5)
                    else:
                        pass

            list_final2 = list_col5 + list_row5
            list_ccc = []
            for a in list_final2:
                list_ccc.append([a[0] + list1[m - i-t][m - i ][0][0], a[1] + list1[m - i- t][m - i] [0][1]])
            list1[m - i-t][m - i] = list_ccc

    list5=[]
    for number in list1[0][0]:
        if number[0]<=number[1]:
            list5.append(number[0])
        else:
            list5.append(number[1])
    list_choose.append(max(list5))
#first
    for i in range(1,m+1):

        list_row=[]
        list_col=[]

        for n1 in list1[m-i+1][m+i]:
            list_row.append(n1)
        list_row1=list_row[:]
        for k in list1[m-i][m+i-1]:
            list_col.append(k)
        list_col1=list_col[:]
        for item1 in list_row:
            for item2 in list_col:
                if item1[0]>=item2[0] and item1[1]>item2[1]:
                    if item2 in list_col1:
                        list_col1.remove(item2)
                elif item1[0]==item2[0] and item1[1]==item2[1]:
                    if item2 in list_col1:
                        list_col1.remove(item2)
                elif item1[0]>item2[0] and item1[1]>=item2[1]:
                    if item2 in list_col1:
                        list_col1.remove(item2)
                elif item1[0]<=item2[0] and item1[1]<item2[1]:
                    if item1 in list_row1:
                        list_row1.remove(item1)
                elif item1[0]<item2[0] and item1[1]<=item2[1]:
                    if item1 in list_row1:
                        list_row1.remove(item1)
                else:
                    pass

        list_final=list_col1+list_row1
        list_c=[]
        for x in list_final:
            list_c.append([x[0] + list1[m - i][m + i ][0][0], x[1] + list1[m - i][m + i ][0][1]])
        list1[m - i][m + i ] = list_c

        for j in range(1,m-i+1):
            list_row2 = []
            list_col2 = []
            for f in list1[m - i + 1][m + i+j]:
                list_row2.append(f)
            list_row3 = list_row2[:]
            for z in list1[m - i][m + i +j- 1]:
                list_col2.append(z)
            list_col3 = list_col2[:]
            for item3 in list_row2:
                for item4 in list_col2:
                    if item3[0] >= item4[0] and item3[1] > item4[1]:
                        if item4 in list_col3:
                            list_col3.remove(item4)
                    elif item3[0] == item4[0] and item3[1] == item4[1]:
                        if item4 in list_col3:
                            list_col3.remove(item4)
                    elif item3[0] > item4[0] and item3[1] >= item4[1]:
                        if item4 in list_col3:
                            list_col3.remove(item4)
                    elif item3[0] <= item4[0] and item3[1] < item4[1]:
                        if item3 in list_row3:
                            list_row3.remove(item3)
                    elif item3[0] < item4[0] and item3[1] <= item4[1]:
                        if item3 in list_row3:
                            list_row3.remove(item3)
                    else:
                        pass


            list_final1 = list_col3 + list_row3
            list_cc = []

            for y in list_final1:
                list_cc.append([y[0]+list1[m - i][m + i+j][0][0],y[1]+list1[m - i][m + i+j][0][1]])
            list1[m - i][m + i+j] = list_cc

        for t in range(1,m-i+1):
            list_row4 = []
            list_col4 = []

            for e in list1[m - i-t + 1][m + i]:
                list_row4.append(e)
            list_row5 = list_row4[:]
            for q in list1[m - i-t][m + i - 1]:
                list_col4.append(q)
            list_col5 = list_col4[:]

            for item5 in list_row4:
                for item6 in list_col4:
                    if item5[0] >= item6[0] and item5[1] > item6[1]:
                        if item6 in list_col5:
                            list_col5.remove(item6)
                    elif item5[0] == item6[0] and item5[1] == item6[1]:
                        if item6 in list_col5:
                            list_col5.remove(item6)
                    elif item5[0] > item6[0] and item5[1] >= item6[1]:
                        if item6 in list_col5:
                            list_col5.remove(item6)
                    elif item5[0] <= item6[0] and item5[1] < item6[1]:
                        if item5 in list_row5:
                            list_row5.remove(item5)
                    elif item5[0] < item6[0] and item5[1] <= item6[1]:
                        if item5 in list_row5:
                            list_row5.remove(item5)
                    else:
                        pass

            list_final2 = list_col5 + list_row5
            list_ccc = []
            for a in list_final2:
                list_ccc.append([a[0] + list1[m - i-t][m + i ][0][0], a[1] + list1[m - i- t][m + i] [0][1]])
            list1[m - i-t][m + i] = list_ccc

    list5=[]
    for number in list1[0][n-1]:
        if number[0]<=number[1]:
            list5.append(number[0])
        else:
            list5.append(number[1])
    list_choose.append(max(list5))
# #third
    for i in range(1,m+1):

        list_row=[]
        list_col=[]

        for n1 in list1[m+i-1][m-i]:
            list_row.append(n1)
        list_row1=list_row[:]
        for k in list1[m+i][m-i+1]:
            list_col.append(k)
        list_col1=list_col[:]
        for item1 in list_row:
            for item2 in list_col:
                if item1[0]>=item2[0] and item1[1]>item2[1]:
                    if item2 in list_col1:
                        list_col1.remove(item2)
                elif item1[0]==item2[0] and item1[1]==item2[1]:
                    if item2 in list_col1:
                        list_col1.remove(item2)
                elif item1[0]>item2[0] and item1[1]>=item2[1]:
                    if item2 in list_col1:
                        list_col1.remove(item2)
                elif item1[0]<=item2[0] and item1[1]<item2[1]:
                    if item1 in list_row1:
                        list_row1.remove(item1)
                elif item1[0]<item2[0] and item1[1]<=item2[1]:
                    if item1 in list_row1:
                        list_row1.remove(item1)
                else:
                    pass

        list_final=list_col1+list_row1
        list_c=[]
        for x in list_final:
            list_c.append([x[0] + list1[m + i][m - i ][0][0], x[1] + list1[m + i][m - i ][0][1]])
        list1[m + i][m - i ] = list_c

        for j in range(1,m-i+1):
            list_row2 = []
            list_col2 = []
            for f in list1[m + i - 1][m - i-j]:
                list_row2.append(f)
            list_row3 = list_row2[:]
            for z in list1[m + i][m - i -j+ 1]:
                list_col2.append(z)
            list_col3 = list_col2[:]
            for item3 in list_row2:
                for item4 in list_col2:
                    if item3[0] >= item4[0] and item3[1] > item4[1]:
                        if item4 in list_col3:
                            list_col3.remove(item4)
                    elif item3[0] == item4[0] and item3[1] == item4[1]:
                        if item4 in list_col3:
                            list_col3.remove(item4)
                    elif item3[0] > item4[0] and item3[1] >= item4[1]:
                        if item4 in list_col3:
                            list_col3.remove(item4)
                    elif item3[0] <= item4[0] and item3[1] < item4[1]:
                        if item3 in list_row3:
                            list_row3.remove(item3)
                    elif item3[0] < item4[0] and item3[1] <= item4[1]:
                        if item3 in list_row3:
                            list_row3.remove(item3)
                    else:
                        pass


            list_final1 = list_col3 + list_row3
            list_cc = []

            for y in list_final1:
                list_cc.append([y[0]+list1[m + i][m - i-j][0][0],y[1]+list1[m + i][m - i-j][0][1]])
            list1[m + i][m - i-j] = list_cc

        for t in range(1,m-i+1):
            list_row4 = []
            list_col4 = []

            for e in list1[m + i+t - 1][m - i]:
                list_row4.append(e)
            list_row5 = list_row4[:]
            for q in list1[m +i+t][m - i + 1]:
                list_col4.append(q)
            list_col5 = list_col4[:]

            for item5 in list_row4:
                for item6 in list_col4:
                    if item5[0] >= item6[0] and item5[1] > item6[1]:
                        if item6 in list_col5:
                            list_col5.remove(item6)
                    elif item5[0] == item6[0] and item5[1] == item6[1]:
                        if item6 in list_col5:
                            list_col5.remove(item6)
                    elif item5[0] > item6[0] and item5[1] >= item6[1]:
                        if item6 in list_col5:
                            list_col5.remove(item6)
                    elif item5[0] <= item6[0] and item5[1] < item6[1]:
                        if item5 in list_row5:
                            list_row5.remove(item5)
                    elif item5[0] < item6[0] and item5[1] <= item6[1]:
                        if item5 in list_row5:
                            list_row5.remove(item5)
                    else:
                        pass

            list_final2 = list_col5 + list_row5
            list_ccc = []
            for a in list_final2:
                list_ccc.append([a[0] + list1[m + i+t][m - i ][0][0], a[1] + list1[m + i+t][m - i] [0][1]])
            list1[m + i+t][m - i] = list_ccc

    list5=[]
    for number in list1[n-1][0]:
        if number[0]<=number[1]:
            list5.append(number[0])
        else:
            list5.append(number[1])
    list_choose.append(max(list5))
#forth
    for i in range(1,m+1):

        list_row=[]
        list_col=[]

        for n1 in list1[m+i-1][m+i]:
            list_row.append(n1)
        list_row1=list_row[:]
        for k in list1[m+i][m+i-1]:
            list_col.append(k)
        list_col1=list_col[:]
        for item1 in list_row:
            for item2 in list_col:
                if item1[0]>=item2[0] and item1[1]>item2[1]:
                    if item2 in list_col1:
                        list_col1.remove(item2)
                elif item1[0]==item2[0] and item1[1]==item2[1]:
                    if item2 in list_col1:
                        list_col1.remove(item2)
                elif item1[0]>item2[0] and item1[1]>=item2[1]:
                    if item2 in list_col1:
                        list_col1.remove(item2)
                elif item1[0]<=item2[0] and item1[1]<item2[1]:
                    if item1 in list_row1:
                        list_row1.remove(item1)
                elif item1[0]<item2[0] and item1[1]<=item2[1]:
                    if item1 in list_row1:
                        list_row1.remove(item1)
                else:
                    pass

        list_final=list_col1+list_row1
        list_c=[]
        for x in list_final:
            list_c.append([x[0] + list1[m +i][m+i ][0][0], x[1] + list1[m +i][m +i ][0][1]])
        list1[m +i][m +i] = list_c

        for j in range(1,m-i+1):
            list_row2 = []
            list_col2 = []
            for f in list1[m +i - 1][m+i+j]:
                list_row2.append(f)
            list_row3 = list_row2[:]
            for z in list1[m +i][m +i +j- 1]:
                list_col2.append(z)
            list_col3 = list_col2[:]
            for item3 in list_row2:
                for item4 in list_col2:
                    if item3[0] >= item4[0] and item3[1] > item4[1]:
                        if item4 in list_col3:
                            list_col3.remove(item4)
                    elif item3[0] == item4[0] and item3[1] == item4[1]:
                        if item4 in list_col3:
                            list_col3.remove(item4)
                    elif item3[0] > item4[0] and item3[1] >= item4[1]:
                        if item4 in list_col3:
                            list_col3.remove(item4)
                    elif item3[0] <= item4[0] and item3[1] < item4[1]:
                        if item3 in list_row3:
                            list_row3.remove(item3)
                    elif item3[0] < item4[0] and item3[1] <= item4[1]:
                        if item3 in list_row3:
                            list_row3.remove(item3)
                    else:
                        pass


            list_final1 = list_col3 + list_row3
            list_cc = []

            for y in list_final1:
                list_cc.append([y[0]+list1[m + i][m + i+j][0][0],y[1]+list1[m + i][m + i+j][0][1]])
            list1[m + i][m + i+j] = list_cc

        for t in range(1,m-i+1):
            list_row4 = []
            list_col4 = []

            for e in list1[m + i+t - 1][m + i]:
                list_row4.append(e)
            list_row5 = list_row4[:]
            for q in list1[m + i+t][m + i- 1]:
                list_col4.append(q)
            list_col5 = list_col4[:]

            for item5 in list_row4:
                for item6 in list_col4:
                    if item5[0] >= item6[0] and item5[1] > item6[1]:
                        if item6 in list_col5:
                            list_col5.remove(item6)
                    elif item5[0] == item6[0] and item5[1] == item6[1]:
                        if item6 in list_col5:
                            list_col5.remove(item6)
                    elif item5[0] > item6[0] and item5[1] >= item6[1]:
                        if item6 in list_col5:
                            list_col5.remove(item6)
                    elif item5[0] <= item6[0] and item5[1] < item6[1]:
                        if item5 in list_row5:
                            list_row5.remove(item5)
                    elif item5[0] < item6[0] and item5[1] <= item6[1]:
                        if item5 in list_row5:
                            list_row5.remove(item5)
                    else:
                        pass

            list_final2 = list_col5 + list_row5
            list_ccc = []
            for a in list_final2:
                list_ccc.append([a[0] + list1[m + i+t][m + i ][0][0], a[1] + list1[m + i+ t][m + i] [0][1]])
            list1[m + i+t][m + i] = list_ccc

    list5=[]
    for number in list1[n-1][n-1]:
        if number[0]<=number[1]:
            list5.append(number[0])
        else:
            list5.append(number[1])
    list_choose.append(max(list5))
    """returns the maximum of min(food,water) that can be collected from given building"""
    return max(list_choose)# dummy implementation - replace
