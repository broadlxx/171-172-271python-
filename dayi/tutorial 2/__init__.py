def total(a,b,c,):
    sum=a+b+c
    return sum
t1=total(2,3,4)+total(4,6,8)
print(t1)

def banner(name):
    print("What is your name?")
    print("  "+name)
    print("ok")
banner("i`m banner")

def someFc(s):
    s = s*2
    return s
food = 'bread'
someFc(food)
print(food)
print(someFc('egg'))

def double(x):
    print('from double:',x)
    return x*3
def subtract(y,z):
    print('from subtract:', y, ' and ', z)
    return y - z
result = subtract(20,double(10))
print(result)


def block(x):
    x=x+3
x=5.6
block(x)
print(x)

def test(a):
    a=a*1.5
    return a
    a=a/0.1
x=10
x=test(x)
print(x)

price = 50.0
gst = price * 15.0 / 100.0
print("Price is ",price," and gst is ",gst)
num1 = float(input('Please enter the cost of one ticket :'))
num2 = float(input('Please enter the number of tickets wanted:'))
t=num1*num2
print('The total cost for all tickets is:',str(t))

def totalGST(x,y,z):
    x=x*0.15
    y=y*0.15
    z=z*0.15
    return x+y+z
print(totalGST(100,200,300))

def townCount(city,year):
    city = 'Blonkton'
    year = 2011
    numberOfPeople = 10100000
    return numberOfPeople
city = 'Blonkton'
year = 2011
print('In 2011, the population of Blonkton was',townCount(city,year))

a = float(input("Digital one :"))
b = float(input("Digital two :"))
c = float(input("Digital three :"))
x=a+b+c
print(x)

def avg(x):
    x=x/4
    return x
a = float(input("Digital one :"))
b = float(input("Digital two :"))
c = float(input("Digital three :"))
d = float(input("Digital four :"))
x=a+b+c+d
print(avg(x))



import math
def Volume(R):
    V = (4*math.pi*R*R*R)/3
    return V
R = float(input("sphere radius:"))
print("volume is:",Volume(R))

def total(R1,R2,R3):
    R=1/(1/R1+1/R2+1/R3)
    return R
R1=float(input("R1 is:"))
R2=float(input("R2 is:"))
R3=float(input("R3 is:"))
print(total(R1,R2,R3))

def num(C):
    F = (C*9)/5+32
    return F
C = int(input("C="))
print(num(C))

def num(x):
    A = 3*x*x-5*x+10
    return A
x = int (input("x="))
print(num(x))

import math
def num(x,y):
    A = math.sqrt(x*x+(-5)*y)
    return A
x = int (input("x="))
y = int(input("y="))
print(num(x,y))














