import random

def randomised_st_connectivity(G, n, s, t):
    stepcount = 0
    current_vertex = s

    while (current_vertex != t) and (stepcount < 2*n**3):
        a=random.randint(0,n-1)
        # print(a)
        if int(G[current_vertex-1][a]) != 0:
            current_vertex = a+1
        else:
            continue
        stepcount = stepcount + 1
    if current_vertex == t:
        return (True, stepcount)
    else:
        return (False, stepcount)

content = []
f = open("testgraph7.txt","r")
list = f.read()
list = list.split("\n")
for i in range(len(list)):
    list[i] = list[i].split()
for l in list:
    if len(l)>3:
        content.append(l)
print(content)
print(randomised_st_connectivity(content, int(list[0][0]), int(list[1][0]), int(list[2][0])))

