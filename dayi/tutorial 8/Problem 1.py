count=0
def X():
    global count
    count+=1
    return
while True:
    A= input("")
    if A=="X()":
        X()
        print("Called %d times"%(count))
    else:
        break

