Word1=["one","two","three","four","five","six","seven","eight","nine"]
Word2=["ten","twenty","thrity","forty","fifty","sixty","seventy","eighty","ninty","one hundred"]
def  toWord(a):
    for i in range(len(Word2)):
        if a//10==i+1:
            x=Word2[i]
        return  Word1[a]
    if a%10!=0:
        for o in range(len(Word1)):
            if a%10==o+1:
                y=Word1[o]
                w=x+" "+y
                return w
    else:
        return x

while True:
    a=int(input())
    print(toWord(a))
