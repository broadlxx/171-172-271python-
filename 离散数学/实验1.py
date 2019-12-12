def b(p,q):
        if(p==1 and q==1):
            return 1
        else:
            return 0
def c(p,q):
        if(p==0 and q==0):
            return 0
        else:
            return 1
def d(p,q):
        if(p==1 and q==0):
            return 0
        else:
            return 1
def e(p,q):
        if(p==q):
            return 1
        else:
            return 0
p = int(input("请输入命题P的真值：（真为1，假为0）"))
q = int(input("请输入命题Q的真值：（真为1，假为0）"))
print("它们的合取的真值:",b(p,q))
print("它们的析取的真值:",c(p,q))
print("它们的条件的真值:",d(p,q))
print("它们的双条件的真值:",e(p,q))
