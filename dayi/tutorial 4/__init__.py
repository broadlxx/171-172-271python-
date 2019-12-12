s=0
i=1
while i<11:
    if i==3:
       i=i+1
       continue
    else:
      a=i**3
      print(i,"      ",a)
      s=s+a
      i=i+1
print("total:",s)



while True:
    name = input("What is my name?")
    if name=="kate":
        print("Got it!")
    else:
        print("Guess again")




def translate(animal,language):
    if animal=="cat" :
        if language=="Chinese":
            print("The translate of a cat into Chinese is Māo")
        elif language=="German":
            print("The translate of a cat into German is katze")
        elif language=="French":
            print("The translate of a cat into French is chat")
        elif language=="Spanish":
            print("The translate of a cat into Spanish is gate")
    elif animal=="dog":
        if language=="Chinese":
            print("The translate of a dog into Chinese is Gǒu")
        elif language=="German":
            print("The translate of a dog into German is hund")
        elif language=="French":
            print("The translate of a dog into French is chien")
        elif language=="Spanish":
            print("The translate of a dog into Spanish is perro")
animal =input("What is your pet? : ")
language =input("What is the language? :")
translate(animal,language)
