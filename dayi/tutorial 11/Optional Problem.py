Word1=["","","twenty","thrity","forty","fifty","sixty","seventy","eighty","ninty","one hundred"]
Word2=["","one","two","three","four","five","six","seven","eight","nine"]
def toWord(a1):
    num1=a1//10
    num2=a1%10
    word1=Word1[num1]
    word2=Word2[num2]
    word=word1+" "+word2
    return word
sentence=[]
s=input("Sentence:")
b=s.split()
for a in b:
    try:
        a1=int(a)
        a1=toWord(a1)
        sentence.append(a1)
    except:
        sentence.append(a)
sent=" ".join(sentence)
print(sent)
