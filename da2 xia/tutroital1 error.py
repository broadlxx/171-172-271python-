import time

def readwordfile(filename):
    word_list = []
    with open(filename,'r') as f:
        while True:
            word = f.readline().strip()
            if word == '':
                break
            word_list.append(word)
    print("%d Words read from %s"%(len(word_list),filename))
    return word_list


c = 0
def perm(list,begin):
    global c
    if begin == len(list):
        print(list)
        c += 1
        str = "".join(list)
        for i in wordlist:
            if str in i:
                list1.append(i)
    else:
        i = begin
        for n in range(begin,len(list)):
            t = list[n]
            list[n] = list[i]
            list[i] = t
            # list[n],list[i] = list[i],list[n]
            perm(list,begin+1)
            t = list[n]
            list[n] = list[i]
            list[i] = t

list1 = []

startTime = time.time()

wordlist = readwordfile('words.txt')
strlist = []
str = input("a word:")
for i in str:
    strlist.append(i)

perm(strlist,0)

list1 = sorted(list1,key = lambda i:len(i),reverse=True)
print(list1)
print(len(list1))
# str1 =" ".join(strlist)

endTime = time.time()
runTime = endTime - startTime
print("The program took %0.4f seconds"%(runTime))

