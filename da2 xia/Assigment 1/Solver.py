# Solver 2019
# Template for the algorithm to solve a sudoku. Builds a recursive backtracking solution
# that branches on possible values that could be placed in the next empty cell. 
# Initial pruning of the recursion tree - 
#       we don't continue on any branch that has already produced an inconsistent solution
#       we stop and return a complete solution once one has been found

import pygame, Sudoku_IO

def solve(snapshot, screen):
    # display current snapshot
    Sudoku = "easy"
    pygame.time.delay(0)
    Sudoku_IO.displayPuzzle(snapshot, screen)
    pygame.display.flip()
    single = checksingle(snapshot)
    if snapshot.unsolvedCells() == []:
        return 0

    allcell = snapshot.unsolvedCells()
    #Sort by the number of fillable values in this blank
    #check single
    allcell.sort(key = lambda i:len(checkava(snapshot,i)),reverse=False)

    i = allcell[0]
    avalist = checkava(snapshot,i)
    if avalist != []:
        for j in avalist:
            #Write the value to this blank
            i.setVal(j)
            newsnapshot = snapshot.clone()
            #Check this value
            if checkConsistency(snapshot,i) == True:
                #Output Sudoku and End
                if solve(newsnapshot,screen) == 0:
                    return 0
            else:
                #Remove non-conforming values
                avalist.remove(j)
    else:

        return 1




    # if(Sudoku == "easy"):6
    #     if single != len(snapshot.unsolvedCells()):
    #         for i in snapshot.unsolvedCells():
    #             liste = checkava(snapshot,i)
    #             if len(liste) == 1:
    #                 i.setVal(liste[0])
    #                 snapshot = snapshot.clone()
    #         solve(snapshot,screen)
    #
    #     elif single == len(snapshot.unsolvedCells()):
    #         Sudoku = "hard"
    #
    # if (Sudoku == "hard"):
    #     allcell = snapshot.unsolvedCells()
    #     allcell.sort(key = lambda i:len(checkava(snapshot,i)),reverse=False)
    #     i = allcell[0]
    #     cellava = checkava(snapshot,i)
    #     for k in cellava:
    #         i.setVal(k)
    #         if checkConsistency(snapshot,i) == True:
    #             newsnapshot = snapshot.clone()
    #             if solve(newsnapshot,screen) == 0:
    #                 return 0
    #         else:
    #             cellava.remove(k)


    # if current snapshot is complete ... return a value
    # if current snapshot not complete ...
    # for each possible value for an empty cell
    #    clone current snapshot and update it,
    #    if new snapshot is consistent, perform recursive call
    # return a value
#This Function is finding out all the fillable values in this blank
def checkava(snapshot,i):
    checklist = [1,2,3,4,5,6,7,8,9]
    nlist = []
    for R in snapshot.cellsByRow(i.getRow()):
        nlist.append(R.getVal())
    for C in snapshot.cellsByCol(i.getCol()):
        nlist.append(C.getVal())
    for B in snapshot.cellsByBlock(i.getRow(),i.getCol()):
        nlist.append(B.getVal())
    nlistw = list(set(checklist).difference(set(nlist)))
    return nlistw

def checksingle(snapshot):
    singlenum = 0
    for i in snapshot.unsolvedCells():
        singlelist=checkava(snapshot,i)
        if len(singlelist) > 1:
            singlenum+=1
    return singlenum


def checkConsistency(snapshot,cell):#This function is checking whether this value can be filled in the blank
        checkblocklist=[]
        checkrowlist=[]
        checkcollist=[]
        for j in snapshot.cellsByBlock(cell.getRow(),cell.getCol()):
            checkblocklist.append(j.getVal())
        for j in snapshot.cellsByRow(cell.getRow()):
            checkrowlist.append(j.getVal())
        for j in snapshot.cellsByCol(cell.getCol()):
            checkcollist.append(j.getVal())
        if checkblocklist.count(cell.getVal())>1: #Verify that the block has the same value
            return False
        if checkrowlist.count(cell.getVal())>1:#Verify that the row has the same value
            return False
        if checkcollist.count(cell.getVal())>1:#Verify that the column has the same value
            return False
        return True

# Check whether a puzzle is solved. 
# return true if the sudoku is solved, false otherwise
def isComplete(snapshot):
    return True


