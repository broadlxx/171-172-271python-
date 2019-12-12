dictionary = []
def displayDictionary():
    if dictionary==[]:
        print("*** The dictionary is empty ***")
    else:
        print("*** Known words ****")
        for i in dictionary:
            print("%-8s      %-8s"%(i[0],i[1]))
def lookup(word):
    if dictionary==[]:
            words=input("How do i translate %s:"%word)
            dictionary.append([word,words])
            return words
    else:
        for i in dictionary:
           if word in i:
               words=i[1]
               return words
        words=input("How do i translate %s:"%word)
        dictionary.append([word,words])
        return word
def file_dic(file1):
    # global file1
    for l in file1.readlines():
        l=l.strip("\n")
        l=l.split("/")
        dictionary.append([l[0],l[1]])
    return file1
def Copydictionary(filename):
    file=open(filename,"w")
    for i in dictionary:
        file.write("%s/%s\n"%(i[0],i[1]))
def main():
    while True:
        reply = input("Eng:>")
        reply.lower()
        reply=reply.replace(","," ")
        reply=reply.replace("."," ")
        reply=reply.replace(":"," ")
        reply=reply.replace("!"," ")
        if reply=="?":
             displayDictionary()
        elif reply=="save":
             Copydictionary(filename)
        elif reply=="quit":
             choice=input("yes or no:")
             if choice=="yes":
                  Copydictionary(filename)
                  break
             else:
                 main()
        else:
             translatedReply=[]
             r=reply.split()
             for word in r:
                  if (word==".")or(word=="?")or(word=="!"):
                      continue
                  else:
                   translation = lookup(word)
                   translatedReply.append(translation)
             for i in range(len(translatedReply)):
                  print(translatedReply[i],end=" ")
             print()
print("quit: quit the program  save: save in file")
filename=input("what file do you open:")
file1=open(filename,"r")
file_dic(file1)
main()
