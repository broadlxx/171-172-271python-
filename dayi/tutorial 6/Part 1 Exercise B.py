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
