import random

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
    stepcount = 0
    return stepcount

shortlistcount = heapify(shortlist)
longlistcount = heapify(longlist)
superlonglistcount = heapify(superlonglist)

for i in range(len(shortlist)):
    print(shortlist[i])
    
print ('\n')

print('Heapify took ' + str(shortlistcount) + ' steps on the list of length ' + str(len(shortlist)-1))
print('Heapify took ' + str(longlistcount) + ' steps on the list of length ' + str(len(longlist)-1))
print('Heapify took ' + str(superlonglistcount) + ' steps on the list of length ' + str(len(superlonglist)-1))


