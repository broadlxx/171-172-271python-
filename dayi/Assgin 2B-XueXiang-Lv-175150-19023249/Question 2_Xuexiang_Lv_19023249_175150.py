print("Name:XueXiang Lv  Student ID:175150  Massey ID:19023249")
        #Name:XueXiang Lv  Student ID:175150  Massey ID:19023249

def printcurrencies(Currency,Symbol,Conversion):
    print("%-30s%-12s%-50.3f"%(Currency,Symbol,Conversion))
# print("%-30s%-12s%-50s"%(Currency,Symbol,Conversion Rate (amount NZ$1 will buy)))
printcurrencies("Australian Dollar","AUD",0.96)
printcurrencies("US Dollar","USD",0.75)
printcurrencies("Euro","Euro",0.67)
printcurrencies("Great British Pound","GBP",0.496)



for i in range(10,101,10):
    N=i
    A=i*0.96
    U=i*0.75
    E=i*0.67
    G=i*0.496
    print("NZ$%10.2f   AUD%10.2f   USD%10.2f   EURO%10.2f   GBP%10.2f"%(N,A,U,E,G))
print("So NS$%3.0f will buy US$%3.0f or Euro %0.2f"%(N,U,E))
