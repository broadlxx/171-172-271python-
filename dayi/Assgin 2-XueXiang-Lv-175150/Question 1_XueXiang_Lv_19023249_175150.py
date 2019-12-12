print("Name:XueXiang Lv  Student ID:175150  Massey ID:19023249")
        #Name:XueXiang Lv  Student ID:175150  Massey ID:19023249



list=["9.95","14.95","19.95","24.95","29.95","34.95","39.95","44.95","49.95"]#define a list
print("**Sale prices**")
print("Normal price:   $9.95  $14.95  $19.95  $24.95  $29.95  $34.95  $39.95  $44.95  $49.95")
print("--------------------------------------------------------------------------------------")
for i in range(5,51,5):# A discount loops
    if i==5:            #If i=5 is other print
        print("\t%off ",i,"%",end= '\t')
    else:
        print("\t\t",i,"%",end="\t")
    for j in range(9,50,5):# Money loops
        N=(j+0.95)*(100-i)/100# Calculate discounted money
        print("{:.2f}".format(N),end="\t",)
    print()

