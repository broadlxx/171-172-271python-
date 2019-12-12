s=0
for i in range(1,11):
    a=i**3
    print(i,"      ",a)
    s=s+a
print("total:",s)


sentence = input("Please enter a sentence :")
print(sentence.split())
t=sentence.upper()
for i in t.split():
    print(i)


sentence1 = "@num tax on a Chocolate cake costing $17.50 is @momey."
sentence1.spilt()
GST = ["5%","10%","15%","20%","25%"]
def GSTmoney(num,money):
    Discount = sentence1.replace("@num",num)
    Discount = sentence1.replace("@money",money)
    print(Discount)
for s in GST:
    GSTmoney(sentence1,"(GST*17.5)/100")


for t in range(5,26,5):
    a=(t*17.5)/100
    print(t,"% tax on a Chocolate cake costing $17.50 is ",a)


import	random
suites	=	["Hearts",	"Diamonds",	"Spades",	"Clubs"]
cardFaces	=	["Ace","2","3","4","5","6","7","8","9",	"Jack","Queen"]
def pickACard(S):
    cardFace	=	random.choice(cardFaces)
    num  =  random.choice(suites)
    S  =  num+"  ""of""  "+cardFace
    return S
S=0
hand	=	[]
for	i	in	range(5):
    card	=	pickACard(S)
    hand.append(card)
print(hand)


import	turtle
wn	=	turtle.Screen()
my_turtle	=	turtle.Turtle()
for i in range(0,101,10):
    my_turtle.forward(i)
    my_turtle.left(90)
    my_turtle.forward(i)
    my_turtle.left(90)
wn.exitonclick()


