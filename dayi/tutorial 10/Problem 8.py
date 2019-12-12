items=[]
itemdict={}
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
while True:
    if getdetails() == None:
        for i in range(len(items)):
            itemdict[items[i]['title']]=items[i]
        break
for a in range(len(itemdict)):
    print(a)
for i in sorted(itemdict):
     print(itemdict[i])
