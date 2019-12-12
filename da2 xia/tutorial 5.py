import time,random
def create_int_list(length, maximum_value):
    L = []
    for i in range(length):
       value = random.randint(1, maximum_value)

       # 30% of the time make the value negative and twice as large
       if random.random() < 0.33:
          value = -value*2
       L.append(value)
    return L


# def maximal_subsequence(d):
#     list = []
#     num= 0
#     for i in range(len(d)):
#         for j in range(i,len(d)):
#             tut = sum(d[i:j])
#             # print("i=",i,"j=",j,"tut=",tut)
#             list.append(tut)
#             num += 1
#
#     list.sort(reverse = True)
#     print("num = ",num)
#     return list[0]

def maximal_subsequence(d):
    tut = d[0]
    max = tut
    num = 0
    for i in range(len(d)):
        if tut>0:
            tut = tut + d[i]  # 判断前面序列的和,如果大于0就保留,继续加下一个数字
        else:
            tut =d[i]  # 前面的序列不大于0,就舍去,从下一个数字开始计算最大和.
        if tut>max:
            max=tut  # 如果计算的最大和是新的最大和,就更新最大和.这样就忽略了后面和小于0的连续序列
        num += 1
    print("num=",num)
    return max




start_time = time.time()

d = [ -3, 12, -7,  5, 9, -10, 2, 6]
print(maximal_subsequence(d))
print("\n")
print("Creating sequences of mostly positive integers")
list15   = create_int_list(15, 10)
print("\n*********** 15 integers:\n",    list15)
print(maximal_subsequence(list15))

list150  = create_int_list(150, 10)
print("\n*********** 150 integers:\n",   list150)
print(maximal_subsequence(list150))

list5000 = create_int_list(5000, 15)
print("\n*********** 5000 integers:\n",   list5000)
print(maximal_subsequence(list5000))


end_time = time.time()
run_time = end_time - start_time
print(run_time, 'seconds')
