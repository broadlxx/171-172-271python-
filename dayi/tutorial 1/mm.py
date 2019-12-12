print(138*270)
print(355/133)
print(17/2)
print(17//2)

a = 20;
b = 10;
c = 15;
d = 5;
e = (a+b)*c/d;
q = ((a + b) * c) / d;
w = (a + b) * (c / d);
r = a + (b * c) / d;
t = a + (b * c) % d ;
print( "Value is",e,q,w,r,t)

x = 3;
y = x+5;
x = 6;
print(x, y)

m = 3;
n = m;
m = m+2;
print(m, n)

x = 0.5;
y = 10*x;
x = x + 0.1;
print(x, y)

print("Good morning")
print("Mary")
print("how's your little cat")
print()
print("how's your \nlittle\ncat")

myName = input("Your name: ")
print(myName * 10)

num = input("What Integer: ")
i = int(num)
print( i * 10 )

num = input("What real number: ")
x = float(num)
print( x * 10 )

width  = float(input("Box width: "))
height = float(input("Box height: "))
depth  = float(input("Box depth: "))
volume = width * height * depth
print("The volume of that box is " + str(volume))


R = float(input("sphere radius:"))
import math
V = (4*math.pi*R*R*R)/3
print("volume is:"+ str(V))

R1=float(input("R1 is:"))
R2=float(input("R2 is:"))
R3=float(input("R3 is:"))
R=1/(1/R1+1/R2+1/R3)
print(R)

C = int(input("C="))
F = (C*9)/5+32
print(F)

x = int (input("x="))
A = 3*x*x-5*x+10
print(A)

import math
x = int (input("x="))
y = int(input("y="))
A = math.sqrt(x*x+(-5)*y)
print(A)




