import pygame
import mazeclass

# Initialize pygame
pygame.init()

# Set the height and width of the screen
size=[1000,500]
screen=pygame.display.set_mode(size)

# Set title of screen
pygame.display.set_caption("Maze Project")

# Get a new maze
mazegrid =  [[2,2,2,2,2,2,2,5,2,2,2,2,2,2,2,2,2,2,2,2],
             [2,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,2],
             [2,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,1,1,0,2],
             [2,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,2],
             [2,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,2],
             [2,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,2],
             [2,0,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,2],
             [2,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,2],
             [2,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0,0,2],
             [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

the_maze = mazeclass.Maze(mazegrid)


##########################################################

# Some (silly) sample code for moving one step forward and backward

def forwardbackward(curpos):
    # Warm up at the current position
    moveto(curpos, 3)
    moveto(curpos, 3)
    moveto(curpos, 3)
    moveto(curpos, 3)
    moveto(curpos, 3)
    # Look for positions that can be visited
    neighbourlist = unvisitedneighbours(curpos)
    if neighbourlist != []:
        # Select the first position that can be visited
        newpos = neighbourlist[0]
        # Go to that position
        moveto(newpos, 3)
        # More warm up at the new position
        moveto(newpos, 4)
        moveto(newpos, 4)
        moveto(newpos, 4)
        moveto(newpos, 4)
        moveto(newpos, 4)
        # Move back
        moveto(curpos, 4)

def unvisitedneighbours(curpos):
    # Return list of unvisited positions that can be reached from current position
    x = curpos[0]
    y = curpos[1]
    free = []
    for newpos in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0 <= newpos[0] < the_maze.rows and 0 <= newpos[1] < the_maze.columns:
                if the_maze.grid[newpos[0]][newpos[1]].status == 0:
                    free.append(newpos)
    return free

def moveto(newpos, status, movebot=True):
    # Mark the new position as being visited
    the_maze.grid[newpos[0]][newpos[1]].status = status
    # If required, move to the new position
    if movebot:
        the_maze.bot_xcoord = newpos[0]
        the_maze.bot_ycoord = newpos[1]
    # Wait a bit and then display the current state of the maze
    pygame.time.delay(30)
    the_maze.display_maze(screen)
    pygame.display.flip()
    pygame.event.pump()

# Code to be implementedc

def movesomesteps(curpos, steps):
    # Move ahead the specified number of steps as long as possible
    newpos = curpos
    while True:
        neiberghbourslist = unvisitedneighbours(newpos) # finding curpos's neiberghbours
        if neiberghbourslist != []:
            moveto(newpos,3)
            newpos = neiberghbourslist[0]
            steps -= 1
        elif neiberghbourslist == []:
            moveto(newpos,3)
            steps -= 1
        if steps == 0: # steps greater than fifteen
                break

def depthfirsttraversal(curpos):
    # Do a depth-first traversal of all unvisited neighbours

    list = [curpos]  # build a position list
    newpos1 = curpos
    while True:
        neiberghbourslist = unvisitedneighbours(newpos1)
        if neiberghbourslist != []:
            moveto(newpos1,3)
            newpos1 = neiberghbourslist[0]
            list.append(newpos1)
        else:
            moveto(newpos1,4)
            newpos2 = list[-1] #
            newpos1 = newpos2
            if unvisitedneighbours(newpos2) == []:
                list.remove(newpos2)
        if list == []:     #When there are no elements in the list
            moveto(newpos1,4)
            break


def depthfirstsearch(curpos):
    # Perform a depth-first search to find the exit

    list = [curpos] # to story all curpos
    newpos1 = curpos
    while True:
        neiberghbourslist = unvisitedneighbours(newpos1)
        if neiberghbourslist != []:
            moveto(newpos1,3)
            newpos1 = neiberghbourslist[0]
            list.append(newpos1)
        else:
            moveto(newpos1,4)
            newpos2 = list[-1] #
            newpos1 = newpos2
            if unvisitedneighbours(newpos2) == []:   # When there are no neighbors
                list.remove(newpos2)
        if (1,7) in list: # Reach the export
            moveto((1,7),3)
            moveto((0,7),3)
            break

# def breadthfirstsearch(curpos):
#     # Perform a breadth-first search to find the exit
#     visitedlist = []
#     dictionary = {curpos:None}
#     list = [curpos]
#     newpos = curpos
#     quit = True
#     while quit:
#         neiberghbourslist = unvisitedneighbours(newpos)
#         if neiberghbourslist != []:
#             for item in neiberghbourslist:
#                 list.append(item)
#             newpos = list[0]
#
#         else:
#             for i in list:
#                     if unvisitedneighbours(i) != []:
#                         for e in unvisitedneighbours(i):
#                             moveto(e,3)
#                             list.append(e)
#

def breadthfirstsearch(curpos):
    # Perform a breadth-first search to find the exit
    dictionary = {curpos:None}
    shortestwaydictionary = {}  # it story the shortest way
    visitedlist = [curpos] # A search list
    list = [curpos] # The list can record all position
    newpos = curpos
    quit = True
    while quit:
        neiberghbourslist = unvisitedneighbours(newpos)
        for item in neiberghbourslist:
            if item not in visitedlist:
                visitedlist.append(item)
                list.append(item)
                dictionary[item] = newpos
                if the_maze.grid[item[0]-1][item[1]].status == 5:
                    short = item
                    quit = False
        visitedlist.remove(visitedlist[0])
        newpos = visitedlist[0]

    for item1 in dictionary.keys():
        the_maze.grid[item1[0]][item1[1]].status = 3

    position = short
    while dictionary[position]  is not None:
        shortestwaydictionary[dictionary[position]] = position
        position = dictionary[position]

    position = curpos
    for s in range(len(shortestwaydictionary)):
        moveto(position,4)
        position = shortestwaydictionary[position]

    moveto(position,4)
    moveto((short[0],short[1]),4)


# Loop until the user clicks the close button.
done=False

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

######################################
# -------- Main Program Loop -----------
while done==False:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN: # If user wants to perform an action
                if event.key == pygame.K_f:
                    the_maze.reset(mazegrid)
                    forwardbackward((the_maze.bot_xcoord, the_maze.bot_ycoord))
                if event.key == pygame.K_s:
                    the_maze.reset(mazegrid)
                    movesomesteps((the_maze.bot_xcoord, the_maze.bot_ycoord), 15)
                if event.key == pygame.K_t:
                    the_maze.reset(mazegrid)
                    depthfirsttraversal((the_maze.bot_xcoord, the_maze.bot_ycoord))
                if event.key == pygame.K_d:
                    the_maze.reset(mazegrid)
                    depthfirstsearch((the_maze.bot_xcoord, the_maze.bot_ycoord))
                if event.key == pygame.K_b:
                    the_maze.reset(mazegrid)
                    breadthfirstsearch((the_maze.bot_xcoord, the_maze.bot_ycoord))

        the_maze.display_maze(screen)
        # Limit to 50 frames per second
        clock.tick(50)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

# If you forget this line, the program will 'hang' on exit.
pygame.quit ()
