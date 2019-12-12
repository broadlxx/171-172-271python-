# f = open("testgraph3.txt","r")
# list = f.read()
# list = list.split("\n")
# for i in list:
#     if i == '':
#         list.remove(i)
# list2 = list[2:len(list)]
#
# Vlist = [i for i in range(1,int(list[0])+1)]
# graphlist = [[0 for i in range(int(list[0]))] for j in range(int(list[0]))]
#
# for j in list2:
#     graphlist[int(j[0])-1][int(j[2])-1] = 1
#     graphlist[int(j[2])-1][int(j[0])-1] = 1
# print(graphlist)



def load_file():

    textlist = []

    for i in range(1, 10):

        textname = "testgraph" + str(i) + ".txt"

        textlist.append(textname)



    pick = textlist[2]

    print(pick)

    with open(pick, "r") as f:

        List = []

        for line in f.readlines():

            x = line.strip("\n").split()
            print(x)

            if x != []:

                List.append(x)

    vertex = int(List.pop(0)[0])

    edge = int(List.pop(0)[0])

    graph = []

    for i in range(vertex):

        list1 = []

        for j in range(vertex):

            list1.append(0)

        graph.append(list1)



    for i in List:

        x = int(i[0]) - 1

        y = int(i[1]) - 1

        graph[x][y] = 1

        graph[y][x] = 1

    print(graph)

    return vertex, edge, graph
load_file()
