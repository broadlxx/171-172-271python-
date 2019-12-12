def A1(t,amount):
    a=(t*amount)/100
    return a
amount =float(input("How mach:"))
for t in range(5,26,5):
    print(t,"% tax on a Chocolate cake costing $",(amount)," is ",round(A1(t,amount),2))
