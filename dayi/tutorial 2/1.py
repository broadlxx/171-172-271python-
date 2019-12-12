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
