Word=["one","two","three","four","five","six","seven","eight","nine"]
def toWord(a):
    for i in range(len(Word)):
        if a==i+1:
            return  Word[i]
a=int(input())
print(toWord(a))
