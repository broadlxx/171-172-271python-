for i in range(3):
    for j in range(3):
        print(i,",",j)


nuts = ["Peanut", "Walnut", "Almond", "Pecan"]
products = ["Butter", "Cake", "Praline", "Pie"]

for i in nuts:
    for j in products:
        print(i,j)


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
print(printRow(startValue, limit))

startVal = int(input("A startVal:"))
limitVal = int(input("A limitVal:"))
numCopies = int(input("How many line you need:"))
def printNumberBlock(startVal, limitVal, numCopies):
    for e in range(numCopies):
        for t in range(startVal,limitVal+1):
            print(t,end= "  ")
        print()
print(printNumberBlock(startVal, limitVal, numCopies))

t=0
mathStudents = ['Audrey','Ben','Julia','Paul','Gerry', 'Sue', 'Helena','Harry','Marco','Rachel','Tina','Mark','Jackson']
csStudents = ['William','Melissa','Sue','Ben','Audrey','Susan','Mark','Hemi','Brendan','Paul','Barry','Julia']
y = len(mathStudents)
x = len(csStudents)
print("There are "+str(y)+" students in the Maths class.")
print("There are "+str(x)+" students in the CompSci class. ")
print("                                                       ")
for i in mathStudents:
    for j in csStudents:
        if i==j:
            print("student :",i,"is enrolled in both classes ")
            t=t+1
            continue
print("                                                 ")
print( t," students are enrolled in Computer Science and Maths	")

S = int(input("A start value:"))
D = int(input("A final value:"))
i = S
while True:
    print(i,end=" ")
    i = i+1
    L = 1
    L = L+1
    if i>D:
        break


A = int(input("The start value:"))
B = int(input("The end value:"))
L=1
count=0
for i in range(A,B+1):
    print(i,end=" ")
    count+=1
    if (L==count):
        print()
        L+=1
        count=0
    else:
        continue


