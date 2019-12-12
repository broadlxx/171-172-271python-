#test3

def selection_sort(list):
    # Loop through the entire array
    for i in range(len(list)):

        # Find the position that has the smallest number
        # Start with the current position
        minPos = i

        # Scan left
        for j in range(i + 1, len(list)):

            # Is this position smallest?
            if list[j] < list[minPos]:
                # It is, mark this position as the smallest
                minPos = j

        # Swap the two values
        temp = list[minPos]
        list[minPos] = list[i]
        list[i] = temp
    return list


def insertion_sort(list):

    # Start at the second element (pos 1).
    # Insert this element into the sorted part of the list.
    for i in range(1, len(list)):

        # Get the value of the element to insert
        keyValue = list[i]

        # Scan to the left
        j = i - 1

        # Loop each element, moving them up until
        # we reach the position the element should go in
        while (j >= 0) and (list[j] > keyValue):
            list[j+1] = list[j]
            j = j - 1

        # Everything's been moved out of the way, insert
        # the key into the correct location
        list[j+1] = keyValue
    return list


list = [5,7,8,9,55,1,2,3,6,9,19,8,35,28,4,]
print(selection_sort(list))
print(insertion_sort(list))
print(list.pop())
list.append(77)
print(list)

def addFirst(self, cargo):
    node = Node(cargo)
    node.next = self.head
    self.head = node
    self.length = self.length + 1


def insertLast(self, cargo):
    node = Node(cargo)
    node.next = None
    if self.head == None:
        # if list is empty the new node goes first
        self.head = node
    else:
        # find the last node in the list
        last = self.head
        while last.next is not None:
            last = last.next
        # append the new node
        last.next = node
        self.length = self.length + 1


print(6//2,6%2,7//2,7%2)

k = 1
while (k < 6):
    j = 6//2
    while (j >= 1) :
        print(j,end=" ")
        j = j//2
    k = k + 1