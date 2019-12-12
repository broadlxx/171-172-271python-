file=input("your file name")
myfile=open(file,'w')
print("what you want to write")
while True:
    L=input("")
    myfile.write(L)
    myfile.write("\n")
    if L==".":
        break
myfile.close()
