import pygame
 
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
 
# This sets the width and height of each grid location
width=10
height=10
 
# This sets the margin between each cell
margin=2
 
# Create a 2 dimensional array. A two dimesional
# array in our implementation is simply a list of lists.
grid=[]
for row in range(30):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(30):
        grid[row].append(0) # Append a cell
 
# Set row 0, cell 0 to one. (Remember rows and
# column numbers start at zero.)
grid[0][0] = 1

# Initialize pygame
pygame.init()
  
# Set the height and width of the screen
size=[362,362]
screen=pygame.display.set_mode(size)
 
# Set title of screen
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done=False
 
# Used to manage how fast the screen updates
clock=pygame.time.Clock()

# Create a list of live cells, initially empty
alive=[]

# Change to play mode when user clicks start position
started=False
 
######################################
# This is code section which you need to implement

# solution using list comprehensions 
def nextgen(gen):
    nlist = [j for i in map(neighbours,gen) for j in i]
    survivors = [x for x in gen if (nlist.count(x)==2 or nlist.count(x)==3)]
    newborn = [x for x in nlist if (nlist.count(x)==3 and x not in gen)]
    newgen = survivors + newborn
    newgen = removedups(newgen)
    return [(y,x) for (y,x) in newgen if 0<y<29 and 0<x<29]  

# solution using for loops
def nextgen1(gen):
    nlist = buildnlist(gen)
    survivors = []
    newborn = []

    for cell in gen:
        if nlist.count(cell) == 2 or nlist.count(cell)==3:
            survivors.append(cell)
    for cell in nlist:
        if nlist.count(cell) == 3 and cell not in gen:
            newborn.append(cell)

    newgen = survivors + newborn
    newgen = removedups(newgen)
    outputlist = []
    for (y,x) in newgen:
        if 0<y<29 and 0<x<29:
            outputlist.append((y,x))
    return outputlist

# build neighbours list using a for loop
def buildnlist(gen): 
    result = []
    for (y,x) in gen:
        result.extend(neighbours((y,x)))
    return result

# build neighbours list using a list comprehension
def buildnlist1(gen):
    return [i for j in gen for i in neighbours(j)]

def removedups(s):
    u = []
    for x in s:
        if x not in u:
            u.append(x)
    return u

# neighbours function implemented using a list comprehension       
def neighbours((y,x)):
    return [(y+a,x+b) for a in [-1,0,1] for b in [-1,0,1] if not(a==0 and b==0)]

# neighbours function implemented using a plain old list
def neighbours1((y,x)):
    return [(y - 1, x - 1), (y, x - 1), (y + 1, x - 1), (y + 1, x), (y + 1, x + 1), (y, y + 1), (y - 1, x + 1), (y - 1, x)]
    
######################################
# -------- Main Program Loop -----------
while done==False:
    if not(started):
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column=pos[0] // (width+margin)
                row=pos[1] // (height+margin)
                # Set that location to one
                grid[row][column]=1
                # If user clicks start position
                if row==0 and column==0:
                    started=True
                    grid[row][column]=0
                    # Set up live cell list
                    for row in range(30):
                        for column in range(30):
                            if grid[row][column] == 1:
                                alive.append((row,column))
                        
                        
    if started:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column=pos[0] // (width+margin)
                row=pos[1] // (height+margin)
                # If user clicks stop position
                if row==0 and column==0:
                    started=False
                    alive=[]
        # Clear the grid       
        for row in range(30):
            for column in range(30):
                grid[row][column]=0
        # Set live cells
        for (row,column)  in alive:   
            grid[row][column]=1      
        # Set up next generation
        alive=nextgen(alive)
                      
    # Set the screen background
    screen.fill(black)
 
    # Draw the grid
    grid[0][0]=1
    for row in range(30):
        for column in range(30):
            color = white
            if grid[row][column] == 1:
                if started:
                    color = green
                else:
                    color = red        
            pygame.draw.rect(screen,color,[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
     
    # Limit to 20 frames per second
    clock.tick(10)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
# If you forget this line, the program will 'hang' on exit.
pygame.quit ()
