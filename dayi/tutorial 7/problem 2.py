def Filecopy(filename):
    newfile=open(filename,'w')
    for i in lines:
         newfile.write(i)
    newfile.close()

filename=input("The file name and format is:")
myfile=open('mytest.txt','r')
lines=myfile.readlines()
myfile.close()
Filecopy(filename)
