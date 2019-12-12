
a = 0
for i in range(10):
    a = a + 1
    print(a,"\n")
    for j in range(10):
        a = a + 1
print(a)

mylist = [1,2,3,4,5,6,7,8,9,10]
mylist[0:10:2] = ['a', 'b', 'c', 'd', 'e']
print(mylist)
mylist[9::-3] = [22, 22, 22, 22]
print(mylist)

lst=['my ', 'big ', 'fat ']
lst.append('wedding ')
lst.extend(['next','week'])
print(lst)

newlst=['my','big','wedding','next','week']
newlst.insert(0, 'fat ')
print(newlst,",,,,")


newlst1=['my ', 'big ', 'fat ', 'wedding', 'next', 'week ']
newlst1.pop()
print(newlst1)
newlst1.pop(0)
print(newlst1)

x=[1,2,3,4]
x.reverse()
print(x)

newlst2=['my ', 'big ', 'fat ', 'wedding ', 'next', 'week ']
print(newlst2.index('next'),)

lst1=['my ', 'big ', 'fat ', 'bottom ']
print(''.join(lst1))

print([x*x for x in range(10) if x % 2 == 0])

print([x+2*y for x in range(4) for y in range(3)])
result = []
for x in range(4):
    for y in range(3):
        result.append(x+2*y)
print(result)

def even(x):
    return  x % 2==0
list(map(even,[1,2,3,4,5]))
print(list(map(even,[1,2,3,4,5])))
print([even(x) for x in [0,1,2,3,4]])

def negative(x):
    return x<0
print(list(filter(negative,[-1, 2, -3, 5, 7, -9])))
print([x for x in [-1, 2, -3, 5, 7, -9] if negative(x)])

ll=[1,2,3,4,5]
print(zip(ll,ll))

def removedups(mylist):
    newlist = [ ]
    for x in mylist:
        if x not in newlist:
           newlist.append(x)
    return newlist

def removedups1(mylist):
    for x in mylist:
        if mylist.count(x) > 1:
           indx = mylist.index(x)
           del mylist[indx]
    return mylist


a=[1,1,2,5,8,9,3,6,6,6,7,9]
print(removedups(a))
print(removedups1(a))

def pascal(n):
    if n == 1:
       return [[1]]
    else:
       result = [[1]]
       x = 1
       while x < n:
          lastRow = result[-1]
          nextRow = [(a+b) for a,b in zip([0]+lastRow,lastRow+[0])]
          result.append(nextRow)
          x += 1
       return result
n=10
print(pascal(n))
import random
p=[[(x,y) for x in range(0,600,15)] for y in range(0,600,15)]
for i in p:
    print(i)
print(p)
q=[ i for i in range(240,480,15)]
print(q)
