def preorder_tree_walk(node):
    if node:
        print (node.key, node.height)
        preorder_tree_walk(node.left)
        preorder_tree_walk(node.right)
class TreeNode():
    __slots__ = ['left', 'right', 'data',"height"]
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 0
    def __str__(self):
        sl = '%s <-' % self.left if self.left else ''
        sr = '-> %s' % self.right if self.right else ''
        return '[%s Node(%s) %s ]' % (sl, self.data, sr)

class AVLTree():
    def __init__(self):
        self.root = None
    def find(self, key):
        if not self.root:
            return None
        else:
            return self._find(key, self.root)
    def _find(self, key, node):
        if not node:
            return None
        elif key < node.data:
            return self._find(key, node.left)
        elif key > node.data:
            return self._find(key, node.right)
        else:
            return node
    def findMin(self):
        if self.root is None:
            return None
        else:
            return self._findMin(self.root)
    def _findMin(self, node):
        if node.left:
            return self._findMin(node.left)
        else:
            return node
    def findMax(self):
        if self.root is None:
            return None
        else:
            return self._findMax(self.root)
    def _findMax(self, node):
        if node.right:
            return self._findMax(node.right)
        else:
            return node
    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def singleLeftRotate(self, node):
        k1 = node.left
        node.left = k1.right
        k1.right = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.left), node.height) + 1
        return k1

    def singleRightRotate(self, node):
        k1 = node.right
        node.right = k1.left
        k1.left = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.right), node.height) + 1
        return k1

    def doubleRightRotate(self, node):
        node.right = self.singleLeftRotate(node.right)
        return self.singleRightRotate(node)

    def doubleLeftRotate(self, node):
        node.left = self.singleRightRotate(node.left)
        return self.singleLeftRotate(node)

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self.root = self._insert(key, self.root)
    def _insert(self, key, node):
        if node is None:
            node = TreeNode(key)
        elif key < node.data:
            node.left = self._insert(key, node.left)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if key < node.left.data:
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeftRotate(node)
        elif key > node.data:
            node.right = self._insert(key, node.right)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if key > node.right.data:
                    node = self.singleRightRotate(node)
                else:
                    node = self.doubleRightRotate(node)
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return node
    def delete(self, key):
        if self.root is None:
            raise KeyError('Error,empty tree')
        else:
            self.root = self._delete(key, self.root)
    def _delete(self, key, node):
        if node is None:
            raise KeyError('Error,key not in tree')
        elif key < node.data:
            node.left = self._delete(key, node.left)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if self.height(node.right.right) >= self.height(node.right.left):
                    node = self.singleRightRotate(node)
                else:
                    node = self.doubleRightRotate(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        elif key > node.data:
            node.right = self._delete(key, node.right)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if self.height(node.left.left) >= self.height(node.left.right):
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeftRotate(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        elif node.left and node.right:
            if node.left.height <= node.right.height:
                minNode = self._findMin(node.right)
                node.data = minNode.data
                node.right = self._delete(node.data, node.right)
            else:
                maxNode = self._findMax(node.left)
                node.data = maxNode.data
                node.left = self._delete(node.data, node.left)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        else:
            if node.right:
                node = node.right
            else:
                node = node.left
        return node
if __name__ == '__main__':
    number_list = [23, 88, 19, 37, 59, 96, 49, 33, 6]
    tree = AVLTree()
    for number in number_list:
        # node = TreeNode(number)
        tree.insert(number)
        print(tree.root)
    tree.delete(37)
    tree.delete(19)
    # while True:
    #     cmd = (input('$ ')).strip().split()
    #     if cmd[0] == 'i':
    #         bst.insert(int(cmd[1]))
    #         print(bst.root)
    #     elif cmd[0] == 'd':
    #         bst.delete(int(cmd[1]))
    #         print(bst.root)
