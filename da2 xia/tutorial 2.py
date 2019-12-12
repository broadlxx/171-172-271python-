class TreeNode:
      def __init__(self, data):
        # initialize the node fields
        self.left = None
        self.right = None
        self.data = data

class orderedTree():
    def __init__(self):
        # initialize the root node
        self.root = None

    def get_root(self):
        return self.root

    def insert(self, root, data):
        # insert new data value
        if root == None:
           return TreeNode(data)
        elif root.data == data:
           return root                  # Data item is already in the tree
        elif data < root.data:
             root.left  = self.insert(root.left, data)
        else:
             root.right = self.insert(root.right, data)
        return root

    def add_to_tree(self, new_data):
        self.root = self.insert(self.root, new_data)

    def __printTree(self, root):
        if root == None:
            return
        self.__printTree(root.left)
        print(root.data) #print the tree data
        self.__printTree(root.right)

    def __printTree2(self, root):
        if root == None:
            return
        self.__printTree2(root.right)
        print(root.data)
        self.__printTree2(root.left)

    def print(self):   # Print in ascending order: 4, 19, 21, 32, 39
        self.__printTree(self.root)

    def printRev(self):        # Print in descending order: 39, 32, 21, 19, 4 ...
        self.__printTree2(self.root)

    def treeToList2(self, root): # refresh the list2
        if root == None:
            return
        self.treeToList2(root.left)
        treelist2.append(root.data)
        self. treeToList2(root.right)
        return  treelist2

    def treeToList(self):      # extract the values from a tree and builds a list of
        treelist = self.treeToList2(self.root)
        return treelist                   # ordered values. This list is returned

    def treeToList4(self, root): #refresh trelist4
        if root == None:
            return
        self.treeToList4(root.left)
        treelist4.append(root.data) #add data to list
        self. treeToList4(root.right)
        return  treelist4

    def treeToList3(self):      # extract the values from a tree and builds a list of
        treelist3 = self.treeToList2(self.root)
        return treelist3

    def recursivePrintList(self, L): # it recurses down list, printing each item
        # for j in L:
        #     if isinstance(j,L):
        #         self.recursivePrintList(j)
        #     else:
        #         print(j)
        if len(L) == 0:
            return
        i = L[-1]
        print(i)
        L.pop() #pop the frist item
        self.recursivePrintList(L)

    def find_height(self,root): # count the tree height
        if root == None:
            return 0
        leftheight = self.find_height(root.left)
        rightheight = self.find_height(root.right)
        if leftheight >= rightheight:
            return leftheight+1
        else:
            print(rightheight)
            return rightheight+1

    def tree_Depth(self):            # returns the height of the tree
        height = self.find_height(self.root)
        return height #return the tree height

    def count_leaf_nodes(self, T):   # returns a count of the nodes for which left & right are None
        global count
        if (T.left != None) and (T.right != None):
            self.count_leaf_nodes(T.right)
            self.count_leaf_nodes(T.left)
        elif (T.left == None) and (T.right != None):
            return self.count_leaf_nodes(T.right)
        elif (T.right == None) and (T.left != None):
            return self.count_leaf_nodes(T.left)
        else:
            count += 1   # count the leaves
        return  count

# T.print()
# T.add_to_tree(9)
# T.add_to_tree(7)
# T.add_to_tree(4)
# T.add_to_tree(12)
# T.add_to_tree(15)
# T.add_to_tree(11)
# T.print()
count = 0
treelist = []
treelist2 = []
treelist3 = []
treelist4 = []
T = orderedTree()
print("Do what to the tree:")
print("   a - Add a data value (all ints or all strings)")
print("   p - print the tree")
print("   l - make a list of the trees data values")
print("   r - recursive print of a list")
print("   h - returns the height of the current tree")
print("   d - print tree descending")
print("   c - count leaf nodes")
print("   q - quit")
while True: # commend :
    C = input("Command>")
    if (C.lower() == 'a'): # lower the charater
        num = int(input("what the number is:"))
        T.add_to_tree(num)
    elif (C.lower() == 'p'):
        T.print()
    elif (C.lower() == 'l'):
        print(T.treeToList())
    elif (C.lower() == 'r'):
        T.recursivePrintList(T.treeToList3())
    elif (C.lower() == 'h'):
        print(T.tree_Depth())
    elif (C.lower() == 'd'):
        T.printRev()
    elif (C.lower() == 'c'):
        t = T.get_root()
        print("No of Leaf Nodes" , T.count_leaf_nodes(t))
    elif (C.lower() == 'q'):
        break
    else:
        print("An error command,please reinput")

