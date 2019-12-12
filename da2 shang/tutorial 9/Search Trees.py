import random

class BSTMap :
    def __init__(self) :
        self._root = None
        self._size = 0

    def __len__(self) :
        return self._size

    def __contains__(self,key):
        return self._bstSearch(self._root,key) is not None

    def valueOf( self, min_key, max_key ):
        dictionary = {}
        for i in range(min_key, max_key):
            node = self._bstSearch( self._root, i )
            if node is not None:
                dictionary[i] = node.value
        return dictionary
    def _bstSearch( self, subtree, target ):
        if subtree is None :
            return None
        elif target < subtree.key :
            return self._bstSearch( subtree.left ,target )
        elif target > subtree.key :
            return self._bstSearch( subtree.right ,target)
        else :
            return subtree
    def add( self, key, value ):
        node = self._bstSearch(self._root ,key)
        if node is not None :
            node.value = value
            return False
        else :
            self._root = self._bstInsert( self._root, key, value )
            self._size += 1
            return True
    def _bstInsert( self, subtree, key, value ):
        if subtree is None :
            subtree = _BSTNode( key, value )
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


class _BSTNode :
    def __init__(self, key, value) :
        self.key = key
        self.value = value
        self.left = None
        self.right = None

value = []
for item in range(1,100):
    # a = random.randint(1,100)
    value.append(item)

tree = BSTMap()

for item in value:
    tree.add(item, item**2)

min_key = int(input("Please enter a min number :"))
max_key = int(input("Please enter a max number :"))


print(tree.valueOf(min_key,max_key))
