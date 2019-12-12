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



Coin_list=[100,50,20,10,5,1]
def Calculator(money):
    for i in range(len(Coin_list)):
        a=money//Coin_list[i]
        money=money%Coin_list[i]
        if a!=0:
            print(a,"× $",Coin_list[i])
money = int(input("Initial amount ($):"))
Calculator(money)
