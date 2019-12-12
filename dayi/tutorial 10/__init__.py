b=0
items=[]
dictionary={}
def getdetails():
     # while True:
        a=input("What the title is:")
        if a=="quit":
            return  None
        else:
            dictionary['title']=a
            dictionary['cost']=input("What the num is:")
            items.append(dictionary)
            print(items)
def fixCosts():
    global b
    for d in items:
        while True:
            try:
                d['cost']=float(d['cost'])
                b+=d['cost']
                break
            except:
                print("It is not a number")
                d['cost']=float(input("number is :"))

dictionary['title']=input("answer :")
if dictionary['title']=="quit":
    print("The total number is %s",b)
else:
    getdetails()
    fixCosts()
print("The total number is %s"%b)
