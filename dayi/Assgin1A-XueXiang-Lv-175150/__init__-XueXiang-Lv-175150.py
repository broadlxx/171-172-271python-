print("XueXiangLv 175150")
def num(loan_amount,number_of_weeks):
    S = loan_amount/number_of_weeks
    return S
loan_amount = float(input("How mach do you borrow:"))
number_of_weeks = int(input("How long do you need repay"))
print("Enter an amount",loan_amount)
print("Enter a number",number_of_weeks)
print("You must repay $",num(loan_amount,number_of_weeks) ," per week to repay a loan of $",loan_amount,"in",
number_of_weeks,"weeks")



list = []
A  =  int(input("How many birthday gifts do you need to buy?"))
for i in range(A):
    name = input("Enter name"+str(i+1)+":")
    list.append(name)
print(list)
tot=0
for i in list:
    s = len(i)
    print("My budget for s gift for ",name,"is $",10*s)
    tot=tot+10*s
print("My total birthday gift budget is: $",tot)


print("Welcome to Best Man Speech Generator ! ")
print("Please provide the following to help")
print("create a new speech")
name1 = input("Enter your name:")
name2 = input("Enter the grooms name:")
name3 = input("Enter the brides name:")
num = input("Enter a number less then 10:")
Age = input("Age you met the groom:")
where = input("Where did the bride and groom meet:")
describe_the_groom = input("How would you describe the groom?")
describe_the_bride = input("How would you describe the bride?")
animal = input("Name an animal:")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Here is your speech {0}:".format(name1))
print("Good evening everyone! For those who don't know me,I`m {0}".format(name1))
print("I met"+name2+"when we"+Age+".Right away,I knew he was a"+describe_the_groom)
print("kid and the perfect friend for me. He was always a hit with the")
print("ladies even at the young age of {0} .Then along came {1} and".format(Age,name3))
print("everything changed. It takes a {0} girl to tame the {1} that".format(describe_the_bride,animal))
print("is {0}. I remeber when they met at {1} and within the space".format(name2,where))
print("of {0} minutes he was smitten! He told me way back then".format(num))
print('"{0} is the girl I'.format(name3)+"'"+'m going to marry"and here we are!')
print("Ladies and gentlemen, I ask you to raise your glasses for {0} and {1}" .format(name3,name2))
print("May they live happily ever after.")

