print( list(map(len, [[1,2,3], [4,5,6], [7,8,9], [10,11,12]])))

d = dict.fromkeys(range(8))
print(d)
print(d.get('5', 5))


def printx(n):
    print(n,end=" ")
    if n == 0:
        return
    printx(n - 1)
    print(n,end=" ")

printx(5)

print("\n",7//2,7%2,7/2)




vowels = ["a", "e", 'i', 'o', 'u']

print(vowels[1:3])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[::-1])

name = list("Pearl")
name[2:] = list("ar")
print(name)