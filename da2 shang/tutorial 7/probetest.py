import random

# I was reaching the recursion limit before I had checked all positions with the linear probe.
# Therefore, I needed to increase the recursion limit (python standard recursion limit is 1000).
import sys
sys.setrecursionlimit(100000)

class HashTable:
    def __init__(self, size=1009):
        self.size = size
        self.table = [None for x in range(size)]

    def hash(self, data):
        assert isinstance(data, int), "Data input must be an integer value."
        return data % self.size
    
    def linearProbe(self, start, attemptNumber):
        checkPos = start + attemptNumber - 1
        # This if statement 'wraps' the checkPos around, once it goes outside of the list's limit (1009 in this tutorial)
        if checkPos >= self.size:
            checkPos -= self.size
    
        # If there is nothing in the position being checked, return that position's number and the number of attempts
        if self.table[checkPos] == None:# or self.table[checkPos] == "deletedNode":
            return (checkPos, attemptNumber)
        # If the probe has searched as many times as the list has spaces, assume that each space has been looked at, and return None (and attemptNumber)
        # (i.e. all positions must be full, don't get stuck in an infinite loop)
        elif attemptNumber > self.size:
            return (None, attemptNumber)
        # If we've not reached the end of our search, make a recursive call, incrementing the attemptNumber
        else:
            return self.linearProbe(start, attemptNumber+1)
        
    def quadraticProbe(self, start, attemptNumber):
        checkPos = start +(attemptNumber**2)
        # This if statement 'wraps' the checkPos around, once it goes outside of the list's limit (1009 in this tutorial)
        while checkPos >= self.size:
            checkPos -= self.size
    
        # If there is nothing in the position being checked, return that position's number and the number of attempts
        if self.table[checkPos] == None:# or self.table[checkPos] == "deletedNode":
            return (checkPos, attemptNumber)
        # If the probe has searched as many times as the list has spaces, assume that each space has been looked at, and return None (and attemptNumber)
        # (i.e. all positions must be full, don't get stuck in an infinite loop)
        elif attemptNumber > self.size:
            return (None, attemptNumber)
        # If we've not reached the end of our search, make a recursive call, incrementing the attemptNumber
        else:
            return self.quadraticProbe(start, attemptNumber+1)
       
    
    def insert(self, data, probe):
        startPos = self.hash(data)
        # Depending on the probe being used, find the position to input the data inside of the table.
        if probe == "l":
            insertPos = self.linearProbe(startPos, 1)
        elif probe == "q":
            insertPos = self.quadraticProbe(startPos, 1)
            
        if insertPos[0] == None:
            # If insertion has failed for this item, there is a likely a problem with the size of the table. I.E 1010 items being inserted into a 1009 sized table.
            # In these cases, the code must be fixed, and so the user is told what's happened, and the program exits.
            print(str(self.size) + " positions have been checked. None of these positions were empty; Insertion has failed.")
            print("Please increase the table size before running this program again.")
            sys.exit() 
        else: 
            self.table[insertPos[0]] = data
            return insertPos[1]-1 # Return number of attempts minus 1, which should give the number of collisions. We minus 1, because one attempt would have succeeded. 
    

def comp_lists(list1, list2):
    def comp_elem(elem1, elem2):
        return 1 if elem1 < elem2 else 2
    return list(map(comp_elem, list1, list2))

def compareCollisions(output = True):
    linearTable = HashTable()
    quadraticTable = HashTable()
    count = 0
    linearCollisions = 0
    linearList = []
    quadraticCollisions = 0 
    quadraticList = []
    for rand in random.sample(range(10000), 1000):
        count += 1
        linearCollisions += linearTable.insert(rand, "l")
        quadraticCollisions += quadraticTable.insert(rand, "q")
        if count % 10 == 0:
            # After every 10 insertions, add the number of total collisions to a list
            linearList.append(linearCollisions)
            quadraticList.append(quadraticCollisions)
    compList = comp_lists(linearList, quadraticList)
    
    # This prints out a nice bit of output telling the user which probe has the least total collisions, at the given insertion number.
    # This can be prevented by the call compareCollisions(False).
    if output == True:
        insertionNumber = 0 
        for item in compList:
            insertionNumber += 10
            if item == 1:
                print("After " +str(insertionNumber)+" insertions, the LINEAR probe had the least total collisions.")
            if item == 2:
                print("After " +str(insertionNumber)+" insertions, the QUADRATIC probe had the least total collisions.")
    
    # Return the comparision list, so that if the user wants to, they may use this for their own means.
    # Printing of linear and quadratic lists so that we can see what was being compared.
    return compList   

# Added the print command, so that marker can see the list after the output.            
print(compareCollisions())
