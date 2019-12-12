item = []
amount = 0

def getDetials():
    global dictionary
    dictionary = {}
    title = input("title is:")
    if title == "quit":
        return None
    dictionary['title'] = title
    cost = input("cost is:")
    dictionary['cost'] = cost
    item.append(dictionary)
    return item

def fixCosts():
    global dictionary
    for i in item:
        while True:
            try:
                dictionary['cost'] = float(dictionary['cost'])
                break
            except:
                print("your print is wrong")
                dictionary['cost'] = input("num is:")

while True:
    result = getDetials()
    if result == None:
        print(item)
        break
    else:
        fixCosts()
        amount += dictionary['cost']
print(amount)

