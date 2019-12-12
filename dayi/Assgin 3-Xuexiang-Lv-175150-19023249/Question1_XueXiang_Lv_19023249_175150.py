print("Name:XueXiang Lv  Student ID:175150  Massey ID:19023249")
        #Name:XueXiang Lv  Student ID:175150  Massey ID:19023249

import random
def Loadfile(): # This function is load all files
    global Adjectives
    global Adverbs
    global Conjunctions
    global IntransitiveVerbs
    global NounMarkers
    global Nouns
    global TransitiveVerbs
    global Leadin
    file1=open("Adjectives.txt","r")
    Adjectives=[i.strip() for i in file1]
    file1.close()
    file2=open("Adverbs.txt","r")
    Adverbs=[i.strip() for i in file2]
    file2.close()
    file3=open("Conjunctions.txt","r")
    Conjunctions=[i.strip() for i in file3]
    file3.close()
    file4=open("IntransitiveVerbs.txt","r")
    IntransitiveVerbs=[i.strip() for i in file4]
    file4.close()
    file5=open("NounMarkers.txt","r")
    NounMarkers=[i.strip() for i in file5]
    file5.close()
    file6=open("Nouns.txt","r")
    Nouns=[i.strip() for i in file6]
    file6.close()
    file7=open("TransitiveVerbs.txt","r")
    TransitiveVerbs=[i.strip() for i in file7]
    file7.close()
    file8=open("Leadin.txt","r")
    Leadin=[i.strip() for i in file8]
    file8.close()

def Text():#This funcation print all files first lines
    print("The first lines in Adjecitives is %s"%Adjectives[0])
    print("The first lines in Adverbs is %s"%Adverbs[0])
    print("The first lines in Conjunctions is %s"%Conjunctions[0])
    print("The first lines in IntransitiveVerbs is %s"%IntransitiveVerbs[0])
    print("The first lines in NounMarkers is %s"%NounMarkers[0])
    print("The first lines in Nouns is %s"%Nouns[0])
    print("The frist lines in TransitiveVerbs is %s"%TransitiveVerbs[0])

def Easy_sentance(): #this funcation is finish a easy sentence
    a=[]
    a.append(random.choice(Nouns))
    a.append(random.choice(IntransitiveVerbs))
    a.append(".")
    a=" ".join(a)
    print("Easy_sentance is:",a)

def Noun_Phrase():# This funcation is make the first noun phrase
    global nounphrase1
    num0=random.randint(0,1)
    nounphrase1=[]
    nounphrase1.append(random.choice(NounMarkers))
    if num0==0:
        nounphrase1.append(random.choice(Adjectives))
    nounphrase1.append(random.choice(Nouns))

def Noun_Phrases():# This funcation is make the second noun phrase
    global nounphrase2
    num1=random.randint(0,1)
    nounphrase2=[]
    nounphrase2.append(random.choice(NounMarkers))
    if num1==0:
        nounphrase2.append(random.choice(Adjectives))
    nounphrase2.append(random.choice(Nouns))

def Verb_Phrase():# This funcation is make a verb phrase
    global verbphrase
    verbphrase=[]
    Noun_Phrases()
    num2=random.randint(0,1)
    if num2==0:
        verbphrase.append(random.choice(IntransitiveVerbs))
    else:
        verbphrase.append(random.choice(TransitiveVerbs))
        for i in nounphrase2:
            verbphrase.append(i)

def New_sentance():# This funcation is make a whole sentence
    num3=random.randint(0,1)
    num4=random.randint(0,1)
    Noun_Phrase()
    Verb_Phrase()
    sentence=[]
    if num3==0:
        sentence.append(random.choice(Leadin))
    for i in nounphrase1:
        sentence.append(i)
    if num4==0:
        sentence.append(random.choice(Adverbs))
    for t in verbphrase:
        sentence.append(t)
    sentence=" ".join(sentence)
    print("Random sentence is:",sentence)

print("L - Load all the files of words from disk")
print("T - Test: display the first word from each list to make sure they `re been loaded")
print("E - Easy sentence: display a two word sentence _a random selected noun followed by a randomly selected intransitive verb and then a full stop")
print("S - new Sentence: generat & display a sentence conforming to the grammar dedined in the'Use the grammar to make your sentence'section on the next page.")
print("Q - Quit the program")
while True:
    choice=input("cammand:?")
    # try:
    if choice=="L":
        while True:
            print("L - Load all the files of words from disk")
            print("T - Test: display the first word from each list to make sure they `re been loaded")
            print("E - Easy sentence: display a two word sentence _a random selected noun followed by a randomly selected intransitive verb and then a full stop")
            print("S - new Sentence: generat & display a sentence conforming to the grammar dedined in the'Use the grammar to make your sentence'section on the next page.")
            print("Q - Quit the program")
            choice=input("cammand:?")
            Loadfile()
            if choice=="T":
                Text()
                print()
            elif choice=="E":
                Easy_sentance()
                print()
            elif choice=="S":
                New_sentance()
            elif choice=="Q":
                break
        break
    # except:
    else:
        choice=input("cammand:?")
        continue
