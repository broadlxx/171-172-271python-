item = {'title':'Toaster','cost':'79.95'}
def quit():
    a=input("")
    if a=="quit":
        return "None"
    else:
        item[i]=a
        print("The dict returned was : ",item[i])


for i in item:
    quit()
print("The %s was %s"%(item['title'],item['cost']))
