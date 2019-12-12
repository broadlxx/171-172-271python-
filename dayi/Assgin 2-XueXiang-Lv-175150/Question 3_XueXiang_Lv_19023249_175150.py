print("Name:XueXiang Lv  Student ID:175150  Massey ID:19023249")
        #Name:XueXiang Lv  Student ID:175150  Massey ID:19023249

stories = [
  ['With bloody hands, I say good-bye.'                    , 'Frank Miller'],
  ['TIME MACHINE REACHES FUTURE!!! ... nobody there ...'   , 'Harry Harrison'  ],
  ['The baby\'s blood type? Human, mostly.'                , 'Orson Scott Card'],
  ['For sale: baby shoes, never worn.'                     , 'Ernest Hemingway'],
  ['Corpse parts missing. Doctor buys yacht.'              , 'Margaret Atwood'],
  ['We kissed. She melted. Mop please!'                    , 'James Patrick Kelly'],
  ['Starlet sex scandal. Giant squid involved.'            , 'Margaret Atwood'],
  ['Will this do (lazy writer asked)?'                     , 'Ken McLeod'     ],
  ["I'm sorry, but there's not enough air in here for everyone. I’ll tell them you were a hero.",   'J. Matthew Zoss'],
  ['Waking Up To Silence: Deafening silence. I strain my ears, praying there might be someone else still alive. The only noise I hear are the voices in my head','Mike Jackson'],
  ["Not In My Job Description: Make sure it's done by the end of the day Jones.\nBut, sir, it's not in my ....\nJust do it, and remember, no blood."             ,'Mike Jackson'],
  ['Empty Baggage: The trunk arrived two days later. He lifted the lid and froze, it was empty. No arms, no legs, no head, nothing. Where was she?'             ,'Mike Jackson'],
  ['Forgot My Own Name: The hospital said it was concussion.\nMight be permanent memory loss.\nCan\'t even remember my own name - which is handy considering who I am.','Mike Jackson']
]

def pattern():               #This function user can some word find some stories
    P=input("what the certain pattern:")
    for i in range(len(story)):
        if (P in story[i]):
            print(story[i])
            print("----",name[i])
        else:
            continue

def auther():              #This function user can name find some stories
    A=input("What is the auther`s name:")
    for i in range(len(name)):
        if (A in name[i]):
            print(story[i])
            print("----",name[i])
        else:
            continue
def word():                #This function user can some word or name find some stories
    auther1=input("input a certain author:")
    word=input("input a certain word:")
    for i in range(len(story)):
        if (auther1 in name[i])and(word in story[i]):
            print(story[i])
            print("----",name[i])
        else:
            continue

def number():       #This function user can find some stories less than a number
    N=int(input("Less than how many words :"))
    for i in range(len(story)):
        if N>=len(story[i].split()):
            print(story[i])
            print("----",name[i])

        else:
            continue

def display():
    for i in range(len(story)):
            print(story[i])
            print("----",name[i])


while True:
    print("        *** find a stories***")
    print("P - Find stories that contain a certain pattern ")
    print("A - Find all stories by a certain author ")
    print("AW - Find stories that a by a certain author and a contain a certain word ")
    print("LW - Find stories less than a certain number of words")
    print("D - Display all the stories")
    print("Q - quit the game")
    C=input("your choice:")
    story=[]
    for j in stories:
        story.append(j[0])
    name=[]
    for j in stories:
        name.append(j[1])
    if C=="P":
        pattern()
    elif C=="A":
        auther()
    elif C=="AW":
        word()
    elif C=="LW":
        number()
    elif C=="D":
        display()
    elif C=="Q":
        break          #

