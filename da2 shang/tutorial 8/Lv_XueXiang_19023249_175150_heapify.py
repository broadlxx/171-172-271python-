import random
global stepcount

# Set up some Python Lists
shortlist = []
shortlist.append(0)
longlist = []
longlist.append(0)
superlonglist = []
superlonglist.append(0)

for i in range(100):
    num = random.randrange(0,1000)
    shortlist.append(num)
    
for i in range(10000):
    num = random.randrange(0,10000)
    longlist.append(num)

for i in range(1000000):
    num = random.randrange(0,1000000)
    superlonglist.append(num)

# You need to implement this function.
# Your function should heapify the input list
# and increment the step count for each unit of work carried out.
def heapify(alist):
    global stepcount
    stepcount = 0
    n=len(alist)-1
    for j in range(n//2,0,-1):
        siftdown(alist,j,n)
    return stepcount

def siftdown(h,j,n):
    global stepcount
    temp=h[j]
    while(2*j+2<=n):
        child=2*j
        if (child<n) and (h[child+1]>h[child]):
            child=child+1
            stepcount+=1
        if(h[child]>temp):
            h[j]=h[child]
            stepcount+=1
        else:
            break
        j=child
    h[j]=temp


shortlistcount = heapify(shortlist)
longlistcount = heapify(longlist)
superlonglistcount = heapify(superlonglist)

for i in range(len(shortlist)):

    print(shortlist[i])

print ('\n')

print('Heapify took ' + str(shortlistcount) + ' steps on the list of length ' + str(len(shortlist)-1))
print('Heapify took ' + str(longlistcount) + ' steps on the list of length ' + str(len(longlist)-1))
print('Heapify took ' + str(superlonglistcount) + ' steps on the list of length ' + str(len(superlonglist)-1))
