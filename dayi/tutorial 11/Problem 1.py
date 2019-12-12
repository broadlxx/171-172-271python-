def getNumber(prompt,Type):
    a=input(prompt)
    while True:
        try:
            if Type=="integer":
                a=int(a)
            elif Type=="float":
                a=float(a)
            break
        except:
            print("Please input a number")
            a=input(prompt)
    return a
amount = getNumber("How much is the item: ", 'float')
howMany= getNumber("How many do you want: ", 'integer')
print(amount,howMany)
print(amount * howMany)

