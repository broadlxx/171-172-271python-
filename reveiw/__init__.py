import random
for i in range(0,100):
    print(random.randint(0,3),end="")

def fibs(num):
    assert (num > 1)
    result = [0,1]
    num = num - 2
    for i in range(num):
        result.append(result[-2] + result[-1])
    return result

print("\n",fibs(10))


def change(n):
    n = ['new', 'list']
    n[0] = '159172'

    print(n)

courses = ['old', 'list']
print(change(courses))

