foundCount  = 0
searchCount = 0
names = [ "Mary", "Liz", "Miles", "Bob", "Fred"]
numbers = [4,17 ,19 ]
def find(item):
    global foundCount
    global searchCount
    searchCount+=1
    if item in names:
        print("Found in names")
        foundCount+=1
    elif item in str(numbers):
        print("Found in numbers")
        foundCount+=1
    else:
        print("Not found")
def result():
    global foundCount
    global searchCount
    print("Total searches:%d"%(searchCount))
    print("Total matches:%d"%(foundCount))
    print("Total not found:%d"%(searchCount-foundCount))
print("======= Loading Program =======")
while True:
    item=input()
    if item=="results()":
        break
    find(item)
print("  ***** Search Results *****")
result()
