from sortedcontainers import SortedList

storge = SortedList([1, 3, 4, 6, 7, 7, 8, 9])

def find_diamond(storge, min_weight):
    storge = SortedList(storge)
    position = storge.bisect_right(min_weight)
    if position == len(storge):
        return None
    elif storge[position - 1] != min_weight:
        return storge[position]
    else:
        return storge[position - 1]

def add_diamond(storge, weight):
    storge = SortedList(storge)
    storge.add(find_diamond(storge, weight))
    return storge

def Remove(storge, weight):
    storge = SortedList(storge)
    storge.remove(find_diamond(storge, weight))
    return storge

print("should be: " + str(find_diamond(storge, 6.5)))
print(storge)
storge1 = add_diamond(storge, 6.5)
print(storge1)
s1 = Remove(storge1, 7.6)
print(s1)
