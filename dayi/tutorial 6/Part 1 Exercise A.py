A = int(input("The limit number:"))
for i in range(A):
    if (i+1)%2==0:
        print("even")
    else:
        print("old")



def print_alternates( limit, word1, word2) :
    for i in range(limit):
         if (i+1)%2==0:
             print(word1)
         else:
             print(word2)
limit = int(input("A limit number:"))
word1 = input(":")
word2 = input(":")
print_alternates( limit, word1, word2)
