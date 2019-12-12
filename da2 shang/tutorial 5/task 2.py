def selection_sort(list):
    for i in range( len(list) ):     # Loop through the entire array
        # Find the position that has the smallest number
        # Start with the current position
        minPos = i

        for j in range(i+1, len(list) ):     # Scan what's left

            if len(list[j]) < len(list[minPos]):  # Is this position smallest?
                minPos = j              # yes, save position

        # Swap the two values
        temp = list[minPos]
        list[minPos] = list[i]
        list[i] = temp

# Binary Search, recursive version
# def binary_search(the_list, lower, upper, item):
#   if lower > upper:
#        print( "%s is not in the list." % item )
#        return -1
#
#   middle_pos = (lower + upper) // 2
#   if the_list[middle_pos] < item:
#         lower = middle_pos+1
#         return binary_search(the_list, lower, upper, item)
#   elif the_list[middle_pos] > item:
#         upper = middle_pos-1
#         return binary_search(the_list, lower, upper, item)
#   else:
#         print( "%s is at position %d" %(item,middle_pos))
#         return middle_pos


# Binary Search, iterative versionoip

def binary_search_iterative(the_list, item): #
    selection_sort(the_list)
    lower_bound = 0
    upper_bound = len(the_list)-1
    found = False
    while lower_bound <= upper_bound and not found :
        middle_pos =( (lower_bound + upper_bound) // 2)
        if the_list[middle_pos][0] < item:
            lower_bound = middle_pos+1
        elif the_list[middle_pos][0] > item:
            upper_bound = middle_pos-1
        else:
            print(the_list[middle_pos])
            the_list.remove(the_list[middle_pos])
            binary_search_iterative(the_list, item)
            found = True

    # if found:
    #     print( "%s is at position %d" % (item,middle_pos))
    #     return middle_pos
    # else:
    #     print( "%s is not in the list." % item )
    #     return -1
filename = "example_sorted_names.txt"
with open(filename, 'r') as f:
    lines = f.read()
    name_list = lines.split('\n')
print(name_list)
binary_search_iterative(name_list, 'S')
# K = [ x for x in range(50)]
# print (K[:6])
# print("Test recursive binary search")
# index = binary_search (K, 0, len(K)-1, 5)     # should return 5
# index = binary_search (K, 0, len(K)-1, 1005)  # should return -1 (not found)
#
# print("Test Iterative Binary Search")
# index = binary_search_iterative (K, 5)     # should return 5
# index = binary_search_iterative (K, 1005)  # should return -1 (not found)
