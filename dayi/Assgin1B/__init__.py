P=float(input("Enter the initial value of the investment: "))
j=float(input("Enter the annul interest rate?"))
t=int(input("Hom many years will the amount be invested for?"))
S=P*(1+j/12)**(12*t)
print("The final value of your investment after"+str(t)+"years is $",round(S,2))


tot=1
list = []
A = int(input("Multiples of:"))
B = int(input("Enter an upper limit:"))
for i in range(1,B+1):
    s=i*A
    list.append(s)
    tot = tot*s
    if s>=B:
        break
print(list)
print("The product of the list",list,"is:",tot)


import random
description = ['First', 'Dream', 'New Family', 'Brand New']
adjective = ['Wonderful', 'Sunny', 'Spacious', 'Secluded']
bedrooms = [1, 2, 3, 4, 5]
City = ['Tianjin','Baoding','Shijiazhuang','Tangshan','Chengde']
type_of_owner = ['a couple', 'a family', 'a retired couple','a large family', 'a professional couple']
amenities_close_by = ['great schools', 'shopping centre', 'motorway', 'airport', 'hospital']
print("*** Your "+ random.choice(description)+ " Home *** ")
print( random.choice(adjective)," ",random.choice(bedrooms)," bedroom home in ", random.choice(City))
print("Would suit "+random.choice(type_of_owner))
print("Close to "+random.choice(amenities_close_by))
print("All enquires to Joe on 183-0027-1234.")
print("*** Make it yours today! *** ")


