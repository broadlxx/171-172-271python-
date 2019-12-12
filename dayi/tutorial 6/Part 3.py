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
