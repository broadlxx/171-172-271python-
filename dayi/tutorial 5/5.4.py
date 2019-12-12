t=0
mathStudents = ['Audrey','Ben','Julia','Paul','Gerry', 'Sue', 'Helena','Harry','Marco','Rachel','Tina','Mark','Jackson']
csStudents = ['William','Melissa','Sue','Ben','Audrey','Susan','Mark','Hemi','Brendan','Paul','Barry','Julia']
y = len(mathStudents)
x = len(csStudents)
print("There are "+str(y)+" students in the Maths class.")
print("There are "+str(x)+" students in the CompSci class. ")
print("                                                       ")
for i in mathStudents:
    for j in csStudents:
        if i==j:
            print("student :",i,"is enrolled in both classes ")
            t=t+1
            continue
print("                                                 ")
print( t," students are enrolled in Computer Science and Maths	")
