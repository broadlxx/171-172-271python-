

Item = ["Beer","Food","Books","Music"]
Weight = [6,3,4,2]
Value = [30,14,16,9]


print("---------------(One zero package)0-1背包--------------")

max_weight = 10
n = len(Weight)

dp = [[-1 for j in range(max_weight + 1)] for i in range(n)]

for i in range(n):
    dp[i][0] = 0

for j in range(max_weight + 1):
    if Weight[0] <= j:
        dp[0][j] = Value[0]
    else:
        dp[0][j] = 0


def dp_fun(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    if j >= Weight[i]:
        dp[i][j] = max(dp_fun(i-1, j), dp_fun(i-1, j-Weight[i]) + Value[i])
    else:
        dp[i][j] = dp_fun(i-1, j)
    return dp[i][j]

print('最大值为：' + str(dp_fun(n - 1, max_weight)))

print("____________-(complete package)完全背包-___________")
F = [0 for i in range(0,max_weight+1)]
def CompleteBackPack(cost,value):
    for i in range(cost,max_weight+1):
        F[i] = max(F[i],F[i-cost]+value)
for i in range(0,n):
    CompleteBackPack(Weight[i],Value[i])
print ("Complete pack:",F[max_weight])
