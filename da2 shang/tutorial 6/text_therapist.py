import random
# "Earlier,you said that "
hedges = ( "Please, tell me a little more.",
           "Many of my patients tell me the same thing.",
           "Please, carry on talking." ,
           "What is your point?")

qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your","we":"you", "us":"you", "mine":"yours", "am":"are","your":"my"}
text_replacements = {"you":"u","are":"r","thanks":"thx"}
dictionary = {"a":"","e":"","i":"","o":"","u":""}

def removeVowels(word):
    if len(word) < 4:
        return word
    else:
        sent = []
        for i in word:
            sent.append(dictionary.get(i,i))
        words = "".join(sent)
        return words


def changetoText(sentence):
    Word = sentence.split()
    sentence = []
    for w in Word:
        if w in text_replacements.keys():
            sentence.append(text_replacements.get(w,w))
        else:
            word = removeVowels(w)
            sentence.append(word)

    return  " ".join(sentence)


def reply(sentence):
    """Builds and returns a reply to the sentence."""
    
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence) + " ?"
        
def changePerson(sentence):
    """Replaces first person pronouns with second person pronouns."""
    
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word,word))
    return " ".join(replyWords)

def main():
    """Handles the interaction between patient and doctor."""
    w0 = "Good morning, I hope you are well today ."
    w0 = changetoText(w0)
    print(w0)
    # print("Good morning, I hope yo1+22u are well today .")
    w1 = "What can I do for you ?"
    w1 = changetoText(w1)
    print(w1)
    earliersentence = []
    while True:

        if len(earliersentence) > 5:
            num = random.randint(1,4)
            if num == 1:
                asksentence = random.choice(earliersentence)
                print("Earlier, you said that"+changePerson(asksentence))
                earliersentence.remove(asksentence)

        sentence = input("\n>> ")

        earliersentence.append(sentence)

        if sentence.upper() == "QUIT":
            print("Have a nice day")
            break
        print(changetoText(reply(sentence)))


print(replacements.values())
main()
