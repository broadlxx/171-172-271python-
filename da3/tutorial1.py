import random

print ("Welcome to Camel!")
print ("You have stolen a camel to make your way across the great Mobi desert.")
print ("The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.")

done=0
traveled=0
thirst=0
tiredness=0
distance=20
canteen=5

while(done==0):
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed. ")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit. ")
    choice=input("Your'choice:")
    choice=choice.upper()
    if choice=="A":
        if(canteen>0):
            thirst=0
            print ("thirst=",thirst)
            canteen=canteen-1
        else:
            print("error")

    elif choice=="B":
        travel1=random.randint(5,12)
        traveled+=travel1
        print("miles traveled=",traveled)
        thirst=thirst+1
        print("thirst=%d",thirst)
        tiredness=random.randint(1,2)
        print("camel`s tiredness=",tiredness)
        nativetravel1=random.randint(7,14)
        distance=distance-nativetravel1+travel1
        print ("distance=",distance)

    elif choice=="C":
        travel2=random.randint(10,20)
        traveled+=travel2
        print(" miles traveled=",traveled)
        thirst=thirst+1
        print("thirst=",thirst)
        tiredness=tiredness+random.randint(1,3)
        print("camel's tiredness=",tiredness)
        nativetravel2=random.randint(7,14)
        distance=distance-nativetravel2+travel2
        print("distance=",distance)

    elif choice=="D":
        tiredness=0
        print("camel's tiredness=",tiredness)
        print("printf camel is happy\n")
        nativetravel3=random.randint(7,14)
        distance=distance-nativetravel3
        print("distance=",distance)

    elif choice=="E":
        print("traveled: ",traveled)
        print("Drinks in canteen",canteen)
        print("The natives are %d miles behind you\n",distance)
    elif choice=="Q":
        print("quit game\n")
        done=1
    else :
        print("error Wrong Input\n")
        print("\n")

    if 4<thirst<6:
        print("you are thirst\n")
    elif thirst>=6:
        print("You died of thirst\n")
        done=1

    if 5<=tiredness<8:
        print("Your camel is getting tired.\n ")
    elif tiredness>=8:
        print("Your camel is dead.\n")
        done=1

    if distance<=0:
        print(" they caught you and end the game\n")
        done=1
    if distance<=15:
        print("The natives are getting close!\n")

    if traveled>=200:
        print("you win\n")
        done=1

    t=3
    b=random.randint(0,20)
    if t==b:
        print("you find an oasis.refill the canteen,and rest the camel.\n")
        canteen=5
        tiredness=0
