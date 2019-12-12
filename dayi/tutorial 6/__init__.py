A = int(input("The limit number:"))
for i in range(A):
    if (i+1)%2==0:
        print("even")
    else:
        print("old")



def print_alternates( limit, word1, word2) :
    for i in range(limit):
         if (i+1)%2==0:
             print(word1)
         else:
             print(word2)
limit = int(input("A limit number:"))
word1 = input(":")
word2 = input(":")
print_alternates( limit, word1, word2)


sum=0
Positives=0
Negatives=0
Zeros=0
for i in range(7):
    A = int(input("Enter a number:"))
    sum=sum+A
    if A>0:
        Positives+=1
    elif A==0:
        Zeros+=1
    else:
        Negatives+=1
print("sum ;",sum)
print("Positives :",Positives,", Negatives :",Negatives,", Zeror :",Zeros)



A = int(input("Initial amount ($): "))
X1=A//100
x1=A%100
for i in range(X1):
    print("$100")
X2=x1//50
x2=x1%50
for j in range(X2):
    print("$50")
X3=x2//20
x3=x2%20
for t in range(X3):
    print("$20")
X4=x3//5
x4=x3%5
for e in range(X4):
    print("$5")
X5=x4//2
x5=x4%2
for t in range(X5):
    print("$2")
X6=x5
for t in range(X6):
    print("$1")



import random
def coin_toss(number):
    A = random.randint(0,1)
    if A==0:
        X="heads"
    else:
        X="tails"
    return X
H=0
T=0
number=int(input("number of coin tosses:"))
for i in range(number):
     print(coin_toss(number))
     if coin_toss(number)=="heads":
         H+=1
     else:
         T+=1
print(H,"× heats",T,"× tails")




import random
while True:
   Computer_choice=random.randint(0,2)
   if Computer_choice==0:
       Computer_choice="rock"
   elif Computer_choice==1:
       Computer_choice="paper"
   else :
       Computer_choice="scissors"
   People_choice=input("Please enter the rock paper scissors randomly: ")
   if People_choice==Computer_choice:
       print("ping")
   elif (People_choice=="rock")and(Computer_choice=="scissors"):
       print("you win")
   elif (People_choice=="paper")and(Computer_choice=="rock"):
       print("you win")
   elif (People_choice=="scissors")and(Computer_choice=="paper"):
       print("you win")
   else:
       print("The computer win")
   A=int(input("If you want to play again.Please input 1:"))
   if A==1:
       pass
   else:
       break



