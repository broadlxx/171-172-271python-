A = int(input("A number:"))
for i in range(3):
    for j in range(A):
        print(j+1,end=" ")
    print()

startValue = int(input("A startValue:"))
limit = int(input("A limit:"))
def printRow(startValue, limit):
    for t in range(startValue,limit+1):
         print(t,end="  ")
printRow(startValue, limit)

startVal = int(input("A startVal:"))
limitVal = int(input("A limitVal:"))
numCopies = int(input("How many line you need:"))
def printNumberBlock(startVal, limitVal, numCopies):
    for e in range(numCopies):
        for t in range(startVal,limitVal+1):
            print(t,end= "  ")
        print()
printNumberBlock(startVal, limitVal, numCopies)
