print("XueXiang_Lv 175150 19023249")
P=float(input("Enter the initial value of the investment: "))     #
j=float(input("Enter the annul interest rate?"))
t=int(input("Hom many years will the amount be invested for?"))
S=P*(1+j/12)**(12*t)
print("The final value of your investment after"+str(t)+"years is $",round(S,2))
