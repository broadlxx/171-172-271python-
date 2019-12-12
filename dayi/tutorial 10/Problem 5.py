def getdetails():
    if a=="quit":
        print(items)
        return None
    else:
        dictionary={}
        dictionary['title']=input("What the title is:")
        dictionary['cost']=input("What the title is:")
        items.append(dictionary)
items=[]
while True:
    a=input("answer")
    if a=="quit":
        getdetails()
        break
    else:
        getdetails()
