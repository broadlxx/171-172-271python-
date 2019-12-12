def translate(animal,language):
    if animal=="cat" :
        if language=="Chinese":
            ww="The translate of a cat into Chinese is Māo"
        elif language=="German":
            ww="The translate of a cat into German is katze"
        elif language=="French":
            ww="The translate of a cat into French is chat"
        elif language=="Spanish":
            ww="The translate of a cat into Spanish is gate"
        elif language:
            ww=""
    elif animal=="dog":
        if language=="Chinese":
            ww="The translate of a dog into Chinese is Gǒu"
        elif language=="German":
            ww="The translate of a dog into German is hund"
        elif language=="French":
            ww="The translate of a dog into French is chien"
        elif language=="Spanish":
            ww="The translate of a dog into Spanish is perro"
        elif language:
            ww=""
    elif animal:
         ww=""
    return ww
animal =input("What is your pet? : ")
language =input("What is the language? :")
language=language.capitalize()
print(translate(animal,language))
