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

def insertion_sort (list):
    moveCount = 0
    # Start at the second element (pos 1).
    # Insert this element into the sorted part of the list.
    for i in range(1, len(list)):
        keyValue = list[i]   # Get value of element to insert
        j = i-1              # Scan to the left

        while j >= 0:
            if len(list[j]) > len(keyValue):
               list[j+1] = list[j]
            else:
                break  # hit the top of the sorted section
            j = j-1

        # Everything's been moved out of the way, insert
        # the keyValue into the correct location
        list[j+1] = keyValue
        moveCount +=1



filename = "example_sorted_names.txt"
with open(filename, 'r') as f:
    lines = f.read()
    name_list = lines.split('\n')
selection_sort(name_list)
insertion_sort(name_list)
for o in name_list:
    print(o)
