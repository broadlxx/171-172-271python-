print("Name:XueXiang Lv  Student ID:175150  Massey ID:19023249")
        #Name:XueXiang Lv  Student ID:175150  Massey ID:19023249


detail={}
def add():# This function is add some details
    global detail
    dict={}
    dict['name']=input("The name is:")
    dict['address']=input("The address is:")
    dict['phone-no']=input("The phone-no is:")
    dict['nickname']=input("The nickname is:")
    dict['nickname'].lower()
    for i in detail:
        if dict["nickname"]==i:
            del detail[i]
            detail[dict['nickname']]=dict
    else:
        detail[dict['nickname']]=dict

def find():#This function is find a nickname
    nickname=input("what is the nickname you want to find:")
    nickname.lower()
    print(detail[nickname])

def delete():  # This function is delete a nickname all details
    nickname=input("what nickname do you want to delete:")
    nickname.lower()
    del detail[nickname]

def listall():#This function is show all the information
    n=1
    print("     Nick      Name           Address             Phone_No")
    for i in detail:
        print("%-5d%-10s%-15s%-20s%-20s"%(n,detail[i]['nickname'],detail[i]['name'],detail[i]['address'],detail[i]['phone-no']))
        n+=1

while True:
    print("*** My Contacts ***")
    print("  f - find")
    print("  a - add new entry")
    print("  d - delete")
    print("  l - list all")
    print("  q - quit")
    choice=input("commend:?")
    if choice=="f":
        find()
    elif choice=="a":
        add()
    elif choice=="d":
        choice1=input("yes or no")
        if choice1=="yes":
            delete()
    elif choice=="l":
        listall()
    elif choice=="q":
        break



