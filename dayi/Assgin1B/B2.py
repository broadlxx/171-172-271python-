print("XueXiang_Lv 175150 19023249")
tot=1
list = []
A = int(input("Multiples of:"))      # Enter Variable
B = int(input("Enter an upper limit:"))#
for i in range(1,B+1):
    s=i*A
    list.append(s)
    tot = tot*s
    if s>=B:
        break
print(list)
print("The product of the list",list,"is:",tot)
