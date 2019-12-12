def total(R1,R2,R3):
    R=1/(1/R1+1/R2+1/R3)
    return R
R1=float(input("R1 is:"))
R2=float(input("R2 is:"))
R3=float(input("R3 is:"))
print(total(R1,R2,R3))
