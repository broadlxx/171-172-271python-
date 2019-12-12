b=0
items=[]

def getdetails():
    global dictionary
    while True:
        dictionary={}
        a=input("What the title is:")
        if a=="quit":
            return  None
        else:
            dictionary['title']=a
            dictionary['cost']=input("What the num is:")
            items.append(dictionary)
            return items
def fixCosts():
    global b
    global dictionary
    for d in items:
        while True:
            try:
                d['cost']=float(d['cost'])
                b+=d['cost']
                break
            except:
                print("It is not a number")
                d['cost'] = input("number is :")
while True:
    if getdetails() == None:
        print(items)
        break
    else:
        fixCosts()
        # b+=dictionary['cost']
print("The total number is %s"%b)



