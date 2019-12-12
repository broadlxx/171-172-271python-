def toWord(number):
    list1=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninty"]
    list2=["","one","two","three","four","five","six","seven","eight","nine",]
    num1=number//10
    num2=number%10
    word1=list1[num1]
    word2=list2[num2]
    word=word1+" "+word2
    return word

while True:
    sentence=input("sentence:")
    list0=sentence.split()
    if sentence=="":
        break
    else:
        list4=[]
        for word1 in list0:
            try:
                word2=int(word1)
                word2=toWord(word2)
                list4.append(word2)
            except:
                list4.append(word1)
    s=" ".join(list4)
    print(s)
