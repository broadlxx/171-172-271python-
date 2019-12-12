import	random
suites	=	["Hearts",	"Diamonds",	"Spades",	"Clubs"]
cardFaces	=	["Ace","2","3","4","5","6","7","8","9",	"Jack","Queen"]
def pickACard(S):
    cardFace	=	random.choice(cardFaces)
    num  =  random.choice(suites)
    S  = (num+"  of  "+cardFace)
    return S
S=0
hand	=	[]
for	i	in	range(5):
    if(S  in hand):
         pickACard(S)
    else:
         card	=	pickACard(S)
         hand.append(card)
print(hand)
