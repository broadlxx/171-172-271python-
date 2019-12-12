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


