def fx(n):
   print("递归进入第",n,"层")
   if n == 3:
       return
   fx(n + 1)
   print("递归退出第",n,"层")
fx(1)
print("程序结束")

# def conflict(state,nextx):
#     '定义冲突函数,state为元组，nextx为下一个皇后的水平位置，nexty为下一个皇后的垂直位置'
#     nexty = len(state)
#     for i in range(nexty):
#         if abs(state[i]-nextx) in (0,nexty-i):#若下一个皇后和前面的皇后列相同或者在一条对角线上，则冲突
#             return True
#     return False
# def queens(num=8,state=()):
#     '八皇后问题，这里num表示规模'
#     for pos in range(num):
#         if not conflict(state,pos):#位置不冲突
#             if len(state) == num - 1:#若是最后一个皇后，则返回该位置
#                 yield (pos,)
#             else:#若不是最后一个皇后，则将该位置返回到state元组并传给后面的皇后
#                 for result in queens(num,state + (pos,)):
#                     yield (pos,) + result
# def prettyp(solution):
#     '打印函数'
#     def line(pos,length = len(solution)):
#         '打印一行，皇后位置用X填充，其余用0填充'
#         return 'O'*(pos)+'X'+'O'*(length-pos-1)
#     for pos in solution:
#         print(line(pos))
# import random
# #随机打印一种
# print(random.choice(list(queens(8))))
# prettyp(random.choice(list(queens(8))))
#
#
# def mergeSortedLists(listA, listB):
#     newlist = [ ]
#     a = 0
#     b = 0
# # loop 1
#     while a < len(listA) and b < len(listB):
#         if listA[a] < listB[b]:
#             newlist.append(listA[a])
#             a +=1
#         else:
#             newlist.append(listB[b])
#             b +=1
#     if a < len(listA): newlist.extend(listA[a:])
#     if b < len(listB): newlist.extend(listB[b:])
#     return newlist

# print(mergeSortedLists([4,5,7],[1,3,3,8]))
#
# class TNode:
#     def __init__(self, data): # initialize the node fields
#         self.left = None
#         self.right = None
#         self.data = data
# class BinOrdTree:
#     def __init__(self): # initialize the root node
#         self.root = None
#     def addNode(self, data): # insert new data value into tree
#         self.root = self.__insert(self.root, data)
#     def __insert(self, root, data): # insert new data value into subtree and return new subtree root
#         if root == None:
#             return TNode(data)
#         else:
#             if data <= root.data:
#                 root.left = self.__insert(root.left, data)
#             else:
#                 root.right = self.__insert(root.right, data)
#         return root
# def recursion(x,tree):
#     root = tree.root
#     if tree.root == x:
#         return True
#     else:
#         if root.left and root.right is None:
#             return False
#         else:
#             recursion(x,root.left)
#             recursion(x,root.right)
# a = 0
# def maxpath(tree):
#     if len(tree) == 1:
#         return 0
#     if tree == []:
#         return False
#     else:
#         root = tree.root
#         if

def bag(n, c, w, v):
    """
    测试数据：
    n = 6  物品的数量，
    c = 10 书包能承受的重量，
    w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
    v = [2, 3, 1, 5, 4, 3] 每个物品的价值
    """
    # 置零，表示初始状态
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            value[i][j] = value[i - 1][j]
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
    for x in value:
        print(x)
    return value

def show(n, c, w, value):
    print('最大价值为:', value[n][c])
    x = [False for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    print('背包中所装物品为:')
    for i in range(n):
        if x[i]:
            print('第', i+1, '个,', end='')

n = 6 # 物品的数量，
c = 10 #书包能承受的重量，
w = [2, 2, 3, 1, 5, 2]# 每个物品的重量，
v = [2, 3, 1, 5, 4, 3] #每个物品的价值
show(n,c,w,bag(n, c, w, v))


def ii(d):
    if d == []:
        return 0
    dp = [1]*len(d)
    for i in range(len(d)):
        for j in range(i):
            if d[i] > d[j]:
                dp[i] = max(dp[i],dp[j]+1)
    print(dp)
    return max(dp)
print("\n")
print(ii([4,1,2,4,5,3,4,8,11,9]),"aaaa")
