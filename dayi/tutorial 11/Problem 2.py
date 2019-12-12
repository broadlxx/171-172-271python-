def toInt(a):
    try:
        return int(a)
    except:
        return a
a=input()
print(toInt(a)*3)
