print("XueXiangLv 175150")
list = []
A  =  int(input("How many birthday gifts do you need to buy?"))
for i in range(A):
    name = input("Enter name"+str(i+1)+":")
    list.append(name)
print(list)
tot=0
for i in list:
    s = len(i)
    print("My budget for s gift for ",name,"is $",10*s)
    tot=tot+10*s
print("My total birthday gift budget is: $",tot)
