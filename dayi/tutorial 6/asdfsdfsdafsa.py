
Coin_list=[100,50,20,10,5,1]
def Calculator(money):
    for i in range(len(Coin_list)):
        a=money//Coin_list[i]
        money=money%Coin_list[i]
        if a!=0:
            print(a,"× $",Coin_list[i])
money = int(input("Initial amount ($):"))
Calculator(money)
