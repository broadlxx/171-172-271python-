class TreeNode:
      def __init__(self, data):
        # initialize the node fields
        self.left = None
        self.right = None
        self.data = data

lst = []
lst2 = []
count = 0

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
        print(root.data)
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


    def bianli(self, root):
        if root == None:
            return
        self.bianli(root.left)
        lst.append(root.data)
        self.bianli(root.right)
        return  lst

    def treeToList(self):      # extract the values from a tree and builds a list of ordered values. This list is returned
        l = self.bianli(self.root)
        return l

    def bianli2(self, root):
        if root == None:
            return
        self.bianli2(root.left)
        lst2.append(root.data)
        self.bianli2(root.right)
        return  lst2

    def treeToList2(self):
        l = self.bianli2(self.root)
        return l

    def recursivePrintList(self, L): # it recurses down list, printing each item
        if len(L) == 0:
            return
        i = L[-1]
        print(i)
        L.pop()
        self.recursivePrintList(L)

    def find_height(self,root):
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
        return height

    def count_leaf_nodes(self, T):   # returns a count of the nodes for which left & right are None
        global count
        if T.left and T.right != None:
            self.count_leaf_nodes(T.right)
            self.count_leaf_nodes(T.left)
        elif T.left == None and T.right != None:
            return self.count_leaf_nodes(T.right)
        elif T.right == None and T.left != None:
            return self.count_leaf_nodes(T.left)
        else:
            count += 1
        return  count





T = orderedTree()
print("Do what to the tree:\n  a - Add a data value all ints or all strings\n  p - print the tree\n  l - make a list of the trees data values\n"
      "  r - recursive print of a list\n  h - returns the height of the current tree\n  d - print tree descending\n  c - count leaf nodes")
while True:

    command = input("command>")
    if command.lower() == "a" :
        num = int(input('data is?'))
        T.add_to_tree(num)
    elif command.lower() == "p":
        T.print()
    elif command.lower() == "l":
        L = T.treeToList()
        print(L)
    elif command.lower() == "r":
        L = T.treeToList2()
        T.recursivePrintList(L)
    elif command.lower() == "h":
        print(T.tree_Depth())
    elif command.lower() == "d":
        T.printRev()
    elif command.lower() == "c":
        t = T.get_root()
        print("No of Leaf Nodes" , T.count_leaf_nodes(t))


# T.add_to_tree(9)
# T.add_to_tree(7)
# T.add_to_tree(4)
# T.add_to_tree(12)
# T.add_to_tree(15)
# T.add_to_tree(11)
# T. print()
# T.printRev()
# print(T.treeToList())
# T.recursivePrintList(L=T.treeToList())
# print(T.tree_Depth())
# t = T.get_root()
# print("No of Leaf Nodes" , T.count_leaf_nodes(t))
