class _BSTNode:
    def __init__(self,key,data):
        self.key=key
        self.data=data
        self.left=None
        self.right=None

dic={}
keylist=[]

class BStMap:
    def __init__(self):
        self._root=None
        self.__size=0

    def __len__(self):
        return self.__size

    def valueof(self):
        for i in keylist:
            node=self._bstSearch(self._root,i)
            dic[i]=node.data
        return dic

    def bstSearch1(self,subtree,min,max):
        if subtree is None:
            return None
        elif max<subtree.key:
            return self.bstSearch1(subtree.left,min,max)
        elif min>subtree.key:
            return self.bstSearch1(subtree.right,min,max)
        else:
            keylist.append(subtree.key)
            subtree=self._bstRemove(subtree,subtree.key)
            if self.bstSearch1(subtree,min,max) is  None:
                return keylist


    def _bstSearch(self,subtree,target):
        if subtree is None:
            return None
        elif target<subtree.key:
            return self._bstSearch(subtree.left,target)
        elif target>subtree.key:
            return self._bstSearch(subtree.right,target)
        else:
            return subtree


    def add(self,subtree,key,value):
        node=self._bstSearch(subtree,key)
        if node is not None:
            node.value=value
            return False
        else:
            self._root=self._bstInsert(self._root,key,value)
            self.__size+=1
            return True

    def _bstInsert(self,subtree,key,value):
        if subtree is None:
            subtree=_BSTNode(key,value)
        elif key < subtree.key :
            subtree.left = self._bstInsert(subtree.left, key, value)
        elif key > subtree.key :
            subtree.right = self._bstInsert(subtree.right, key, value)
        return subtree

    def _bstMinumun(self,subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bstMinumun(subtree.left)

    def _bstRemove(self,subtree,target):
        if subtree is None:
            return subtree
        elif target < subtree.key :
            subtree.left = self._bstRemove( subtree.left, target )
            return subtree
        elif target < subtree.key :
            subtree.right = self._bstRemove( subtree.right, target )
            return subtree
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:
                successor=self._bstMinumun(subtree.right)
                subtree.key=successor.key
                subtree.value=successor.value
                subtree.right=self._bstRemove(subtree.right,successor.key)
                return subtree

nt=BStMap()

values = [x for x in range(1,10)]

for item in values:
    nt.add(nt._root,item, item**2)

nt.bstSearch1(nt._root,3,5)
# print(keylist)

nt.valueof()
print(dic)

